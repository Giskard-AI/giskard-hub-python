"""Scheduled evaluation domain types."""

from typing import List, Union, Literal, Optional, Annotated, TypeAlias, TypedDict
from datetime import datetime
from typing_extensions import Required

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .._models import BaseModel
from .execution import (
    ErrorExecutionStatus,
    SuccessExecutionStatus,
    ErrorExecutionStatusParam,
    SuccessExecutionStatusParam,
)

__all__ = [
    "FrequencyOption",
    "ScheduledEvaluation",
    "ScheduledEvaluationListParams",
    "ScheduledEvaluationCreateParams",
    "ScheduledEvaluationUpdateParams",
    "ScheduledEvaluationRetrieveParams",
    "ScheduledEvaluationBulkDeleteParams",
    "ScheduledEvaluationListEvaluationsParams",
]


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

FrequencyOption: TypeAlias = Literal["daily", "weekly", "monthly"]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------

LastExecutionStatus: TypeAlias = Union[SuccessExecutionStatus, ErrorExecutionStatus, None]


class ScheduledEvaluation(BaseModel):
    id: str
    agent_id: str
    created_at: datetime
    dataset_id: str
    day_of_month: Optional[int] = None
    day_of_week: Optional[int] = None
    frequency: FrequencyOption
    last_execution_at: Optional[datetime] = None
    last_execution_status: Optional[LastExecutionStatus] = None
    name: str
    paused: bool
    project_id: str
    run_count: int
    tags: List[str]
    time: str
    updated_at: datetime


# ---------------------------------------------------------------------------
# Params
# ---------------------------------------------------------------------------


class ScheduledEvaluationListParams(TypedDict, total=False):
    project_id: Required[str]
    last_days: Optional[int]
    include: Optional[List[Literal["evaluations"]]]


class ScheduledEvaluationCreateParams(TypedDict, total=False):
    project_id: Required[str]
    name: Required[str]
    agent_id: Required[str]
    dataset_id: Required[str]
    tags: SequenceNotStr[str]
    run_count: int
    frequency: Required[FrequencyOption]
    time: Required[str]
    day_of_week: Optional[int]
    day_of_month: Optional[int]


LastExecutionStatusParam: TypeAlias = Union[SuccessExecutionStatusParam, ErrorExecutionStatusParam]


class ScheduledEvaluationUpdateParams(TypedDict, total=False):
    name: Optional[str]
    run_count: Optional[int]
    frequency: Optional[FrequencyOption]
    time: Optional[str]
    day_of_week: Optional[int]
    day_of_month: Optional[int]
    last_execution_at: Optional[Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]]
    last_execution_status: Optional[LastExecutionStatusParam]
    paused: Optional[bool]


class ScheduledEvaluationRetrieveParams(TypedDict, total=False):
    include: Optional[List[Literal["evaluations"]]]


class ScheduledEvaluationBulkDeleteParams(TypedDict, total=False):
    scheduled_evaluation_ids: Required[SequenceNotStr[str]]


class ScheduledEvaluationListEvaluationsParams(TypedDict, total=False):
    include: Optional[List[Literal["agent", "dataset"]]]
