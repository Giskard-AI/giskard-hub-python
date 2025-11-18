
from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["DatasetGenerateDocumentBasedParams"]


class DatasetGenerateDocumentBasedParams(TypedDict, total=False):
    agent_id: Required[str]

    knowledge_base_id: Required[str]

    project_id: Required[str]

    dataset_name: str

    description: Optional[str]

    n_examples: int
    """Total number of examples to generate"""

    topic_ids: SequenceNotStr[str]
