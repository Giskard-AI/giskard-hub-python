from __future__ import annotations

from typing import TypedDict
from typing_extensions import Required

__all__ = ["CommentEditParams"]


class CommentEditParams(TypedDict, total=False):
    test_case_id: Required[str]

    comment: Required[str]
