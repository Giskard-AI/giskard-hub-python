from typing import Union, Optional
from datetime import datetime

from .user import User
from .._types import SequenceNotStr
from .._models import BaseModel
from .task_status import TaskStatus
from .task_priority import TaskPriority
from .test_case_reference import TestCaseReferencence
from .probe_attempt_reference import ProbeAttemptReference
from .test_case_evaluation_reference import TestCaseEvaluationReference

__all__ = ["TaskAPIResource"]


class TaskAPIResource(BaseModel):
    id: str

    project_id: str

    priority: Optional[TaskPriority] = None

    status: TaskStatus

    description: str

    created_by: User

    assignees: SequenceNotStr[User]

    references: SequenceNotStr[Union[TestCaseEvaluationReference, ProbeAttemptReference, TestCaseReferencence]]

    created_at: datetime

    updated_at: datetime
