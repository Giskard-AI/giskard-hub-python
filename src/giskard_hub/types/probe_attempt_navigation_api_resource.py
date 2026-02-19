from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["ProbeAttemptNavigationAPIResource"]


class ProbeAttemptNavigationAPIResource(BaseModel):
    probe_attempt_id: str

    previous_id: Optional[str] = None

    next_id: Optional[str] = None

    current_index: Optional[int] = None

    total_count: Optional[int] = None
