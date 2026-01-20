
from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .action_type import ActionType
from .audit_diff_item import AuditDiffItem

__all__ = ["AuditAPIResource"]


class AuditAPIResource(BaseModel):
    id: str

    action: ActionType

    created_at: datetime

    entity_id: str

    entity_type: str

    project_id: str

    user_id: Optional[str] = None

    diff: Optional[List[AuditDiffItem]] = None
