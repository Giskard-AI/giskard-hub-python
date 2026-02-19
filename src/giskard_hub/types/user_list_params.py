from __future__ import annotations

from typing import List, Literal, Optional
from typing_extensions import TypedDict

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    include: Optional[List[Literal["groups"]]]
