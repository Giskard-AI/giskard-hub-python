from __future__ import annotations

from typing import TypedDict
from typing_extensions import Required

from .._types import SequenceNotStr

__all__ = ["PlaygroundChatBulkDeleteParams"]


class PlaygroundChatBulkDeleteParams(TypedDict, total=False):
    chat_ids: Required[SequenceNotStr[str]]
