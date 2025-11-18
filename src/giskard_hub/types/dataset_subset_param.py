
from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["DatasetSubsetParam"]


class DatasetSubsetParam(TypedDict, total=False):
    dataset_id: Required[str]

    tags: Optional[SequenceNotStr[str]]

    target_type: Literal["dataset"]
