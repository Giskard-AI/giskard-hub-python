
from .._models import BaseModel

__all__ = ["AgentAPIReference"]


class AgentAPIReference(BaseModel):
    id: str

    name: str
