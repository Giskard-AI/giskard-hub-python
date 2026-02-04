from typing import Dict, List, Literal, Optional

from ..types import EvaluationAPIResource
from .._models import BaseModel
from .scheduled_evaluation import ScheduledEvaluation

__all__ = ["ScheduledEvaluationListResponse", "IncludedItem"]


class IncludedItem(BaseModel):
    data: EvaluationAPIResource


class ScheduledEvaluationListResponse(BaseModel):
    data: List[ScheduledEvaluation]

    included: Optional[Dict[str, Dict[Literal["evaluations"], List[IncludedItem]]]] = None
