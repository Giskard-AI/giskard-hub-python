"""Dataset search selection summary parameters."""

from __future__ import annotations

from typing import Optional, TypedDict

from .dataset_test_cases_search_filters import DatasetTestCasesSearchFiltersParam

__all__ = ["DatasetSearchSelectionSummaryParams"]


class DatasetSearchSelectionSummaryParams(TypedDict, total=False):
    """Parameters for getting dataset test cases selection summary."""

    filters: Optional[DatasetTestCasesSearchFiltersParam]
    """Search filters to apply."""
