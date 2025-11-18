
from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel
from .metadata_params import MetadataParams
from .conformity_params import ConformityParams
from .correctness_params import CorrectnessParams
from .groundedness_params import GroundednessParams
from .string_match_params import StringMatchParams
from .semantic_similarity_params import SemanticSimilarityParams

__all__ = ["CheckAPIResource", "Assertion"]

Assertion: TypeAlias = Union[
    CorrectnessParams, ConformityParams, GroundednessParams, StringMatchParams, MetadataParams, SemanticSimilarityParams
]


class CheckAPIResource(BaseModel):
    id: str

    assertions: Optional[List[Assertion]] = None

    built_in: bool

    created_at: datetime

    description: Optional[str] = None

    identifier: str

    name: str

    project_id: str

    updated_at: datetime
