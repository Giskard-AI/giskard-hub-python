
from __future__ import annotations

from typing import List

from .._models import BaseModel
from .task_state import TaskState

__all__ = ["ListFilterValueTaskState"]


class ListFilterValueTaskState(BaseModel):
    values: List[TaskState]
