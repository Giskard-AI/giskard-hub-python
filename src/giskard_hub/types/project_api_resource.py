from typing import List
from datetime import datetime

from .._models import BaseModel
from .evaluations.failure_category import FailureCategory

__all__ = ["ProjectAPIResource"]


class ProjectAPIResource(BaseModel):
    id: str

    created_at: datetime

    description: str

    failure_categories: List[FailureCategory]

    name: str

    updated_at: datetime
