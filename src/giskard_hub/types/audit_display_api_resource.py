from __future__ import annotations

from typing import List, Literal, Optional
from datetime import datetime

from .._models import BaseModel
from .action_type import ActionType

__all__ = ["AuditDisplayAPIResource"]


class AuditDiffItem(BaseModel):
    kind: Literal[
        "added",
        "removed",
        "changed",
        "skip",
    ]
    scope: str
    root: str
    skip_count: int | None = None
    label: str | None = None
    before_str: str | None = None
    after_str: str | None = None


class AuditDisplayAPIResource(BaseModel):
    id: str

    created_at: datetime

    user_id: str

    user_name: Optional[str] = None

    action: ActionType

    diffs: List[AuditDiffItem]

    real_change_count: int

    summary_fields: List[str]
