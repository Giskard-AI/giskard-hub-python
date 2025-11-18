
from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConformityParams"]


class ConformityParams(BaseModel):
    rules: List[str]

    type: Optional[Literal["conformity"]] = None
