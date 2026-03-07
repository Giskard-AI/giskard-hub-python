from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["BulkMoveTestCasesParams"]


class BulkMoveTestCasesParams(TypedDict, total=False):
    chat_test_case_ids: Required[SequenceNotStr[str]]

    dataset_id: Required[str]

    duplicate: Optional[bool]
