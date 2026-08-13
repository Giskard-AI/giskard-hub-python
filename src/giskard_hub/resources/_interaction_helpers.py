"""Translate legacy `messages`/`demo_output`/`checks` args into the new
`interactions` shape.

Used by :class:`giskard_hub.resources.test_cases.TestCasesResource` to keep
pre-v3 documented snippets working unchanged.
"""

from __future__ import annotations

from typing import Any, Dict, List, Mapping, Iterable, cast

from .._types import Omit
from ..types.check import CheckConfigParam, InteractionParam

# ---------------------------------------------------------------------------
# Pure helpers (no I/O)
# ---------------------------------------------------------------------------


def _is_omit_or_none(value: Any) -> bool:
    return isinstance(value, Omit) or value is None


def _coerce_messages(
    messages: Iterable[Mapping[str, Any]] | None | Omit,
) -> List[Dict[str, Any]]:
    if _is_omit_or_none(messages):
        return []
    return [dict(m) for m in cast(Iterable[Mapping[str, Any]], messages)]


def _normalize_demo_output(demo_output: Any) -> Dict[str, Any] | None:
    """Convert legacy `demo_output` into an interaction's structured `output` dict.

    Mirrors the default chat `output_schema`:
    `{"response": {role, content}, "metadata": {...}}`.
    """
    if _is_omit_or_none(demo_output):
        return None
    if isinstance(demo_output, str):
        return {"response": {"role": "assistant", "content": demo_output}}
    if isinstance(demo_output, Mapping):
        d: Dict[str, Any] = dict(cast(Mapping[str, Any], demo_output))
        metadata = d.pop("metadata", None)
        result: Dict[str, Any] = {"response": d}
        if metadata is not None:
            result["metadata"] = metadata
        return result
    raise TypeError(f"Unsupported demo_output type: {type(demo_output).__name__}")


def _build_check_configs(
    checks: Iterable[CheckConfigParam],
) -> List[Dict[str, Any]]:
    """Normalize check dicts for the API, which resolves `identifier` itself."""
    configs: List[Dict[str, Any]] = []
    for index, check in enumerate(checks):
        entry: Dict[str, Any] = dict(cast(Mapping[str, Any], check))
        if not entry.get("identifier") and not entry.get("check_id"):
            raise ValueError("Each check must include an 'identifier' or a 'check_id'")
        params = entry.pop("params", None)
        if params:
            override_spec = {k: v for k, v in cast(Mapping[str, Any], params).items() if k != "type"}
            if override_spec:
                entry.setdefault("override_spec", override_spec)
        entry.setdefault("position", index)
        entry.setdefault("enabled", True)
        configs.append(entry)
    return configs


def _fill_positions(interactions: List[Dict[str, Any]]) -> None:
    """Default each interaction's `position` to its index in the list."""
    for index, interaction in enumerate(interactions):
        interaction.setdefault("position", index)


# ---------------------------------------------------------------------------
# Legacy `datasets.upload` translation
# ---------------------------------------------------------------------------


_LEGACY_UPLOAD_KEYS = ("messages", "input_data", "checks", "demo_output")


def is_legacy_upload_item(item: Mapping[str, Any]) -> bool:
    """Detect whether an item from `datasets.upload(data=[...])` uses the
    pre-v3 shape (`messages`/`checks`/`demo_output` etc) rather than the new
    `interactions=[...]` shape."""
    if "interactions" in item:
        return False
    return any(k in item for k in _LEGACY_UPLOAD_KEYS)


def translate_legacy_upload_item(item: Mapping[str, Any]) -> Dict[str, Any]:
    """Convert one legacy test-case dict (as accepted by `datasets.upload`)
    into the new `{interactions: [...], tags: [...], status: ...}` import
    shape.
    """
    raw_messages: List[Mapping[str, Any]] = item.get("input_data") or item.get("messages") or []
    msgs = [dict(m) for m in raw_messages]

    interaction: Dict[str, Any] = {
        "position": 0,
        "input": {"messages": msgs},
    }

    output = _normalize_demo_output(item.get("demo_output"))
    if output is not None:
        interaction["output"] = output

    raw_checks = item.get("checks")
    if raw_checks:
        interaction["checks"] = _build_check_configs(cast(Iterable[CheckConfigParam], raw_checks))

    out: Dict[str, Any] = {"interactions": [interaction]}
    if "tags" in item:
        out["tags"] = item["tags"]
    if "status" in item:
        out["status"] = item["status"]
    return out


def upload_item_needs_position_fill(item: Mapping[str, Any]) -> bool:
    """True when a new-shape upload item has an interaction missing `position`."""
    interactions = item.get("interactions")
    if not isinstance(interactions, list):
        return False
    return any(isinstance(i, Mapping) and "position" not in i for i in cast(List[Any], interactions))


def fill_upload_item_positions(item: Mapping[str, Any]) -> Dict[str, Any]:
    """Return a copy of a new-shape upload item with each interaction's
    `position` defaulted to its list index. The caller's dicts are not mutated."""
    out: Dict[str, Any] = dict(item)
    interactions = out.get("interactions")
    if isinstance(interactions, list):
        filled = [dict(cast(Mapping[str, Any], i)) for i in cast(List[Any], interactions)]
        _fill_positions(filled)
        out["interactions"] = filled
    return out


def _assemble_interaction(
    *,
    messages: List[Dict[str, Any]],
    demo_output: Any,
    checks: Iterable[CheckConfigParam] | None | Omit,
) -> InteractionParam:
    """Build one `InteractionParam` from already-normalized pieces."""
    interaction: Dict[str, Any] = {
        "position": 0,
        "input": {"messages": messages},
    }

    output = _normalize_demo_output(demo_output)
    if output is not None:
        interaction["output"] = output

    if not _is_omit_or_none(checks):
        interaction["checks"] = _build_check_configs(cast("Iterable[CheckConfigParam]", checks))

    return cast("InteractionParam", interaction)


# ---------------------------------------------------------------------------
# Interaction builders
# ---------------------------------------------------------------------------


def build_legacy_interaction(
    *,
    messages: Iterable[Mapping[str, Any]] | None | Omit,
    demo_output: Any,
    checks: Iterable[CheckConfigParam] | None | Omit,
) -> InteractionParam:
    """Build one `InteractionParam` from legacy create/update args."""
    return _assemble_interaction(
        messages=_coerce_messages(messages),
        demo_output=demo_output,
        checks=checks,
    )


def normalize_interactions(
    interactions: Iterable[InteractionParam],
) -> List[InteractionParam]:
    """Fill default positions and normalize check dicts.

    Check `identifier`s are passed through and resolved by the API.
    """
    materialized: List[Dict[str, Any]] = [dict(interaction) for interaction in interactions]
    _fill_positions(materialized)
    for item in materialized:
        checks = item.get("checks")
        if checks:
            item["checks"] = _build_check_configs(cast("Iterable[CheckConfigParam]", checks))
    return cast("List[InteractionParam]", materialized)
