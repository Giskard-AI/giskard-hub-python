
from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ConformityParamsParam"]


class ConformityParamsParam(TypedDict, total=False):
    rules: Required[SequenceNotStr[str]]

    type: Literal["conformity"]
