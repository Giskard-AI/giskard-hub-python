from __future__ import annotations

from typing import Optional, TypedDict

from .._types import SequenceNotStr
from .task_status import TaskStatus
from .task_priority import TaskPriority

__all__ = ["TaskUpdateParams"]


class TaskUpdateParams(TypedDict, total=False):
    assignee_ids: Optional[SequenceNotStr[str]]

    description: Optional[str]

    priority: Optional[TaskPriority]

    status: Optional[TaskStatus]

    set_test_case_status: Optional[str]
