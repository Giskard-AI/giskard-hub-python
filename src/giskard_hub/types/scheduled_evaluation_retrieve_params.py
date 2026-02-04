from __future__ import annotations

from typing import List, Literal, Optional, TypedDict

__all__ = ["ScheduledEvaluationRetrieveParams"]


class ScheduledEvaluationRetrieveParams(TypedDict, total=False):
    include: Optional[List[Literal["evaluations"]]]
