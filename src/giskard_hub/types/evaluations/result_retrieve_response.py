
from __future__ import annotations

from typing import Dict, Optional

from .._models import BaseModel
from .test_case_evaluation_api_resource import TestCaseEvaluationAPIResource

__all__ = ["ResultRetrieveResponse", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class ResultRetrieveResponse(BaseModel):
    data: TestCaseEvaluationAPIResource

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
