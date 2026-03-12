"""Playground chat domain types."""

from typing import List, Literal, Optional, TypedDict
from datetime import datetime
from typing_extensions import Required

from .chat import ChatMessageWithMetadata
from .user import UserReference
from .agent import AgentReference
from .._types import SequenceNotStr
from .._models import BaseModel

__all__ = [
    "PlaygroundChat",
    "PlaygroundChatListParams",
    "PlaygroundChatRetrieveParams",
    "PlaygroundChatBulkDeleteParams",
]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class PlaygroundChat(BaseModel):
    id: str
    project_id: str
    created_at: datetime
    updated_at: datetime
    user: Optional[UserReference] = None
    agent: Optional[AgentReference] = None
    messages: List[ChatMessageWithMetadata]


# ---------------------------------------------------------------------------
# Params
# ---------------------------------------------------------------------------


class PlaygroundChatListParams(TypedDict, total=False):
    project_id: str
    include: Optional[List[Literal["agent"]]]
    limit: Optional[int]
    offset: Optional[int]


class PlaygroundChatRetrieveParams(TypedDict, total=False):
    include: Optional[List[Literal["agent"]]]


class PlaygroundChatBulkDeleteParams(TypedDict, total=False):
    chat_ids: Required[SequenceNotStr[str]]
