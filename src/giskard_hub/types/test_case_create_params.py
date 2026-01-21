from __future__ import annotations

from typing import Iterable, Optional, TypedDict
from typing_extensions import Required

from .._types import SequenceNotStr
from .chat_message_param import ChatMessageParam
from .test_case_check_config_param import TestCaseCheckConfigParam
from .chat_message_with_metadata_param import ChatMessageWithMetadataParam

__all__ = ["TestCaseCreateParams"]


class TestCaseCreateParams(TypedDict, total=False):
    dataset_id: Required[str]

    messages: Required[Iterable[ChatMessageParam]]

    checks: Iterable[TestCaseCheckConfigParam]

    demo_output: Optional[ChatMessageWithMetadataParam]

    tags: SequenceNotStr[str]
