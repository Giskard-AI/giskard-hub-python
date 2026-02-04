from typing import List

from .._models import BaseModel
from .check_api_resource import CheckAPIResource

__all__ = ["CheckListResponse"]


class CheckListResponse(BaseModel):
    data: List[CheckAPIResource]
