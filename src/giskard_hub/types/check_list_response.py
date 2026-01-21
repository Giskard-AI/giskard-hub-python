from typing import Dict, List, Optional

from .._models import BaseModel
from .check_api_resource import CheckAPIResource

__all__ = ["CheckListResponse", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class CheckListResponse(BaseModel):
    data: List[CheckAPIResource]

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
