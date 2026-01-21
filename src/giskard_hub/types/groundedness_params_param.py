from __future__ import annotations

from typing import Literal, TypedDict
from typing_extensions import Required

__all__ = ["GroundednessParamsParam"]


class GroundednessParamsParam(TypedDict, total=False):
    context: Required[str]

    type: Literal["groundedness"]
