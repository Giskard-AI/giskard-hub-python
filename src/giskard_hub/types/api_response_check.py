from .._models import BaseModel
from .check_api_resource import CheckAPIResource

__all__ = ["APIResponseCheck"]


class APIResponseCheck(BaseModel):
    data: CheckAPIResource
