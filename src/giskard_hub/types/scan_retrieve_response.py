from typing import Dict, Union, Optional

from ..types import Agent, KnowledgeBase
from .._models import BaseModel
from .scan_result import ScanResult

__all__ = ["ScanRetrieveResponse", "IncludedItem"]


class IncludedItem(BaseModel):
    data: Union[Agent, KnowledgeBase]


class ScanRetrieveResponse(BaseModel):
    data: ScanResult

    included: Optional[Dict[str, Dict[str, IncludedItem]]] = None
