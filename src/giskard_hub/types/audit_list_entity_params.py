from __future__ import annotations

from typing import Optional, TypedDict

__all__ = ["AuditListEntityParams"]


class AuditListEntityParams(TypedDict, total=False):
    limit: Optional[int]

    offset: Optional[int]
