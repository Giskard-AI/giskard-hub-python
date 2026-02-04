from __future__ import annotations

from typing import Optional
from datetime import datetime

from giskard_hub._types import SequenceNotStr

from .._models import BaseModel

__all__ = ["ScenarioAPIResource"]


class ScenarioAPIResource(BaseModel):
    id: str

    created_at: datetime

    updated_at: datetime

    name: str

    description: Optional[str] = None

    rules: SequenceNotStr[str]
