"""Tests for `EvaluationsResource` helpers and `run_single` validation (sync + async)."""

from typing import Any

from giskard_hub.resources._check_helpers import (
    flat_check_specs,
    check_params_to_specs,
)
from giskard_hub.resources.evaluations.evaluations import _normalize_agent_output

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def test_check_params_to_specs_emits_flat_shape() -> None:
    api = check_params_to_specs([{"identifier": "hub_correctness", "params": {"reference": "x"}}], flat=True)
    assert api == [{"identifier": "hub_correctness", "reference": "x"}]


def test_check_params_to_specs_strips_redundant_type_when_flat() -> None:
    api = check_params_to_specs(
        [{"identifier": "string_matching", "params": {"type": "string_matching", "keyword": "k"}}],
        flat=True,
    )
    assert api == [{"identifier": "string_matching", "keyword": "k"}]


def test_normalize_agent_output_wraps_string() -> None:
    assert _normalize_agent_output("hi") == {"response": {"role": "assistant", "content": "hi"}}


def test_normalize_agent_output_passes_dict_through() -> None:
    payload: Any = {"response": {"role": "assistant", "content": "hi"}}
    assert _normalize_agent_output(payload) is payload


def test_flat_check_specs_passes_identifier_through() -> None:
    out = flat_check_specs(
        [{"identifier": "hub_correctness", "params": {"reference": "x", "type": "hub_correctness"}}],
    )
    assert out == [{"identifier": "hub_correctness", "override_spec": {"reference": "x"}}]


def test_flat_check_specs_passes_custom_identifier_through() -> None:
    out = flat_check_specs([{"identifier": "tone_pro", "params": {"reference": "x"}}])
    assert out == [{"identifier": "tone_pro", "override_spec": {"reference": "x"}}]
