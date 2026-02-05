"""Check list response type.

Note: This type is equivalent to APIListResponse[CheckAPIResource] from common.responses.
For new code, consider using the generic type instead.
"""

from typing import List

from .._models import BaseModel
from .check_api_resource import CheckAPIResource

__all__ = ["CheckListResponse"]


class CheckListResponse(BaseModel):
    """Response containing a list of checks.
    
    This is equivalent to: APIListResponse[CheckAPIResource]
    """

    data: List[CheckAPIResource]
