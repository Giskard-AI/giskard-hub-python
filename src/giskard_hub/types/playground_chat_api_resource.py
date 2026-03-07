from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .user_api_reference import UserAPIReference
from .agent_api_reference import AgentAPIReference
from .chat_message_with_metadata import ChatMessageWithMetadata

__all__ = ["PlaygroundChatAPIResource"]


class PlaygroundChatAPIResource(BaseModel):
    id: str

    project_id: str

    created_at: datetime

    updated_at: datetime

    user: Optional[UserAPIReference] = None

    agent: Optional[AgentAPIReference] = None

    messages: List[ChatMessageWithMetadata]
