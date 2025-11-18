
from typing import Optional

from .._models import BaseModel
from .evaluations.task_state import TaskState

__all__ = ["TaskProgress"]


class TaskProgress(BaseModel):
    total: int

    current: Optional[int] = None

    error: Optional[str] = None

    state: Optional[TaskState] = None
