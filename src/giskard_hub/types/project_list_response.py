"""Project list response type.

Note: This type is equivalent to APIListResponse[ProjectAPIResource] from common.responses.
For new code, consider using the generic type instead.
"""

from typing import List

from .._models import BaseModel
from .project_api_resource import ProjectAPIResource

__all__ = ["ProjectListResponse"]


class ProjectListResponse(BaseModel):
    """Response containing a list of projects.
    
    This is equivalent to: APIListResponse[ProjectAPIResource]
    """

    data: List[ProjectAPIResource]
