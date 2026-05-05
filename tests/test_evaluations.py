"""Tests for `EvaluationsResource` helpers and `run_single` validation (sync + async)."""

from typing import Any

from giskard_hub.resources._check_helpers import check_params_to_specs
from giskard_hub.resources.evaluations.evaluations import (
    _flat_check_specs,
    _normalize_agent_output,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def test_check_params_to_specs_emits_flat_shape() -> None:
    api = check_params_to_specs([{"identifier": "correctness", "params": {"reference": "x"}}], flat=True)
    assert api == [{"identifier": "correctness", "reference": "x"}]


def test_check_params_to_specs_strips_redundant_type_when_flat() -> None:
    api = check_params_to_specs(
        [{"identifier": "string_match", "params": {"type": "string_match", "keyword": "k"}}],
        flat=True,
    )
    assert api == [{"identifier": "string_match", "keyword": "k"}]


def test_normalize_agent_output_wraps_string() -> None:
    assert _normalize_agent_output("hi") == {"response": {"role": "assistant", "content": "hi"}}


def test_normalize_agent_output_passes_dict_through() -> None:
    payload: Any = {"response": {"role": "assistant", "content": "hi"}}
    assert _normalize_agent_output(payload) is payload


def test_flat_check_specs_emits_identifier_and_override_spec() -> None:
    out = _flat_check_specs(
        [
            {"identifier": "correctness", "params": {"reference": "x", "type": "correctness"}},
            {"identifier": "string_match", "params": {"keyword": "k"}},
        ]
    )
    assert out == [
        {"identifier": "correctness", "override_spec": {"reference": "x"}},
        {"identifier": "string_match", "override_spec": {"keyword": "k"}},
    ]
