
from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FailureCategoryParam"]


class FailureCategoryParam(TypedDict, total=False):
    description: Required[str]

    identifier: Required[str]

    title: Required[str]
