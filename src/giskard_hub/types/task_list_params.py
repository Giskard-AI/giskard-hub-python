from __future__ import annotations

from typing import TypedDict
from typing_extensions import Required

__all__ = ["TaskListParams"]


class TaskListParams(TypedDict, total=False):
    project_id: Required[str]
