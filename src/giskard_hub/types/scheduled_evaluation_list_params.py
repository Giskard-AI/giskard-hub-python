
from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ScheduledEvaluationListParams"]


class ScheduledEvaluationListParams(TypedDict, total=False):
    project_id: Required[str]

    include: Optional[List[Literal["evaluations"]]]

    last_days: Optional[int]
