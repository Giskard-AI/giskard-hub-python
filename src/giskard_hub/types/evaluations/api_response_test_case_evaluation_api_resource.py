from typing import Dict, Optional

from ..._models import BaseModel
from ...types.test_case import TestCase
from .test_case_evaluation_api_resource import TestCaseEvaluationAPIResource

__all__ = ["APIResponseTestCaseEvaluationAPIResource", "IncludedItem"]


class IncludedItem(BaseModel):
    data: TestCase


class APIResponseTestCaseEvaluationAPIResource(BaseModel):
    data: TestCaseEvaluationAPIResource

    included: Optional[Dict[str, Dict[str, IncludedItem]]] = None
