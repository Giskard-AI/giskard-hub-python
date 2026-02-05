from typing import List, Union, Optional, TypeAlias
from datetime import datetime

from .._models import BaseModel
from .metadata_params import MetadataParams
from .conformity_params import ConformityParams
from .output_annotation import OutputAnnotation
from .correctness_params import CorrectnessParams
from .groundedness_params import GroundednessParams
from .string_match_params import StringMatchParams
from .evaluations.task_state import TaskState
from .semantic_similarity_params import SemanticSimilarityParams

__all__ = ["CheckAPIResource", "Assertion", "CheckResultAPIResource"]

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


class CheckResultAPIResource(BaseModel):
    annotations: Optional[List[OutputAnnotation]] = None

    display_name: Optional[str] = None

    error: Optional[str] = None

    name: str

    passed: Optional[bool] = None

    reason: Optional[str] = None

    status: TaskState
