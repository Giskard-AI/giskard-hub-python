from ..._models import BaseModel
from .navigation_info_api_resource import NavigationInfoAPIResource

__all__ = ["APIResponseNavigationInfo"]


class APIResponseNavigationInfo(BaseModel):
    data: NavigationInfoAPIResource
