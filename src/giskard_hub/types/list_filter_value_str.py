
from __future__ import annotations

from typing import List

from .._models import BaseModel

__all__ = ["ListFilterValueStr"]


class ListFilterValueStr(BaseModel):
    values: List[str]
