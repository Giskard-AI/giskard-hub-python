import time
import asyncio
import inspect
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Callable,
    Optional,
    Protocol,
    Awaitable,
    Collection,
    cast,
    runtime_checkable,
)

from pydantic import TypeAdapter

from .._types import Omit, SequenceNotStr, omit
from .._models import BaseModel
from .._resource import SyncAPIResource, AsyncAPIResource
from ..types.chat import ChatMessage
from ..types.scan import ScanResult, ScanProbeResult
from ..types.agent import Agent, AgentOutput, AgentOutputParam
from ..types.common import TaskState
from ..types.dataset import Dataset
from ..types.project import Project
from ..types.test_case import TestCase
from ..types.evaluation import Evaluation, TestCaseEvaluation
from ..types.knowledge_base import KnowledgeBase

if TYPE_CHECKING:
    from .._client import HubClient, AsyncHubClient

__all__ = ["HelpersResource", "AsyncHelpersResource"]


@runtime_checkable
class StatefulEntity(Protocol):
    """Protocol for entities that expose task-like fields."""

    id: str
    state: TaskState


class RetrievableResource(Protocol):
    def retrieve(self, id: str) -> StatefulEntity: ...


class AsyncRetrievableResource(Protocol):
    async def retrieve(self, id: str) -> StatefulEntity: ...


TStateful = TypeVar("TStateful", bound=StatefulEntity)

AgentReturn = str | ChatMessage | AgentOutput
agent_return_adapter: TypeAdapter[AgentReturn] = TypeAdapter(AgentReturn)


def _map_entity_to_resource_from_client(
    client: "HubClient | AsyncHubClient",
    entity: BaseModel,
) -> SyncAPIResource | AsyncAPIResource:
    """
    Map a model instance to the corresponding API resource on a client.

    This helper is shared by both the synchronous and asynchronous helpers,
    which operate on different client types but expose the same resource
    attributes.

    Parameters
    ----------
    client :
        The API client that exposes resource attributes such as ``agents``,
        ``datasets``, ``evaluations``, etc.
    entity :
        The entity instance whose managing resource should be resolved.

    Returns
    -------
    SyncAPIResource or AsyncAPIResource
        The API resource responsible for the given entity type.

    Raises
    ------
    TypeError
        If the entity type is not supported.
    """
    if isinstance(entity, Agent):
        return client.agents
    if isinstance(entity, Dataset):
        return client.datasets
    if isinstance(entity, Evaluation):
        return client.evaluations
    if isinstance(entity, KnowledgeBase):
        return client.knowledge_bases
    if isinstance(entity, ScanResult):
        return client.scans
    if isinstance(entity, ScanProbeResult):
        return client.scans.probes
    if isinstance(entity, TestCaseEvaluation):
        return client.evaluations.results
    raise TypeError(f"Unsupported entity type for wait_for_completion: {type(entity)!r}")


def _normalize_agent_output(value: Any) -> AgentOutput:
    parsed: AgentReturn = agent_return_adapter.validate_python(value)

    match parsed:
        case AgentOutput():
            return parsed
        case ChatMessage():
            return AgentOutput(response=parsed)
        case str():
            return AgentOutput(response=ChatMessage(role="assistant", content=parsed))
        case _:
            raise ValueError(f"Invalid agent output: {value!r}")


class HelpersResource(SyncAPIResource):
    def _map_entity_to_resource(self, entity: BaseModel) -> SyncAPIResource:
        """
        Map a model instance to the corresponding synchronous API resource.

        Parameters
        ----------
        entity :
            The entity instance whose managing resource should be resolved.

        Returns
        -------
        SyncAPIResource
            The synchronous API resource responsible for the given entity type.

        Raises
        ------
        TypeError
            If the entity type is not supported.
        """
        # Cast to the concrete resource type expected by this helper.
        return cast(SyncAPIResource, _map_entity_to_resource_from_client(self._client, entity))

    def wait_for_completion(
        self,
        entity: TStateful,
        *,
        poll_interval: float = 5.0,
        max_retries: int = 360,
        running_states: Collection[TaskState] = frozenset({"running"}),
        error_states: Collection[TaskState] = frozenset({"error"}),
        raise_on_error: bool = True,
    ) -> TStateful:
        """
        Wait until an entity leaves a running state and return its final value.

        Parameters
        ----------
        entity :
            The entity to monitor for completion.
        poll_interval :
            Time in seconds to wait between polling attempts.
        max_retries :
            Maximum number of polling attempts before timing out.
        running_states :
            Set of states considered as still running.
        error_states :
            Set of states considered as terminal error states.
        raise_on_error :
            Whether to raise an exception if an error state is reached.

        Returns
        -------
        StatefulEntity
            The refreshed entity once it has left the running states, or is in
            an error state when ``raise_on_error`` is ``False``.

        Raises
        ------
        ValueError
            If the entity reaches an error state and ``raise_on_error`` is ``True``.
        RuntimeError
            If the entity does not complete within the allotted number of retries.
        """

        resource = cast(RetrievableResource, self._map_entity_to_resource(cast(BaseModel, entity)))

        current: TStateful = entity

        for _ in range(max_retries):
            current = cast(TStateful, resource.retrieve(current.id))

            if current.state in error_states:
                if raise_on_error:
                    raise ValueError(f"Entity {current.id} reached an error state: {current.state}")
                return current

            if current.state not in running_states:
                return current

            time.sleep(poll_interval)

        raise RuntimeError(
            f"Timeout waiting for entity {current.id} to complete "
            f"after {max_retries} retries (~{max_retries * poll_interval:.0f}s)"
        )

    def evaluate(
        self,
        *,
        agent: str | Agent | Callable[[list[ChatMessage]], AgentReturn],
        dataset: str | Dataset,
        project: Optional[str | Project] | Omit = omit,
        name: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
    ) -> Evaluation:
        """
        Run an evaluation for a given agent over a dataset.

        This helper handles both remote agents (referenced by ID or `Agent`) and
        local Python callables that take a list of `ChatMessage` and return an
        `AgentOutput`-compatible value.

        Parameters
        ----------
        agent :
            Either a remote agent identifier (`str` or `Agent`) or a callable
            with signature ``(messages: list[ChatMessage]) -> AgentReturn``.
        dataset :
            Dataset identifier or `Dataset` instance containing the test cases
            to evaluate the agent on.
        project :
            Project identifier or `Project` instance. Required when `agent` is a
            remote agent (string or `Agent`). Ignored for local callable agents.
        name :
            Optional name to assign to the created evaluation.
        tags :
            Optional list of tags to filter the dataset's test cases when
            creating the evaluation.

        Returns
        -------
        Evaluation
            The created evaluation, either remote or local depending on the
            `agent` argument.

        Raises
        ------
        ValueError
            If `project` is not provided when running a remote evaluation.
        TypeError
            If the local agent callable returns a value that cannot be
            normalized into an `AgentOutput`, or if test cases returned by the
            API do not include full `TestCase` objects during local evaluation.
        """
        dataset_id = dataset if isinstance(dataset, str) else dataset.id

        # Remote evaluation
        if isinstance(agent, str) or isinstance(agent, Agent):
            if project is omit or project is None:
                raise ValueError("Project is required when running a remote evaluation")

            if isinstance(project, str):
                project_id: str = project
            else:
                project_model = cast(Project, project)
                project_id = project_model.id

            agent_id = agent if isinstance(agent, str) else agent.id

            name_arg: str | Omit = omit if name is None else name

            return self._client.evaluations.create(
                project_id=project_id,
                agent_id=agent_id,
                name=name_arg,
                dataset_id=dataset_id,
                tags=tags,
            )

        # Local evaluation
        # Create evaluation
        evaluation = self._client.evaluations.create_local(
            agent_info={
                "name": agent.__name__,
                "description": agent.__doc__ or "",
            },
            name=name,
            dataset_id=dataset_id,
            tags=tags,
        )

        # Retrieve entries (test case messages)
        entries = self._client.evaluations.results.list(evaluation_id=evaluation.id, include=["test_case"])

        # Submit outputs
        for entry in entries:
            test_case = entry.test_case
            if not isinstance(test_case, TestCase):
                raise TypeError("Expected `test_case` to be a full TestCase for local evaluation")

            agent_output_model = _normalize_agent_output(agent(test_case.messages))
            agent_output_param = cast(AgentOutputParam, agent_output_model.to_dict())

            self._client.evaluations.results.submit_local_output(
                result_id=entry.id,
                evaluation_id=evaluation.id,
                agent_output=agent_output_param,
            )

        return evaluation


class AsyncHelpersResource(AsyncAPIResource):
    def _map_entity_to_resource(self, entity: BaseModel) -> AsyncAPIResource:
        """
        Map a model instance to the corresponding asynchronous API resource.

        Parameters
        ----------
        entity :
            The entity instance whose managing async resource should be resolved.

        Returns
        -------
        AsyncAPIResource
            The asynchronous API resource responsible for the given entity type.

        Raises
        ------
        TypeError
            If the entity type is not supported.
        """
        return cast(AsyncAPIResource, _map_entity_to_resource_from_client(self._client, entity))

    async def wait_for_completion(
        self,
        entity: TStateful,
        *,
        poll_interval: float = 5.0,
        max_retries: int = 360,
        running_states: Collection[TaskState] = frozenset({"running"}),
        error_states: Collection[TaskState] = frozenset({"error"}),
        raise_on_error: bool = True,
    ) -> TStateful:
        """
        Asynchronously wait until an entity leaves a running state and return its final value.

        Parameters
        ----------
        entity :
            The entity to monitor for completion.
        poll_interval :
            Time in seconds to wait between polling attempts.
        max_retries :
            Maximum number of polling attempts before timing out.
        running_states :
            Set of states considered as still running.
        error_states :
            Set of states considered as terminal error states.
        raise_on_error :
            Whether to raise an exception if an error state is reached.

        Returns
        -------
        StatefulEntity
            The refreshed entity once it has left the running states, or is in
            an error state when ``raise_on_error`` is ``False``.

        Raises
        ------
        ValueError
            If the entity reaches an error state and ``raise_on_error`` is ``True``.
        RuntimeError
            If the entity does not complete within the allotted number of retries.
        """

        resource = cast(AsyncRetrievableResource, self._map_entity_to_resource(cast(BaseModel, entity)))

        current: TStateful = entity

        for _ in range(max_retries):
            current = cast(TStateful, await resource.retrieve(current.id))

            if current.state in error_states:
                if raise_on_error:
                    raise ValueError(f"Entity {current.id} reached an error state: {current.state}")
                return current

            if current.state not in running_states:
                return current

            await asyncio.sleep(poll_interval)

        raise RuntimeError(
            f"Timeout waiting for entity {current.id} to complete "
            f"after {max_retries} retries (~{max_retries * poll_interval:.0f}s)"
        )

    async def evaluate(
        self,
        *,
        agent: str | Agent | Callable[[list[ChatMessage]], AgentReturn | Awaitable[AgentReturn]],
        dataset: str | Dataset,
        project: Optional[str | Project] | Omit = omit,
        name: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
    ) -> Evaluation:
        """
        Asynchronously run an evaluation for a given agent over a dataset.

        This helper handles both remote agents (referenced by ID or `Agent`) and
        local Python callables that take a list of `ChatMessage` and return an
        `AgentOutput`-compatible value.

        Parameters
        ----------
        agent :
            Either a remote agent identifier (`str` or `Agent`) or a callable
            with signature ``(messages: list[ChatMessage]) -> AgentReturn``.
        dataset :
            Dataset identifier or `Dataset` instance containing the test cases
            to evaluate the agent on.
        project :
            Project identifier or `Project` instance. Required when `agent` is a
            remote agent (string or `Agent`). Ignored for local callable agents.
        name :
            Optional name to assign to the created evaluation.
        tags :
            Optional list of tags to filter the dataset's test cases when
            creating the evaluation.

        Returns
        -------
        Evaluation
            The created evaluation, either remote or local depending on the
            `agent` argument.

        Raises
        ------
        ValueError
            If `project` is not provided when running a remote evaluation.
        TypeError
            If the local agent callable returns a value that cannot be
            normalized into an `AgentOutput`, or if test cases returned by the
            API do not include full `TestCase` objects during local evaluation.
        """
        dataset_id = dataset if isinstance(dataset, str) else dataset.id

        # Remote evaluation
        if isinstance(agent, str) or isinstance(agent, Agent):
            if project is omit or project is None:
                raise ValueError("Project is required when running a remote evaluation")

            if isinstance(project, str):
                project_id: str = project
            else:
                project_model = cast(Project, project)
                project_id = project_model.id

            agent_id = agent if isinstance(agent, str) else agent.id

            name_arg: str | Omit = omit if name is None else name

            return await self._client.evaluations.create(
                project_id=project_id,
                agent_id=agent_id,
                name=name_arg,
                dataset_id=dataset_id,
                tags=tags,
            )

        # Local evaluation
        # Create evaluation
        evaluation = await self._client.evaluations.create_local(
            agent_info={
                "name": agent.__name__,
                "description": agent.__doc__ or "",
            },
            name=name,
            dataset_id=dataset_id,
            tags=tags,
        )

        # Retrieve entries (test case messages)
        entries = await self._client.evaluations.results.list(
            evaluation_id=evaluation.id,
            include=["test_case"],
        )

        # Submit outputs
        async def _process_entry(entry: TestCaseEvaluation) -> None:
            test_case = entry.test_case
            if not isinstance(test_case, TestCase):
                raise TypeError("Expected `test_case` to be a full TestCase for local evaluation")

            output = agent(test_case.messages)
            if inspect.isawaitable(output):
                output = await output

            agent_output_model = _normalize_agent_output(output)
            agent_output_param = cast(AgentOutputParam, agent_output_model.to_dict())

            await self._client.evaluations.results.submit_local_output(
                result_id=entry.id,
                evaluation_id=evaluation.id,
                agent_output=agent_output_param,
            )

        await asyncio.gather(*(_process_entry(entry) for entry in entries))

        return evaluation
