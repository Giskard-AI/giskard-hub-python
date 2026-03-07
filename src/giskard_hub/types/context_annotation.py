from typing import Literal

from .._models import BaseModel

__all__ = ["ContextAnnotation"]


class ContextAnnotation(BaseModel):
    end_char_index: int

    label: str

    start_char_index: int

    text: str

    type: Literal["context"]
