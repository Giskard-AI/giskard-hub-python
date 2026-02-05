from __future__ import annotations

from typing import Optional, TypedDict
from typing_extensions import Required

from .._types import SequenceNotStr
from .task_status import TaskStatus
from .task_priority import TaskPriority

__all__ = ["TaskCreateParams"]


class TaskCreateParams(TypedDict, total=False):
    project_id: Required[str]

    priority: Optional[TaskPriority]

    status: TaskStatus

    description: Required[str]

    assignee_ids: SequenceNotStr[str]

    evaluation_result_id: Optional[str]

    dataset_test_case_id: Optional[str]

    probe_attempt_id: Optional[str]

    disable_test: bool

    hide_result: bool
