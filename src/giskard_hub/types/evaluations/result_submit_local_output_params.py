from __future__ import annotations

from typing import Optional, TypedDict

from ..model_output_param import AgentOutputParam

__all__ = ["ResultSubmitLocalOutputParams"]


class ResultSubmitLocalOutputParams(TypedDict, total=False):
    error: Optional[str]

    output: Optional[AgentOutputParam]
