from __future__ import annotations

from .._models import BaseModel

__all__ = ["PaginatedMetadata"]


class PaginatedMetadata(BaseModel):
    total: int

    limit: int

    offset: int
