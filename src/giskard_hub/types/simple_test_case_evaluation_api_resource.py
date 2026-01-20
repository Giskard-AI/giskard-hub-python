
from __future__ import annotations

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .task_state import TaskState

__all__ = ["SimpleTestCaseEvaluationAPIResource"]


class SimpleTestCaseEvaluationAPIResource(BaseModel):
    id: str

    created_at: datetime

    evaluation_id: str

    status: TaskState

    test_case_id: str

    updated_at: datetime

    failure_category_name: Optional[str] = None

    hidden: Optional[bool] = None

    sample_success: Optional[bool] = None
