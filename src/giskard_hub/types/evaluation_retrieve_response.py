
from typing import Dict, Optional

from .._models import BaseModel
from .evaluation_api_resource import EvaluationAPIResource

__all__ = ["EvaluationRetrieveResponse", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class EvaluationRetrieveResponse(BaseModel):
    data: EvaluationAPIResource

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
