"""Agent domain types."""

from typing import Dict, Iterable, Optional, TypedDict
from datetime import datetime
from typing_extensions import Required

from pydantic import Field, AliasChoices

from .chat import Header, ChatMessage, HeaderParam, ChatMessageParam
from .._types import SequenceNotStr
from .._models import BaseModel
from .execution import ExecutionError, ExecutionErrorParam

__all__ = [
    "Agent",
    "AgentReference",
    "AgentOutput",
    "AgentOutputParam",
    "MinimalAgent",
    "MinimalAgentParam",
    "AgentListParams",
    "AgentCreateParams",
    "AgentUpdateParams",
    "AgentBulkDeleteParams",
    "AgentTestConnectionParams",
    "AgentGenerateCompletionParams",
    "AgentAutofillDescriptionParams",
]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class Agent(BaseModel):
    id: str
    created_at: datetime
    description: Optional[str] = None
    headers: list[Header]
    name: str
    project_id: str
    supported_languages: list[str]
    updated_at: datetime
    url: str


class AgentReference(BaseModel):
    id: str
    name: str


class AgentOutput(BaseModel):
    response: Optional[ChatMessage] = Field(
        default=None,
        validation_alias=AliasChoices("response", "message"),
    )
    error: Optional[ExecutionError] = None
    metadata: Optional[Dict[str, object]] = None


class AgentOutputParam(TypedDict, total=False):
    response: Required[Optional[ChatMessageParam]]
    error: Optional[ExecutionErrorParam]
    metadata: Dict[str, object]


class MinimalAgent(BaseModel):
    name: str
    description: Optional[str] = None


class MinimalAgentParam(TypedDict, total=False):
    name: Required[str]
    description: Optional[str]


# ---------------------------------------------------------------------------
# Params
# ---------------------------------------------------------------------------


class AgentListParams(TypedDict, total=False):
    project_id: Optional[str]


class AgentCreateParams(TypedDict, total=False):
    headers: Required[Iterable[HeaderParam]]
    name: Required[str]
    project_id: Required[str]
    supported_languages: Required[SequenceNotStr[str]]
    url: Required[str]
    description: Optional[str]


class AgentUpdateParams(TypedDict, total=False):
    description: Optional[str]
    headers: Optional[Iterable[HeaderParam]]
    name: Optional[str]
    supported_languages: Optional[SequenceNotStr[str]]
    url: Optional[str]


class AgentBulkDeleteParams(TypedDict, total=False):
    agent_ids: Required[SequenceNotStr[str]]


class AgentTestConnectionParams(TypedDict, total=False):
    url: Required[str]
    headers: Dict[str, str]


class AgentGenerateCompletionParams(TypedDict, total=False):
    messages: Required[Iterable[ChatMessageParam]]


class AgentAutofillDescriptionParams(TypedDict, total=False):
    pass
