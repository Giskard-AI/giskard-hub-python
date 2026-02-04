from __future__ import annotations

from typing import Literal, Optional, TypedDict
from typing_extensions import Required

from .._types import SequenceNotStr

__all__ = ["TestCaseBulkUpdateParams"]


class TestCaseBulkUpdateParams(TypedDict, total=False):
    ids: Required[SequenceNotStr[str]]
    """IDs of the objects to be patched"""

    disabled_checks: Optional[SequenceNotStr[str]]
    """Partial list of checks to be disabled"""

    enabled_checks: Optional[SequenceNotStr[str]]
    """Partial list of checks to be enabled"""

    added_tags: Optional[SequenceNotStr[str]]
    """Tags to be added to the test cases"""

    removed_tags: Optional[SequenceNotStr[str]]
    """Tags to be removed from the test cases"""

    status: Optional[Literal["active", "draft"]]
    """Status of the test cases"""
