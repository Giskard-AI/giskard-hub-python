from __future__ import annotations

from typing import Optional, TypedDict

from .severity import Severity
from .review_status import ReviewStatus

__all__ = ["AttemptUpdateParams"]


class AttemptUpdateParams(TypedDict, total=False):
    review_status: Optional[ReviewStatus]

    severity: Optional[Severity]

    successful: Optional[bool]
