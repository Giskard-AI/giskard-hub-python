import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, Mapping, Set, Tuple


def load_spec(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _short_schema_repr(schema: Mapping[str, Any] | None) -> str:
    if not isinstance(schema, Mapping):
        return repr(schema)

    ref = schema.get("$ref")
    if isinstance(ref, str):
        return f"$ref={ref}"

    type_ = schema.get("type")
    fmt = schema.get("format")
    enum = schema.get("enum")

    parts: list[str] = []
    if type_:
        parts.append(f"type={type_}")
    if fmt:
        parts.append(f"format={fmt}")
    if enum:
        parts.append(f"enum={enum}")

    if parts:
        return ", ".join(parts)

    # Fallback to a small JSON snippet of interesting keys
    interesting = {
        k: v
        for k, v in schema.items()
        if k in {"oneOf", "anyOf", "allOf", "items"}  # compound shapes
    }
    if interesting:
        return json.dumps(interesting)

    return "{}"


def _build_param_map(
    params: Iterable[Mapping[str, Any]] | None,
) -> Dict[Tuple[str, str], Mapping[str, Any]]:
    result: Dict[Tuple[str, str], Mapping[str, Any]] = {}
    if not params:
        return result

    for p in params:
        name = p.get("name")
        loc = p.get("in")
        if isinstance(name, str) and isinstance(loc, str):
            result[(name, loc)] = p
    return result


def _extract_main_schema(
    response_or_rb: Mapping[str, Any] | None,
) -> Mapping[str, Any] | None:
    if not isinstance(response_or_rb, Mapping):
        return None

    content = response_or_rb.get("content")
    if not isinstance(content, Mapping):
        return None

    # Prefer application/json if present, otherwise first content type
    if "application/json" in content:
        ct_schema = content["application/json"]
    else:
        first = next(iter(content.values()), None)
        ct_schema = first

    if not isinstance(ct_schema, Mapping):
        return None

    schema = ct_schema.get("schema")
    if isinstance(schema, Mapping):
        return schema
    return None


def _print_operation_signature(path: str, method: str, op: Mapping[str, Any]) -> None:
    """Print a concise description of an operation's inputs and outputs."""

    print(f"\n  {path}  [{method.upper()}]")

    summary = op.get("summary")
    if summary:
        print(f"    summary: {summary}")

    # Parameters
    params_map = _build_param_map(op.get("parameters"))
    if params_map:
        print("    parameters:")
        for (name, loc), p in sorted(params_map.items()):
            required = bool(p.get("required", False))
            schema = p.get("schema") if isinstance(p.get("schema"), Mapping) else None
            print(
                f"      - {name!r} in {loc!r} "
                f"(required={required}): {_short_schema_repr(schema)}"
            )

    # Request body
    rb = op.get("requestBody")
    if isinstance(rb, Mapping):
        rb_schema = _extract_main_schema(rb)
        print(
            "    requestBody:"
            f" {_short_schema_repr(rb_schema) if rb_schema is not None else 'no schema'}"
        )

    # Responses
    responses = op.get("responses") or {}
    if isinstance(responses, Mapping) and responses:
        print("    responses:")
        for code in sorted(responses.keys()):
            schema = _extract_main_schema(responses.get(code))
            print(
                f"      - {code}: "
                f"{_short_schema_repr(schema) if schema is not None else 'no schema'}"
            )


def compare_paths(
    current: Dict[str, Any], new: Dict[str, Any]
) -> Tuple[Set[str], Set[str], Set[str]]:
    current_paths = set(current.get("paths", {}).keys())
    new_paths = set(new.get("paths", {}).keys())

    added_paths = new_paths - current_paths
    removed_paths = current_paths - new_paths
    common_paths = current_paths & new_paths

    print("=" * 80)
    print("PATHS COMPARISON")
    print("=" * 80)

    if added_paths:
        print(f"\n✅ ADDED PATHS ({len(added_paths)}):")
        for path in sorted(added_paths):
            path_item = new.get("paths", {}).get(path) or {}
            methods = list(path_item.keys()) if isinstance(path_item, Mapping) else []
            print(f"  {path}: {methods}")

            # For new paths, print full operation signatures for each method so
            # downstream codegen can understand inputs and outputs.
            if isinstance(path_item, Mapping):
                for method, op in sorted(path_item.items()):
                    if isinstance(op, Mapping):
                        _print_operation_signature(path, method, op)

    if removed_paths:
        print(f"\n❌ REMOVED PATHS ({len(removed_paths)}):")
        for path in sorted(removed_paths):
            methods = list(current["paths"][path].keys())
            print(f"  {path}: {methods}")

    print(f"\n📝 CHECKING CHANGES IN COMMON PATHS ({len(common_paths)}):")
    changed_paths: list[str] = []
    for path in sorted(common_paths):
        current_methods = set(current["paths"][path].keys())
        new_methods = set(new["paths"][path].keys())

        added_methods = new_methods - current_methods
        removed_methods = current_methods - new_methods

        if added_methods or removed_methods:
            changed_paths.append(path)
            print(f"\n  {path}:")
            if added_methods:
                print(f"    ➕ Added methods: {sorted(added_methods)}")
                # Also print full signatures for newly added methods on existing
                # paths (these are effectively "new endpoints" for client code).
                path_item = new.get("paths", {}).get(path) or {}
                if isinstance(path_item, Mapping):
                    for method in sorted(added_methods):
                        op = path_item.get(method)
                        if isinstance(op, Mapping):
                            _print_operation_signature(path, method, op)
            if removed_methods:
                print(f"    ➖ Removed methods: {sorted(removed_methods)}")

    if not changed_paths:
        print("  No changes in existing paths")

    return added_paths, removed_paths, set(changed_paths)


def compare_operations(current: Dict[str, Any], new: Dict[str, Any]) -> int:
    """Print detailed per-operation diffs for paths present in both specs.

    Returns the number of operations (path+method) that have any detected change.
    """

    current_paths = current.get("paths", {}) or {}
    new_paths = new.get("paths", {}) or {}
    common_paths = set(current_paths.keys()) & set(new_paths.keys())

    print("\n" + "=" * 80)
    print("DETAILED OPERATION COMPARISON")
    print("=" * 80)

    changed_operations = 0

    for path in sorted(common_paths):
        current_ops = current_paths.get(path) or {}
        new_ops = new_paths.get(path) or {}
        if not isinstance(current_ops, Mapping) or not isinstance(new_ops, Mapping):
            continue

        common_methods = set(current_ops.keys()) & set(new_ops.keys())
        for method in sorted(common_methods):
            op_current = current_ops.get(method) or {}
            op_new = new_ops.get(method) or {}
            if not isinstance(op_current, Mapping) or not isinstance(op_new, Mapping):
                continue

            operation_changed = False
            diffs: list[str] = []

            # Summary / description / operationId changes
            if op_current.get("summary") != op_new.get("summary"):
                diffs.append(
                    f"      - summary changed: {op_current.get('summary')!r} -> {op_new.get('summary')!r}"
                )
            if op_current.get("description") != op_new.get("description"):
                diffs.append("      - description changed")
            if op_current.get("operationId") != op_new.get("operationId"):
                diffs.append(
                    f"      - operationId changed: "
                    f"{op_current.get('operationId')!r} -> {op_new.get('operationId')!r}"
                )

            # Parameters
            params_current = _build_param_map(op_current.get("parameters"))
            params_new = _build_param_map(op_new.get("parameters"))

            added_params = params_new.keys() - params_current.keys()
            removed_params = params_current.keys() - params_new.keys()
            common_params = params_current.keys() & params_new.keys()

            if added_params:
                added_desc = ", ".join(
                    f"{name} in {loc}" for (name, loc) in sorted(added_params)
                )
                diffs.append(f"      - added parameters: {added_desc}")
            if removed_params:
                removed_desc = ", ".join(
                    f"{name} in {loc}" for (name, loc) in sorted(removed_params)
                )
                diffs.append(f"      - removed parameters: {removed_desc}")

            for key in sorted(common_params):
                cur = params_current[key]
                nxt = params_new[key]
                param_changes: list[str] = []

                if cur.get("required") != nxt.get("required"):
                    param_changes.append(
                        f"required {cur.get('required')} -> {nxt.get('required')}"
                    )

                cur_schema = (
                    cur.get("schema")
                    if isinstance(cur.get("schema"), Mapping)
                    else None
                )
                new_schema = (
                    nxt.get("schema")
                    if isinstance(nxt.get("schema"), Mapping)
                    else None
                )
                if cur_schema != new_schema:
                    param_changes.append(
                        f"schema {_short_schema_repr(cur_schema)} -> {_short_schema_repr(new_schema)}"
                    )

                if param_changes:
                    name, loc = key
                    diffs.append(
                        f"      - parameter {name!r} in {loc!r} changed: "
                        + "; ".join(param_changes)
                    )

            # Request body
            rb_current = op_current.get("requestBody")
            rb_new = op_new.get("requestBody")

            if (rb_current is None) != (rb_new is None):
                diffs.append(
                    "      - requestBody presence changed: "
                    f"{'present' if rb_current is not None else 'absent'} -> "
                    f"{'present' if rb_new is not None else 'absent'}"
                )
            elif isinstance(rb_current, Mapping) and isinstance(rb_new, Mapping):
                cur_schema = _extract_main_schema(rb_current)
                new_schema = _extract_main_schema(rb_new)
                if cur_schema != new_schema:
                    diffs.append(
                        "      - requestBody schema changed: "
                        f"{_short_schema_repr(cur_schema)} -> {_short_schema_repr(new_schema)}"
                    )

            # Responses
            resp_current = op_current.get("responses") or {}
            resp_new = op_new.get("responses") or {}
            if isinstance(resp_current, Mapping) and isinstance(resp_new, Mapping):
                codes_current = set(resp_current.keys())
                codes_new = set(resp_new.keys())

                added_codes = codes_new - codes_current
                removed_codes = codes_current - codes_new
                common_codes = codes_current & codes_new

                if added_codes:
                    diffs.append(f"      - added response codes: {sorted(added_codes)}")
                if removed_codes:
                    diffs.append(
                        f"      - removed response codes: {sorted(removed_codes)}"
                    )

                for code in sorted(common_codes):
                    cur_schema = _extract_main_schema(resp_current.get(code))
                    new_schema = _extract_main_schema(resp_new.get(code))
                    if cur_schema != new_schema:
                        diffs.append(
                            f"      - response {code} schema changed: "
                            f"{_short_schema_repr(cur_schema)} -> {_short_schema_repr(new_schema)}"
                        )

            if diffs:
                if not operation_changed:
                    print(f"\n  {path}  [{method.upper()}]")
                    operation_changed = True
                    changed_operations += 1

                for line in diffs:
                    print(line)

    if changed_operations == 0:
        print("  No detailed operation-level changes detected.")

    return changed_operations


def compare_schemas(
    current: Dict[str, Any],
    new: Dict[str, Any],
    sample_limit: int = 100,
) -> Tuple[Set[str], Set[str], Set[str]]:
    current_schemas = set(current.get("components", {}).get("schemas", {}).keys())
    new_schemas = set(new.get("components", {}).get("schemas", {}).keys())

    added_schemas = new_schemas - current_schemas
    removed_schemas = current_schemas - new_schemas

    print("\n" + "=" * 80)
    print("SCHEMAS COMPARISON")
    print("=" * 80)

    if added_schemas:
        print(f"\n✅ ADDED SCHEMAS ({len(added_schemas)}):")
        for schema in sorted(added_schemas):
            print(f"  {schema}")

    if removed_schemas:
        print(f"\n❌ REMOVED SCHEMAS ({len(removed_schemas)}):")
        for schema in sorted(removed_schemas):
            print(f"  {schema}")

    common_schemas = current_schemas & new_schemas
    print(f"\n📝 CHECKING CHANGES IN COMMON SCHEMAS (sample of first {sample_limit}):")

    changed_schemas: list[str] = []
    for i, schema in enumerate(sorted(common_schemas)):
        if i >= sample_limit:
            break

        current_schema = current["components"]["schemas"].get(schema, {})
        new_schema = new["components"]["schemas"].get(schema, {})

        current_props = set(current_schema.get("properties", {}).keys())
        new_props = set(new_schema.get("properties", {}).keys())

        added_props = new_props - current_props
        removed_props = current_props - new_props

        if added_props or removed_props:
            changed_schemas.append(schema)
            print(f"\n  {schema}:")
            if added_props:
                print(f"    ➕ Added properties: {sorted(added_props)}")
            if removed_props:
                print(f"    ➖ Removed properties: {sorted(removed_props)}")

    if not changed_schemas:
        print("  No significant changes detected in sample")

    return added_schemas, removed_schemas, set(changed_schemas)


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Compare two OpenAPI JSON specs and print a high-level summary of "
            "changes in paths and schemas."
        )
    )
    parser.add_argument(
        "current",
        type=Path,
        help="Path to the current (old) OpenAPI JSON file.",
    )
    parser.add_argument(
        "new",
        type=Path,
        help="Path to the new OpenAPI JSON file.",
    )
    parser.add_argument(
        "--schema-sample-limit",
        type=int,
        default=100,
        help="Maximum number of common schemas to inspect for property changes.",
    )

    args = parser.parse_args()

    current_spec = load_spec(args.current)
    new_spec = load_spec(args.new)

    added_paths, removed_paths, changed_paths = compare_paths(current_spec, new_spec)
    changed_operations = compare_operations(current_spec, new_spec)
    added_schemas, removed_schemas, changed_schemas = compare_schemas(
        current_spec,
        new_spec,
        sample_limit=args.schema_sample_limit,
    )

    print("\n" + "=" * 80)
    print(
        f"SUMMARY: {len(added_paths)} paths added, "
        f"{len(removed_paths)} paths removed, "
        f"{len(changed_paths)} paths with method changes, "
        f"{changed_operations} operations with detailed changes"
    )
    print(
        f"SUMMARY: {len(added_schemas)} schemas added, "
        f"{len(removed_schemas)} schemas removed, "
        f"{len(changed_schemas)} schemas with property changes (in sample)"
    )
    print("=" * 80)


if __name__ == "__main__":
    main()
