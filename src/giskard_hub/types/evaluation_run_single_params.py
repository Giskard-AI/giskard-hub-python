from __future__ import annotations

from typing import Dict, Iterable, Optional, TypedDict
from typing_extensions import Required

from ..types import AgentOutputParam
from .chat_message_param import ChatMessageParam

__all__ = ["EvaluationRunSingleParams"]


class EvaluationRunSingleParams(TypedDict, total=False):
    checks: Required[Iterable[Dict[str, object]]]

    messages: Required[Iterable[ChatMessageParam]]

    model_output: Required[AgentOutputParam]

    model_description: str

    project_id: Optional[str]
