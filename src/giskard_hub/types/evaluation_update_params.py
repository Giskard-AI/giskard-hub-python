
from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EvaluationUpdateParams"]


class EvaluationUpdateParams(TypedDict, total=False):
    name: Required[str]
