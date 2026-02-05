from .navigation_info_api_resource import NavigationInfoAPIResource
from .._models import BaseModel

__all__ = ["APIResponseNavigationInfoAPIResource"]


class APIResponseNavigationInfoAPIResource(BaseModel):
    data: NavigationInfoAPIResource
