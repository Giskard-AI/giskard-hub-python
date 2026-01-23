from typing import Any, Dict, Optional

from ..._models import BaseModel
from .test_case_evaluation_api_resource import TestCaseEvaluationAPIResource

__all__ = ["ResultRetrieveResponse"]


class ResultRetrieveResponse(BaseModel):
    data: TestCaseEvaluationAPIResource

    included: Optional[Dict[str, Any]] = None
