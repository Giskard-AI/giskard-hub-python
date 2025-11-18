
from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CorrectnessParams"]


class CorrectnessParams(BaseModel):
    reference: str

    type: Optional[Literal["correctness"]] = None
