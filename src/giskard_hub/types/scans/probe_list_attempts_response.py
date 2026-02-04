from typing import List

from ..._models import BaseModel
from .scan_probe_attempt import ScanProbeAttempt

__all__ = ["ProbeListAttemptsResponse"]


class ProbeListAttemptsResponse(BaseModel):
    data: List[ScanProbeAttempt]
