from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ScheduledEvaluationLatestRunsAPIResource"]


class ScheduledEvaluationLatestRunsAPIResource(BaseModel):
    scheduled_evaluation_id: str

    name: str

    latest_runs: Optional[List[object]] = None

    last_run_at: Optional[datetime] = None
