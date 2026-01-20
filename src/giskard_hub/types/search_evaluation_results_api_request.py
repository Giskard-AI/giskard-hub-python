
from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .evaluation_results_search_filters import EvaluationResultsSearchFilters
from .sort_by_evaluation_results import SortByEvaluationResults

__all__ = ["SearchEvaluationResultsAPIRequest"]


class SearchEvaluationResultsAPIRequest(BaseModel):
    filters: Optional[EvaluationResultsSearchFilters] = None

    sort_by: Optional[SortByEvaluationResults] = None
