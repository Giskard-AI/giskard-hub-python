from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CreateGroupRequest"]


class CreateGroupRequest(TypedDict, total=False):
    name: str

    description: Optional[str]

    permissions: Optional[list[str]]
