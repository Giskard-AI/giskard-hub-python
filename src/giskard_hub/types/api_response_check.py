
from typing import Dict, Optional

from .._models import BaseModel
from .check_api_resource import CheckAPIResource

__all__ = ["APIResponseCheck", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class APIResponseCheck(BaseModel):
    data: CheckAPIResource

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
