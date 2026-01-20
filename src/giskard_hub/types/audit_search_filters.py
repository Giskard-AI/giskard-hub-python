
from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .date_range_filter_values import DateRangeFilterValues
from .list_filter_value_action_type import ListFilterValueActionType
from .list_filter_value_uuid import ListFilterValueUUID
from .list_filter_value_str import ListFilterValueStr

__all__ = ["AuditSearchFilters"]


class AuditSearchFilters(BaseModel):
    action: Optional[ListFilterValueActionType] = None

    created_at: Optional[DateRangeFilterValues] = None

    entity_id: Optional[ListFilterValueUUID] = None

    entity_type: Optional[ListFilterValueStr] = None

    project_id: Optional[ListFilterValueUUID] = None

    user_id: Optional[ListFilterValueUUID] = None
