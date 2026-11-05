import os
from typing import Any, Dict

import httpx
import pytest
from respx import MockRouter

from giskard_hub import HubClient

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

AUDIT_ID = "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"

AUDIT: Dict[str, Any] = {
    "id": AUDIT_ID,
    "project_id": AUDIT_ID,
    "target_agent_id": AUDIT_ID,
    "input_evaluation_ids": [],
    "output_evaluation_id": None,
    "output_evaluation_name": None,
    "output_dataset_id": None,
    "output_dataset_name": None,
    "name": "imported",
    "mode": "regular",
    "status": "finished",
    "created_at": "2026-11-02T10:00:00Z",
    "updated_at": "2026-11-02T10:00:00Z",
    "started_at": None,
    "run_deadline": None,
    "finished_at": None,
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
}

RISK_MODEL: Dict[str, Any] = {
    "schema_version": 1,
    "wave": "w1",
    "meta": {
        "updated": "2026-11-02",
        "based_on": ["doc"],
        "scope": {"in": ["chat"], "out": ["billing"]},
        "assumptions": [{"text": "t", "source": "s"}],
    },
    "missions": [{"id": "M-1", "name": "m"}],
    "business_assets": [{"id": "BA-1", "name": "b", "why": "w"}],
    "supporting_assets": [{"id": "SA-1", "name": "s", "supports": ["BA-1"]}],
    "feared_events": [{"id": "FE-1", "description": "d", "asset_ids": ["BA-1"], "impact": "G2"}],
    "risk_origins": [{"id": "RO-1", "name": "r", "target_objective": "o"}],
    "scenarios": [
        {
            "id": "SS-1",
            "title": "t",
            "origin_id": "RO-1",
            "feared_event_id": "FE-1",
            "surface": "public_chat",
            "dedup_key": "k",
            "rationale": "r",
        }
    ],
}


@pytest.mark.respx(base_url=base_url)
def test_upload_sends_files_as_multipart(client: HubClient, respx_mock: MockRouter) -> None:
    route = respx_mock.post("/v2/red-team-audits/import").mock(
        return_value=httpx.Response(200, json={"data": AUDIT}),
    )

    audit = client.red_team_audits.upload(
        project_id=AUDIT_ID,
        target_agent_id=AUDIT_ID,
        content=("audit.json", b'{"findings": []}', "application/json"),
        name="imported",
        report=("report.pdf", b"%PDF-1.7", "application/pdf"),
    )

    assert audit.name == "imported"
    request = route.calls.last.request
    assert request.headers["Content-Type"].startswith("multipart/form-data; boundary=")
    body = request.read()
    assert b'name="project_id"' in body
    assert b'name="target_agent_id"' in body
    assert b'name="name"\r\n\r\nimported' in body
    assert b'name="content"; filename="audit.json"' in body
    assert b'{"findings": []}' in body
    assert b'name="report"; filename="report.pdf"' in body
    assert b'name="risk_model"' not in body


@pytest.mark.respx(base_url=base_url)
def test_retrieve_content_parses_risk_model(client: HubClient, respx_mock: MockRouter) -> None:
    respx_mock.get(f"/v2/red-team-audits/{AUDIT_ID}/content").mock(
        return_value=httpx.Response(
            200,
            json={
                "data": {
                    "report": {"raw": True},
                    "generated_at": None,
                    "trust_level": "high",
                    "trust_level_grade": "A",
                    "overall_assessment": {"headline": "h", "body": "b"},
                    "conclusion": None,
                    "risk_model": RISK_MODEL,
                    "attack_counts": {"prompt_injection": 3},
                    "coverage": {"mode": "light", "scenarios_total": 1, "covered_scenario_ids": ["SS-1"]},
                    "findings": [],
                    "remediations": [],
                }
            },
        ),
    )

    content = client.red_team_audits.retrieve_content(AUDIT_ID)

    assert content.risk_model is not None
    assert content.risk_model.meta.scope.in_ == ["chat"]
    assert content.risk_model.supporting_assets[0].notes == ""
    assert content.coverage is not None
    assert content.coverage.uncovered_scenario_ids == []


@pytest.mark.respx(base_url=base_url)
def test_retrieve_parses_progress(client: HubClient, respx_mock: MockRouter) -> None:
    respx_mock.get(f"/v2/red-team-audits/{AUDIT_ID}").mock(
        return_value=httpx.Response(
            200,
            json={
                "data": {
                    **AUDIT,
                    "status": "running",
                    "progress": {"phase": "attacks", "wave": 1, "waves": 3, "findings": 2},
                }
            },
        ),
    )

    audit = client.red_team_audits.retrieve(AUDIT_ID)

    assert audit.progress is not None
    assert audit.progress.phase == "attacks"
    assert audit.progress.attackers_total is None
