"""Request-side helpers for converting `CheckConfigParam` into the wire format."""

from typing import Any, Dict, Iterable, Optional, cast

from .._models import BaseModel
from ..types.check import CheckConfigParam

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
