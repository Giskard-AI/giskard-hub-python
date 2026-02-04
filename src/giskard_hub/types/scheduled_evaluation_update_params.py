from __future__ import annotations

from typing import Union, Optional, Annotated, TypeAlias, TypedDict
from datetime import datetime

from .._utils import PropertyInfo
from .frequency_option import FrequencyOption
from .error_execution_status_param import ErrorExecutionStatusParam
from .success_execution_status_param import SuccessExecutionStatusParam

__all__ = ["ScheduledEvaluationUpdateParams", "LastExecutionStatus"]


class ScheduledEvaluationUpdateParams(TypedDict, total=False):
    name: Optional[str]

    run_count: Optional[int]

    frequency: Optional[FrequencyOption]

    time: Optional[str]

    day_of_week: Optional[int]

    day_of_month: Optional[int]

    last_execution_at: Optional[Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]]

    last_execution_status: Optional[LastExecutionStatus]

    paused: Optional[bool]


LastExecutionStatus: TypeAlias = Union[SuccessExecutionStatusParam, ErrorExecutionStatusParam]
