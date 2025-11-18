
from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["APIResponseTestCaseComment", "Data", "DataUser", "IncludedIncludedItem"]


class DataUser(BaseModel):
    id: str

    name: str


class Data(BaseModel):
    id: str

    comment: str

    created_at: datetime

    updated_at: datetime

    user: DataUser


class IncludedIncludedItem(BaseModel):
    data: object


class APIResponseTestCaseComment(BaseModel):
    data: Data

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
