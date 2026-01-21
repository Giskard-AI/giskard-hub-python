from __future__ import annotations

from typing import Literal, TypedDict
from typing_extensions import Required

from .._types import SequenceNotStr

__all__ = ["ConformityParamsParam"]


class ConformityParamsParam(TypedDict, total=False):
    rules: Required[SequenceNotStr[str]]

    type: Literal["conformity"]
