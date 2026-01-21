from __future__ import annotations

from typing import Optional, TypedDict
from typing_extensions import Required

from .dataset_subset_param import DatasetSubsetParam

__all__ = ["EvaluationCreateParams"]


class EvaluationCreateParams(TypedDict, total=False):
    agent_id: Required[str]

    project_id: Required[str]

    criteria: Optional[DatasetSubsetParam]

    name: str

    old_evaluation_id: Optional[str]

    run_count: int
    """
    The number of times to run each test case. This is useful to get a more accurate
    result when the chatbot's generation is not deterministic. Testing stops at the
    first failure. If all runs pass, the test case is considered successful.
    """

    scheduled_evaluation_id: Optional[str]
