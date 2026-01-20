
from __future__ import annotations

from typing import List, Dict

from .._models import BaseModel

__all__ = ["ScenarioPreviewAPIResponse"]


class ScenarioPreviewAPIResponse(BaseModel):
    examples: List[Dict[str, object]]
