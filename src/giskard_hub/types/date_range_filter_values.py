
from __future__ import annotations

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["DateRangeFilterValues"]


class DateRangeFilterValues(BaseModel):
    from_: Optional[datetime] = None
    """The start of the date range."""

    to: Optional[datetime] = None
    """The end of the date range."""
