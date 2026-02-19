from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["DatasetImportParams"]


class DatasetImportParams(TypedDict, total=False):
    project_id: str

    dataset_id: Optional[str]

    name: Optional[str]
