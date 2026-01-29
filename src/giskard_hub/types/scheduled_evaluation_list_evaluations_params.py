from __future__ import annotations

from typing import List, Literal, Optional, TypedDict

__all__ = ["ScheduledEvaluationListEvaluationsParams"]


class ScheduledEvaluationListEvaluationsParams(TypedDict, total=False):
    include: Optional[List[Literal["agent", "dataset"]]]
