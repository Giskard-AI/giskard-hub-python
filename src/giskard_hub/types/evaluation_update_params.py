from __future__ import annotations

from typing import TypedDict
from typing_extensions import Required

__all__ = ["EvaluationUpdateParams"]


class EvaluationUpdateParams(TypedDict, total=False):
    name: Required[str]
