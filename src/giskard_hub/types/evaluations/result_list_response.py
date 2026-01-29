from typing import Dict, List, Optional

from ..._models import BaseModel
from ...types.test_case import TestCase
from .test_case_evaluation_api_resource import TestCaseEvaluationAPIResource

__all__ = ["ResultListResponse", "IncludedItem"]


class IncludedItem(BaseModel):
    data: TestCase


class ResultListResponse(BaseModel):
    data: List[TestCaseEvaluationAPIResource]

    included: Optional[Dict[str, Dict[str, IncludedItem]]] = None
