"""Tests for `giskard_hub.types.check` helpers/models and `ChecksResource` validation."""

from typing import Any, Dict

import pytest

from giskard_hub import HubClient, AsyncHubClient
from giskard_hub.types import (
    Check,
    CheckConfig,
    CheckResult,
    JsonPathRule,
    OutputAnnotation,
    ContextAnnotation,
    CorrectnessParams,
    JsonPathRuleParam,
)
from giskard_hub.types.check import _extract_check_params
from giskard_hub.resources._check_helpers import (
    IDENTIFIER_TO_KIND,
    check_param_to_spec,
    check_params_to_specs,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def test_identifier_to_kind_mapping() -> None:
    assert IDENTIFIER_TO_KIND == {
        "correctness": "hub_correctness",
        "conformity": "hub_conformity",
        "groundedness": "hub_groundedness",
        "oss_conformity": "conformity",
        "oss_groundedness": "groundedness",
        "string_match": "string_matching",
        "regex_match": "regex_matching",
        "metadata": "hub_metadata",
    }


@pytest.mark.parametrize(
    "identifier",
    [
        "llm_judge",
        "equals",
        "not_equals",
        "greater_than",
        "greater_than_equals",
        "less_than",
        "less_than_equals",
        "semantic_similarity",
    ],
)
def test_identifier_to_kind_falls_back_to_identity(identifier: str) -> None:
    """Identifiers not in IDENTIFIER_TO_KIND resolve to themselves via check_param_to_spec."""
    assert identifier not in IDENTIFIER_TO_KIND
    spec = check_param_to_spec(identifier, {})
    assert spec["kind"] == identifier


def test_check_param_to_spec_prefers_params_type_over_identifier() -> None:
    spec = check_param_to_spec("custom_name", {"type": "conformity", "rules": ["r"]})
    assert spec == {"kind": "hub_conformity", "rules": ["r"]}


def test_check_param_to_spec_falls_back_to_identifier() -> None:
    spec = check_param_to_spec("correctness", {"reference": "x"})
    assert spec == {"kind": "hub_correctness", "reference": "x"}


def test_check_param_to_spec_passes_through_unknown_kind() -> None:
    spec = check_param_to_spec("future_kind", {"foo": 1})
    assert spec == {"kind": "future_kind", "foo": 1}


def test_check_param_to_spec_raises_when_no_kind_derivable() -> None:
    with pytest.raises(ValueError, match="Cannot derive check kind"):
        check_param_to_spec(None, {"reference": "x"})


def test_check_param_to_spec_accepts_basemodel() -> None:
    spec = check_param_to_spec("correctness", CorrectnessParams(reference="x"))
    assert spec == {"kind": "hub_correctness", "reference": "x"}


def test_extract_check_params_strips_kind() -> None:
    spec = {"kind": "hub_correctness", "reference": "r"}
    assert _extract_check_params({"spec": spec}) == {"reference": "r"}


def test_extract_check_params_empty_when_no_spec() -> None:
    assert _extract_check_params({}) == {}
    assert _extract_check_params({"spec": None}) == {}


def test_check_params_to_specs_emits_nested_with_kind() -> None:
    api = check_params_to_specs([{"identifier": "correctness", "params": {"reference": "x"}}])
    assert api == [
        {
            "identifier": "correctness",
            "enabled": True,
            "spec": {"kind": "hub_correctness", "reference": "x"},
        }
    ]


def test_check_params_to_specs_omits_spec_when_no_params() -> None:
    api = check_params_to_specs([{"identifier": "tone_pro_xyz"}])
    assert api == [{"identifier": "tone_pro_xyz", "enabled": True}]


def test_check_params_to_specs_strips_redundant_type() -> None:
    api = check_params_to_specs([{"identifier": "string_match", "params": {"type": "string_match", "keyword": "k"}}])
    assert api == [
        {
            "identifier": "string_match",
            "enabled": True,
            "spec": {"kind": "string_matching", "keyword": "k"},
        }
    ]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


def _check_payload(**overrides: Any) -> Dict[str, Any]:
    base = {
        "id": "1",
        "built_in": False,
        "created_at": "2025-01-01T00:00:00",
        "identifier": "correctness",
        "name": "n",
        "project_id": "p",
        "updated_at": "2025-01-01T00:00:00",
        "spec": {"kind": "hub_correctness", "reference": "ref"},
    }
    base.update(overrides)
    return base


def test_check_derives_params_from_spec() -> None:
    c = Check.model_validate(_check_payload())
    assert c.spec == {"kind": "hub_correctness", "reference": "ref"}
    assert c.params == {"reference": "ref"}


def test_check_source_defaults_to_project() -> None:
    assert Check.model_validate(_check_payload()).source == "project"


def test_check_source_accepts_builtin() -> None:
    c = Check.model_validate(_check_payload(source="builtin", built_in=True))
    assert c.source == "builtin"


def test_check_config_derives_params_from_spec() -> None:
    cc = CheckConfig.model_validate(
        {
            "identifier": "correctness",
            "enabled": True,
            "position": 0,
            "spec": {"kind": "hub_correctness", "reference": "r"},
        }
    )
    assert cc.params == {"reference": "r"}


def test_check_config_empty_params_when_spec_is_none() -> None:
    cc = CheckConfig.model_validate({"identifier": "tone_pro", "enabled": True, "position": 0, "spec": None})
    assert cc.params == {}


def test_check_result_discriminates_annotations() -> None:
    cr = CheckResult.model_validate(
        {
            "name": "n",
            "status": "finished",
            "passed": False,
            "annotations": [
                {"text": "o", "label": "L", "start_char_index": 0, "end_char_index": 1, "type": "output"},
                {"text": "c", "label": "L", "start_char_index": 0, "end_char_index": 1, "type": "context"},
            ],
        }
    )
    assert cr.annotations is not None
    assert isinstance(cr.annotations[0], OutputAnnotation)
    assert isinstance(cr.annotations[1], ContextAnnotation)


def test_json_path_rule_accepts_int() -> None:
    rule = JsonPathRule(expected_value=5, expected_value_type="number", json_path="$.x")
    assert rule.expected_value == 5


def test_json_path_rule_param_is_importable() -> None:
    rule: JsonPathRuleParam = {  # type: ignore[typeddict-item]
        "expected_value": True,
        "expected_value_type": "boolean",
        "json_path": "$.y",
    }
    assert rule["expected_value"] is True


# ---------------------------------------------------------------------------
# ChecksResource validation (sync + async). Validation raises before any HTTP.
# ---------------------------------------------------------------------------


@pytest.fixture
def hub() -> HubClient:
    return HubClient(api_key="test", base_url="http://localhost")


@pytest.fixture
def async_hub() -> AsyncHubClient:
    return AsyncHubClient(api_key="test", base_url="http://localhost")


def test_create_rejects_both_params_and_spec(hub: HubClient) -> None:
    with pytest.raises(ValueError, match="Cannot provide both 'params' and 'spec'"):
        hub.checks.create(
            identifier="correctness",
            name="n",
            project_id="p",
            params={"reference": "r"},
            spec={"kind": "hub_correctness", "reference": "r"},
        )


def test_create_rejects_neither(hub: HubClient) -> None:
    with pytest.raises(ValueError, match="Must provide either 'params' or 'spec'"):
        hub.checks.create(identifier="correctness", name="n", project_id="p")


def test_update_rejects_both_params_and_spec(hub: HubClient) -> None:
    with pytest.raises(ValueError, match="Cannot provide both 'params' and 'spec'"):
        hub.checks.update(
            "check-id",
            params={"reference": "r"},
            spec={"kind": "hub_correctness", "reference": "r"},
        )


@pytest.mark.asyncio
async def test_async_create_rejects_both(async_hub: AsyncHubClient) -> None:
    with pytest.raises(ValueError, match="Cannot provide both 'params' and 'spec'"):
        await async_hub.checks.create(
            identifier="correctness",
            name="n",
            project_id="p",
            params={"reference": "r"},
            spec={"kind": "hub_correctness", "reference": "r"},
        )


@pytest.mark.asyncio
async def test_async_update_rejects_both(async_hub: AsyncHubClient) -> None:
    with pytest.raises(ValueError, match="Cannot provide both 'params' and 'spec'"):
        await async_hub.checks.update(
            "check-id",
            params={"reference": "r"},
            spec={"kind": "hub_correctness", "reference": "r"},
        )
