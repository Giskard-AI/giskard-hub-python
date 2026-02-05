from .._models import BaseModel

__all__ = ["APIResponseStr"]


class APIResponseStr(BaseModel):
    data: str
