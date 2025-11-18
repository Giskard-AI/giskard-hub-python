
from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel
from .frequency_option import FrequencyOption
from .error_execution_status import ErrorExecutionStatus
from .success_execution_status import SuccessExecutionStatus

__all__ = ["ScheduledEvaluation", "LastExecutionStatus"]

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
