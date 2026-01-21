from typing import Dict, List, Optional

from .._models import BaseModel
from .evaluation_api_resource import EvaluationAPIResource

__all__ = ["ScheduledEvaluationListEvaluationsResponse", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class ScheduledEvaluationListEvaluationsResponse(BaseModel):
    data: List[EvaluationAPIResource]

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
