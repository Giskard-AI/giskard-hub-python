from typing import Dict, Optional

from .agent import Agent
from .._models import BaseModel

__all__ = ["APIResponseAgent", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class APIResponseAgent(BaseModel):
    data: Agent

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
