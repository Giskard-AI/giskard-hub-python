from __future__ import annotations

from typing import Optional

from ..._models import BaseModel
from .task_state import TaskState

__all__ = ["SimpleTestCaseEvaluationAPIResource"]


class SimpleTestCaseEvaluationAPIResource(BaseModel):
    id: str

    test_case_id: str

    status: TaskState

    hidden: Optional[bool] = None
