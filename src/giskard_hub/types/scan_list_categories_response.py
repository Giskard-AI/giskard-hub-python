from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["ScanListCategoriesResponse", "Data", "IncludedIncludedItem"]


class Data(BaseModel):
    id: str

    description: str

    owasp_id: Optional[str] = None

    title: str


class IncludedIncludedItem(BaseModel):
    data: object


class ScanListCategoriesResponse(BaseModel):
    data: List[Data]

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
