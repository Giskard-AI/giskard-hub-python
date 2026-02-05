from typing import Dict, List, Optional
from datetime import datetime

from .header import Header
from .._models import BaseModel
from .chat_message import ChatMessage
from .execution_error import ExecutionError

__all__ = ["Agent"]


class Agent(BaseModel):
    id: str

    created_at: datetime

    description: Optional[str] = None

    headers: List[Header]

    name: str

    project_id: str

    supported_languages: List[str]

    updated_at: datetime

    url: str


class AgentOutput(BaseModel):
    error: Optional[ExecutionError] = None

    metadata: Dict[str, object]

    response: Optional[ChatMessage] = None
