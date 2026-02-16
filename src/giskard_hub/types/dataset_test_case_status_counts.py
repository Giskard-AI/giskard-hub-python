"""Dataset test case status counts type."""

from __future__ import annotations

from typing import Literal

from .._models import BaseModel

__all__ = ["DatasetTestCaseStatusCounts"]


class DatasetTestCaseStatusCounts(BaseModel):
    """Count of test cases grouped by status."""

    status: Literal["active", "draft"]

    count: int
