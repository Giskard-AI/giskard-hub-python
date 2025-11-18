
from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CorrectnessParamsParam"]


class CorrectnessParamsParam(TypedDict, total=False):
    reference: Required[str]

    type: Literal["correctness"]
