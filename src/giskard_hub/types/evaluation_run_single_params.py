from __future__ import annotations

from typing import Dict, Iterable, Optional, TypedDict
from typing_extensions import Required

from .chat_message_param import ChatMessageParam
from .model_output_param import ModelOutputParam

__all__ = ["EvaluationRunSingleParams"]


class EvaluationRunSingleParams(TypedDict, total=False):
    checks: Required[Iterable[Dict[str, object]]]

    messages: Required[Iterable[ChatMessageParam]]

    model_output: Required[ModelOutputParam]

    model_description: str

    project_id: Optional[str]
