from typing import List

from ..._models import BaseModel
from .simple_test_case_evaluation_api_resource import SimpleTestCaseEvaluationAPIResource

__all__ = ["APIResponseSimpleTestCaseEvaluation"]


class APIResponseSimpleTestCaseEvaluation(BaseModel):
    data: List[SimpleTestCaseEvaluationAPIResource]
