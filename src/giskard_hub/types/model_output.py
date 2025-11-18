
from typing import Dict, Optional

from .._models import BaseModel
from .chat_message import ChatMessage
from .execution_error import ExecutionError

__all__ = ["ModelOutput"]


class ModelOutput(BaseModel):
    response: Optional[ChatMessage] = None

    error: Optional[ExecutionError] = None

    metadata: Optional[Dict[str, object]] = None
