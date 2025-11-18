
from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["StringMatchParams"]


class StringMatchParams(BaseModel):
    keyword: str

    type: Optional[Literal["string_match"]] = None
