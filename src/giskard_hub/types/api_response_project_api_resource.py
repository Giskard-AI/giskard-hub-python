from .._models import BaseModel
from .project_api_resource import ProjectAPIResource

__all__ = ["APIResponseProjectAPIResource"]


class APIResponseProjectAPIResource(BaseModel):
    data: ProjectAPIResource
