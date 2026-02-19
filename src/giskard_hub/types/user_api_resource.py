from __future__ import annotations

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["UserAPIResource"]


class UserAPIResource(BaseModel):
    id: str

    email: str

    name: str

    created_at: datetime

    updated_at: datetime

    is_active: Optional[bool] = None

    role: Optional[str] = None
