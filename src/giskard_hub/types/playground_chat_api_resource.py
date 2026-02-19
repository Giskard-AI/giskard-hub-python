from __future__ import annotations

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["PlaygroundChatAPIResource"]


class PlaygroundChatAPIResource(BaseModel):
    id: str

    project_id: str

    name: str

    created_at: datetime

    updated_at: datetime

    agent_id: Optional[str] = None

    description: Optional[str] = None
