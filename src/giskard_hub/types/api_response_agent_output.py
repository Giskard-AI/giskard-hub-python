from typing import Dict, Optional

from .._models import BaseModel
from .chat_message import ChatMessage
from .execution_error import ExecutionError

__all__ = ["APIResponseAgentOutput", "Data", "IncludedIncludedItem"]


class Data(BaseModel):
    error: Optional[ExecutionError] = None

    metadata: Dict[str, object]

    response: Optional[ChatMessage] = None


class IncludedIncludedItem(BaseModel):
    data: object


class APIResponseAgentOutput(BaseModel):
    data: Data

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
