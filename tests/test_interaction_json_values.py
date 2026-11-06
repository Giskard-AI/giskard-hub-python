"""`Interaction.input` / `.output` accept any JSON value, like the API (`JsonValue`)."""

# pyright: reportDeprecated=false

import os
import warnings
from typing import Any, Dict, List

import httpx
import pytest
from respx import MockRouter

from giskard_hub import HubClient, AsyncHubClient
from giskard_hub.types import Scenario
from giskard_hub.types.scenario import _first_interaction_messages

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

ID = "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
NOW = "2026-01-01T00:00:00Z"
CHAT_INPUT: Dict[str, Any] = {"messages": [{"role": "user", "content": "hi"}]}

JSON_VALUES: List[Any] = [
    CHAT_INPUT,
    {"query": "hi"},
    {},
    ["a", 1, {"b": None}],
    [],
    "plain text",
    "",
    42,
    -1.5,
    True,
    False,
    None,
]


def _scenario(input_value: Any, output_value: Any) -> Dict[str, Any]:
    return {
        "id": ID,
        "dataset_id": ID,
        "created_at": NOW,
        "updated_at": NOW,
        "interactions": [{"position": 0, "input": input_value, "output": output_value}],
    }


@pytest.mark.parametrize("value", JSON_VALUES, ids=repr)
@pytest.mark.respx(base_url=base_url)
def test_retrieve_parses_any_json_input_and_output(client: HubClient, respx_mock: MockRouter, value: Any) -> None:
    # `client` uses strict response validation: a type mismatch would raise APIResponseValidationError.
    respx_mock.get(f"/v2/scenarios/{ID}").mock(return_value=httpx.Response(200, json={"data": _scenario(value, value)}))
    scenario = client.scenarios.retrieve(ID)
    assert scenario.interactions is not None
    assert scenario.interactions[0].input == value
    assert scenario.interactions[0].output == value


@pytest.mark.parametrize("value", JSON_VALUES, ids=repr)
@pytest.mark.respx(base_url=base_url)
async def test_async_search_parses_any_json_input_and_output(
    async_client: AsyncHubClient, respx_mock: MockRouter, value: Any
) -> None:
    page = {
        "data": [_scenario(value, value)],
        "metadata": {"count": 1, "offset": 0, "limit": 50, "total": 1},
    }
    respx_mock.post(f"/v2/datasets/{ID}/scenarios/search").mock(return_value=httpx.Response(200, json=page))
    items = await async_client.datasets.search_scenarios(ID)
    assert items[0].interactions is not None
    assert items[0].interactions[0].input == value


def test_output_defaults_to_none_when_missing() -> None:
    scenario = Scenario.model_validate({**_scenario(CHAT_INPUT, None), "interactions": [{"position": 0, "input": "x"}]})
    assert scenario.interactions is not None
    assert scenario.interactions[0].output is None


@pytest.mark.parametrize("value", JSON_VALUES, ids=repr)
def test_messages_accessor_never_raises(value: Any) -> None:
    scenario = Scenario.model_validate(_scenario(value, None))
    expected = [("user", "hi")] if value == CHAT_INPUT else []
    assert [(m.role, m.content) for m in _first_interaction_messages(scenario.interactions)] == expected
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        assert [(m.role, m.content) for m in scenario.messages] == expected
