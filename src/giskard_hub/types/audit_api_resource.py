from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .action_type import ActionType
from .audit_diff_item import AuditDiffItem

__all__ = ["AuditAPIResource"]


class AuditAPIResource(BaseModel):
    id: str

    action: ActionType

    entity_id: str

    entity_type: str

    created_at: datetime

    user_id: Optional[str] = None

    project_id: Optional[str] = None

    diff: Optional[List[AuditDiffItem]] = None

    metadata: Optional[Dict[str, object]] = None
