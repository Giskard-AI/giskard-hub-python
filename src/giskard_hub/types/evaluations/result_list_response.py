
from typing import Dict, List, Optional

from ..._models import BaseModel
from .test_case_evaluation_api_resource import TestCaseEvaluationAPIResource

__all__ = ["ResultListResponse", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class ResultListResponse(BaseModel):
    data: List[TestCaseEvaluationAPIResource]

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
