from typing import Dict, List, Optional

from .severity import Severity
from ..._models import BaseModel
from .review_status import ReviewStatus
from ..chat_message_with_metadata import ChatMessageWithMetadata

__all__ = ["ScanProbeAttempt", "Error"]


class Error(BaseModel):
    message: str


class ScanProbeAttempt(BaseModel):
    id: str

    error: Optional[Error] = None

    messages: List[ChatMessageWithMetadata]

    metadata: Dict[str, object]

    probe_result_id: str

    reason: str

    review_status: ReviewStatus

    severity: Severity
