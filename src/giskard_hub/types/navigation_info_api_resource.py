
from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["NavigationInfoAPIResource"]


class NavigationInfoAPIResource(BaseModel):
    current_index: int

    total: int

    next_id: Optional[str] = None

    previous_id: Optional[str] = None
