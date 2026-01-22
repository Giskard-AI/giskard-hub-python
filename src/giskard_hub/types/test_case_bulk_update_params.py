from __future__ import annotations

from typing import Optional, TypedDict
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
