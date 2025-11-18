
from typing import Dict, Optional

from .dataset import Dataset
from .._models import BaseModel

__all__ = ["APIResponseDataset", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class APIResponseDataset(BaseModel):
    data: Dataset

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
