from __future__ import annotations

from typing import Any, Optional

from .._models import BaseModel
from .audit_diff_kind import AuditDiffKind

__all__ = ["AuditDiffItem"]


class AuditDiffItem(BaseModel):
    kind: AuditDiffKind

    field: str

    old_value: Optional[Any] = None

    new_value: Optional[Any] = None
