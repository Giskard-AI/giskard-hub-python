"""Request and response checks for the latest Hub API changes."""

import os
import json
from typing import Any, Dict

import httpx
import pytest
from respx import MockRouter

from giskard_hub import HubClient
from giskard_hub.types import TaskUser, CreditEstimate

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

ID = "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
NOW = "2026-01-01T00:00:00Z"

AUDIT = {
    "id": ID,
    "project_id": ID,
    "target_agent_id": ID,
    "input_evaluation_ids": [],
    "scan_types": ["vulnerability", "lidar"],
    "completed_scan_types": [],
    "output_evaluation_id": None,
    "output_evaluation_name": None,
    "output_dataset_id": None,
    "output_dataset_name": None,
    "name": "audit",
    "mode": "regular",
    "status": "finished",
    "created_at": NOW,
    "updated_at": NOW,
    "started_at": None,
    "run_deadline": None,
    "finished_at": NOW,
    "last_heartbeat_at": None,
    "last_log_at": None,
    "runner": None,
    "error": None,
    "logs_truncated": False,
    "evaluation_upload_status": "skipped",
    "evaluation_upload_error": None,
    "evaluation_uploaded_count": 0,
    "trust_level": None,
    "trust_level_grade": None,
    "agent_request_count": 4,
}

KB: Dict[str, Any] = {
    "id": ID,
    "project_id": ID,
    "name": "kb",
    "description": None,
    "created_at": NOW,
    "updated_at": NOW,
    "status": {"state": "finished", "current": 1, "total": 1, "error": None},
    "n_documents": 1,
    "topics": [],
}

DATASET: Dict[str, Any] = {
    "id": ID,
    "project_id": ID,
    "name": "ds",
    "description": None,
    "created_at": NOW,
    "updated_at": NOW,
    "status": {"state": "finished", "current": 0, "total": 0, "error": None},
    "tags": [],
    "input_schema": {},
    "output_schema": {},
}


@pytest.mark.respx(base_url=base_url)
def test_create_audit_sends_run_pre_scan(client: HubClient, respx_mock: MockRouter) -> None:
    route = respx_mock.post("/v2/red-team-audits").mock(return_value=httpx.Response(200, json={"data": AUDIT}))

    audit = client.red_team_audits.create(
        project_id=ID,
        target_agent_id=ID,
        run_pre_scan=False,
    )

    body = json.loads(route.calls.last.request.read())
    assert body["run_pre_scan"] is False
    assert "scan_types" not in body
    assert audit.scan_types == ["vulnerability", "lidar"]
    assert audit.agent_request_count == 4


@pytest.mark.respx(base_url=base_url)
def test_attestation_endpoints(client: HubClient, respx_mock: MockRouter) -> None:
    estimate_route = respx_mock.post("/v2/red-team-audits/attestation-request/estimate").mock(
        return_value=httpx.Response(
            200,
            json={"data": {"operation": "audit_attestation", "item_count": None, "estimated_amount": 1.5}},
        )
    )
    eligibility_route = respx_mock.get(f"/v2/red-team-audits/{ID}/attestation").mock(
        return_value=httpx.Response(
            200,
            json={
                "data": {
                    "audit_id": ID,
                    "eligible": False,
                    "reasons": [
                        {
                            "code": "missing_retest",
                            "message": "Retest the findings first.",
                            "finding_ids": ["F-1"],
                        }
                    ],
                    "latest_request": None,
                }
            },
        )
    )
    request_route = respx_mock.post(f"/v2/red-team-audits/{ID}/attestation-request").mock(
        return_value=httpx.Response(
            201,
            json={
                "data": {
                    "id": ID,
                    "audit_id": ID,
                    "status": "under_review",
                    "requested_at": NOW,
                    "requested_by_email": "user@example.com",
                    "retest_evaluation_id": None,
                    "retest_evaluation_ids": [],
                    "decided_at": None,
                }
            },
        )
    )

    estimate = client.red_team_audits.estimate_attestation()
    eligibility = client.red_team_audits.retrieve_attestation(ID)
    request = client.red_team_audits.request_attestation(ID)

    assert estimate_route.called
    assert isinstance(estimate, CreditEstimate)
    assert estimate.operation == "audit_attestation"
    assert estimate.estimated_amount == 1.5
    assert eligibility_route.called
    assert eligibility.eligible is False
    assert eligibility.reasons[0].code == "missing_retest"
    assert request_route.called
    assert request.status == "under_review"
    assert request.retest_evaluation_id is None


@pytest.mark.respx(base_url=base_url)
def test_bulk_create_scenarios(client: HubClient, respx_mock: MockRouter) -> None:
    route = respx_mock.post(f"/v2/datasets/{ID}/scenarios/bulk").mock(
        return_value=httpx.Response(
            200,
            json={"data": {"dataset_id": ID, "created_count": 1, "scenario_ids": [ID]}},
        )
    )

    result = client.datasets.bulk_create_scenarios(
        ID,
        scenarios=[{"tags": ["billing"], "status": "draft", "interactions": [{"position": 0, "input": {"q": "hi"}}]}],
    )

    body = json.loads(route.calls.last.request.read())
    assert body["scenarios"][0]["tags"] == ["billing"]
    assert body["scenarios"][0]["status"] == "draft"
    assert result.created_count == 1
    assert result.scenario_ids == [ID]


@pytest.mark.respx(base_url=base_url)
def test_create_knowledge_base_from_documents(client: HubClient, respx_mock: MockRouter) -> None:
    route = respx_mock.post("/v2/knowledge-bases/from-documents").mock(
        return_value=httpx.Response(200, json={"data": KB})
    )

    knowledge_base = client.knowledge_bases.create_from_documents(
        project_id=ID,
        name="Policies",
        documents=[{"text": "Refunds take 5 days.", "topic": "billing"}],
        description="Support docs",
    )

    body = json.loads(route.calls.last.request.read())
    assert body == {
        "project_id": ID,
        "name": "Policies",
        "description": "Support docs",
        "documents": [{"text": "Refunds take 5 days.", "topic": "billing"}],
    }
    assert knowledge_base.id == ID


@pytest.mark.respx(base_url=base_url)
def test_retrieve_check_sends_project_id(client: HubClient, respx_mock: MockRouter) -> None:
    route = respx_mock.get(f"/v2/checks/{ID}").mock(
        return_value=httpx.Response(
            200,
            json={
                "data": {
                    "id": ID,
                    "project_id": ID,
                    "identifier": "correctness",
                    "name": "Correctness",
                    "description": None,
                    "created_at": NOW,
                    "updated_at": NOW,
                    "built_in": True,
                    "spec": {"type": "correctness"},
                }
            },
        )
    )

    client.checks.retrieve(ID, project_id=ID)

    assert route.calls.last.request.url.params["project_id"] == ID


@pytest.mark.respx(base_url=base_url)
def test_update_dataset_and_knowledge_base_drop_removed_fields(client: HubClient, respx_mock: MockRouter) -> None:
    dataset_route = respx_mock.patch(f"/v2/datasets/{ID}").mock(
        return_value=httpx.Response(200, json={"data": DATASET})
    )
    kb_route = respx_mock.patch(f"/v2/knowledge-bases/{ID}").mock(return_value=httpx.Response(200, json={"data": KB}))

    client.datasets.update(ID, name="renamed")
    client.knowledge_bases.update(ID, name="renamed", description="docs")

    assert json.loads(dataset_route.calls.last.request.read()) == {"name": "renamed"}
    assert json.loads(kb_route.calls.last.request.read()) == {"name": "renamed", "description": "docs"}


def test_task_user_parses_without_email() -> None:
    user = TaskUser.model_validate({"id": ID, "name": None})
    assert user.id == ID
    assert user.name is None
