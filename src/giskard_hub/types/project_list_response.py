from typing import List

from .._models import BaseModel
from .project_api_resource import ProjectAPIResource

__all__ = ["ProjectListResponse"]


class ProjectListResponse(BaseModel):
    data: List[ProjectAPIResource]
