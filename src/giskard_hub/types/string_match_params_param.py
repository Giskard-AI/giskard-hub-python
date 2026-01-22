from __future__ import annotations

from typing import Literal, TypedDict
from typing_extensions import Required

__all__ = ["StringMatchParamsParam"]


class StringMatchParamsParam(TypedDict, total=False):
    keyword: Required[str]

    type: Literal["string_match"]
