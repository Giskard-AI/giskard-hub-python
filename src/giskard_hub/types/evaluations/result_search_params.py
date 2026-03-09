from __future__ import annotations

from typing import Dict, List, Literal, Optional, TypedDict

from ..filter_param import FilterValueParam
from ..order_by_param import OrderByParam

__all__ = ["ResultSearchParams", "ResultOrderByParam", "ResultFiltersParam"]

ResultSortColumn = Literal["failure_category_name", "id", "sample_success", "status", "visibility"]
ResultFilterColumn = Literal["failure_category_name", "metrics", "sample_success", "status", "tags", "visibility"]

ResultOrderByParam = OrderByParam[ResultSortColumn]
ResultFiltersParam = Dict[ResultFilterColumn, FilterValueParam]


class ResultSearchParams(TypedDict, total=False):
    search: Optional[str]

    order_by: Optional[List[ResultOrderByParam]]

    filters: Optional[ResultFiltersParam]

    limit: int

    offset: int

    include: Optional[List[Literal["test_case"]]]
