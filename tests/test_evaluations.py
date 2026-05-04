"""Tests for `EvaluationsResource` helpers and `run_single` validation (sync + async)."""

from typing import Any

import pytest

from giskard_hub import HubClient, AsyncHubClient
from giskard_hub.resources.evaluations.evaluations import (
    _check_params_to_api,
    _normalize_agent_output,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def test_check_params_to_api_emits_flat_shape() -> None:
    api = list(_check_params_to_api([{"identifier": "correctness", "params": {"reference": "x"}}]))
    assert api == [{"identifier": "correctness", "reference": "x"}]


def test_check_params_to_api_strips_redundant_type() -> None:
    api = list(
        _check_params_to_api([{"identifier": "string_match", "params": {"type": "string_match", "keyword": "k"}}])
    )
    assert api == [{"identifier": "string_match", "keyword": "k"}]


def test_normalize_agent_output_wraps_string() -> None:
    assert _normalize_agent_output("hi") == {"response": {"role": "assistant", "content": "hi"}}


def test_normalize_agent_output_passes_dict_through() -> None:
    payload: Any = {"response": {"role": "assistant", "content": "hi"}}
    assert _normalize_agent_output(payload) is payload


# ---------------------------------------------------------------------------
# run_single validation (sync + async). Validation raises before any HTTP.
# ---------------------------------------------------------------------------


@pytest.fixture
def hub() -> HubClient:
    return HubClient(api_key="test", base_url="http://localhost")


@pytest.fixture
def async_hub() -> AsyncHubClient:
    return AsyncHubClient(api_key="test", base_url="http://localhost")


def test_run_single_rejects_both_messages_and_input_data(hub: HubClient) -> None:
    with pytest.raises(ValueError, match="Cannot provide both 'messages' and 'input_data'"):
        hub.evaluations.run_single(
            checks=[],
            agent_output={"response": {"role": "assistant", "content": "x"}},
            messages=[{"role": "user", "content": "x"}],
            input_data=[{"role": "user", "content": "x"}],
        )


@pytest.mark.asyncio
async def test_async_run_single_rejects_both(async_hub: AsyncHubClient) -> None:
    with pytest.raises(ValueError, match="Cannot provide both 'messages' and 'input_data'"):
        await async_hub.evaluations.run_single(
            checks=[],
            agent_output={"response": {"role": "assistant", "content": "x"}},
            messages=[{"role": "user", "content": "x"}],
            input_data=[{"role": "user", "content": "x"}],
        )
