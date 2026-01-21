from __future__ import annotations

from typing import Iterable, Optional, TypedDict

from .._types import SequenceNotStr
from .header_param import HeaderParam

__all__ = ["AgentUpdateParams"]


class AgentUpdateParams(TypedDict, total=False):
    description: Optional[str]

    headers: Optional[Iterable[HeaderParam]]

    name: Optional[str]

    supported_languages: Optional[SequenceNotStr[str]]

    url: Optional[str]
