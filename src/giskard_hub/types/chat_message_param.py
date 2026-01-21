from __future__ import annotations

from typing import TypedDict
from typing_extensions import Required

__all__ = ["ChatMessageParam"]


class ChatMessageParam(TypedDict, total=False):
    content: Required[str]

    role: Required[str]
