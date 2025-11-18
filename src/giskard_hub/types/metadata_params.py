
from typing import List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MetadataParams", "JsonPathRule"]


class JsonPathRule(BaseModel):
    expected_value: Union[bool, float, str]

    expected_value_type: Literal["string", "number", "boolean"]

    json_path: str


class MetadataParams(BaseModel):
    json_path_rules: List[JsonPathRule]

    type: Optional[Literal["metadata"]] = None
