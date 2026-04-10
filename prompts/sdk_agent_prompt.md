Given the following API changes summary, implement the necessary updates to the Python SDK in this repository.

**Task:**

1. Analyze the API changes carefully
2. Study existing resource files, types, and tests to understand the architecture and patterns before writing any code
3. Implement ONLY the changes mentioned in the summary — no unrelated modifications
4. Maintain consistency with the current implementation style (see conventions below)
5. Update ALL required files for each change (see checklist)

**Checklist — files to update for every new or modified endpoint:**

- [ ] `src/giskard_hub/resources/<resource>.py` — Both the sync class (`SyncAPIResource`) and async class (`AsyncAPIResource`), plus all 4 wrapper classes (`WithRawResponse` and `WithStreamingResponse`, sync and async variants)
- [ ] `src/giskard_hub/types/<resource>.py` — Pydantic `BaseModel` subclasses for responses, `TypedDict` with `Required[]` for request params. Add new types to `__all__` in the same file.
- [ ] `src/giskard_hub/types/__init__.py` — Export every new type (both in the imports section and in `__all__`)
- [ ] `tests/api_resources/test_<resource>.py` — Tests for both sync and async classes
- [ ] `api.md` — Update the API reference (follow the existing format with `<code>` tags and links)

**Coding conventions:**

- **Docstrings**: NumPy style with `Parameters`, `Other Parameters`, `Returns`, and `Raises` sections
- **Method signature**: Path params as positional-only args, then `*` to force keyword-only. Always include these kwargs: `extra_headers`, `extra_query`, `extra_body`, `timeout`
- **Request pattern**: `maybe_transform()` for body, `make_request_options()` for options, `self._unwrap(response)` to return the model. Async uses `async_maybe_transform()` and `await`.
- **Path param validation**: Raise `ValueError` with message `"Expected a non-empty value for 'param' but received {param!r}"` when a path parameter is empty
- **Type safety**: Code must pass strict pyright and mypy. Use `Required[]` on TypedDict fields, `Omit` sentinel for optional params.
- **Tests**: Decorate with `@pytest.mark.skip(reason="Prism tests are disabled")` and `@pytest.mark.parametrize("strict_validation", [False, True], ids=["loose", "strict"])`. Cover these variants for each method: `test_method_<name>`, `test_raw_response_<name>`, `test_streaming_response_<name>`, and `test_path_params_<name>` (if path params exist). Duplicate all tests for the async class. Use `assert_matches_type()`.
- **Linting**: Run `uv run ruff check . --fix` and `uv run ruff format` before committing.

---

**API CHANGES SUMMARY:**

{{SUMMARY}}
