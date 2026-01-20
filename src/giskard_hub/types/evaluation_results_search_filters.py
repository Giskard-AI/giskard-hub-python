
from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .list_filter_value_uuid import ListFilterValueUUID
from .list_filter_value_str import ListFilterValueStr
from .list_filter_value_task_state import ListFilterValueTaskState

__all__ = ["EvaluationResultsSearchFilters"]


class EvaluationResultsSearchFilters(BaseModel):
    failure_category_name: Optional[ListFilterValueStr] = None

    id: Optional[ListFilterValueUUID] = None

    sample_success: Optional[bool] = None

    status: Optional[ListFilterValueTaskState] = None

    visibility: Optional[bool] = None
