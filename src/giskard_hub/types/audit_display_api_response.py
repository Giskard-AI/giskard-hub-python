
from __future__ import annotations

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .action_type import ActionType

__all__ = ["AuditDisplayAPIResponse"]


class AuditDisplayAPIResponse(BaseModel):
    id: str

    action: ActionType

    created_at: datetime

    display_name: str

    entity_id: str

    entity_type: str

    project_id: str

    user_id: Optional[str] = None

    user_name: Optional[str] = None
