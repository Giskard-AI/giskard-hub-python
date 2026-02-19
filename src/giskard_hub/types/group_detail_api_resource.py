from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["GroupDetailAPIResource"]


class GroupDetailAPIResource(BaseModel):
    id: str

    name: str

    created_at: datetime

    updated_at: datetime

    description: Optional[str] = None

    member_count: Optional[int] = None

    permissions: Optional[List[str]] = None
