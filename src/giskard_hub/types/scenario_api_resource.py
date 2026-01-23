from __future__ import annotations

from typing import Any, Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ScenarioAPIResource"]


class ScenarioAPIResource(BaseModel):
    id: str

    name: str

    project_id: str

    created_at: datetime

    updated_at: datetime

    description: Optional[str] = None

    config: Optional[Dict[str, Any]] = None

    agent_id: Optional[str] = None
