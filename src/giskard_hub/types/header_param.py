
from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["HeaderParam"]


class HeaderParam(TypedDict, total=False):
    name: Required[str]

    value: Required[str]
