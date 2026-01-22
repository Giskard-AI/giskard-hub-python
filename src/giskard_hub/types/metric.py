from typing import Optional

from .._models import BaseModel

__all__ = ["Metric"]


class Metric(BaseModel):
    name: str

    display_name: Optional[str] = None

    errored: Optional[int] = None

    failed: Optional[int] = None

    passed: Optional[int] = None

    total: Optional[int] = None
