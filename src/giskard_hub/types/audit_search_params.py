
from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AuditSearchParams"]


class AuditSearchParams(TypedDict, total=False):
    limit: Optional[int]

    offset: Optional[int]
