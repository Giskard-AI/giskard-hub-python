from __future__ import annotations

from typing import TypedDict
from typing_extensions import Required

__all__ = ["CheckListParams"]


class CheckListParams(TypedDict, total=False):
    project_id: Required[str]

    filter_builtin: bool
