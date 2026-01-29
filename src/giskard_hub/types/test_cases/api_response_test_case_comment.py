from datetime import datetime

from ..._models import BaseModel

__all__ = ["APIResponseTestCaseComment", "Data", "DataUser"]


class DataUser(BaseModel):
    id: str

    name: str


class Data(BaseModel):
    id: str

    comment: str

    created_at: datetime

    updated_at: datetime

    user: DataUser


class APIResponseTestCaseComment(BaseModel):
    data: Data
