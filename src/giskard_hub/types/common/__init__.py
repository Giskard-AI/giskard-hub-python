"""Common type definitions shared across resources."""

from typing import Any, Dict, List, Union, Generic, Literal, TypeVar, Optional, TypeAlias
from typing_extensions import Required, TypedDict, override

from ..._models import BaseModel

__all__ = [
    "APIResponse",
    "APIPaginatedMetadata",
    "APIPaginatedResponse",
    "APIResponseWithIncluded",
    "PaginatedMetadata",
    "FilterValueParam",
    "ListFilterValueParam",
    "DateRangeFilterValueParam",
    "OrderByParam",
    "TaskState",
    "TaskProgress",
    "TaskProgressParam",
]

T = TypeVar("T")
TIncluded = TypeVar("TIncluded")


# ---------------------------------------------------------------------------
# Response wrappers
# ---------------------------------------------------------------------------


class APIResponse(BaseModel, Generic[T]):
    data: T

    @override
    def __repr__(self) -> str:
        return f"APIResponse[{type(self.data).__name__}](data={self.data!r})"


class APIResponseWithIncluded(BaseModel, Generic[T, TIncluded]):
    data: T
    included: Optional[Dict[str, Dict[str, TIncluded]]] = None


class APIPaginatedMetadata(BaseModel):
    count: int
    offset: int
    limit: int
    total: int


class APIPaginatedResponse(BaseModel, Generic[T, TIncluded]):
    data: List[T]
    included: Optional[Dict[str, Dict[str, TIncluded]]] = None
    metadata: APIPaginatedMetadata


class PaginatedMetadata(BaseModel):
    total: int
    limit: int
    offset: int


# ---------------------------------------------------------------------------
# Filter / ordering helpers
# ---------------------------------------------------------------------------


class ListFilterValueParam(TypedDict, total=False):
    selected_options: List[Any]
    is_empty: bool
    match_mode: Literal["include", "exclude"]
    match_logic: Literal["any", "all"]


class DateRangeFilterValueParam(TypedDict, total=False):
    from_: Optional[str]
    to_: Optional[str]


FilterValueParam: TypeAlias = Union[ListFilterValueParam, DateRangeFilterValueParam]


class OrderByParam(TypedDict, Generic[T], total=False):
    id: Required[T]
    desc: bool


# ---------------------------------------------------------------------------
# Task state / progress (shared across many domain modules)
# ---------------------------------------------------------------------------

TaskState: TypeAlias = Literal["skipped", "finished", "error", "running", "canceled"]


class TaskProgress(BaseModel):
    total: int
    current: Optional[int] = None
    error: Optional[str] = None
    state: Optional[TaskState] = None


class TaskProgressParam(TypedDict, total=False):
    total: Required[int]
    current: int
    error: Optional[str]
    state: TaskState
