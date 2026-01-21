from typing import Optional, Literal

from .._models import BaseModel

__all__ = ["GroundednessParams"]


class GroundednessParams(BaseModel):
    context: str

    type: Optional[Literal["groundedness"]] = None
