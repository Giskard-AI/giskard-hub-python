
from .._models import BaseModel

__all__ = ["ChatMessage"]


class ChatMessage(BaseModel):
    content: str

    role: str
