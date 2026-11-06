"""`Task.references` items get the model that matches their `type` (the API's LinkedEntityReference)."""

import os
import itertools
from typing import Any, Dict, List, Type

import httpx
import pytest
from respx import MockRouter

from giskard_hub import HubClient, AsyncHubClient
from giskard_hub.types import (
    ScenarioReference,
    ScenarioEvaluation,
    UnknownTaskReference,
    ScanProbeAttemptReference,
    ScenarioEvaluationReference,
)
from giskard_hub._models import BaseModel

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

ID = "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
NOW = "2026-01-01T00:00:00Z"
PROJECT = {"type": "project", "id": ID}

# Payloads as the v3.1.0 API serializes them (models/entity_reference.py).
EVAL_REF = {
    "type": "test_case_evaluation",
    "id": "e1",
    "evaluation": {"type": "evaluation", "id": ID, "project": PROJECT},
}
PROBE_REF = {
    "type": "probe_attempt",
    "id": "p1",
    "probe_result": {"type": "probe_result", "id": ID, "scan": {"type": "scan", "id": ID, "project": PROJECT}},
}
SCENARIO_REF = {
    "type": "test_case",
    "id": "s1",
    "dataset": {"type": "dataset", "id": ID, "project": PROJECT},
    "source_evaluation": None,
}
SCENARIO_REF_FROM_EVAL = {**SCENARIO_REF, "id": "s2", "source_evaluation": EVAL_REF}

EXPECTED: Dict[str, Type[BaseModel]] = {
    "test_case_evaluation": ScenarioEvaluationReference,
    "probe_attempt": ScanProbeAttemptReference,
    "test_case": ScenarioReference,
}
ALL_REFS: List[Dict[str, Any]] = [EVAL_REF, PROBE_REF, SCENARIO_REF, SCENARIO_REF_FROM_EVAL]


def _task(references: List[Dict[str, Any]]) -> Dict[str, Any]:
    user = {"id": ID, "email": "u@example.com", "name": "u"}
    return {
        "id": ID,
        "project_id": ID,
        "status": "open",
        "description": "d",
        "created_by": user,
        "assignees": [user],
        "references": references,
        "created_at": NOW,
        "updated_at": NOW,
    }


def _check(references: List[Any], payloads: List[Dict[str, Any]]) -> None:
    assert len(references) == len(payloads)
    for ref, payload in zip(references, payloads, strict=True):
        assert ref.id == payload["id"]
        assert ref.type == payload["type"]
        assert type(ref) is EXPECTED[payload["type"]]


# every ordered combination of 1..4 references (all permutations), so position never decides the type
COMBOS = [list(p) for n in range(1, len(ALL_REFS) + 1) for p in itertools.permutations(ALL_REFS, n)]


@pytest.mark.parametrize("payloads", COMBOS, ids=lambda p: "+".join(r["id"] for r in p))
@pytest.mark.respx(base_url=base_url)
def test_retrieve_picks_model_by_type(
    client: HubClient, respx_mock: MockRouter, payloads: List[Dict[str, Any]]
) -> None:
    respx_mock.get(f"/v2/tasks/{ID}").mock(return_value=httpx.Response(200, json={"data": _task(payloads)}))
    _check(client.tasks.retrieve(ID).references, payloads)


@pytest.mark.respx(base_url=base_url)
async def test_async_list_picks_model_by_type(async_client: AsyncHubClient, respx_mock: MockRouter) -> None:
    tasks = [_task(p) for p in COMBOS]
    respx_mock.get("/v2/tasks").mock(return_value=httpx.Response(200, json={"data": tasks}))
    result = await async_client.tasks.list(project_id=ID)
    for task, payloads in zip(result, COMBOS, strict=True):
        _check(task.references, payloads)


def test_nested_data_is_kept_as_extra_fields() -> None:
    ref = ScenarioReference.model_validate(SCENARIO_REF_FROM_EVAL)
    assert ref.model_dump()["dataset"]["id"] == ID
    assert ref.model_dump()["source_evaluation"]["type"] == "test_case_evaluation"


@pytest.mark.parametrize("model", [ScenarioEvaluationReference, ScanProbeAttemptReference, ScenarioReference])
def test_id_only_payload_still_parses_with_default_type(model: Type[Any]) -> None:
    ref = model.model_validate({"id": "x"})
    assert ref.id == "x"
    assert ref.type == model.model_fields["type"].default


def test_scenario_evaluation_scenario_reference_and_full_scenario() -> None:
    base: Dict[str, Any] = {
        "id": "r1",
        "evaluation_id": ID,
        "state": "finished",
        "results": [],
        "hidden": False,
        "created_at": NOW,
        "updated_at": NOW,
    }
    # The API sends `scenario` as {"id": ...} (ScenarioAPIReference, no `type`) or the full scenario when included.
    ref_only = ScenarioEvaluation.model_validate({**base, "scenario": {"id": "s1"}}, strict=False)
    assert type(ref_only.scenario) is ScenarioReference
    full: Dict[str, Any] = {"id": "s1", "dataset_id": ID, "created_at": NOW, "updated_at": NOW, "interactions": []}
    with_full = ScenarioEvaluation.model_validate({**base, "scenario": full}, strict=False)
    assert type(with_full.scenario).__name__ == "Scenario"


UNKNOWN_REF = {"type": "some_future_type", "id": "x1", "anything": {"nested": True}}


@pytest.mark.parametrize("strict", [True, False], ids=["strict", "loose"])
@pytest.mark.respx(base_url=base_url)
def test_unknown_type_falls_back_instead_of_failing(respx_mock: MockRouter, strict: bool) -> None:
    payloads = [SCENARIO_REF, UNKNOWN_REF, PROBE_REF, {"id": "no-type"}]
    respx_mock.get(f"/v2/tasks/{ID}").mock(return_value=httpx.Response(200, json={"data": _task(payloads)}))
    client = HubClient(api_key="k", base_url=base_url, auto_add_api_suffix=False, _strict_response_validation=strict)
    refs = client.tasks.retrieve(ID).references
    assert [type(r) for r in refs] == [
        ScenarioReference,
        UnknownTaskReference,
        ScanProbeAttemptReference,
        ScenarioEvaluationReference,  # no `type`: same model as before this change
    ]
    assert [r.id for r in refs] == ["s1", "x1", "p1", "no-type"]
    assert refs[1].type == "some_future_type"


@pytest.mark.parametrize("payloads", COMBOS[:20], ids=lambda p: "+".join(r["id"] for r in p))
@pytest.mark.respx(base_url=base_url)
def test_loose_client_picks_model_by_type(respx_mock: MockRouter, payloads: List[Dict[str, Any]]) -> None:
    respx_mock.get(f"/v2/tasks/{ID}").mock(return_value=httpx.Response(200, json={"data": _task(payloads)}))
    client = HubClient(api_key="k", base_url=base_url, auto_add_api_suffix=False, _strict_response_validation=False)
    _check(client.tasks.retrieve(ID).references, payloads)
