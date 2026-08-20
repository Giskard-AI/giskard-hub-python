"""Tests for `TestCasesResource` argument validation (sync + async)."""
# pyright: reportDeprecated=false

from typing import List

import pytest

pytestmark = [
    pytest.mark.filterwarnings("ignore:`client.test_cases` is deprecated:DeprecationWarning"),
]

from giskard_hub import HubClient, AsyncHubClient
from giskard_hub._types import omit
from giskard_hub.types.check import Interaction, InteractionParam
from giskard_hub.types.test_case import TestCase
from giskard_hub.resources._interaction_helpers import (
    _coerce_messages,
    _build_check_configs,
    _normalize_demo_output,
    normalize_interactions,
)


@pytest.fixture
def hub() -> HubClient:
    return HubClient(api_key="test", base_url="http://localhost")


@pytest.fixture
def async_hub() -> AsyncHubClient:
    return AsyncHubClient(api_key="test", base_url="http://localhost")


def test_create_rejects_interactions_with_legacy(hub: HubClient) -> None:
    with pytest.raises(ValueError, match="Cannot mix `interactions` with legacy parameters"):
        hub.test_cases.create(
            dataset_id="d",
            interactions=[{"position": 0, "input": {"messages": []}}],
            messages=[{"role": "user", "content": "x"}],
        )


def test_create_rejects_neither(hub: HubClient) -> None:
    with pytest.raises(ValueError, match=r"Must provide either `interactions=`"):
        hub.test_cases.create(dataset_id="d")


@pytest.mark.asyncio
async def test_async_create_rejects_interactions_with_legacy(async_hub: AsyncHubClient) -> None:
    with pytest.raises(ValueError, match="Cannot mix `interactions` with legacy parameters"):
        await async_hub.test_cases.create(
            dataset_id="d",
            interactions=[{"position": 0, "input": {"messages": []}}],
            messages=[{"role": "user", "content": "x"}],
        )


@pytest.mark.asyncio
async def test_async_create_rejects_neither(async_hub: AsyncHubClient) -> None:
    with pytest.raises(ValueError, match=r"Must provide either `interactions=`"):
        await async_hub.test_cases.create(dataset_id="d")


# ---------------------------------------------------------------------------
# Legacy translation helpers (no HTTP)
# ---------------------------------------------------------------------------


def test_normalize_demo_output_string_wraps_to_response_dict() -> None:
    assert _normalize_demo_output("hi") == {"response": {"role": "assistant", "content": "hi"}}


def test_normalize_demo_output_dict_extracts_metadata() -> None:
    assert _normalize_demo_output({"role": "assistant", "content": "ok", "metadata": {"k": "v"}}) == {
        "response": {"role": "assistant", "content": "ok"},
        "metadata": {"k": "v"},
    }


def test_normalize_demo_output_dict_without_metadata_uses_response_only() -> None:
    assert _normalize_demo_output({"role": "assistant", "content": "ok"}) == {
        "response": {"role": "assistant", "content": "ok"}
    }


def test_coerce_messages_returns_list_of_dicts() -> None:
    assert _coerce_messages([{"role": "user", "content": "a"}]) == [{"role": "user", "content": "a"}]


def test_coerce_messages_returns_empty_for_omit() -> None:
    assert _coerce_messages(omit) == []


def test_build_check_configs_passes_identifier_through_and_strips_type() -> None:
    configs = _build_check_configs(
        [
            {"identifier": "hub_correctness", "params": {"reference": "x", "type": "hub_correctness"}},
            {"identifier": "string_matching", "params": {"keyword": "k"}, "enabled": False},
        ],
    )
    assert configs == [
        {
            "identifier": "hub_correctness",
            "position": 0,
            "enabled": True,
            "override_spec": {"reference": "x"},
        },
        {
            "identifier": "string_matching",
            "position": 1,
            "enabled": False,
            "override_spec": {"keyword": "k"},
        },
    ]


def test_build_check_configs_passes_check_id_and_override_spec_through() -> None:
    configs = _build_check_configs(
        [{"check_id": "uuid-1", "override_spec": {"reference": "x"}}],
    )
    assert configs == [
        {
            "check_id": "uuid-1",
            "position": 0,
            "enabled": True,
            "override_spec": {"reference": "x"},
        }
    ]


def test_build_check_configs_raises_without_identifier_or_check_id() -> None:
    with pytest.raises(ValueError, match="'identifier' or a 'check_id'"):
        _build_check_configs([{"enabled": True}])


def test_normalize_interactions_normalizes_checks_and_leaves_checkless_alone() -> None:
    interactions: List[InteractionParam] = [
        {
            "position": 0,
            "input": {"messages": []},
            "checks": [{"identifier": "hub_correctness", "params": {"reference": "r"}}],
        },
        {"position": 1, "input": {"messages": []}},
    ]
    resolved = normalize_interactions(interactions)

    assert resolved[0].get("checks") == [
        {"identifier": "hub_correctness", "position": 0, "enabled": True, "override_spec": {"reference": "r"}}
    ]
    assert "checks" not in resolved[1]
    # The caller's dicts are copied, not mutated in place.
    assert interactions[0].get("checks") == [{"identifier": "hub_correctness", "params": {"reference": "r"}}]


def test_normalize_interactions_is_noop_without_checks() -> None:
    interactions: List[InteractionParam] = [{"position": 0, "input": {"messages": []}}]
    assert normalize_interactions(interactions) == interactions


def test_normalize_interactions_defaults_position_to_index() -> None:
    # Omitted `position` falls back to the interaction's list index; an
    # explicit position is left untouched.
    interactions: List[InteractionParam] = [
        {"input": {"a": 1}},
        {"position": 7, "input": {"b": 2}},
        {"input": {"c": 3}},
    ]
    resolved = normalize_interactions(interactions)
    assert [i.get("position") for i in resolved] == [0, 7, 2]


# ---------------------------------------------------------------------------
# Back-compat property: TestCase.messages
# ---------------------------------------------------------------------------


def test_test_case_messages_synthesizes_from_first_interaction() -> None:
    interaction = Interaction.model_construct(  # type: ignore[arg-type]
        position=0,
        input={
            "messages": [
                {"role": "user", "content": "hi"},
                {"role": "assistant", "content": "hello"},
            ]
        },
    )
    tc = TestCase.model_construct(id="tc-1", interactions=[interaction])  # type: ignore[arg-type]
    with pytest.deprecated_call():
        msgs = tc.messages
    assert [(m.role, m.content) for m in msgs] == [("user", "hi"), ("assistant", "hello")]


def test_test_case_messages_returns_empty_when_no_interactions() -> None:
    tc = TestCase.model_construct(id="tc-1", interactions=[])  # type: ignore[arg-type]
    with pytest.deprecated_call():
        assert tc.messages == []


def test_test_case_messages_returns_empty_when_input_has_no_messages_key() -> None:
    interaction = Interaction.model_construct(  # type: ignore[arg-type]
        position=0,
        input={"some_other_shape": "x"},
    )
    tc = TestCase.model_construct(id="tc-1", interactions=[interaction])  # type: ignore[arg-type]
    with pytest.deprecated_call():
        assert tc.messages == []
