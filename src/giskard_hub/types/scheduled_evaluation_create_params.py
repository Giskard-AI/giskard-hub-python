
from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .frequency_option import FrequencyOption

__all__ = ["ScheduledEvaluationCreateParams"]


class ScheduledEvaluationCreateParams(TypedDict, total=False):
    agent_id: Required[str]

    dataset_id: Required[str]

    frequency: Required[FrequencyOption]

    name: Required[str]

    project_id: Required[str]

    time: Required[str]

    day_of_month: Optional[int]

    day_of_week: Optional[int]

    run_count: int
    """
    The number of times to run each test case. This is useful to get a more accurate
    result when the chatbot's generation is not deterministic. Testing stops at the
    first failure. If all runs pass, the test case is considered successful.
    """

    tags: SequenceNotStr[str]
