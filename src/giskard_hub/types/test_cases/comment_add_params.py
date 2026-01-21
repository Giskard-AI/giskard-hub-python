from __future__ import annotations

from typing import TypedDict
from typing_extensions import Required

__all__ = ["CommentAddParams"]


class CommentAddParams(TypedDict, total=False):
    comment: Required[str]
