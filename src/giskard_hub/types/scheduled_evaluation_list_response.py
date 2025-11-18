
from typing import Dict, List, Optional

from .._models import BaseModel
from .scheduled_evaluation import ScheduledEvaluation

__all__ = ["ScheduledEvaluationListResponse", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class ScheduledEvaluationListResponse(BaseModel):
    data: List[ScheduledEvaluation]

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
