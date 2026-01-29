from typing import List, Optional

from .._models import BaseModel
from .output_annotation import OutputAnnotation
from .evaluations.task_state import TaskState

__all__ = ["EvaluationRunSingleResponse", "Data"]


class Data(BaseModel):
    annotations: Optional[List[OutputAnnotation]] = None

    display_name: Optional[str] = None

    error: Optional[str] = None

    name: str

    passed: Optional[bool] = None

    reason: Optional[str] = None

    status: TaskState


class EvaluationRunSingleResponse(BaseModel):
    data: List[Data]
