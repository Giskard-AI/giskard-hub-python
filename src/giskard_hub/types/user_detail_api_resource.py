from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["UserDetailAPIResource"]


class UserDetailAPIResource(BaseModel):
    id: str

    email: str

    name: str

    created_at: datetime

    updated_at: datetime

    is_active: Optional[bool] = None

    role: Optional[str] = None

    permissions: Optional[List[str]] = None

    last_login: Optional[datetime] = None
