"""Protocols, type aliases, and utility functions for the helpers resource."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeVar, Callable, Protocol, Awaitable, runtime_checkable
from functools import partial

from pydantic import TypeAdapter

from .._models import BaseModel
from ..types.chat import ChatMessage
from ..types.scan import Scan, ScanProbe
from ..types.agent import AgentOutput
from ..types.common import TaskState
from ..types.dataset import Dataset
from ..types.evaluation import Evaluation, TestCaseEvaluation
from ..types.knowledge_base import KnowledgeBase

if TYPE_CHECKING:
    from .._client import HubClient, AsyncHubClient

__all__ = [
    "StatefulEntity",
    "Retriever",
    "AsyncRetriever",
    "TStateful",
    "AgentReturn",
    "agent_return_adapter",
    "PrintMetricsEntity",
    "normalize_agent_output",
    "make_retriever",
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


# ---------------------------------------------------------------------------
# Type aliases & adapters
# ---------------------------------------------------------------------------

Retriever = Callable[[str], StatefulEntity]
AsyncRetriever = Callable[[str], Awaitable[StatefulEntity]]

TStateful = TypeVar("TStateful", bound=StatefulEntity)

AgentReturn = str | ChatMessage | AgentOutput
agent_return_adapter: TypeAdapter[AgentReturn] = TypeAdapter(AgentReturn)

PrintMetricsEntity = Evaluation | Scan


# ---------------------------------------------------------------------------
# Utility functions
# ---------------------------------------------------------------------------


def normalize_agent_output(value: Any) -> AgentOutput:
    """Validate and normalize arbitrary agent return values into an `AgentOutput`."""
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


def make_retriever(
    client: "HubClient | AsyncHubClient",
    entity: BaseModel,
) -> Callable[..., Any]:
    """Create a callable that retrieves the latest state of `entity` by ID.

    For most entity types the callable is the `retrieve` method of the
    corresponding API resource. For entity types whose `retrieve` requires
    additional context (e.g. `TestCaseEvaluation` needs `evaluation_id`),
    the extra arguments are captured via `functools.partial`.

    Parameters
    ----------
    client :
        The API client that exposes resource attributes such as `agents`,
        `datasets`, `evaluations`, etc.
    entity :
        The entity instance whose retriever should be resolved.

    Returns
    -------
    Callable[..., Any]
        A callable `(id: str) -> StatefulEntity` (sync or async depending
        on the client).

    Raises
    ------
    TypeError
        If the entity type is not supported.
    """
    if isinstance(entity, Dataset):
        return client.datasets.retrieve
    if isinstance(entity, Evaluation):
        return client.evaluations.retrieve
    if isinstance(entity, KnowledgeBase):
        return client.knowledge_bases.retrieve
    if isinstance(entity, Scan):
        return client.scans.retrieve
    if isinstance(entity, ScanProbe):
        return client.scans.probes.retrieve
    if isinstance(entity, TestCaseEvaluation):
        return partial(client.evaluations.results.retrieve, evaluation_id=entity.evaluation_id)
    raise TypeError(f"Unsupported entity type for wait_for_completion: {type(entity)!r}")
