"""Audit domain types."""

from typing import Any, Dict, List, Literal, Optional, TypeAlias, TypedDict
from datetime import datetime

from .common import OrderByParam, FilterValueParam
from .._models import BaseModel

__all__ = [
    "ActionType",
    "AuditDiffKind",
    "AuditDiffItem",
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
AuditDiffKind: TypeAlias = Literal["added", "removed", "changed"]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class AuditDiffItem(BaseModel):
    kind: AuditDiffKind
    field: str
    old_value: Optional[Any] = None
    new_value: Optional[Any] = None


class Audit(BaseModel):
    id: str
    action: ActionType
    entity_id: str
    entity_type: str
    created_at: datetime
    user_id: Optional[str] = None
    project_id: Optional[str] = None
    diff: Optional[List[AuditDiffItem]] = None
    metadata: Optional[Dict[str, object]] = None


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
