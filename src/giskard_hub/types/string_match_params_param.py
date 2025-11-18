
from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["StringMatchParamsParam"]


class StringMatchParamsParam(TypedDict, total=False):
    keyword: Required[str]

    type: Literal["string_match"]
