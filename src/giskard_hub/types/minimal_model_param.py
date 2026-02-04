from __future__ import annotations

from typing import Dict, Union, Optional, TypeAlias, TypedDict
from typing_extensions import Required

__all__ = ["MinimalModelParam", "MinimalAgentParam"]


class MinimalModelParamTyped(TypedDict, total=False):
    name: Required[str]

    description: Optional[str]


MinimalModelParam: TypeAlias = Union[MinimalModelParamTyped, Dict[str, object]]

MinimalAgentParam = MinimalModelParam
