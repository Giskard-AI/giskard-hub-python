"""Check, assertion, and annotation types."""

from typing import Any, Dict, List, Literal, Optional, TypedDict
from datetime import datetime
from typing_extensions import Required

from .common import TaskState
from .._types import SequenceNotStr
from .._models import BaseModel

__all__ = [
    "Check",
    "CheckResult",
    "CheckConfig",
    "CheckConfigParam",
    "CheckSource",
    "FlatCheckSpec",
    "FlatCheckSpecParam",
    "OutputAnnotation",
    "TestCaseCheckConfig",
    "TestCaseCheckConfigParam",
    "CheckListParams",
    "CheckCreateParams",
    "CheckUpdateParams",
    "CheckBulkDeleteParams",
]


# ---------------------------------------------------------------------------
# Check source and spec
# ---------------------------------------------------------------------------


class CheckSource(BaseModel):
    type: Literal["builtin", "custom"]
    identifier: Optional[str] = None


class FlatCheckSpec(BaseModel):
    pass


class FlatCheckSpecParam(TypedDict, total=False):
    pass


# ---------------------------------------------------------------------------
# Output annotation
# ---------------------------------------------------------------------------


class OutputAnnotation(BaseModel):
    end_char_index: int
    label: str
    start_char_index: int
    text: str
    type: Literal["output", "context"]


# ---------------------------------------------------------------------------
# Check models
# ---------------------------------------------------------------------------


class Check(BaseModel):
    id: str
    built_in: bool
    created_at: datetime
    description: Optional[str] = None
    identifier: str
    name: str
    spec: Optional[FlatCheckSpec] = None
    project_id: str
    updated_at: datetime


class CheckResult(BaseModel):
    name: str
    display_name: Optional[str] = None
    status: TaskState
    passed: Optional[bool] = None
    error: Optional[str] = None
    reason: Optional[str] = None
    annotations: Optional[List[OutputAnnotation]] = None
    details: Optional[Dict[str, Any]] = None


# ---------------------------------------------------------------------------
# Test case check config
# ---------------------------------------------------------------------------


class TestCaseCheckConfig(BaseModel):
    __test__ = False
    identifier: str
    spec: Optional[FlatCheckSpec] = None
    position: Optional[int] = None
    enabled: Optional[bool] = None


class TestCaseCheckConfigParam(TypedDict, total=False):
    identifier: Required[str]
    spec: Optional[FlatCheckSpecParam]
    position: int
    enabled: bool


# ---------------------------------------------------------------------------
# User-facing check config
# ---------------------------------------------------------------------------


class CheckConfig(BaseModel):
    """Check configuration with spec and position."""

    identifier: str
    enabled: Optional[bool] = None
    spec: Optional[FlatCheckSpec] = None
    position: Optional[int] = None


class CheckConfigParam(TypedDict, total=False):
    identifier: Required[str]
    enabled: bool
    spec: Optional[FlatCheckSpecParam]
    position: int


# ---------------------------------------------------------------------------
# Check params
# ---------------------------------------------------------------------------


class CheckListParams(TypedDict, total=False):
    project_id: Required[str]
    filter_builtin: bool


class CheckCreateParams(TypedDict, total=False):
    spec: Required[FlatCheckSpecParam]
    description: Optional[str]
    identifier: Required[str]
    name: Required[str]
    project_id: Required[str]


class CheckUpdateParams(TypedDict, total=False):
    spec: Optional[FlatCheckSpecParam]
    description: Optional[str]
    identifier: Optional[str]
    name: Optional[str]


class CheckBulkDeleteParams(TypedDict, total=False):
    check_ids: Required[SequenceNotStr[str]]
