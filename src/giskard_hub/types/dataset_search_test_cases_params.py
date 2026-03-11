"""Dataset search test cases parameters."""

from __future__ import annotations

from typing import Dict, List, Literal, Optional, TypedDict

from .filter_param import FilterValueParam
from .order_by_param import OrderByParam

__all__ = ["DatasetSearchTestCasesParams", "TestCaseOrderByParam", "TestCaseFiltersParam"]


TestCaseSortColumn = Literal["created_at", "id", "status", "updated_at"]
TestCaseFilterColumn = Literal["metrics", "status", "tags"]

TestCaseOrderByParam = OrderByParam[TestCaseSortColumn]
TestCaseFiltersParam = Dict[TestCaseFilterColumn, FilterValueParam]


class DatasetSearchTestCasesParams(TypedDict, total=False):
    """Parameters for searching dataset test cases."""

    search: Optional[str]

    order_by: Optional[List[TestCaseOrderByParam]]

    filters: Optional[TestCaseFiltersParam]

    limit: int

    offset: int
