from __future__ import annotations

from typing import Optional

from ..._models import BaseModel

__all__ = ["NavigationInfoAPIResource"]


class NavigationInfoAPIResource(BaseModel):
    current_index: int

    total_count: int

    previous_id: Optional[str] = None

    next_id: Optional[str] = None
