"""Playground chat domain types."""

from typing import Any, Dict, List, Literal, Optional, TypedDict, Iterable
from datetime import datetime
from typing_extensions import Required

from .chat import ChatMessageWithMetadata, ChatMessageWithMetadataParam
from .user import UserReference
from .agent import Agent, AgentReference
from .._types import SequenceNotStr
from .._models import BaseModel

__all__ = [
    "PlaygroundChat",
    "PlaygroundExchange",
    "PlaygroundChatListParams",
    "PlaygroundChatCreateParams",
    "PlaygroundChatUpdateParams",
    "PlaygroundChatRetrieveParams",
    "PlaygroundChatBulkDeleteParams",
]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class PlaygroundExchange(BaseModel):
    input: str
    output: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class PlaygroundChat(BaseModel):
    id: str
    project_id: str
    created_at: datetime
    updated_at: datetime
    user: Optional[UserReference] = None
    agent: Optional[AgentReference | Agent] = None
    agent_id: Optional[str] = None
    exchanges: Optional[List[PlaygroundExchange]] = None
    forwarded: Optional[bool] = None


# ---------------------------------------------------------------------------
# Params
# ---------------------------------------------------------------------------


class PlaygroundExchangeParam(TypedDict, total=False):
    input: Required[str]
    output: Optional[str]
    metadata: Optional[Dict[str, Any]]


class PlaygroundChatCreateParams(TypedDict, total=False):
    project_id: Required[str]
    agent_id: Optional[str]
    exchanges: Optional[Iterable[PlaygroundExchangeParam]]


class PlaygroundChatUpdateParams(TypedDict, total=False):
    agent_id: Optional[str]
    exchanges: Optional[Iterable[PlaygroundExchangeParam]]


class PlaygroundChatListParams(TypedDict, total=False):
    project_id: str
    include: Optional[List[Literal["agent"]]]
    limit: Optional[int]
    offset: Optional[int]


class PlaygroundChatRetrieveParams(TypedDict, total=False):
    include: Optional[List[Literal["agent"]]]


class PlaygroundChatBulkDeleteParams(TypedDict, total=False):
    chat_ids: Required[SequenceNotStr[str]]
