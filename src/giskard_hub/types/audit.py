"""Audit domain types."""

from typing import Dict, List, Literal, Optional, TypeAlias, TypedDict
from datetime import datetime

from pydantic import Field

from .common import OrderByParam, FilterValueParam
from .._models import BaseModel

__all__ = [
    "ActionType",
    "Audit",
    "AuditDisplay",
    "AuditDisplayDiffItem",
    "AuditListEntityParams",
    "AuditSearchParams",
    "AuditOrderByParam",
    "AuditFiltersParam",
]


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

ActionType: TypeAlias = Literal["insert", "update", "delete"]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class Audit(BaseModel):
    id: str
    action: ActionType
    entity_id: str
    entity_type: str
    created_at: datetime
    updated_at: datetime
    user_id: str
    project_id: Optional[str] = None
    user_name: Optional[str] = None
    data: Dict[str, object] = Field(default_factory=dict)
    triggered_by_entity_id: Optional[str] = None
    triggered_by_entity_type: Optional[str] = None


class AuditDisplayDiffItem(BaseModel):
    kind: Literal["added", "removed", "changed", "skip"]
    scope: str
    root: str
    skip_count: int | None = None
    label: str | None = None
    before_str: str | None = None
    after_str: str | None = None


class AuditDisplay(BaseModel):
    id: str
    created_at: datetime
    user_id: str
    user_name: Optional[str] = None
    action: ActionType
    diffs: List[AuditDisplayDiffItem]
    real_change_count: int
    summary_fields: List[str]


# ---------------------------------------------------------------------------
# Params
# ---------------------------------------------------------------------------

AuditSortColumn = Literal["action", "created_at", "entity_type", "project_id", "user_id"]
AuditFilterColumn = Literal["action", "created_at", "entity_type", "project_id", "user_id"]

AuditOrderByParam = OrderByParam[AuditSortColumn]
AuditFiltersParam = Dict[AuditFilterColumn, FilterValueParam]


class AuditListEntityParams(TypedDict, total=False):
    limit: Optional[int]
    offset: Optional[int]


class AuditSearchParams(TypedDict, total=False):
    search: Optional[str]
    order_by: Optional[List[AuditOrderByParam]]
    filters: Optional[AuditFiltersParam]
    limit: int
    offset: int
