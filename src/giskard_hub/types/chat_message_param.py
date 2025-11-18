
from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ChatMessageParam"]


class ChatMessageParam(TypedDict, total=False):
    content: Required[str]

    role: Required[str]
