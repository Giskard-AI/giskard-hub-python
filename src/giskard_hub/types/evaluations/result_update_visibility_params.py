from __future__ import annotations

from typing import TypedDict
from typing_extensions import Required

__all__ = ["ResultUpdateVisibilityParams"]


class ResultUpdateVisibilityParams(TypedDict, total=False):
    hidden: Required[bool]
