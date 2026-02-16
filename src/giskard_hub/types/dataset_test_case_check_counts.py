"""Dataset test case check counts type."""

from __future__ import annotations

from .._models import BaseModel

__all__ = ["DatasetTestCaseCheckCounts"]


class DatasetTestCaseCheckCounts(BaseModel):
    """Count of test cases grouped by check name."""

    check_name: str

    count: int
