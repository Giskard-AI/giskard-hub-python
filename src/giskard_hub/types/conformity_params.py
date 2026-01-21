from typing import Literal, List, Optional

from .._models import BaseModel

__all__ = ["ConformityParams"]


class ConformityParams(BaseModel):
    rules: List[str]

    type: Optional[Literal["conformity"]] = None
