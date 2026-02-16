"""Dataset test cases sort options type."""

from __future__ import annotations

from typing import Literal, TypedDict

__all__ = ["DatasetTestCasesSortBy", "DatasetTestCasesSortByParam"]


class DatasetTestCasesSortBy(TypedDict, total=False):
    """Sort options for dataset test cases."""

    field: Literal["id", "created_at", "updated_at", "status"]
    """Field to sort by."""

    order: Literal["asc", "desc"]
    """Sort order."""


class DatasetTestCasesSortByParam(TypedDict, total=False):
    """Parameter version of DatasetTestCasesSortBy."""

    field: Literal["id", "created_at", "updated_at", "status"]
    """Field to sort by."""

    order: Literal["asc", "desc"]
    """Sort order."""
