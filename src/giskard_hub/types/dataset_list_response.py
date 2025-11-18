
from typing import Dict, List, Optional

from .dataset import Dataset
from .._models import BaseModel

__all__ = ["DatasetListResponse", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class DatasetListResponse(BaseModel):
    data: List[Dataset]

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
