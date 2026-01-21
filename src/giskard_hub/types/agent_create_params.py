from __future__ import annotations

from typing import Iterable, Optional, TypedDict
from typing_extensions import Required

from .._types import SequenceNotStr
from .header_param import HeaderParam

__all__ = ["AgentCreateParams"]


class AgentCreateParams(TypedDict, total=False):
    headers: Required[Iterable[HeaderParam]]

    name: Required[str]

    project_id: Required[str]

    supported_languages: Required[SequenceNotStr[str]]

    url: Required[str]

    description: Optional[str]
