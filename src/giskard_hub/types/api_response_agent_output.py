from typing import Dict, Optional

from .._models import BaseModel
from .chat_message import ChatMessage
from .execution_error import ExecutionError

__all__ = ["APIResponseAgentOutput", "Data"]


class Data(BaseModel):
    error: Optional[ExecutionError] = None

    metadata: Dict[str, object]

    response: Optional[ChatMessage] = None


class APIResponseAgentOutput(BaseModel):
    data: Data
