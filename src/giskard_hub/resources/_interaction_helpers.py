"""Translate legacy `messages`/`demo_output`/`checks` args into the new
`interactions` shape.

Used by :class:`giskard_hub.resources.test_cases.TestCasesResource` to keep
pre-v3 documented snippets working unchanged.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Mapping, Iterable, Optional, cast

from .._types import Omit
from ..types.role import Role
from ..types.check import CheckConfigParam, InteractionParam

if TYPE_CHECKING:
    from .._client import HubClient, AsyncHubClient


_DEFAULT_ROLE_NAME = "default"

# Schemas matching a chat-style agent (input.messages: list[ChatMessage] →
# output.response: ChatMessage with optional metadata). Used when the legacy
# translator needs to materialize a default role on a fresh dataset.
_DEFAULT_CHAT_INPUT_SCHEMA: Dict[str, Any] = {
    "type": "object",
    "required": ["messages"],
    "properties": {
        "messages": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["role", "content"],
                "properties": {
                    "role": {"type": "string"},
                    "content": {"type": "string"},
                },
            },
        }
    },
}
_DEFAULT_CHAT_OUTPUT_SCHEMA: Dict[str, Any] = {
    "type": "object",
    "required": ["response"],
    "properties": {
        "metadata": {"type": "object"},
        "response": {
            "type": "object",
            "required": ["role", "content"],
            "properties": {
                "role": {"type": "string"},
                "content": {"type": "string"},
            },
        },
    },
}


# ---------------------------------------------------------------------------
# Pure helpers (no I/O)
# ---------------------------------------------------------------------------


def _is_omit_or_none(value: Any) -> bool:
    return isinstance(value, Omit) or value is None


def _coerce_messages(messages: Iterable[Mapping[str, Any]] | None | Omit) -> List[Dict[str, Any]]:
    if _is_omit_or_none(messages):
        return []
    return [dict(m) for m in cast(Iterable[Mapping[str, Any]], messages)]


def _normalize_demo_output(demo_output: Any) -> Optional[Dict[str, Any]]:
    """Convert legacy `demo_output` into the role's structured `output` dict.

    Mirrors the default chat role's `output_schema`:
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
            raise ValueError("Each legacy check must include an 'identifier'")
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


def _pick_default_role_id(roles: List[Role]) -> str:
    """Pick the `default` role's id, falling back to the first role."""
    return next((r for r in roles if r.name == _DEFAULT_ROLE_NAME), roles[0]).id


def _assemble_interaction(
    *,
    role_id: str,
    messages: List[Dict[str, Any]],
    demo_output: Any,
    checks: Iterable[CheckConfigParam] | None | Omit,
    identifier_to_id: Optional[Mapping[str, str]],
) -> InteractionParam:
    """Build one `InteractionParam` from already-resolved pieces.

    `identifier_to_id` is required iff `checks` is set.
    """
    interaction: Dict[str, Any] = {
        "role_id": role_id,
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

    project_id = client.datasets.retrieve(dataset_id).project_id

    roles = client.roles.list(dataset_id, project_id=project_id)
    if not roles:
        roles = [
            client.roles.create(
                dataset_id,
                project_id=project_id,
                name=_DEFAULT_ROLE_NAME,
                input_schema=_DEFAULT_CHAT_INPUT_SCHEMA,
                output_schema=_DEFAULT_CHAT_OUTPUT_SCHEMA,
            )
        ]

    identifier_to_id: Optional[Dict[str, str]] = None
    if not _is_omit_or_none(checks):
        identifier_to_id = {c.identifier: c.id for c in client.checks.list(project_id=project_id, filter_builtin=False)}

    return _assemble_interaction(
        role_id=_pick_default_role_id(roles),
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

    project_id = (await client.datasets.retrieve(dataset_id)).project_id

    roles = await client.roles.list(dataset_id, project_id=project_id)
    if not roles:
        roles = [
            await client.roles.create(
                dataset_id,
                project_id=project_id,
                name=_DEFAULT_ROLE_NAME,
                input_schema=_DEFAULT_CHAT_INPUT_SCHEMA,
                output_schema=_DEFAULT_CHAT_OUTPUT_SCHEMA,
            )
        ]

    identifier_to_id: Optional[Dict[str, str]] = None
    if not _is_omit_or_none(checks):
        identifier_to_id = {
            c.identifier: c.id for c in await client.checks.list(project_id=project_id, filter_builtin=False)
        }

    return _assemble_interaction(
        role_id=_pick_default_role_id(roles),
        messages=msgs,
        demo_output=demo_output,
        checks=checks,
        identifier_to_id=identifier_to_id,
    )
