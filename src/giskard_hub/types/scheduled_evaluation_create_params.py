from __future__ import annotations

from typing import Optional, TypedDict
from typing_extensions import Required

from .._types import SequenceNotStr
from .frequency_option import FrequencyOption

__all__ = ["ScheduledEvaluationCreateParams"]


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
