"""Playground chat domain types."""

from typing import Any, Dict, List, Literal, Iterable, Optional, TypedDict, cast
from datetime import datetime
from typing_extensions import Required, deprecated

from .chat import ChatMessageWithMetadata
from .user import UserReference
from .agent import Agent, AgentReference
from .._types import SequenceNotStr
from .._models import BaseModel

__all__ = [
    "PlaygroundChat",
    "PlaygroundExchange",
    "PlaygroundChatListParams",
    "PlaygroundChatCreateParams",
    "PlaygroundChatUpdateParams",
    "PlaygroundChatRetrieveParams",
    "PlaygroundChatBulkDeleteParams",
]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class PlaygroundExchange(BaseModel):
    input: Dict[str, Any]
    output: Dict[str, Any]
    metadata: Optional[Dict[str, Any]] = None


class PlaygroundChat(BaseModel):
    id: str
    project_id: str
    created_at: datetime
    updated_at: datetime
    user: Optional[UserReference] = None
    agent: Optional[AgentReference | Agent] = None
    agent_id: Optional[str] = None
    user_id: Optional[str] = None
    exchanges: List[PlaygroundExchange] = []

    @property
    @deprecated("`PlaygroundChat.messages` is deprecated; read `exchanges` directly.")
    def messages(self) -> List[ChatMessageWithMetadata]:
        """Deprecated flattened view of `exchanges`.

        Each exchange is unfolded into its user message (from `input.messages[-1]`
        when present, else the raw input dict) followed by the assistant
        response (from `output.response` when present, else the raw output
        dict). Prefer reading `chat.exchanges` directly.
        """
        out: List[ChatMessageWithMetadata] = []
        for exchange in self.exchanges or []:
            inp = exchange.input
            input_msgs = inp.get("messages")
            if isinstance(input_msgs, list) and input_msgs:
                last = cast(Any, input_msgs[-1])
                if isinstance(last, dict):
                    last_d = cast(Dict[str, Any], last)
                    role, content = last_d.get("role"), last_d.get("content")
                    if isinstance(role, str) and isinstance(content, str):
                        out.append(ChatMessageWithMetadata(role=role, content=content))
            elif "role" in inp and "content" in inp:
                role, content = inp.get("role"), inp.get("content")
                if isinstance(role, str) and isinstance(content, str):
                    out.append(ChatMessageWithMetadata(role=role, content=content))

            outp = exchange.output
            response = (outp.get("response") or outp) if outp is not None else None
            if isinstance(response, dict):
                resp_d = cast(Dict[str, Any], response)
                role, content = resp_d.get("role"), resp_d.get("content")
                if isinstance(role, str) and isinstance(content, str):
                    out.append(
                        ChatMessageWithMetadata(
                            role=role,
                            content=content,
                            metadata=exchange.metadata,
                        )
                    )
        return out


# ---------------------------------------------------------------------------
# Params
# ---------------------------------------------------------------------------


class PlaygroundExchangeParam(TypedDict, total=False):
    input: Required[Dict[str, Any]]
    output: Required[Dict[str, Any]]
    metadata: Optional[Dict[str, Any]]


class PlaygroundChatCreateParams(TypedDict, total=False):
    project_id: Required[str]
    agent_id: Optional[str]
    exchanges: Optional[Iterable[PlaygroundExchangeParam]]


class PlaygroundChatUpdateParams(TypedDict, total=False):
    agent_id: Optional[str]
    exchanges: Optional[Iterable[PlaygroundExchangeParam]]


class PlaygroundChatListParams(TypedDict, total=False):
    project_id: str
    include: Optional[List[Literal["agent"]]]
    limit: Optional[int]
    offset: Optional[int]


class PlaygroundChatRetrieveParams(TypedDict, total=False):
    include: Optional[List[Literal["agent"]]]


class PlaygroundChatBulkDeleteParams(TypedDict, total=False):
    chat_ids: Required[SequenceNotStr[str]]
