from typing import Union, Optional
from datetime import datetime

from .._models import BaseModel
from .user import User
from .task_status import TaskStatus
from .task_priority import TaskPriority
from .dataset_reference import DatasetReference
from .evaluation_reference import EvaluationReference
from .scan_reference import ScanReference
from .project_reference import ProjectReference
from .probe_result_reference import ProbeResultReference
from .probe_attempt_reference import ProbeAttemptReference
from .chat_test_case_reference import ChatTestCaseReference
from .chat_test_case_evaluation_reference import ChatTestCaseEvaluationReference

__all__ = ["TaskAPIResource", "RelatedEntity"]


RelatedEntity = Union[
    DatasetReference,
    EvaluationReference,
    ScanReference,
    ProbeResultReference,
    ProbeAttemptReference,
    ChatTestCaseReference,
    ChatTestCaseEvaluationReference,
]


class TaskAPIResource(BaseModel):
    id: str

    project: ProjectReference

    name: str

    status: TaskStatus

    created_at: datetime

    updated_at: datetime

    assignee: Optional[User] = None

    description: Optional[str] = None

    priority: Optional[TaskPriority] = None

    related_entity: Optional[RelatedEntity] = None
