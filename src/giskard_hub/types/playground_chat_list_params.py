from __future__ import annotations

from typing import List, Literal, Optional
from typing_extensions import TypedDict

__all__ = ["PlaygroundChatListParams"]


class PlaygroundChatListParams(TypedDict, total=False):
    project_id: str

    include: Optional[List[Literal["agent"]]]

    limit: Optional[int]

    offset: Optional[int]
