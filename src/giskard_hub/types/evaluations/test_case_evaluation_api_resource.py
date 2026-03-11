from typing import List, Optional
from datetime import datetime

from . import failure_category
from ..._models import BaseModel
from .task_state import TaskState
from ..model_output import AgentOutput
from ..output_annotation import OutputAnnotation

__all__ = ["TestCaseEvaluationAPIResource", "FailureCategory", "Result", "TestCase"]


class FailureCategory(BaseModel):
    category: Optional[failure_category.FailureCategory] = None

    error: Optional[str] = None

    status: Optional[TaskState] = None


class Result(BaseModel):
    name: str

    annotations: Optional[List[OutputAnnotation]] = None

    display_name: Optional[str] = None

    error: Optional[str] = None

    passed: Optional[bool] = None

    reason: Optional[str] = None

    status: Optional[TaskState] = None


class TestCase(BaseModel):
    __test__ = False
    id: str


class TestCaseEvaluationAPIResource(BaseModel):
    __test__ = False
    id: str

    created_at: datetime

    error: Optional[str] = None

    evaluation_id: str

    failure_category: Optional[FailureCategory] = None

    output: Optional[AgentOutput] = None

    results: List[Result]

    state: TaskState

    test_case: TestCase

    updated_at: datetime
