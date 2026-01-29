from typing import List

from .._models import BaseModel
from .test_case import TestCase

__all__ = ["APIResponseListTestCase"]


class APIResponseListTestCase(BaseModel):
    data: List[TestCase]
