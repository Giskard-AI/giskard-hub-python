
from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["MinimalModelParam"]


class MinimalModelParamTyped(TypedDict, total=False):
    name: Required[str]

    description: Optional[str]


MinimalModelParam: TypeAlias = Union[MinimalModelParamTyped, Dict[str, object]]
