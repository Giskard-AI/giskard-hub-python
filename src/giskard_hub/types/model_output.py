from typing import Dict, Optional

from ..types import ChatMessage, ExecutionError
from .._models import BaseModel

__all__ = ["AgentOutput"]


class AgentOutput(BaseModel):
    response: Optional[ChatMessage] = None

    error: Optional[ExecutionError] = None

    metadata: Optional[Dict[str, object]] = None
