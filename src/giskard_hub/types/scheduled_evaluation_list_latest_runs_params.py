
from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ScheduledEvaluationListLatestRunsParams"]


class ScheduledEvaluationListLatestRunsParams(TypedDict, total=False):
    project_id: Required[str]

    include: Optional[List[Literal["scheduled_evaluation", "latest_runs"]]]

    last_days: Optional[int]
    """If provided, only include evaluation runs created in the last N days."""
