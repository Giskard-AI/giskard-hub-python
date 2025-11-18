
from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CommentEditParams"]


class CommentEditParams(TypedDict, total=False):
    test_case_id: Required[str]

    comment: Required[str]
