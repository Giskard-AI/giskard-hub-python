from typing import List

from ..._models import BaseModel
from ..paginated_metadata import PaginatedMetadata
from .test_case_evaluation_api_resource import TestCaseEvaluationAPIResource

__all__ = ["ResultSearchResponse"]


class ResultSearchResponse(BaseModel):
    data: List[TestCaseEvaluationAPIResource]

    metadata: PaginatedMetadata
