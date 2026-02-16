"""Dataset test cases search filters type."""

from __future__ import annotations

from typing import List, Literal, Optional, TypedDict

__all__ = ["DatasetTestCasesSearchFilters", "DatasetTestCasesSearchFiltersParam"]


class DatasetTestCasesSearchFilters(TypedDict, total=False):
    """Filters for searching dataset test cases."""

    status: Optional[List[Literal["active", "draft"]]]
    """Filter by test case status."""

    tags: Optional[List[str]]
    """Filter by tags (OR operation - test cases matching any of the tags)."""

    checks: Optional[List[str]]
    """Filter by check names."""


class DatasetTestCasesSearchFiltersParam(TypedDict, total=False):
    """Parameter version of DatasetTestCasesSearchFilters."""

    status: Optional[List[Literal["active", "draft"]]]
    """Filter by test case status."""

    tags: Optional[List[str]]
    """Filter by tags (OR operation - test cases matching any of the tags)."""

    checks: Optional[List[str]]
    """Filter by check names."""
