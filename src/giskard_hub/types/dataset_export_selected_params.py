from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["DatasetExportSelectedParams"]


class DatasetExportSelectedParams(TypedDict, total=False):
    test_case_ids: SequenceNotStr[str]
    """IDs of the test cases to export"""
