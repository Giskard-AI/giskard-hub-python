from typing import List, Optional, Literal

from .._models import BaseModel

__all__ = ["DatasetSubset"]


class DatasetSubset(BaseModel):
    dataset_id: str

    tags: Optional[List[str]] = None

    target_type: Optional[Literal["dataset"]] = None
