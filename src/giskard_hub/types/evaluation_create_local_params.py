from __future__ import annotations

from typing import Union, Literal, Iterable, Optional, TypeAlias, TypedDict
from typing_extensions import Required

from ..types import MinimalAgentParam, DatasetSubsetParam

__all__ = ["EvaluationCreateLocalParams", "Criterion", "CriterionEvaluationDataset"]


class EvaluationCreateLocalParams(TypedDict, total=False):
    criteria: Required[Iterable[Criterion]]

    model: Required[MinimalAgentParam]

    name: Optional[str]


class CriterionEvaluationDataset(TypedDict, total=False):
    evaluation_id: Required[str]

    target_type: Literal["evaluation"]


Criterion: TypeAlias = Union[DatasetSubsetParam, CriterionEvaluationDataset]
