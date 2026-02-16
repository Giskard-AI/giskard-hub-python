"""Simple test case API resource type."""

from __future__ import annotations

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["SimpleTestCaseAPIResource"]


class SimpleTestCaseAPIResource(BaseModel):
    """Simplified test case representation for search results."""

    __test__ = False

    id: str

    created_at: datetime

    dataset_id: str

    tags: List[str]

    updated_at: datetime
