from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["APIResponseNone", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class APIResponseNone(BaseModel):
    data: None = None

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
