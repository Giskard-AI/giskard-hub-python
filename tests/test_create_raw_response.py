"""`create` methods that send an analytics event must also work through
`with_raw_response` / `with_streaming_response`, whose result is not a parsed model."""

import os
from typing import Any, Dict, List, Tuple, Callable

import httpx
import pytest
from respx import MockRouter

from giskard_hub import HubClient, AsyncHubClient, _analytics

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

ID = "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
NOW = "2026-01-01T00:00:00Z"
STATUS = {"state": "finished", "current": 1, "total": 1}
REF = {"id": ID}

# (method id, POST path, event name, id property, call(resource client), response data for the parsed model)
Case = Tuple[str, str, str, str, Callable[[Any], Any], Dict[str, Any]]
CASES: List[Case] = [
    (
        "agents",
        "/v2/agents",
        "agent_created",
        "agent_id",
        lambda c: c.agents.create(name="a", project_id=ID, supported_languages=["en"], url="http://x"),
        {
            "id": ID,
            "name": "a",
            "project_id": ID,
            "supported_languages": ["en"],
            "url": "http://x",
            "created_at": NOW,
            "updated_at": NOW,
        },
    ),
    (
        "projects",
        "/v2/projects",
        "project_created",
        "project_id",
        lambda c: c.projects.create(name="p"),
        {"id": ID, "name": "p", "description": "d", "failure_categories": [], "created_at": NOW, "updated_at": NOW},
    ),
    (
        "datasets",
        "/v2/datasets",
        "dataset_created",
        "dataset_id",
        lambda c: c.datasets.create(project_id=ID, name="d"),
        {
            "id": ID,
            "name": "d",
            "project_id": ID,
            "status": STATUS,
            "tags": [],
            "input_schema": {"type": "object"},
            "output_schema": {"type": "object"},
            "created_at": NOW,
            "updated_at": NOW,
        },
    ),
    (
        "knowledge_bases",
        "/v2/knowledge-bases",
        "knowledge_base_created",
        "knowledge_base_id",
        lambda c: c.knowledge_bases.create(project_id=ID, name="k", data=[{"text": "t"}]),
        {
            "id": ID,
            "name": "k",
            "project_id": ID,
            "status": STATUS,
            "n_documents": 1,
            "topics": [],
            "filename": "f",
            "created_at": NOW,
            "updated_at": NOW,
        },
    ),
    (
        "evaluations",
        "/v2/evaluations",
        "evaluation_created",
        "evaluation_id",
        lambda c: c.evaluations.create(project_id=ID, agent_id=ID, dataset_id=ID),
        {},
    ),
    (
        "evaluations.create_local",
        "/v2/evaluations/create-local",
        "local_evaluation_created",
        "evaluation_id",
        lambda c: c.evaluations.create_local(agent_info={"name": "a", "description": "d"}, dataset_id=ID),
        {},
    ),
    ("scans", "/v2/scans", "scan_created", "scan_id", lambda c: c.scans.create(project_id=ID, agent_id=ID), {}),
    (
        "red_team_audits",
        "/v2/red-team-audits",
        "red_team_audit_created",
        "red_team_audit_id",
        lambda c: c.red_team_audits.create(project_id=ID, target_agent_id=ID),
        {},
    ),
]
IDS = [case[0] for case in CASES]


@pytest.fixture
def events(monkeypatch: pytest.MonkeyPatch) -> List[Tuple[str, Dict[str, Any]]]:
    captured: List[Tuple[str, Dict[str, Any]]] = []

    class FakePosthog:
        def capture(self, distinct_id: str, event: str, properties: Dict[str, Any]) -> None:  # noqa: ARG002
            captured.append((event, properties))

    monkeypatch.setattr(_analytics, "_should_disable", lambda: False)
    monkeypatch.setattr(_analytics, "_get_client", lambda: FakePosthog())
    return captured


@pytest.mark.parametrize("case", CASES, ids=IDS)
@pytest.mark.respx(base_url=base_url)
def test_raw_and_streaming_create_do_not_crash(
    client: HubClient, respx_mock: MockRouter, events: List[Tuple[str, Dict[str, Any]]], case: Case
) -> None:
    _, path, event, id_key, call, data = case
    route = respx_mock.post(path).mock(return_value=httpx.Response(200, json={"data": data or REF}))

    raw = call(client.with_raw_response)
    assert raw.http_response.status_code == 200
    with call(client.with_streaming_response) as streamed:
        assert streamed.http_response.status_code == 200

    assert route.call_count == 2
    assert events == [(event, {**events[0][1], id_key: None})] * 2


@pytest.mark.parametrize("case", CASES, ids=IDS)
@pytest.mark.respx(base_url=base_url)
async def test_async_raw_and_streaming_create_do_not_crash(
    async_client: AsyncHubClient, respx_mock: MockRouter, events: List[Tuple[str, Dict[str, Any]]], case: Case
) -> None:
    _, path, event, id_key, call, data = case
    respx_mock.post(path).mock(return_value=httpx.Response(200, json={"data": data or REF}))

    raw = await call(async_client.with_raw_response)
    assert raw.http_response.status_code == 200
    async with call(async_client.with_streaming_response) as streamed:
        assert streamed.http_response.status_code == 200
    assert [(e, p[id_key]) for e, p in events] == [(event, None)] * 2


@pytest.mark.parametrize("case", [c for c in CASES if c[5]], ids=[c[0] for c in CASES if c[5]])
@pytest.mark.respx(base_url=base_url)
def test_plain_create_still_sends_the_id(
    client: HubClient, respx_mock: MockRouter, events: List[Tuple[str, Dict[str, Any]]], case: Case
) -> None:
    _, path, event, id_key, call, data = case
    respx_mock.post(path).mock(return_value=httpx.Response(200, json={"data": data}))
    result = call(client)
    assert result.id == ID
    assert [(e, p[id_key]) for e, p in events] == [(event, ID)]
