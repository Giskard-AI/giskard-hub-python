"""Dataset test case tag counts type."""

from __future__ import annotations

from .._models import BaseModel

__all__ = ["DatasetTestCaseTagCounts"]


class DatasetTestCaseTagCounts(BaseModel):
    """Count of test cases grouped by tag."""

    tag: str

    count: int
