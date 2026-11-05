"""An explicit `None` must be left out of the body for fields the API does not accept as null."""

import os
import json
from typing import Any, Dict, Callable, Awaitable

import httpx
import pytest
from respx import MockRouter

from giskard_hub import HubClient, AsyncHubClient

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

ID = "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
FILTERS: Dict[str, Any] = {"status": {"selected_options": ["active"], "match_logic": "any"}}
ORDER_BY: Any = [{"id": "created_at", "desc": True}]
SCHEMA: Dict[str, Any] = {"type": "object"}

AGENT_ARGS: Dict[str, Any] = {"name": "a", "project_id": ID, "supported_languages": ["en"], "url": "http://agent"}
NOW = "2026-01-01T00:00:00Z"
# Valid agent payload, so `agents.create` (no raw-response variant, see analytics) can parse it.
RESPONSE = {"data": {**AGENT_ARGS, "id": ID, "created_at": NOW, "updated_at": NOW}}

# (case id, path, {field: non-null value}, sync call, async call)
CASES: Any = [
    (
        "audit_logs.search",
        "/v2/audit/search",
        {"filters": {"action": {"selected_options": ["insert"], "match_logic": "any"}}, "order_by": ORDER_BY},
        lambda c, kw: c.audit_logs.with_raw_response.search(**kw),
        lambda c, kw: c.audit_logs.with_raw_response.search(**kw),
    ),
    (
        "knowledge_bases.search_documents",
        f"/v2/knowledge-bases/{ID}/documents/search",
        {"filters": {"topic_id": {"selected_options": ["t"], "match_logic": "any"}}, "order_by": ORDER_BY},
        lambda c, kw: c.knowledge_bases.with_raw_response.search_documents(ID, **kw),
        lambda c, kw: c.knowledge_bases.with_raw_response.search_documents(ID, **kw),
    ),
    (
        "datasets.search_scenarios",
        f"/v2/datasets/{ID}/scenarios/search",
        {"filters": FILTERS, "order_by": ORDER_BY},
        lambda c, kw: c.datasets.with_raw_response.search_scenarios(ID, **kw),
        lambda c, kw: c.datasets.with_raw_response.search_scenarios(ID, **kw),
    ),
    (
        "evaluations.results.search",
        f"/v2/evaluations/{ID}/results/search",
        {"filters": {"failure_category": {"selected_options": ["x"], "match_logic": "any"}}, "order_by": ORDER_BY},
        lambda c, kw: c.evaluations.results.with_raw_response.search(ID, **kw),
        lambda c, kw: c.evaluations.results.with_raw_response.search(ID, **kw),
    ),
    (
        "agents.create",
        "/v2/agents",
        {"input_schema": SCHEMA, "output_schema": SCHEMA},
        lambda c, kw: c.agents.create(**AGENT_ARGS, **kw),
        lambda c, kw: c.agents.create(**AGENT_ARGS, **kw),
    ),
    (
        "scenarios.bulk_move",
        "/v2/scenarios/bulk-move",
        {"duplicate": False},
        lambda c, kw: c.scenarios.with_raw_response.bulk_move(scenario_ids=[ID], target_dataset_id=ID, **kw),
        lambda c, kw: c.scenarios.with_raw_response.bulk_move(scenario_ids=[ID], target_dataset_id=ID, **kw),
    ),
    (
        "test_cases.bulk_move",
        "/v2/scenarios/bulk-move",
        {"duplicate": False},
        lambda c, kw: c.test_cases.with_raw_response.bulk_move(test_case_ids=[ID], target_dataset_id=ID, **kw),
        lambda c, kw: c.test_cases.with_raw_response.bulk_move(test_case_ids=[ID], target_dataset_id=ID, **kw),
    ),
]
IDS = [case[0] for case in CASES]
MODES = ["none", "value", "omitted"]


def _kwargs(values: Dict[str, Any], mode: str) -> Dict[str, Any]:
    if mode == "omitted":
        return {}
    return {k: (None if mode == "none" else v) for k, v in values.items()}


def _check_body(route: Any, values: Dict[str, Any], mode: str) -> None:
    body = json.loads(route.calls.last.request.read())
    for field, value in values.items():
        if mode == "value":
            assert body[field] == value
        else:
            assert field not in body


@pytest.mark.filterwarnings("ignore::DeprecationWarning")
@pytest.mark.parametrize("mode", MODES)
@pytest.mark.parametrize("case", CASES, ids=IDS)
@pytest.mark.respx(base_url=base_url)
def test_none_is_left_out_of_body(client: HubClient, respx_mock: MockRouter, case: Any, mode: str) -> None:
    _, path, values, call, _ = case
    route = respx_mock.post(path).mock(return_value=httpx.Response(200, json=RESPONSE))
    call(client, _kwargs(values, mode))
    _check_body(route, values, mode)


@pytest.mark.filterwarnings("ignore::DeprecationWarning")
@pytest.mark.parametrize("mode", MODES)
@pytest.mark.parametrize("case", CASES, ids=IDS)
@pytest.mark.respx(base_url=base_url)
async def test_async_none_is_left_out_of_body(
    async_client: AsyncHubClient, respx_mock: MockRouter, case: Any, mode: str
) -> None:
    _, path, values, _, acall = case
    route = respx_mock.post(path).mock(return_value=httpx.Response(200, json=RESPONSE))
    acall_typed: Callable[[AsyncHubClient, Dict[str, Any]], Awaitable[Any]] = acall
    await acall_typed(async_client, _kwargs(values, mode))
    _check_body(route, values, mode)


UPDATE_NONE = ["name", "url", "supported_languages", "input_schema", "output_schema"]


@pytest.mark.respx(base_url=base_url)
def test_agents_update_leaves_out_none_only_where_null_is_rejected(client: HubClient, respx_mock: MockRouter) -> None:
    route = respx_mock.patch(f"/v2/agents/{ID}").mock(return_value=httpx.Response(200, json=RESPONSE))
    client.agents.update(ID, description=None, auto_bindings=None, **{f: None for f in UPDATE_NONE})
    assert json.loads(route.calls.last.request.read()) == {"description": None, "auto_bindings": None}

    client.agents.update(ID, name="n", url="u", supported_languages=["fr"], input_schema=SCHEMA, output_schema=SCHEMA)
    assert json.loads(route.calls.last.request.read()) == {
        "name": "n",
        "url": "u",
        "supported_languages": ["fr"],
        "input_schema": SCHEMA,
        "output_schema": SCHEMA,
    }


@pytest.mark.respx(base_url=base_url)
async def test_async_agents_update_leaves_out_none(async_client: AsyncHubClient, respx_mock: MockRouter) -> None:
    route = respx_mock.patch(f"/v2/agents/{ID}").mock(return_value=httpx.Response(200, json=RESPONSE))
    await async_client.agents.update(ID, description=None, **{f: None for f in UPDATE_NONE})
    assert json.loads(route.calls.last.request.read()) == {"description": None}
