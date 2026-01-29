from __future__ import annotations

from typing import List, Literal, Optional, TypedDict
from typing_extensions import Required

__all__ = ["ScheduledEvaluationRetrieveParams"]


class ScheduledEvaluationRetrieveParams(TypedDict, total=False):
    project_id: Required[str]
    include: Optional[List[Literal["evaluations"]]]
