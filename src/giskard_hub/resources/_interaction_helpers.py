"""Translate legacy `messages`/`demo_output`/`checks` args into the new
`interactions` shape.

Used by :class:`giskard_hub.resources.test_cases.TestCasesResource` to keep
pre-v3 documented snippets working unchanged.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Mapping, Iterable, Optional, cast

from .._types import Omit
from ..types.check import CheckConfigParam, InteractionParam

if TYPE_CHECKING:
    from .._client import HubClient, AsyncHubClient


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


def _normalize_demo_output(demo_output: Any) -> Optional[Dict[str, Any]]:
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
    identifier_to_id: Mapping[str, str],
) -> List[Dict[str, Any]]:
    configs: List[Dict[str, Any]] = []
    for index, check in enumerate(checks):
        identifier = check.get("identifier")
        if not identifier:
            raise ValueError("Each check must include an 'identifier'")
        check_id = identifier_to_id.get(identifier)
        if not check_id:
            raise ValueError(
                f"Check identifier {identifier!r} not found in project. "
                "Make sure the check exists or pass a fully-formed `interactions` list."
            )
        params = check.get("params") or {}
        override_spec = {k: v for k, v in params.items() if k != "type"}
        entry: Dict[str, Any] = {
            "check_id": check_id,
            "position": index,
            "enabled": bool(check.get("enabled", True)),
        }
        if override_spec:
            entry["override_spec"] = override_spec
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


def translate_legacy_upload_item(
    item: Mapping[str, Any],
    identifier_to_id: Mapping[str, str],
) -> Dict[str, Any]:
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
        interaction["checks"] = _build_check_configs(cast(Iterable[CheckConfigParam], raw_checks), identifier_to_id)

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
    identifier_to_id: Optional[Mapping[str, str]],
) -> InteractionParam:
    """Build one `InteractionParam` from already-resolved pieces.

    `identifier_to_id` is required iff `checks` is set.
    """
    interaction: Dict[str, Any] = {
        "position": 0,
        "input": {"messages": messages},
    }

    output = _normalize_demo_output(demo_output)
    if output is not None:
        interaction["output"] = output

    if not _is_omit_or_none(checks):
        if identifier_to_id is None:
            raise RuntimeError("identifier_to_id must be provided when checks are present")
        interaction["checks"] = _build_check_configs(checks, identifier_to_id)  # type: ignore[arg-type]

    return interaction  # type: ignore[return-value]


# ---------------------------------------------------------------------------
# Sync/async builders — only differ in the awaited I/O.
# ---------------------------------------------------------------------------


def build_legacy_interaction_sync(
    client: "HubClient",
    *,
    dataset_id: str,
    messages: Iterable[Mapping[str, Any]] | None | Omit,
    demo_output: Any,
    checks: Iterable[CheckConfigParam] | None | Omit,
) -> InteractionParam:
    """Build one `InteractionParam` from legacy create/update args."""
    msgs = _coerce_messages(messages)

    identifier_to_id: Optional[Dict[str, str]] = None
    if not _is_omit_or_none(checks):
        project_id = client.datasets.retrieve(dataset_id).project_id
        identifier_to_id = {c.identifier: c.id for c in client.checks.list(project_id=project_id, filter_builtin=False)}

    return _assemble_interaction(
        messages=msgs,
        demo_output=demo_output,
        checks=checks,
        identifier_to_id=identifier_to_id,
    )


async def build_legacy_interaction_async(
    client: "AsyncHubClient",
    *,
    dataset_id: str,
    messages: Iterable[Mapping[str, Any]] | None | Omit,
    demo_output: Any,
    checks: Iterable[CheckConfigParam] | None | Omit,
) -> InteractionParam:
    """Async variant of :func:`build_legacy_interaction_sync`."""
    msgs = _coerce_messages(messages)

    identifier_to_id: Optional[Dict[str, str]] = None
    if not _is_omit_or_none(checks):
        project_id = (await client.datasets.retrieve(dataset_id)).project_id
        identifier_to_id = {
            c.identifier: c.id for c in await client.checks.list(project_id=project_id, filter_builtin=False)
        }

    return _assemble_interaction(
        messages=msgs,
        demo_output=demo_output,
        checks=checks,
        identifier_to_id=identifier_to_id,
    )


def _interactions_have_checks(interactions: Iterable[Mapping[str, Any]]) -> bool:
    return any(interaction.get("checks") for interaction in interactions)


def _resolve_interaction_checks(
    interactions: Iterable[Mapping[str, Any]],
    identifier_to_id: Mapping[str, str],
) -> List[Dict[str, Any]]:
    resolved: List[Dict[str, Any]] = []
    for interaction in interactions:
        item: Dict[str, Any] = dict(interaction)
        checks = item.get("checks")
        if checks:
            item["checks"] = _build_check_configs(cast(Iterable[CheckConfigParam], checks), identifier_to_id)
        resolved.append(item)
    return resolved


def resolve_interaction_checks_sync(
    client: "HubClient",
    *,
    interactions: Iterable[InteractionParam],
    dataset_id: Optional[str] = None,
    test_case_id: Optional[str] = None,
) -> List[InteractionParam]:
    """Resolve each interaction check's `identifier` to a `check_id`."""
    materialized = [dict(interaction) for interaction in interactions]
    _fill_positions(materialized)
    if not _interactions_have_checks(materialized):
        return cast("List[InteractionParam]", materialized)

    if dataset_id is None:
        if test_case_id is None:
            raise RuntimeError("dataset_id or test_case_id is required to resolve interaction checks")
        dataset_id = client.test_cases.retrieve(test_case_id).dataset_id

    project_id = client.datasets.retrieve(dataset_id).project_id
    identifier_to_id = {c.identifier: c.id for c in client.checks.list(project_id=project_id, filter_builtin=False)}
    return cast(
        "List[InteractionParam]",
        _resolve_interaction_checks(materialized, identifier_to_id),
    )


async def resolve_interaction_checks_async(
    client: "AsyncHubClient",
    *,
    interactions: Iterable[InteractionParam],
    dataset_id: Optional[str] = None,
    test_case_id: Optional[str] = None,
) -> List[InteractionParam]:
    """Async variant of :func:`resolve_interaction_checks_sync`."""
    materialized = [dict(interaction) for interaction in interactions]
    _fill_positions(materialized)
    if not _interactions_have_checks(materialized):
        return cast("List[InteractionParam]", materialized)

    if dataset_id is None:
        if test_case_id is None:
            raise RuntimeError("dataset_id or test_case_id is required to resolve interaction checks")
        dataset_id = (await client.test_cases.retrieve(test_case_id)).dataset_id

    project_id = (await client.datasets.retrieve(dataset_id)).project_id
    identifier_to_id = {
        c.identifier: c.id for c in await client.checks.list(project_id=project_id, filter_builtin=False)
    }
    return cast(
        "List[InteractionParam]",
        _resolve_interaction_checks(materialized, identifier_to_id),
    )
