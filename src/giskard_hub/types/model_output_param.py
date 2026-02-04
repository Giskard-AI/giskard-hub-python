from __future__ import annotations

from typing import Dict, Optional, TypedDict
from typing_extensions import Required

from .chat_message_param import ChatMessageParam
from .execution_error_param import ExecutionErrorParam

__all__ = ["ModelOutputParam", "AgentOutputParam"]


class ModelOutputParam(TypedDict, total=False):
    response: Required[Optional[ChatMessageParam]]

    error: Optional[ExecutionErrorParam]

    metadata: Dict[str, object]


AgentOutputParam = ModelOutputParam
