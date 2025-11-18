
from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CheckListParams"]


class CheckListParams(TypedDict, total=False):
    project_id: Required[str]

    filter_builtin: bool
