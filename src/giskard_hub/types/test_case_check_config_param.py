from __future__ import annotations

from typing import Union, Iterable, Optional, TypeAlias, TypedDict
from typing_extensions import Required

from .metadata_params_param import MetadataParamsParam
from .conformity_params_param import ConformityParamsParam
from .correctness_params_param import CorrectnessParamsParam
from .groundedness_params_param import GroundednessParamsParam
from .string_match_params_param import StringMatchParamsParam
from .semantic_similarity_params_param import SemanticSimilarityParamsParam

__all__ = ["TestCaseCheckConfigParam", "Assertion"]

Assertion: TypeAlias = Union[
    CorrectnessParamsParam,
    ConformityParamsParam,
    GroundednessParamsParam,
    StringMatchParamsParam,
    MetadataParamsParam,
    SemanticSimilarityParamsParam,
]


class TestCaseCheckConfigParam(TypedDict, total=False):
    identifier: Required[str]

    assertions: Optional[Iterable[Assertion]]

    enabled: bool
