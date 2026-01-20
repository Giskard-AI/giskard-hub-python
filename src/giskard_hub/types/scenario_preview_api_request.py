
from __future__ import annotations

from typing import Dict, List

from .._models import BaseModel

__all__ = ["ScenarioPreviewAPIRequest"]


class ScenarioPreviewAPIRequest(BaseModel):
    scenario: Dict[str, object]

    variables: List[Dict[str, str]]
