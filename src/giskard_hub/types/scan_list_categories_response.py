from typing import List, Optional

from .._models import BaseModel

__all__ = ["ScanListCategoriesResponse", "ScanCategory"]


class ScanCategory(BaseModel):
    id: str

    description: str

    owasp_id: Optional[str] = None

    title: str


class ScanListCategoriesResponse(BaseModel):
    data: List[ScanCategory]
