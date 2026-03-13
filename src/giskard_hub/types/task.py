"""Task domain types."""

from typing import Union, Optional, TypeAlias, TypedDict
from datetime import datetime
from typing_extensions import Literal, Required

from .scan import ScanProbeAttemptReference
from .user import User
from .._types import SequenceNotStr
from .._models import BaseModel
from .test_case import TestCaseReference
from .evaluation import TestCaseEvaluationReference

__all__ = [
    "Task",
    "TaskStatus",
    "TaskPriority",
    "TaskListParams",
    "TaskCreateParams",
    "TaskUpdateParams",
    "TaskBulkDeleteParams",
]


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

TaskStatus: TypeAlias = Literal["open", "in_progress", "resolved"]
TaskPriority: TypeAlias = Literal["low", "medium", "high"]


# ---------------------------------------------------------------------------
# Task model
# ---------------------------------------------------------------------------


class Task(BaseModel):
    id: str
    project_id: str
    priority: Optional[TaskPriority] = None
    status: TaskStatus
    description: str
    created_by: User
    assignees: SequenceNotStr[User]
    references: SequenceNotStr[Union[TestCaseEvaluationReference, ScanProbeAttemptReference, TestCaseReference]]
    created_at: datetime
    updated_at: datetime


# ---------------------------------------------------------------------------
# Params
# ---------------------------------------------------------------------------


class TaskListParams(TypedDict, total=False):
    project_id: Required[str]


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


class TaskUpdateParams(TypedDict, total=False):
    assignee_ids: Optional[SequenceNotStr[str]]
    description: Optional[str]
    priority: Optional[TaskPriority]
    status: Optional[TaskStatus]
    set_test_case_status: Optional[str]


class TaskBulkDeleteParams(TypedDict, total=False):
    task_ids: Required[SequenceNotStr[str]]
