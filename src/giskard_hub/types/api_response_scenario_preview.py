from .._models import BaseModel
from .scenario_preview_api_resource import ScenarioPreviewAPIResource

__all__ = ["APIResponseScenarioPreview"]


class APIResponseScenarioPreview(BaseModel):
    data: ScenarioPreviewAPIResource
