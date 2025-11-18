
from .._models import BaseModel

__all__ = ["Header"]


class Header(BaseModel):
    name: str

    value: str
