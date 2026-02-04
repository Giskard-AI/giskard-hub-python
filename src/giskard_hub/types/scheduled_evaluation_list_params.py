from __future__ import annotations

from typing import List, Literal, Optional, TypedDict
from typing_extensions import Required

__all__ = ["ScheduledEvaluationListParams"]


class ScheduledEvaluationListParams(TypedDict, total=False):
    project_id: Required[str]
    last_days: Optional[int]
    include: Optional[List[Literal["evaluations"]]]
