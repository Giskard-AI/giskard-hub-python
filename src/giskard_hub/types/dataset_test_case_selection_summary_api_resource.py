"""Dataset test case selection summary API resource type."""

from __future__ import annotations

from typing import List

from .._models import BaseModel
from .dataset_test_case_check_counts import DatasetTestCaseCheckCounts
from .dataset_test_case_status_counts import DatasetTestCaseStatusCounts
from .dataset_test_case_tag_counts import DatasetTestCaseTagCounts

__all__ = ["DatasetTestCaseSelectionSummaryAPIResource"]


class DatasetTestCaseSelectionSummaryAPIResource(BaseModel):
    """Summary statistics for filtered test case selection."""

    check_counts: List[DatasetTestCaseCheckCounts]

    status_counts: List[DatasetTestCaseStatusCounts]

    tag_counts: List[DatasetTestCaseTagCounts]

    total_count: int
