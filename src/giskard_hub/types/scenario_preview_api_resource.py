from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._models import BaseModel

__all__ = ["ScenarioPreviewAPIResource"]


class ScenarioPreviewAPIResource(BaseModel):
    conversation: List[Dict[str, Any]]
    generated_rules: Optional[List[str]]
