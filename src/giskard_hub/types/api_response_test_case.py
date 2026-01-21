from typing import Dict, Optional

from .._models import BaseModel
from .test_case import TestCase

__all__ = ["APIResponseTestCase", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class APIResponseTestCase(BaseModel):
    data: TestCase

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
