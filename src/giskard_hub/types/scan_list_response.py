from typing import Dict, List, Union, Optional

from ..types import Agent, KnowledgeBase
from .._models import BaseModel
from .scan_result import ScanResult

__all__ = ["ScanListResponse", "IncludedItem"]


class IncludedItem(BaseModel):
    data: Union[Agent, KnowledgeBase]


class ScanListResponse(BaseModel):
    data: List[ScanResult]

    included: Optional[Dict[str, Dict[str, IncludedItem]]] = None
