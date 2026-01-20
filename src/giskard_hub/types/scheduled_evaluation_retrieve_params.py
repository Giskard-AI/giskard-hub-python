
from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ScheduledEvaluationRetrieveParams"]


class ScheduledEvaluationRetrieveParams(TypedDict, total=False):
    include: Optional[List[Literal["evaluations"]]]
