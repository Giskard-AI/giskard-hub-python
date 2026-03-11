from typing import Optional

from .._models import BaseModel

__all__ = ["MinimalAgent"]


class MinimalAgent(BaseModel):
    name: str

    description: Optional[str] = None
