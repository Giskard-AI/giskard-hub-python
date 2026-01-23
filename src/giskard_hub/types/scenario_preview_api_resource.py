from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._models import BaseModel

__all__ = ["ScenarioPreviewAPIResource"]


class ScenarioPreviewAPIResource(BaseModel):
    preview_data: List[Dict[str, Any]]

    sample_count: int

    error: Optional[str] = None
