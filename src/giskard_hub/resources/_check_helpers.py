"""Request-side helpers for converting `CheckConfigParam` into the wire format."""

import warnings
from typing import TYPE_CHECKING, Any, Dict, List, Mapping, Iterable, Optional, FrozenSet, cast

from .._types import Omit
from .._models import BaseModel
from ..types.chat import ChatMessageParam
from ..types.check import CheckConfigParam

if TYPE_CHECKING:
    from .._client import HubClient, AsyncHubClient


# Built-in check identifiers recognized by `/v2/evaluations/run-interaction-checks`'s
# `FlatCheckSpec` validator. Keep in sync with the backend.
_BUILTIN_CHECK_IDENTIFIERS: FrozenSet[str] = frozenset(
    {
        "conformity",
        "correctness",
        "equals",
        "greater_than",
        "greater_than_equals",
        "groundedness",
        "lesser_than",
        "lesser_than_equals",
        "llm_judge",
        "metadata",
        "not_equals",
        "oss_conformity",
        "oss_groundedness",
        "regex_match",
        "semantic_similarity",
        "string_match",
    }
)

# Maps a built-in check identifier to its `kind` discriminator.
IDENTIFIER_TO_KIND: Dict[str, str] = {
    "correctness": "hub_correctness",
    "conformity": "hub_conformity",
    "groundedness": "hub_groundedness",
    "string_match": "string_matching",
    "metadata": "hub_metadata",
    "semantic_similarity": "semantic_similarity",
}


def check_param_to_spec(identifier: Optional[str], params: Any) -> Dict[str, Any]:
    """Build a `spec` dict, deriving `kind` from `params["type"]` then `identifier`."""
    if isinstance(params, BaseModel):
        params_dict: Dict[str, Any] = params.model_dump(exclude_none=True)
    elif isinstance(params, dict):
        params_dict = dict(cast(Dict[str, Any], params))
    else:
        params_dict = {}
    type_from_params = params_dict.pop("type", None)
    type_str = type_from_params or identifier or ""
    if not type_str:
        raise ValueError(
            "Cannot derive check kind: provide 'identifier' or include 'type' in 'params', "
            "or pass 'spec' directly with an explicit 'kind'."
        )
    kind = IDENTIFIER_TO_KIND.get(type_str, type_str)
    return {"kind": kind, **params_dict}


def coerce_messages_to_input_dict(
    *,
    input: Mapping[str, Any] | Iterable[ChatMessageParam] | Omit,
    messages: Iterable[ChatMessageParam] | Omit,
    new_param: str,
    deprecated_param: str,
    method_name: str,
) -> Dict[str, Any]:
    """Resolve a structured input dict from the new dict-form arg or a
    legacy list-of-messages arg.

    Accepts:
      - `input` as a `Mapping` (new shape, returned as-is); or
      - `input` as a list of chat messages (legacy alias, wrapped); or
      - `messages` as a list of chat messages (legacy alias, wrapped).

    Emits a `DeprecationWarning` whenever the legacy list form is used, no
    matter under which parameter name it arrived.
    """
    has_input = not isinstance(input, Omit)
    has_messages = not isinstance(messages, Omit)

    if has_input and has_messages:
        raise ValueError(
            f"Cannot provide both `{new_param}` and `{deprecated_param}`. "
            f"Use `{new_param}` (recommended) or `{deprecated_param}` (deprecated)."
        )
    if not has_input and not has_messages:
        raise ValueError(f"Must provide `{new_param}` (recommended) or `{deprecated_param}` (deprecated).")

    raw = input if has_input else messages
    if isinstance(raw, Mapping):
        return dict(cast(Mapping[str, Any], raw))

    warnings.warn(
        f"Passing a list of messages to `{method_name}` is deprecated; "
        f"pass `{new_param}={{'messages': [...]}}` instead.",
        DeprecationWarning,
        stacklevel=3,
    )
    return {"messages": list(cast(Iterable[ChatMessageParam], raw))}


def flat_check_specs_with_resolution(
    checks: Iterable[CheckConfigParam],
    identifier_to_id: Mapping[str, str],
) -> List[Dict[str, Any]]:
    """Convert checks into `FlatCheckSpec` payloads for `/v2/evaluations/run-interaction-checks`.

    Built-in identifiers are sent as `{identifier, override_spec}` (the
    backend recognizes them directly). Custom identifiers are resolved via
    `identifier_to_id` and sent as `{check_id, override_spec}`. Raises
    `ValueError` if an identifier is neither built-in nor in the lookup.
    """
    out: List[Dict[str, Any]] = []
    for check in checks:
        identifier = check.get("identifier")
        params = check.get("params") or {}
        override_spec = {k: v for k, v in params.items() if k != "type"}
        entry: Dict[str, Any] = {}
        if identifier:
            if identifier in _BUILTIN_CHECK_IDENTIFIERS:
                entry["identifier"] = identifier
            else:
                check_id = identifier_to_id.get(identifier)
                if not check_id:
                    raise ValueError(
                        f"Check identifier {identifier!r} is not a built-in and was not "
                        "found in the project's checks. Create the check first or use a "
                        "built-in identifier."
                    )
                entry["check_id"] = check_id
        if override_spec:
            entry["override_spec"] = override_spec
        out.append(entry)
    return out


def needs_check_lookup(checks: Iterable[CheckConfigParam]) -> bool:
    """Return True iff any check identifier is not a known built-in (so we
    must fetch the project's checks list to resolve identifier→check_id)."""
    for check in checks:
        identifier = check.get("identifier")
        if identifier and identifier not in _BUILTIN_CHECK_IDENTIFIERS:
            return True
    return False


def fetch_check_identifier_map(client: "HubClient", *, project_id: str) -> Dict[str, str]:
    """Fetch all checks (built-in + custom) for a project and return an
    `identifier → check_id` map."""
    return {c.identifier: c.id for c in client.checks.list(project_id=project_id, filter_builtin=False)}


async def fetch_check_identifier_map_async(client: "AsyncHubClient", *, project_id: str) -> Dict[str, str]:
    """Async variant of :func:`fetch_check_identifier_map`."""
    return {c.identifier: c.id for c in await client.checks.list(project_id=project_id, filter_builtin=False)}


def check_params_to_specs(
    checks: Iterable[CheckConfigParam],
    *,
    flat: bool = False,
) -> list[Dict[str, Any]]:
    """Convert checks to the wire format.

    `flat=False` (default) wraps params under a `spec` key:
    `{identifier, enabled, spec: {kind, ...params}}`.

    `flat=True` spreads params alongside `identifier`:
    `{identifier, ...params}` (with the redundant `type` key stripped).
    """
    result: list[Dict[str, Any]] = []
    for check in checks:
        identifier = check["identifier"]
        params = check.get("params") or {}
        if flat:
            result.append({"identifier": identifier, **{k: v for k, v in params.items() if k != "type"}})
        else:
            entry: Dict[str, Any] = {"identifier": identifier, "enabled": check.get("enabled", True)}
            if params:
                entry["spec"] = check_param_to_spec(identifier, params)
            result.append(entry)
    return result
