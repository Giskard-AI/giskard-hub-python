from __future__ import annotations

from typing import Literal, TypedDict
from typing_extensions import Required

__all__ = ["CorrectnessParamsParam"]


class CorrectnessParamsParam(TypedDict, total=False):
    reference: Required[str]

    type: Literal["correctness"]
