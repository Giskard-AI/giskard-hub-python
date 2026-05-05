"""Role domain types."""

from typing import Any, Dict, Optional, TypedDict
from typing_extensions import Required

from pydantic import Field

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
    dataset_id: str
    name: str
    source_agent_id: Optional[str] = None
    input_schema: Dict[str, Any] = Field(default_factory=dict)
    output_schema: Dict[str, Any] = Field(default_factory=dict)


# ---------------------------------------------------------------------------
# Params
# ---------------------------------------------------------------------------


class RoleListParams(TypedDict, total=False):
    project_id: Required[str]


class RoleCreateParams(TypedDict, total=False):
    project_id: Required[str]
    name: Required[str]
    input_schema: Required[Dict[str, Any]]
    output_schema: Required[Dict[str, Any]]
    source_agent_id: Optional[str]


class RoleUpdateParams(TypedDict, total=False):
    project_id: Required[str]
    name: Optional[str]
    input_schema: Optional[Dict[str, Any]]
    output_schema: Optional[Dict[str, Any]]
