from typing import List

from .._models import BaseModel

__all__ = ["DatasetListTagsResponse"]


class DatasetListTagsResponse(BaseModel):
    data: List[str]
