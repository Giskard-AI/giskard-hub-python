from .._models import BaseModel

__all__ = ["APIResponseNone"]


class APIResponseNone(BaseModel):
    data: None = None
