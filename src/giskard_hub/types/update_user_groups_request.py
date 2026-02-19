from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UpdateUserGroupsRequest"]


class UpdateUserGroupsRequest(TypedDict, total=False):
    group_ids: list[str]
