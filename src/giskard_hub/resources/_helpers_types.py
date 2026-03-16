"""Protocols, type aliases, and utility functions for the helpers resource."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeVar, Protocol, runtime_checkable

from pydantic import TypeAdapter

from .._models import BaseModel
from .._resource import SyncAPIResource, AsyncAPIResource
from ..types.chat import ChatMessage
from ..types.scan import Scan, ScanProbe
from ..types.agent import Agent, AgentOutput
from ..types.common import TaskState
from ..types.dataset import Dataset
from ..types.evaluation import Evaluation, TestCaseEvaluation
from ..types.knowledge_base import KnowledgeBase

if TYPE_CHECKING:
    from .._client import HubClient, AsyncHubClient

__all__ = [
    "StatefulEntity",
    "RetrievableResource",
    "AsyncRetrievableResource",
    "TStateful",
    "AgentReturn",
    "agent_return_adapter",
    "PrintMetricsEntity",
    "normalize_agent_output",
    "map_entity_to_resource",
]


# ---------------------------------------------------------------------------
# Protocols
# ---------------------------------------------------------------------------


@runtime_checkable
class StatefulEntity(Protocol):
    """Protocol for entities that expose task-like fields."""

    id: str

    @property
    def state(self) -> TaskState: ...


class RetrievableResource(Protocol):
    def retrieve(self, id: str) -> StatefulEntity: ...


class AsyncRetrievableResource(Protocol):
    async def retrieve(self, id: str) -> StatefulEntity: ...


# ---------------------------------------------------------------------------
# Type aliases & adapters
# ---------------------------------------------------------------------------

TStateful = TypeVar("TStateful", bound=StatefulEntity)

AgentReturn = str | ChatMessage | AgentOutput
agent_return_adapter: TypeAdapter[AgentReturn] = TypeAdapter(AgentReturn)

PrintMetricsEntity = Evaluation | Scan


# ---------------------------------------------------------------------------
# Utility functions
# ---------------------------------------------------------------------------


def normalize_agent_output(value: Any) -> AgentOutput:
    """Validate and normalize arbitrary agent return values into an ``AgentOutput``."""
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


def map_entity_to_resource(
    client: "HubClient | AsyncHubClient",
    entity: BaseModel,
) -> SyncAPIResource | AsyncAPIResource:
    """Map a model instance to the corresponding API resource on a client.

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
    if isinstance(entity, Scan):
        return client.scans
    if isinstance(entity, ScanProbe):
        return client.scans.probes
    if isinstance(entity, TestCaseEvaluation):
        return client.evaluations.results
    raise TypeError(f"Unsupported entity type for wait_for_completion: {type(entity)!r}")
