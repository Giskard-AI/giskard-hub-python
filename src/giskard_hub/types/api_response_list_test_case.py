
from typing import Dict, List, Optional

from .._models import BaseModel
from .test_case import TestCase

__all__ = ["APIResponseListTestCase", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class APIResponseListTestCase(BaseModel):
    data: List[TestCase]

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
