from __future__ import annotations

from typing import List, Literal, Optional
from typing_extensions import TypedDict

__all__ = ["ScheduledEvaluationListRunsParams"]


class ScheduledEvaluationListRunsParams(TypedDict, total=False):
    project_id: str

    include: Optional[List[Literal["latest_runs"]]]

    last_days: Optional[int]
