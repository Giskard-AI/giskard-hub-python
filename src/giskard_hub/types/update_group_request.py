from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["UpdateGroupRequest"]


class UpdateGroupRequest(TypedDict, total=False):
    name: Optional[str]

    description: Optional[str]

    permissions: Optional[list[str]]
