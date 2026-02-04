from .._models import BaseModel
from .scenario_api_resource import ScenarioAPIResource

__all__ = ["APIResponseScenario"]


class APIResponseScenario(BaseModel):
    data: ScenarioAPIResource
