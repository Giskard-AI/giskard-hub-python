
from typing import Dict, Optional

from .._models import BaseModel
from .scan_result import ScanResult

__all__ = ["ScanCreateResponse", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class ScanCreateResponse(BaseModel):
    data: ScanResult

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
