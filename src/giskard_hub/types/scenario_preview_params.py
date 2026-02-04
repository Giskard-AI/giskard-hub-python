from __future__ import annotations

from typing import Optional, TypedDict
from typing_extensions import Required

from .._types import SequenceNotStr

__all__ = ["ScenarioPreviewParams"]


class ScenarioPreviewParams(TypedDict, total=False):
    description: Required[str]

    rules: Optional[SequenceNotStr[str]]
