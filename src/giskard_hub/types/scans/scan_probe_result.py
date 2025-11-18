
from typing import List, Optional

from .severity import Severity
from ..._models import BaseModel
from ..task_progress import TaskProgress

__all__ = ["ScanProbeResult", "Metric"]


class Metric(BaseModel):
    count: int

    severity: Severity


class ScanProbeResult(BaseModel):
    id: str

    metrics: Optional[List[Metric]] = None

    probe_category: str

    probe_description: str

    probe_lidar_id: str

    probe_name: str

    probe_tags: List[str]

    scan_result_id: str

    status: TaskProgress
