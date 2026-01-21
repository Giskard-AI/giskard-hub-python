from __future__ import annotations

from typing import Literal, Optional, TypedDict
from typing_extensions import Required

from .._types import SequenceNotStr

__all__ = ["DatasetSubsetParam"]


class DatasetSubsetParam(TypedDict, total=False):
    dataset_id: Required[str]

    tags: Optional[SequenceNotStr[str]]

    target_type: Literal["dataset"]
