
from __future__ import annotations

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SortByAudit"]


class SortByAudit(BaseModel):
    field: Literal["-created_at", "-action", "-entity_type", "-user_id", "-project_id"]

    order: Literal["asc", "desc"]
