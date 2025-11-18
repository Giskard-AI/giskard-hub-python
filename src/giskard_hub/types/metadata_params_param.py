
from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MetadataParamsParam", "JsonPathRule"]


class JsonPathRule(TypedDict, total=False):
    expected_value: Required[Union[bool, float, str]]

    expected_value_type: Required[Literal["string", "number", "boolean"]]

    json_path: Required[str]


class MetadataParamsParam(TypedDict, total=False):
    json_path_rules: Required[Iterable[JsonPathRule]]

    type: Literal["metadata"]
