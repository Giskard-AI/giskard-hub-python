
from __future__ import annotations

from typing import List

from .._models import BaseModel
from .paginated_metadata import PaginatedMetadata
from .evaluations.test_case_evaluation_api_resource import TestCaseEvaluationAPIResource

__all__ = ["PaginatedAPIResponseTestCaseEvaluationAPIResource"]


class PaginatedAPIResponseTestCaseEvaluationAPIResource(BaseModel):
    data: List[TestCaseEvaluationAPIResource]

    metadata: PaginatedMetadata
