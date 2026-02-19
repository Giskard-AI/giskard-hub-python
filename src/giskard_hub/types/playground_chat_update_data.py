from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PlaygroundChatUpdateData"]


class PlaygroundChatUpdateData(TypedDict, total=False):
    name: Optional[str]

    agent_id: Optional[str]

    description: Optional[str]
