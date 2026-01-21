from __future__ import annotations

from typing import Union, Iterable, Optional, TypeAlias, TypedDict
from typing_extensions import Required

from .metadata_params_param import MetadataParamsParam
from .conformity_params_param import ConformityParamsParam
from .correctness_params_param import CorrectnessParamsParam
from .groundedness_params_param import GroundednessParamsParam
from .string_match_params_param import StringMatchParamsParam
from .semantic_similarity_params_param import SemanticSimilarityParamsParam

__all__ = ["CheckCreateParams", "Assertion"]


class CheckCreateParams(TypedDict, total=False):
    assertions: Required[Iterable[Assertion]]

    description: Required[Optional[str]]

    identifier: Required[str]

    name: Required[str]

    project_id: Required[str]


Assertion: TypeAlias = Union[
    CorrectnessParamsParam,
    ConformityParamsParam,
    GroundednessParamsParam,
    StringMatchParamsParam,
    MetadataParamsParam,
    SemanticSimilarityParamsParam,
]
