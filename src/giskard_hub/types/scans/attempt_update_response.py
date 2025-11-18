
from typing import Dict, Optional

from ..._models import BaseModel
from .scan_probe_attempt import ScanProbeAttempt

__all__ = ["AttemptUpdateResponse", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class AttemptUpdateResponse(BaseModel):
    data: ScanProbeAttempt

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
