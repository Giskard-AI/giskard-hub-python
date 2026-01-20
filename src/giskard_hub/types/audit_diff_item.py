
from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel
from .audit_diff_kind import AuditDiffKind

__all__ = ["AuditDiffItem"]


class AuditDiffItem(BaseModel):
    kind: AuditDiffKind

    path: List[str]

    lhs: Optional[object] = None

    rhs: Optional[object] = None
