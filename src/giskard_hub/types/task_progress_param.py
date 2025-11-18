
from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .evaluations.task_state import TaskState

__all__ = ["TaskProgressParam"]


class TaskProgressParam(TypedDict, total=False):
    total: Required[int]

    current: int

    error: Optional[str]

    state: TaskState
