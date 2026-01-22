from __future__ import annotations

from typing import Iterable, TypedDict
from typing_extensions import Required

from .chat_message_param import ChatMessageParam

__all__ = ["AgentGenerateCompletionParams"]


class AgentGenerateCompletionParams(TypedDict, total=False):
    messages: Required[Iterable[ChatMessageParam]]
