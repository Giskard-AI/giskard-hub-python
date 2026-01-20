
from __future__ import annotations

from typing import List

from .._models import BaseModel

__all__ = ["ListFilterValueUUID"]


class ListFilterValueUUID(BaseModel):
    values: List[str]
