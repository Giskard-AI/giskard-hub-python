from .._models import BaseModel
from .navigation_info_api_resource import NavigationInfoAPIResource

__all__ = ["APIResponseNavigationInfoAPIResource"]


class APIResponseNavigationInfoAPIResource(BaseModel):
    data: NavigationInfoAPIResource
