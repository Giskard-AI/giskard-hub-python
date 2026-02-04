from .dataset import Dataset
from .._models import BaseModel

__all__ = ["APIResponseDataset"]


class APIResponseDataset(BaseModel):
    data: Dataset
