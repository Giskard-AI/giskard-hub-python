
from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CommentAddParams"]


class CommentAddParams(TypedDict, total=False):
    comment: Required[str]
