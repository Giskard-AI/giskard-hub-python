
from __future__ import annotations

from typing import List

from .._models import BaseModel
from .simple_test_case_evaluation_api_resource import SimpleTestCaseEvaluationAPIResource

__all__ = ["APIResponseListSimpleTestCaseEvaluationAPIResource"]


class APIResponseListSimpleTestCaseEvaluationAPIResource(BaseModel):
    data: List[SimpleTestCaseEvaluationAPIResource]
