
from typing import Dict, List, Optional

from .._models import BaseModel
from .scan_result import ScanResult

__all__ = ["ScanListResponse", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class ScanListResponse(BaseModel):
    data: List[ScanResult]

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
