from __future__ import annotations

import os
import json

import httpx
import pytest
from respx import MockRouter

from giskard_hub import HubClient
from giskard_hub.types import PromptPreset

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

_PRESET_JSON = {
    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    "created_at": "2026-01-01T00:00:00Z",
    "updated_at": "2026-01-01T00:00:00Z",
    "name": "name",
    "description": "description",
    "rules": ["rule"],
}


class TestPromptPresetsEndpoint:
    @pytest.mark.respx(base_url=base_url)
    def test_create_calls_prompt_presets_endpoint(self, respx_mock: MockRouter, client: HubClient) -> None:
        route = respx_mock.post("/v2/projects/pid/prompt-presets").mock(
            return_value=httpx.Response(200, json={"data": _PRESET_JSON})
        )

        preset = client.projects.prompt_presets.create(project_id="pid", name="name", description="description")

        assert route.called
        assert isinstance(preset, PromptPreset)
        assert preset.name == "name"

    @pytest.mark.respx(base_url=base_url)
    def test_scenarios_warns_and_calls_prompt_presets_endpoint(self, respx_mock: MockRouter, client: HubClient) -> None:
        route = respx_mock.post("/v2/projects/pid/prompt-presets").mock(
            return_value=httpx.Response(200, json={"data": _PRESET_JSON})
        )

        with pytest.deprecated_call(match="projects.scenarios"):
            scenario = client.projects.scenarios.create(project_id="pid", name="name", description="description")

        assert route.called
        assert isinstance(scenario, PromptPreset)


class TestGeneratePresetBasedEndpoint:
    @pytest.mark.respx(base_url=base_url)
    def test_generate_preset_based_calls_new_endpoint(self, respx_mock: MockRouter, client: HubClient) -> None:
        route = respx_mock.post("/v2/datasets/generate-preset-based").mock(
            return_value=httpx.Response(200, json={"data": {}})
        )

        response = client.datasets.with_raw_response.generate_preset_based(
            project_id="pid",
            agent_id="aid",
            prompt_preset_id="ppid",
            dataset_name="ds",
        )

        assert route.called
        assert response.is_closed is True
        body = json.loads(route.calls.last.request.content)
        assert body["prompt_preset_id"] == "ppid"

    @pytest.mark.respx(base_url=base_url)
    def test_generate_scenario_based_warns_and_calls_new_endpoint(
        self, respx_mock: MockRouter, client: HubClient
    ) -> None:
        route = respx_mock.post("/v2/datasets/generate-preset-based").mock(
            return_value=httpx.Response(200, json={"data": {}})
        )

        with pytest.deprecated_call(match="generate_scenario_based"):
            response = client.datasets.with_raw_response.generate_scenario_based(
                project_id="pid",
                agent_id="aid",
                scenario_id="ppid",
                dataset_name="ds",
            )

        assert route.called
        assert response.is_closed is True
        body = json.loads(route.calls.last.request.content)
        assert body["prompt_preset_id"] == "ppid"
        assert "scenario_id" not in body
