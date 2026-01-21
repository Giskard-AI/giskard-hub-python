from __future__ import annotations

from typing import Union, Iterable, Optional, Literal, TypeAlias, TypedDict
from typing_extensions import Required

from .minimal_model_param import MinimalModelParam
from .dataset_subset_param import DatasetSubsetParam

__all__ = ["EvaluationCreateLocalParams", "Criterion", "CriterionEvaluationDataset"]


class EvaluationCreateLocalParams(TypedDict, total=False):
    criteria: Required[Iterable[Criterion]]

    model: Required[MinimalModelParam]

    name: Optional[str]


class CriterionEvaluationDataset(TypedDict, total=False):
    evaluation_id: Required[str]

    target_type: Literal["evaluation"]


Criterion: TypeAlias = Union[DatasetSubsetParam, CriterionEvaluationDataset]
