from __future__ import annotations

from typing import List, Literal, Optional
from typing_extensions import TypedDict

__all__ = ["PlaygroundChatRetrieveParams"]


class PlaygroundChatRetrieveParams(TypedDict, total=False):
    include: Optional[List[Literal["agent"]]]
