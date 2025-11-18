
from typing import Dict, Optional

from .._models import BaseModel
from .scan_result import ScanResult

__all__ = ["ScanRetrieveResponse", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class ScanRetrieveResponse(BaseModel):
    data: ScanResult

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
