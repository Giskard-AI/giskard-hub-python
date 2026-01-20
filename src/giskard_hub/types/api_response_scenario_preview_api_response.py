
from __future__ import annotations

from .._models import BaseModel
from .scenario_preview_api_response import ScenarioPreviewAPIResponse

__all__ = ["APIResponseScenarioPreviewAPIResponse"]


class APIResponseScenarioPreviewAPIResponse(BaseModel):
    data: ScenarioPreviewAPIResponse
