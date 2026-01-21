from __future__ import annotations

from typing import Iterable, Optional, TypedDict
from typing_extensions import Required

__all__ = ["DatasetGenerateAdversarialParams", "Category"]


class DatasetGenerateAdversarialParams(TypedDict, total=False):
    agent_id: Required[str]

    project_id: Required[str]

    categories: Iterable[Category]

    dataset_name: str

    description: Optional[str]

    n_examples_per_category: int
    """Number of examples to generate for each category"""


class Category(TypedDict, total=False):
    desc: Required[str]

    name: Required[str]

    id: Optional[str]
