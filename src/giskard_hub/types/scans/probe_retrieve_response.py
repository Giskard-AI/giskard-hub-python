
from typing import Dict, Optional

from ..._models import BaseModel
from .scan_probe_result import ScanProbeResult

__all__ = ["ProbeRetrieveResponse", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class ProbeRetrieveResponse(BaseModel):
    data: ScanProbeResult

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
