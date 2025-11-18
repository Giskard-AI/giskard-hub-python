
from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .task_progress import TaskProgress

__all__ = ["Dataset"]


class Dataset(BaseModel):
    id: str

    created_at: datetime

    description: Optional[str] = None

    name: str

    project_id: str

    status: TaskProgress

    tags: List[str]

    updated_at: datetime
