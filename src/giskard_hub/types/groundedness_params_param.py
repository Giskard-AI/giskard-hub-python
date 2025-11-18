
from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["GroundednessParamsParam"]


class GroundednessParamsParam(TypedDict, total=False):
    context: Required[str]

    type: Literal["groundedness"]
