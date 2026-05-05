"""Tests for backward-compatible property accessors that synthesize the
pre-v3 `.messages` view from new-API fields.

Each accessor is `@deprecated`, so we exercise it under
`pytest.deprecated_call()` to assert both the warning and the value.
"""
# pyright: reportDeprecated=false

import pytest

from giskard_hub.types.scan import ScanProbeAttempt
from giskard_hub.types.agent import GenerateCompletionOutput
from giskard_hub.types.playground_chat import PlaygroundChat, PlaygroundExchange


def test_playground_chat_messages_synthesized_from_exchanges() -> None:
    chat = PlaygroundChat.model_construct(  # type: ignore[arg-type]
        id="c-1",
        project_id="p",
        exchanges=[
            PlaygroundExchange.model_construct(
                input={"messages": [{"role": "user", "content": "hi"}]},
                output={"response": {"role": "assistant", "content": "hello"}},
                metadata={"k": "v"},
            ),
        ],
    )
    with pytest.deprecated_call():
        msgs = chat.messages
    assert [(m.role, m.content) for m in msgs] == [("user", "hi"), ("assistant", "hello")]
    assert msgs[1].metadata == {"k": "v"}


def test_playground_chat_messages_handles_empty_exchanges() -> None:
    chat = PlaygroundChat.model_construct(id="c-1", project_id="p", exchanges=[])  # type: ignore[arg-type]
    with pytest.deprecated_call():
        assert chat.messages == []


def test_scan_probe_attempt_messages_pairs_chat_input_and_response() -> None:
    """Chat-style probe: input.messages → user turns, output.response → assistant."""
    attempt = ScanProbeAttempt.model_construct(  # type: ignore[arg-type]
        id="a-1",
        input={"messages": [{"role": "user", "content": "attack prompt"}]},
        output={"response": {"role": "assistant", "content": "model reply"}},
        metadata={},
        probe_result_id="p-1",
        reason="x",
        review_status="pending",
        severity=10,
    )
    with pytest.deprecated_call():
        msgs = attempt.messages
    assert [(m.role, m.content) for m in msgs] == [
        ("user", "attack prompt"),
        ("assistant", "model reply"),
    ]


def test_scan_probe_attempt_messages_falls_back_to_probe_text() -> None:
    """Non-chat probe: input.probe_text + dict output get json-dumped reasonably."""
    attempt = ScanProbeAttempt.model_construct(  # type: ignore[arg-type]
        id="a-1",
        input={"probe_text": "decode this"},
        output={"output": "decoded payload"},
        metadata={},
        probe_result_id="p-1",
        reason="x",
        review_status="pending",
        severity=10,
    )
    with pytest.deprecated_call():
        msgs = attempt.messages
    assert msgs[0].role == "user"
    assert msgs[0].content == "decode this"
    assert msgs[1].role == "assistant"
    # json-dumped output dict
    assert "decoded payload" in msgs[1].content


def test_generate_completion_output_response_extracts_chat_message() -> None:
    out = GenerateCompletionOutput(
        output={"response": {"role": "assistant", "content": "hi"}, "metadata": {"k": "v"}},
    )
    with pytest.deprecated_call():
        response = out.response
    assert response is not None
    assert response.role == "assistant"
    assert response.content == "hi"
    with pytest.deprecated_call():
        message = out.message
    assert message is not None
    assert message.role == "assistant"
    assert message.content == "hi"


def test_generate_completion_output_response_returns_none_for_unstructured_output() -> None:
    out = GenerateCompletionOutput(output={"foo": "bar"})
    with pytest.deprecated_call():
        assert out.response is None
