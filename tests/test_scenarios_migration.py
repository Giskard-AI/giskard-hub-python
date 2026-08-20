from __future__ import annotations

import os
import json

import httpx
import pytest
from respx import MockRouter

from giskard_hub import HubClient
from giskard_hub.types import Scenario, TestCase

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

_SCENARIO_JSON: dict[str, object] = {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "dataset_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "created_at": "2026-01-01T00:00:00Z",
    "updated_at": "2026-01-01T00:00:00Z",
    "tags": [],
    "interactions": [],
    "comments": [],
    "status": "active",
}


class TestScenariosEndpointMigration:
    @pytest.mark.respx(base_url=base_url)
    def test_scenarios_create_hits_new_endpoint(self, respx_mock: MockRouter, client: HubClient) -> None:
        route = respx_mock.post("/v2/scenarios").mock(return_value=httpx.Response(200, json={"data": _SCENARIO_JSON}))

        scenario = client.scenarios.create(dataset_id="d", interactions=[])

        assert route.called
        assert isinstance(scenario, Scenario)

    @pytest.mark.respx(base_url=base_url)
    def test_test_cases_create_warns_and_hits_new_endpoint(self, respx_mock: MockRouter, client: HubClient) -> None:
        route = respx_mock.post("/v2/scenarios").mock(return_value=httpx.Response(200, json={"data": _SCENARIO_JSON}))

        with pytest.deprecated_call(match="client.test_cases"):
            test_case = client.test_cases.create(dataset_id="d", interactions=[])

        assert route.called
        assert isinstance(test_case, TestCase)

    @pytest.mark.respx(base_url=base_url)
    def test_test_cases_bulk_delete_sends_scenario_ids(self, respx_mock: MockRouter, client: HubClient) -> None:
        route = respx_mock.delete("/v2/scenarios").mock(return_value=httpx.Response(200, json={"data": None}))

        with pytest.deprecated_call(match="client.test_cases"):
            client.test_cases.bulk_delete(test_case_ids=["a", "b"])

        assert route.called
        assert "scenario_ids=a" in str(route.calls.last.request.url)

    @pytest.mark.respx(base_url=base_url)
    def test_tasks_create_maps_deprecated_dataset_test_case_id(self, respx_mock: MockRouter, client: HubClient) -> None:
        route = respx_mock.post("/v2/tasks").mock(return_value=httpx.Response(200, json={"data": {}}))

        with pytest.deprecated_call(match="dataset_test_case_id"):
            client.tasks.with_raw_response.create(project_id="p", description="d", dataset_test_case_id="sc-1")

        assert route.called
        body = json.loads(route.calls.last.request.content)
        assert body["dataset_scenario_id"] == "sc-1"
        assert "dataset_test_case_id" not in body

    @pytest.mark.respx(base_url=base_url)
    def test_visibility_maps_deprecated_set_test_case_draft(self, respx_mock: MockRouter, client: HubClient) -> None:
        route = respx_mock.patch("/v2/evaluations/e/results/r/visibility").mock(
            return_value=httpx.Response(200, json={"data": {}})
        )

        with pytest.deprecated_call(match="set_test_case_draft"):
            client.evaluations.results.with_raw_response.update_visibility(
                "r", evaluation_id="e", hidden=True, set_test_case_draft=True
            )

        assert route.called
        body = json.loads(route.calls.last.request.content)
        assert body["set_scenario_draft"] is True
        assert "set_test_case_draft" not in body

    @pytest.mark.respx(base_url=base_url)
    def test_results_list_translates_include_test_case(self, respx_mock: MockRouter, client: HubClient) -> None:
        route = respx_mock.post("/v2/evaluations/e/results/search").mock(
            return_value=httpx.Response(
                200,
                json={
                    "data": [],
                    "metadata": {"total": 0, "offset": 0, "count": 0, "limit": 1},
                },
            )
        )

        with pytest.deprecated_call(match="include"):
            client.evaluations.results.list(evaluation_id="e", include=["test_case"])

        assert route.called
        assert "include=scenario" in str(route.calls.last.request.url)

    @pytest.mark.respx(base_url=base_url)
    def test_datasets_search_test_cases_warns_and_hits_new_path(
        self, respx_mock: MockRouter, client: HubClient
    ) -> None:
        route = respx_mock.post("/v2/datasets/d/scenarios/search").mock(
            return_value=httpx.Response(
                200,
                json={
                    "data": [],
                    "metadata": {"total": 0, "offset": 0, "count": 0, "limit": 1},
                },
            )
        )

        with pytest.deprecated_call(match="datasets.search_test_cases"):
            client.datasets.search_test_cases("d", limit=1)

        assert route.called

    @pytest.mark.respx(base_url=base_url)
    def test_rerun_scenario_hits_new_endpoint_without_warning(self, respx_mock: MockRouter, client: HubClient) -> None:
        route = respx_mock.post("/v2/evaluations/e/results/r/rerun-scenario").mock(
            return_value=httpx.Response(200, json={"data": {}})
        )

        client.evaluations.results.with_raw_response.rerun_scenario("r", evaluation_id="e")

        assert route.called

    @pytest.mark.respx(base_url=base_url)
    def test_visibility_accepts_set_scenario_draft_without_warning(
        self, respx_mock: MockRouter, client: HubClient
    ) -> None:
        route = respx_mock.patch("/v2/evaluations/e/results/r/visibility").mock(
            return_value=httpx.Response(200, json={"data": {}})
        )

        client.evaluations.results.with_raw_response.update_visibility(
            "r", evaluation_id="e", hidden=True, set_scenario_draft=True
        )

        assert route.called
        body = json.loads(route.calls.last.request.content)
        assert body["set_scenario_draft"] is True

    def test_deprecated_types_are_plain_aliases(self) -> None:
        from giskard_hub.types import ScenarioComment, TestCaseComment
        from giskard_hub.types.evaluation import ScenarioEvaluation, TestCaseEvaluation

        assert TestCase is Scenario
        assert TestCaseComment is ScenarioComment
        assert TestCaseEvaluation is ScenarioEvaluation
