from .agent import Agent
from .._models import BaseModel

__all__ = ["APIResponseAgent"]


class APIResponseAgent(BaseModel):
    data: Agent
