from __future__ import annotations

from typing import TypedDict
from typing_extensions import Required

__all__ = ["HeaderParam"]


class HeaderParam(TypedDict, total=False):
    name: Required[str]

    value: Required[str]
