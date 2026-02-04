from ..._models import BaseModel
from .scan_probe_attempt import ScanProbeAttempt

__all__ = ["AttemptUpdateResponse"]


class AttemptUpdateResponse(BaseModel):
    data: ScanProbeAttempt
