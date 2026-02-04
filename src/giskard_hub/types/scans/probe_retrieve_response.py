from ..._models import BaseModel
from .scan_probe_result import ScanProbeResult

__all__ = ["ProbeRetrieveResponse"]


class ProbeRetrieveResponse(BaseModel):
    data: ScanProbeResult
