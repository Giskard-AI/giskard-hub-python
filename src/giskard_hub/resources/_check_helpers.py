"""Request-side helpers for converting `CheckConfigParam` into the wire format."""

import warnings
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Mapping,
    Iterable,
    Optional,
    cast,
)

from .._types import Omit
from .._models import BaseModel
from ..types.chat import ChatMessageParam
from ..types.check import CheckConfigParam

if TYPE_CHECKING:
    pass


def check_param_to_spec(identifier: Optional[str], params: Any) -> Dict[str, Any]:
    """Build a `spec` dict, deriving `kind` from `params["type"]` then `identifier`."""
    if isinstance(params, BaseModel):
        params_dict: Dict[str, Any] = params.model_dump(exclude_none=True)
    elif isinstance(params, dict):
        params_dict = dict(cast(Dict[str, Any], params))
    else:
        params_dict = {}
    type_from_params = params_dict.pop("type", None)
    kind = type_from_params or identifier or ""
    if not kind:
        raise ValueError(
            "Cannot derive check kind: provide 'identifier' or include 'type' in 'params', "
            "or pass 'spec' directly with an explicit 'kind'."
        )
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


def flat_check_specs(checks: Iterable[CheckConfigParam]) -> List[Dict[str, Any]]:
    """Convert checks into `FlatCheckSpec` payloads for `/v2/evaluations/run-interaction-checks`.

    Identifiers are sent as-is; the API resolves built-in and custom
    identifiers alike.
    """
    out: List[Dict[str, Any]] = []
    for check in checks:
        identifier = check.get("identifier")
        params = check.get("params") or {}
        override_spec = {k: v for k, v in params.items() if k != "type"}
        entry: Dict[str, Any] = {}
        if identifier:
            entry["identifier"] = identifier
        if override_spec:
            entry["override_spec"] = override_spec
        out.append(entry)
    return out


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
        identifier = check.get("identifier")
        if not identifier:
            raise ValueError("Each check must include an 'identifier'")
        params = check.get("params") or {}
        if flat:
            result.append(
                {
                    "identifier": identifier,
                    **{k: v for k, v in params.items() if k != "type"},
                }
            )
        else:
            entry: Dict[str, Any] = {
                "identifier": identifier,
                "enabled": check.get("enabled", True),
            }
            if params:
                entry["spec"] = check_param_to_spec(identifier, params)
            result.append(entry)
    return result
