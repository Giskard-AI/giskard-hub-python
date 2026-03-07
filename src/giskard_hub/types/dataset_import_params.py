from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["DatasetImportParams"]


class DatasetImportParams(TypedDict, total=False):
    file: Required[FileTypes]

    project_id: Required[str]

    dataset_id: Optional[str]

    name: Optional[str]
