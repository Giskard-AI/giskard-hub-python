"""Dataset search test cases parameters."""

from __future__ import annotations

from typing import Optional, TypedDict

from .dataset_test_cases_sort_by import DatasetTestCasesSortByParam
from .dataset_test_cases_search_filters import DatasetTestCasesSearchFiltersParam

__all__ = ["DatasetSearchTestCasesParams"]


class DatasetSearchTestCasesParams(TypedDict, total=False):
    """Parameters for searching dataset test cases."""

    filters: Optional[DatasetTestCasesSearchFiltersParam]
    """Search filters to apply."""

    sort_by: Optional[DatasetTestCasesSortByParam]
    """Sort options."""
