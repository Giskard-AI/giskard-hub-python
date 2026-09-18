import os
import json
import inspect
from typing import Any, Dict, Literal

import httpx
import pytest
from respx import MockRouter

from giskard_hub import HubClient, AsyncHubClient
from giskard_hub.types.common import FilterValueParam
from giskard_hub.types.evaluation import ResultFilterColumn, ResultFiltersParam
from giskard_hub.resources._check_helpers import (
    flat_check_specs,
    check_params_to_specs,
)
from giskard_hub.resources.evaluations.evaluations import (
    EvaluationsResource,
    AsyncEvaluationsResource,
    _normalize_agent_output,
)


def test_check_params_to_specs_emits_flat_shape() -> None:
    api = check_params_to_specs([{"identifier": "hub_correctness", "params": {"reference": "x"}}], flat=True)
    assert api == [{"identifier": "hub_correctness", "reference": "x"}]


def test_check_params_to_specs_strips_redundant_type_when_flat() -> None:
    api = check_params_to_specs(
        [{"identifier": "string_matching", "params": {"type": "string_matching", "keyword": "k"}}],
        flat=True,
    )
    assert api == [{"identifier": "string_matching", "keyword": "k"}]


def test_normalize_agent_output_wraps_string() -> None:
    assert _normalize_agent_output("hi") == {"response": {"role": "assistant", "content": "hi"}}


def test_normalize_agent_output_passes_dict_through() -> None:
    payload: Any = {"response": {"role": "assistant", "content": "hi"}}
    assert _normalize_agent_output(payload) is payload


def test_flat_check_specs_passes_identifier_through() -> None:
    out = flat_check_specs(
        [{"identifier": "hub_correctness", "params": {"reference": "x", "type": "hub_correctness"}}],
    )
    assert out == [{"identifier": "hub_correctness", "override_spec": {"reference": "x"}}]


def test_flat_check_specs_passes_custom_identifier_through() -> None:
    out = flat_check_specs([{"identifier": "tone_pro", "params": {"reference": "x"}}])
    assert out == [{"identifier": "tone_pro", "override_spec": {"reference": "x"}}]


def test_retrieve_and_list_still_accept_include() -> None:
    assert "include" in inspect.signature(EvaluationsResource.retrieve).parameters
    assert "include" in inspect.signature(EvaluationsResource.list).parameters
    assert "include" in inspect.signature(AsyncEvaluationsResource.retrieve).parameters
    assert "include" in inspect.signature(AsyncEvaluationsResource.list).parameters


base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


@pytest.fixture
def evaluation_response(included: bool) -> Dict[str, Any]:
    common = {"created_at": "2026-01-01T00:00:00Z", "updated_at": "2026-01-01T00:00:00Z", "project_id": "p"}
    status = {"state": "finished", "current": 1, "total": 1}
    response: Dict[str, Any] = {
        "data": {
            **common,
            "id": "e",
            "name": "Evaluation",
            "agent": {"id": "a", "name": "Agent"},
            "dataset": {"id": "d", "name": "Dataset"},
            "local": False,
            "status": status,
            "metrics": [],
            "tags": [],
            "failure_categories": {},
        }
    }
    if included:
        response["included"] = {
            "e": {
                "agent": {
                    "data": {
                        **common,
                        "id": "a",
                        "name": "Agent",
                        "url": "https://example.com/agent",
                        "supported_languages": ["en"],
                    }
                },
                "dataset": {
                    "data": {
                        **common,
                        "id": "d",
                        "name": "Dataset",
                        "status": status,
                        "tags": ["smoke"],
                        "input_schema": {},
                        "output_schema": {},
                    }
                },
            }
        }
    return response


@pytest.mark.respx(base_url=base_url)
@pytest.mark.parametrize("included", [False, True])
@pytest.mark.parametrize("include", [None, [], ["agent", "dataset"]])
def test_evaluation_included_resources(
    respx_mock: MockRouter,
    client: HubClient,
    evaluation_response: Dict[str, Any],
    included: bool,
    include: list[Literal["agent", "dataset"]] | None,
) -> None:
    detail = respx_mock.get("/v2/evaluations/e").mock(return_value=httpx.Response(200, json=evaluation_response))
    listing = respx_mock.get("/v2/evaluations").mock(
        return_value=httpx.Response(200, json={**evaluation_response, "data": [evaluation_response["data"]]})
    )

    retrieved = client.evaluations.retrieve("e", include=include)
    listed = client.evaluations.list(project_id="p", include=include)

    for evaluation in [retrieved, *listed]:
        assert evaluation.id == "e"
        assert evaluation.agent.model_dump().get("url") == (
            "https://example.com/agent" if included and include else None
        )
        assert evaluation.dataset.model_dump().get("tags") == (["smoke"] if included and include else None)
    for route in (detail, listing):
        assert route.calls.last.request.url.params.get_list("include") == (include or [])


@pytest.mark.respx(base_url=base_url)
@pytest.mark.parametrize("included", [False, True])
@pytest.mark.parametrize("include", [None, [], ["agent", "dataset"]])
async def test_async_evaluation_included_resources(
    respx_mock: MockRouter,
    async_client: AsyncHubClient,
    evaluation_response: Dict[str, Any],
    included: bool,
    include: list[Literal["agent", "dataset"]] | None,
) -> None:
    detail = respx_mock.get("/v2/evaluations/e").mock(return_value=httpx.Response(200, json=evaluation_response))
    listing = respx_mock.get("/v2/evaluations").mock(
        return_value=httpx.Response(200, json={**evaluation_response, "data": [evaluation_response["data"]]})
    )

    retrieved = await async_client.evaluations.retrieve("e", include=include)
    listed = await async_client.evaluations.list(project_id="p", include=include)

    for evaluation in [retrieved, *listed]:
        assert evaluation.id == "e"
        assert evaluation.agent.model_dump().get("url") == (
            "https://example.com/agent" if included and include else None
        )
        assert evaluation.dataset.model_dump().get("tags") == (["smoke"] if included and include else None)
    for route in (detail, listing):
        assert route.calls.last.request.url.params.get_list("include") == (include or [])
    raw = await async_client.evaluations.with_raw_response.retrieve("e", include=include)
    assert raw.status_code == 200
    async with async_client.evaluations.with_streaming_response.list(project_id="p", include=include) as streamed:
        assert streamed.status_code == 200


@pytest.mark.respx(base_url=base_url)
def test_results_search_accepts_existing_filter_dictionary(respx_mock: MockRouter, client: HubClient) -> None:
    route = respx_mock.post("/v2/evaluations/e/results/search").mock(
        return_value=httpx.Response(
            200,
            json={
                "data": [],
                "metadata": {"total": 0, "offset": 0, "count": 0, "limit": 50},
            },
        )
    )
    filters: Dict[ResultFilterColumn, FilterValueParam] = {"tags": {"selected_options": ["smoke"]}}
    compatible_filters: ResultFiltersParam = filters

    assert client.evaluations.results.search("e", filters=compatible_filters) == []
    assert json.loads(route.calls.last.request.content)["filters"] == filters
