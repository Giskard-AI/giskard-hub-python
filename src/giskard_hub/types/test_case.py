from typing import List, Optional
from datetime import datetime

from .user import UserReference
from .._models import BaseModel
from .chat_message import ChatMessage
from .test_case_check_config import TestCaseCheckConfig
from .chat_message_with_metadata import ChatMessageWithMetadata

__all__ = ["TestCase", "TestCaseComment"]


class TestCaseComment(BaseModel):
    __test__ = False

    id: str

    comment: str

    created_at: datetime

    updated_at: datetime

    user: UserReference


class TestCase(BaseModel):
    __test__ = False

    id: str

    checks: List[TestCaseCheckConfig]

    comments: List[TestCaseComment]

    created_at: datetime

    dataset_id: str

    demo_output: Optional[ChatMessageWithMetadata] = None

    messages: List[ChatMessage]

    tags: List[str]

    updated_at: datetime
