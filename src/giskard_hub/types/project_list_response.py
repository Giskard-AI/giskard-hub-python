from typing import Dict, List, Optional

from .._models import BaseModel
from .project_api_resource import ProjectAPIResource

__all__ = ["ProjectListResponse", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class ProjectListResponse(BaseModel):
    data: List[ProjectAPIResource]

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
