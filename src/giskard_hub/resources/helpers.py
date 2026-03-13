import time
import asyncio
from typing import TYPE_CHECKING, Any, TypeVar, Protocol, Collection, cast, runtime_checkable

from .._models import BaseModel
from .._resource import SyncAPIResource, AsyncAPIResource
from ..types.scan import ScanResult, ScanProbeResult
from ..types.agent import Agent
from ..types.common import TaskState
from ..types.dataset import Dataset
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


TStateful = TypeVar("TStateful", bound=StatefulEntity)


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

        resource = cast(Any, self._map_entity_to_resource(cast(BaseModel, entity)))
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

    def print_metrics(self, entity: BaseModel) -> None:
        """
        Pretty-print metrics for the given entity.

        Implementation is intentionally left for future versions.
        """
        pass

    def evaluate(self, *args: object, **kwargs: object) -> None:
        """
        Run a combined remote and local evaluation.

        Implementation is intentionally left for future versions.
        """
        pass


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

        resource = cast(Any, self._map_entity_to_resource(cast(BaseModel, entity)))
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

    async def print_metrics(self, entity: BaseModel) -> None:
        """
        Async variant of ``HelpersResource.print_metrics``.
        """
        pass

    async def evaluate(self, *args: object, **kwargs: object) -> None:
        """
        Async variant of ``HelpersResource.evaluate``.
        """
        pass
