from typing import List

from .._models import BaseModel
from .scenario_api_resource import ScenarioAPIResource

__all__ = ["APIResponseListScenario"]


class APIResponseListScenario(BaseModel):
    data: List[ScenarioAPIResource]
