from .._models import BaseModel
from .test_case import TestCase

__all__ = ["APIResponseTestCase"]


class APIResponseTestCase(BaseModel):
    data: TestCase
