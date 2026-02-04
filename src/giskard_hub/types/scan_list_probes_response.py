from typing import List

from .._models import BaseModel
from .scans.scan_probe_result import ScanProbeResult

__all__ = ["ScanListProbesResponse"]


class ScanListProbesResponse(BaseModel):
    data: List[ScanProbeResult]
