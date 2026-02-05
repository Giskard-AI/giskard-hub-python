from typing import Optional

from .._types import Omit, SequenceNotStr, omit
from .._models import BaseModel

__all__ = ["ExportChatTestCasesRequest"]


class ExportChatTestCasesRequest(BaseModel):
    test_case_ids: SequenceNotStr[str] | Omit = omit
    """IDs of the test cases to export"""
