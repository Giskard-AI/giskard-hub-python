from .._models import BaseModel
from .scan_result import ScanResult

__all__ = ["ScanCreateResponse"]


class ScanCreateResponse(BaseModel):
    data: ScanResult
