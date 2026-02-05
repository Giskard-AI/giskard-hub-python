from __future__ import annotations

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .action_type import ActionType

__all__ = ["AuditDisplayAPIResource"]


class AuditDisplayAPIResource(BaseModel):
    id: str

    action: ActionType

    entity_id: str

    entity_type: str

    created_at: datetime

    user_name: Optional[str] = None

    user_email: Optional[str] = None

    display_message: Optional[str] = None
