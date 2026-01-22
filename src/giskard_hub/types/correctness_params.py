from typing import Literal, Optional

from .._models import BaseModel

__all__ = ["CorrectnessParams"]


class CorrectnessParams(BaseModel):
    reference: str

    type: Optional[Literal["correctness"]] = None
