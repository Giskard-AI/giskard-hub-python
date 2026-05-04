"""Role domain types."""

from typing import Optional, TypedDict
from datetime import datetime
from typing_extensions import Required

from .._models import BaseModel

__all__ = [
    "Role",
    "RoleListParams",
    "RoleCreateParams",
    "RoleUpdateParams",
]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class Role(BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime
    dataset_id: str
    name: str
    description: Optional[str] = None


# ---------------------------------------------------------------------------
# Params
# ---------------------------------------------------------------------------


class RoleListParams(TypedDict, total=False):
    project_id: Required[str]


class RoleCreateParams(TypedDict, total=False):
    project_id: Required[str]
    name: Required[str]
    description: Optional[str]


class RoleUpdateParams(TypedDict, total=False):
    project_id: Required[str]
    name: Optional[str]
    description: Optional[str]
