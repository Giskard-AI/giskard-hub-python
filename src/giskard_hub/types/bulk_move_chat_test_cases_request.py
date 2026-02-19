from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BulkMoveChatTestCasesRequest"]


class BulkMoveChatTestCasesRequest(TypedDict, total=False):
    test_case_ids: list[str]

    target_dataset_id: str
