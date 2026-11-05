import os
import json

import httpx
import pytest
from respx import MockRouter

from giskard_hub import HubClient

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

ID = "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
ESTIMATE = {"data": {"operation": "evaluation", "item_count": 3, "estimated_amount": 3}}


@pytest.mark.respx(base_url=base_url)
def test_evaluation_estimate_builds_criteria_like_create(client: HubClient, respx_mock: MockRouter) -> None:
    route = respx_mock.post("/v2/evaluations/estimate").mock(return_value=httpx.Response(200, json=ESTIMATE))

    client.evaluations.estimate(project_id=ID, dataset_id=ID, tags=["a"], run_count=2)

    assert json.loads(route.calls.last.request.read()) == {
        "project_id": ID,
        "criteria": {"dataset_id": ID, "tags": ["a"]},
        "run_count": 2,
    }


def test_evaluation_estimate_requires_exactly_one_target(client: HubClient) -> None:
    with pytest.raises(ValueError, match="Exactly one of"):
        client.evaluations.estimate(project_id=ID)
    with pytest.raises(ValueError, match="Exactly one of"):
        client.evaluations.estimate(project_id=ID, dataset_id=ID, old_evaluation_id=ID)


@pytest.mark.respx(base_url=base_url)
def test_estimate_run_interaction_checks_converts_checks_like_run_single(
    client: HubClient, respx_mock: MockRouter
) -> None:
    route = respx_mock.post("/v2/evaluations/run-interaction-checks/estimate").mock(
        return_value=httpx.Response(200, json=ESTIMATE)
    )

    client.evaluations.estimate_run_interaction_checks(
        project_id=ID,
        checks=[{"identifier": "correctness", "params": {"type": "correctness", "reference": "r"}}],
    )

    assert json.loads(route.calls.last.request.read())["checks"] == [
        {"identifier": "correctness", "override_spec": {"reference": "r"}}
    ]
