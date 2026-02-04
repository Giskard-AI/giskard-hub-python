from __future__ import annotations

from typing import Any, Dict, Optional, TypedDict

from giskard_hub._types import SequenceNotStr

__all__ = ["AuditSearchParams"]


class AuditSearchParams(TypedDict, total=False):
    search: Optional[str]

    order_by: Optional[SequenceNotStr[Dict[str, Any]]]

    filters: Optional[Dict[str, Dict[str, Any]]]

    limit: Optional[int]

    offset: Optional[int]
