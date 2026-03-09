from typing import List, Optional
from datetime import datetime

from ..types import Header
from .._models import BaseModel

__all__ = ["Agent"]


class Agent(BaseModel):
    id: str

    created_at: datetime

    description: Optional[str] = None

    headers: List[Header]

    name: str

    project_id: str

    supported_languages: List[str]

    updated_at: datetime

    url: str
