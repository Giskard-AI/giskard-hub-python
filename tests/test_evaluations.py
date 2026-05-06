"""Tests for `EvaluationsResource` helpers and `run_single` validation (sync + async)."""

from typing import Any

import pytest

from giskard_hub.resources._check_helpers import (
    needs_check_lookup,
    check_params_to_specs,
    flat_check_specs_with_resolution,
)
from giskard_hub.resources.evaluations.evaluations import _normalize_agent_output

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


def test_flat_check_specs_built_in_uses_identifier() -> None:
    out = flat_check_specs_with_resolution(
        [{"identifier": "correctness", "params": {"reference": "x", "type": "correctness"}}],
        identifier_to_id={},
    )
    assert out == [{"identifier": "correctness", "override_spec": {"reference": "x"}}]


def test_flat_check_specs_custom_uses_check_id() -> None:
    out = flat_check_specs_with_resolution(
        [{"identifier": "tone_pro", "params": {"reference": "x"}}],
        identifier_to_id={"tone_pro": "uuid-1"},
    )
    assert out == [{"check_id": "uuid-1", "override_spec": {"reference": "x"}}]


def test_flat_check_specs_unknown_identifier_raises() -> None:
    with pytest.raises(ValueError, match="not a built-in"):
        flat_check_specs_with_resolution(
            [{"identifier": "mystery"}],
            identifier_to_id={},
        )


def test_needs_check_lookup_true_for_custom() -> None:
    assert needs_check_lookup([{"identifier": "tone_pro"}]) is True


def test_needs_check_lookup_false_for_built_ins_only() -> None:
    assert (
        needs_check_lookup(
            [
                {"identifier": "correctness"},
                {"identifier": "string_match"},
            ]
        )
        is False
    )
