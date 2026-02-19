from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["InviteUserRequest"]


class InviteUserRequest(TypedDict, total=False):
    email: str

    name: str

    role: Optional[str]

    permissions: Optional[list[str]]

    group_ids: Optional[list[str]]
