from __future__ import annotations

from typing import Dict, List, Literal, Optional, TypedDict

from .filter_param import FilterValueParam
from .order_by_param import OrderByParam

__all__ = ["AuditSearchParams", "AuditOrderByParam", "AuditFiltersParam"]

AuditSortColumn = Literal["action", "created_at", "entity_type", "project_id", "user_id"]
AuditFilterColumn = Literal["action", "created_at", "entity_type", "project_id", "user_id"]

AuditOrderByParam = OrderByParam[AuditSortColumn]
AuditFiltersParam = Dict[AuditFilterColumn, FilterValueParam]


class AuditSearchParams(TypedDict, total=False):
    search: Optional[str]

    order_by: Optional[List[AuditOrderByParam]]

    filters: Optional[AuditFiltersParam]

    limit: int

    offset: int
