from __future__ import annotations

from typing import Optional, TypedDict
from typing_extensions import Required

__all__ = ["ResultUpdateVisibilityParams"]


class ResultUpdateVisibilityParams(TypedDict, total=False):
    hidden: Required[bool]
    set_test_case_draft: Optional[bool]
