from typing import Dict, List, Optional

from .._models import BaseModel
from .evaluation_api_resource import EvaluationAPIResource

__all__ = ["EvaluationListResponse", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class EvaluationListResponse(BaseModel):
    data: List[EvaluationAPIResource]

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
