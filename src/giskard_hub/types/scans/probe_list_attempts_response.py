
from typing import Dict, List, Optional

from ..._models import BaseModel
from .scan_probe_attempt import ScanProbeAttempt

__all__ = ["ProbeListAttemptsResponse", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class ProbeListAttemptsResponse(BaseModel):
    data: List[ScanProbeAttempt]

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
