"""Tests for `AgentsResource.generate_completion` argument coercion."""

from typing import Any, Dict

import pytest

from giskard_hub._types import omit
from giskard_hub.resources._check_helpers import coerce_messages_to_input_dict


def _coerce(input: object = omit, messages: object = omit) -> Dict[str, Any]:
    """Invoke the shared coercer with `agents.generate_completion`'s param names."""
    return coerce_messages_to_input_dict(
        input=input,  # type: ignore[arg-type]
        messages=messages,  # type: ignore[arg-type]
        new_param="input",
        deprecated_param="messages",
        method_name="agents.generate_completion",
    )


def test_passes_dict_through_unchanged() -> None:
    payload = {"messages": [{"role": "user", "content": "hi"}]}
    out = _coerce(input=payload)
    assert out == payload
    assert out is not payload  # defensive copy


def test_wraps_legacy_messages_under_messages_key() -> None:
    with pytest.deprecated_call():
        out = _coerce(messages=[{"role": "user", "content": "hi"}])
    assert out == {"messages": [{"role": "user", "content": "hi"}]}


def test_rejects_both_input_and_messages() -> None:
    with pytest.raises(ValueError, match="Cannot provide both `input` and `messages`"):
        _coerce(
            input={"messages": []},
            messages=[{"role": "user", "content": "x"}],
        )


def test_rejects_neither() -> None:
    with pytest.raises(ValueError, match=r"Must provide `input`"):
        _coerce()
