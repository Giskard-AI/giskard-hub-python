"""High-level helper resources that orchestrate common workflows.

This module provides ``HelpersResource`` and ``AsyncHelpersResource``, which
wrap lower-level API resources to offer convenience methods such as
``wait_for_completion``, ``evaluate``, and ``print_metrics``.
"""

import time
import asyncio
import inspect
from typing import Callable, Optional, Awaitable, Collection, cast
from concurrent.futures import ThreadPoolExecutor

from .._types import Omit, SequenceNotStr, omit
from .._models import BaseModel
from ._display import (
    build_scan_probe_data,
    print_scan_metrics_table,
    print_evaluation_metrics_table,
)
from .._resource import SyncAPIResource, AsyncAPIResource
from ..types.chat import ChatMessage
from ..types.scan import ScanProbe, ScanProbeAttempt
from ..types.agent import Agent, AgentOutputParam
from ..types.dataset import Dataset
from ..types.project import Project
from ._helpers_types import (
    TStateful,
    AgentReturn,
    PrintMetricsEntity,
    RetrievableResource,
    AsyncRetrievableResource,
    map_entity_to_resource,
    normalize_agent_output,
)
from ..types.test_case import TestCase
from ..types.evaluation import Evaluation, TestCaseEvaluation

__all__ = ["HelpersResource", "AsyncHelpersResource"]


class HelpersResource(SyncAPIResource):
    """Synchronous high-level helpers wrapping lower-level API resources."""

    def _map_entity_to_resource(self, entity: BaseModel) -> SyncAPIResource:
        return cast(SyncAPIResource, map_entity_to_resource(self._client, entity))

    def wait_for_completion(
        self,
        entity: TStateful,
        *,
        poll_interval: float = 5.0,
        max_retries: int = 360,
        running_states: Collection[str] = frozenset({"running"}),
        error_states: Collection[str] = frozenset({"error"}),
        raise_on_error: bool = True,
    ) -> TStateful:
        """Wait until an entity leaves a running state and return its final value.

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
        """Run an evaluation for a given agent over a dataset.

        Handles both remote agents (referenced by ID or ``Agent``) and local
        Python callables that take a list of ``ChatMessage`` and return an
        ``AgentOutput``-compatible value.

        Parameters
        ----------
        agent :
            Either a remote agent identifier (``str`` or ``Agent``) or a callable
            with signature ``(messages: list[ChatMessage]) -> AgentReturn``.
        dataset :
            Dataset identifier or ``Dataset`` instance containing the test cases
            to evaluate the agent on.
        project :
            Project identifier or ``Project`` instance.  Required when ``agent``
            is a remote agent (string or ``Agent``).
        name :
            Optional name to assign to the created evaluation.
        tags :
            Optional list of tags to filter the dataset's test cases.

        Returns
        -------
        Evaluation
            The created evaluation.

        Raises
        ------
        ValueError
            If ``project`` is not provided when running a remote evaluation.
        TypeError
            If the local agent callable returns an unsupported value, or if test
            cases do not include full ``TestCase`` objects during local evaluation.
        """
        dataset_id = dataset if isinstance(dataset, str) else dataset.id

        if isinstance(agent, (str, Agent)):
            return self._evaluate_remote(agent=agent, dataset_id=dataset_id, project=project, name=name, tags=tags)

        return self._evaluate_local(agent=agent, dataset_id=dataset_id, name=name, tags=tags)

    def print_metrics(self, entity: PrintMetricsEntity) -> None:
        """Print metrics for an evaluation or scan result to the console.

        For an evaluation, displays a table of metric names, success rates, and
        pass/fail/error/skipped counts.  For a scan result, displays probe
        categories, names, severity, and issue/attack counts.
        """
        if isinstance(entity, Evaluation):
            print_evaluation_metrics_table(entity)
        else:
            self._print_scan_metrics(entity)

    # -- Private helpers -----------------------------------------------------

    def _evaluate_remote(
        self,
        *,
        agent: str | Agent,
        dataset_id: str,
        project: Optional[str | Project] | Omit,
        name: Optional[str] | Omit,
        tags: Optional[SequenceNotStr[str]] | Omit,
    ) -> Evaluation:
        if project is omit or project is None:
            raise ValueError("Project is required when running a remote evaluation")

        project_id = project if isinstance(project, str) else cast(Project, project).id
        agent_id = agent if isinstance(agent, str) else agent.id
        name_arg: str | Omit = omit if name is None else name

        return self._client.evaluations.create(
            project_id=project_id,
            agent_id=agent_id,
            name=name_arg,
            dataset_id=dataset_id,
            tags=tags,
        )

    def _evaluate_local(
        self,
        *,
        agent: Callable[[list[ChatMessage]], AgentReturn],
        dataset_id: str,
        name: Optional[str] | Omit,
        tags: Optional[SequenceNotStr[str]] | Omit,
    ) -> Evaluation:
        evaluation = self._client.evaluations.create_local(
            agent_info={
                "name": agent.__name__,
                "description": agent.__doc__ or "",
            },
            name=name,
            dataset_id=dataset_id,
            tags=tags,
        )

        entries = self._client.evaluations.results.list(evaluation_id=evaluation.id, include=["test_case"])

        for entry in entries:
            test_case = entry.test_case
            if not isinstance(test_case, TestCase):
                raise TypeError("Expected `test_case` to be a full TestCase for local evaluation")

            agent_output_model = normalize_agent_output(agent(test_case.messages))
            agent_output_param = cast(AgentOutputParam, agent_output_model.to_dict())

            self._client.evaluations.results.submit_local_output(
                result_id=entry.id,
                evaluation_id=evaluation.id,
                agent_output=agent_output_param,
            )

        return evaluation

    def _print_scan_metrics(self, entity: object) -> None:
        from ..types.scan import Scan as _Scan

        scan = cast(_Scan, entity)
        category_map = {cat.id: cat.title for cat in self._client.scans.list_categories()}
        probe_results = self._client.scans.list_probes(scan_id=scan.id)

        def fetch_attempts(probe: ScanProbe) -> tuple[str, list[ScanProbeAttempt]]:
            return (probe.id, self._client.scans.probes.list_attempts(probe_id=probe.id))

        with ThreadPoolExecutor() as executor:
            attempts_by_probe_id = dict(executor.map(fetch_attempts, probe_results))
        probe_data = build_scan_probe_data(category_map, probe_results, attempts_by_probe_id)
        print_scan_metrics_table(probe_data, scan.id)


class AsyncHelpersResource(AsyncAPIResource):
    """Asynchronous high-level helpers wrapping lower-level API resources."""

    def _map_entity_to_resource(self, entity: BaseModel) -> AsyncAPIResource:
        return cast(AsyncAPIResource, map_entity_to_resource(self._client, entity))

    async def wait_for_completion(
        self,
        entity: TStateful,
        *,
        poll_interval: float = 5.0,
        max_retries: int = 360,
        running_states: Collection[str] = frozenset({"running"}),
        error_states: Collection[str] = frozenset({"error"}),
        raise_on_error: bool = True,
    ) -> TStateful:
        """Asynchronously wait until an entity leaves a running state.

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
        """Asynchronously run an evaluation for a given agent over a dataset.

        Handles both remote agents (referenced by ID or ``Agent``) and local
        Python callables (sync or async) that take a list of ``ChatMessage``
        and return an ``AgentOutput``-compatible value.

        Parameters
        ----------
        agent :
            Either a remote agent identifier (``str`` or ``Agent``) or a callable
            with signature ``(messages: list[ChatMessage]) -> AgentReturn``.
        dataset :
            Dataset identifier or ``Dataset`` instance containing the test cases
            to evaluate the agent on.
        project :
            Project identifier or ``Project`` instance.  Required when ``agent``
            is a remote agent (string or ``Agent``).
        name :
            Optional name to assign to the created evaluation.
        tags :
            Optional list of tags to filter the dataset's test cases.

        Returns
        -------
        Evaluation
            The created evaluation.

        Raises
        ------
        ValueError
            If ``project`` is not provided when running a remote evaluation.
        TypeError
            If the local agent callable returns an unsupported value, or if test
            cases do not include full ``TestCase`` objects during local evaluation.
        """
        dataset_id = dataset if isinstance(dataset, str) else dataset.id

        if isinstance(agent, (str, Agent)):
            return await self._evaluate_remote(
                agent=agent, dataset_id=dataset_id, project=project, name=name, tags=tags
            )

        return await self._evaluate_local(agent=agent, dataset_id=dataset_id, name=name, tags=tags)

    async def print_metrics(self, entity: PrintMetricsEntity) -> None:
        """Print metrics for an evaluation or scan result to the console (async).

        For an evaluation, displays a table of metric names, success rates, and
        pass/fail/error/skipped counts.  For a scan result, displays probe
        categories, names, severity, and issue/attack counts.
        """
        if isinstance(entity, Evaluation):
            print_evaluation_metrics_table(entity)
        else:
            await self._print_scan_metrics(entity)

    # -- Private helpers -----------------------------------------------------

    async def _evaluate_remote(
        self,
        *,
        agent: str | Agent,
        dataset_id: str,
        project: Optional[str | Project] | Omit,
        name: Optional[str] | Omit,
        tags: Optional[SequenceNotStr[str]] | Omit,
    ) -> Evaluation:
        if project is omit or project is None:
            raise ValueError("Project is required when running a remote evaluation")

        project_id = project if isinstance(project, str) else cast(Project, project).id
        agent_id = agent if isinstance(agent, str) else agent.id
        name_arg: str | Omit = omit if name is None else name

        return await self._client.evaluations.create(
            project_id=project_id,
            agent_id=agent_id,
            name=name_arg,
            dataset_id=dataset_id,
            tags=tags,
        )

    async def _evaluate_local(
        self,
        *,
        agent: Callable[[list[ChatMessage]], AgentReturn | Awaitable[AgentReturn]],
        dataset_id: str,
        name: Optional[str] | Omit,
        tags: Optional[SequenceNotStr[str]] | Omit,
    ) -> Evaluation:
        evaluation = await self._client.evaluations.create_local(
            agent_info={
                "name": agent.__name__,
                "description": agent.__doc__ or "",
            },
            name=name,
            dataset_id=dataset_id,
            tags=tags,
        )

        entries = await self._client.evaluations.results.list(
            evaluation_id=evaluation.id,
            include=["test_case"],
        )

        async def _process_entry(entry: TestCaseEvaluation) -> None:
            test_case = entry.test_case
            if not isinstance(test_case, TestCase):
                raise TypeError("Expected `test_case` to be a full TestCase for local evaluation")

            output = agent(test_case.messages)
            if inspect.isawaitable(output):
                output = await output

            agent_output_model = normalize_agent_output(output)
            agent_output_param = cast(AgentOutputParam, agent_output_model.to_dict())

            await self._client.evaluations.results.submit_local_output(
                result_id=entry.id,
                evaluation_id=evaluation.id,
                agent_output=agent_output_param,
            )

        await asyncio.gather(*(_process_entry(entry) for entry in entries))

        return evaluation

    async def _print_scan_metrics(self, entity: object) -> None:
        from ..types.scan import Scan as _Scan

        scan = cast(_Scan, entity)
        category_map = {cat.id: cat.title for cat in await self._client.scans.list_categories()}
        probe_results = await self._client.scans.list_probes(scan_id=scan.id)
        attempts_list = await asyncio.gather(
            *(self._client.scans.probes.list_attempts(probe_id=probe.id) for probe in probe_results)
        )
        attempts_by_probe_id = {
            probe.id: attempts for probe, attempts in zip(probe_results, attempts_list, strict=True)
        }
        probe_data = build_scan_probe_data(category_map, probe_results, attempts_by_probe_id)
        print_scan_metrics_table(probe_data, scan.id)
