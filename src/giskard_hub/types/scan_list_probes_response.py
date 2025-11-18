
from typing import Dict, List, Optional

from .._models import BaseModel
from .scans.scan_probe_result import ScanProbeResult

__all__ = ["ScanListProbesResponse", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class ScanListProbesResponse(BaseModel):
    data: List[ScanProbeResult]

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
