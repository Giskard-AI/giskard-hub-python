
from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["ChatMessageWithMetadata"]


class ChatMessageWithMetadata(BaseModel):
    content: str

    role: str

    metadata: Optional[Dict[str, object]] = None
