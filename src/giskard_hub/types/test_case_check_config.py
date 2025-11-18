
from typing import List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .metadata_params import MetadataParams
from .conformity_params import ConformityParams
from .correctness_params import CorrectnessParams
from .groundedness_params import GroundednessParams
from .string_match_params import StringMatchParams
from .semantic_similarity_params import SemanticSimilarityParams

__all__ = ["TestCaseCheckConfig", "Assertion"]

Assertion: TypeAlias = Union[
    CorrectnessParams, ConformityParams, GroundednessParams, StringMatchParams, MetadataParams, SemanticSimilarityParams
]


class TestCaseCheckConfig(BaseModel):
    __test__ = False
    identifier: str

    assertions: Optional[List[Assertion]] = None

    enabled: Optional[bool] = None
