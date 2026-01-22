from __future__ import annotations

from typing import Optional, TypedDict
from typing_extensions import Required

from ..model_output_param import ModelOutputParam

__all__ = ["ResultSubmitLocalOutputParams"]


class ResultSubmitLocalOutputParams(TypedDict, total=False):
    evaluation_id: Required[str]

    error: Optional[str]

    output: Optional[ModelOutputParam]
