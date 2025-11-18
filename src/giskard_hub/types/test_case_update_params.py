
from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .chat_message_param import ChatMessageParam
from .test_case_check_config_param import TestCaseCheckConfigParam
from .chat_message_with_metadata_param import ChatMessageWithMetadataParam

__all__ = ["TestCaseUpdateParams"]


class TestCaseUpdateParams(TypedDict, total=False):
    checks: Optional[Iterable[TestCaseCheckConfigParam]]

    dataset_id: Optional[str]

    demo_output: Optional[ChatMessageWithMetadataParam]

    messages: Optional[Iterable[ChatMessageParam]]

    tags: Optional[SequenceNotStr[str]]
