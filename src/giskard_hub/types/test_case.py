from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .chat_message import ChatMessage
from .test_case_check_config import TestCaseCheckConfig
from .chat_message_with_metadata import ChatMessageWithMetadata

__all__ = ["TestCase", "Comment", "TestCaseComment", "TestCaseCommentUser"]


class Comment(BaseModel):
    comment: str

    created_at: datetime
    """Date of creation"""

    updated_at: datetime
    """Date of the last modification"""

    user_id: str

    user_name: str

    uuid: Optional[str] = None


class TestCase(BaseModel):
    __test__ = False
    id: str

    checks: List[TestCaseCheckConfig]

    comments: List[Comment]

    created_at: datetime

    dataset_id: str

    demo_output: Optional[ChatMessageWithMetadata] = None

    messages: List[ChatMessage]

    tags: List[str]

    updated_at: datetime


class TestCaseCommentUser(BaseModel):
    id: str

    name: str


class TestCaseComment(BaseModel):
    __test__ = False
    id: str

    comment: str

    created_at: datetime

    updated_at: datetime

    user: TestCaseCommentUser
