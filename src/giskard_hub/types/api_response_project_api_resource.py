
from typing import Dict, Optional

from .._models import BaseModel
from .project_api_resource import ProjectAPIResource

__all__ = ["APIResponseProjectAPIResource", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class APIResponseProjectAPIResource(BaseModel):
    data: ProjectAPIResource

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
