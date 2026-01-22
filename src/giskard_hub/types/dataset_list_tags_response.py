from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["DatasetListTagsResponse", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class DatasetListTagsResponse(BaseModel):
    data: List[str]

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
