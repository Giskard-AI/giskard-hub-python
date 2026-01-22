from typing import Dict, List, Optional

from .agent import Agent
from .._models import BaseModel

__all__ = ["AgentListResponse", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class AgentListResponse(BaseModel):
    data: List[Agent]

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
