
from __future__ import annotations

from .._models import BaseModel

__all__ = ["PaginatedMetadata"]


class PaginatedMetadata(BaseModel):
    limit: int

    offset: int

    total: int
