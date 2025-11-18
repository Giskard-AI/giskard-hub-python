
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["OutputAnnotation"]


class OutputAnnotation(BaseModel):
    end_char_index: int

    label: str

    start_char_index: int

    text: str

    type: Literal["output"]
