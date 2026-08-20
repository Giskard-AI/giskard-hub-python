"""Task domain types."""

from typing import List, Union, Optional, TypeAlias, TypedDict
from datetime import datetime
from typing_extensions import Literal, Required

from .scan import ScanProbeAttemptReference
from .user import User
from .._types import SequenceNotStr
from .._models import BaseModel
from .scenario import ScenarioReference
from .evaluation import ScenarioEvaluationReference

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
    assignees: List[User]
    references: List[Union[ScenarioEvaluationReference, ScanProbeAttemptReference, ScenarioReference]]
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
    dataset_scenario_id: Optional[str]
    probe_attempt_id: Optional[str]
    disable_test: bool
    hide_result: bool


class TaskUpdateParams(TypedDict, total=False):
    assignee_ids: Optional[SequenceNotStr[str]]
    description: Optional[str]
    priority: Optional[TaskPriority]
    status: Optional[TaskStatus]
    set_scenario_status: Optional[str]


class TaskBulkDeleteParams(TypedDict, total=False):
    task_ids: Required[SequenceNotStr[str]]
