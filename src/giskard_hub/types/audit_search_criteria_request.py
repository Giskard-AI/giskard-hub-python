
from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .audit_search_filters import AuditSearchFilters
from .sort_by_audit import SortByAudit

__all__ = ["AuditSearchCriteriaRequest"]


class AuditSearchCriteriaRequest(BaseModel):
    filters: Optional[AuditSearchFilters] = None

    sort_by: Optional[SortByAudit] = None
