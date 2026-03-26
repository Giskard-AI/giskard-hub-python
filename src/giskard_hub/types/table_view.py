"""Table view domain types."""

from typing import Any, Dict, List, Optional, TypedDict
from datetime import datetime
from typing_extensions import Required

from .._models import BaseModel

__all__ = [
    "TableView",
    "TableViewListParams",
    "TableViewCreateParams",
    "TableViewUpdateParams",
]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class TableView(BaseModel):
    id: str
    created_at: datetime
    entity_type: str
    name: str
    project_id: str
    settings: Dict[str, Any]
    updated_at: datetime


# ---------------------------------------------------------------------------
# Params
# ---------------------------------------------------------------------------


class TableViewListParams(TypedDict, total=False):
    entity_type: Required[str]


class TableViewCreateParams(TypedDict, total=False):
    entity_type: Required[str]
    name: Required[str]
    settings: Required[Dict[str, Any]]


class TableViewUpdateParams(TypedDict, total=False):
    name: Optional[str]
    settings: Optional[Dict[str, Any]]
