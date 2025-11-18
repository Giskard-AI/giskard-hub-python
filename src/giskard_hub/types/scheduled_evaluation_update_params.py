
from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .frequency_option import FrequencyOption
from .error_execution_status_param import ErrorExecutionStatusParam
from .success_execution_status_param import SuccessExecutionStatusParam

__all__ = ["ScheduledEvaluationUpdateParams", "LastExecutionStatus"]


class ScheduledEvaluationUpdateParams(TypedDict, total=False):
    day_of_month: Optional[int]

    day_of_week: Optional[int]

    frequency: Optional[FrequencyOption]

    last_execution_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    last_execution_status: Optional[LastExecutionStatus]

    name: Optional[str]

    paused: Optional[bool]

    run_count: Optional[int]

    time: Optional[str]


LastExecutionStatus: TypeAlias = Union[SuccessExecutionStatusParam, ErrorExecutionStatusParam]
