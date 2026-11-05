"""Optional API parameters exposed by the SDK: generation `target_path` / `dataset_id`,
`run_single` `agent_id` / `interactions`, and the `schema_issues` scenario filter."""

import os
import json
import types
import itertools
import collections
from typing import Any, Dict, List, Tuple, Literal, Mapping, Callable, Iterable, Optional

import httpx
import pytest
from respx import MockRouter

from giskard_hub import HubClient, AsyncHubClient
from giskard_hub.types.dataset import ScenarioFiltersParam

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

ID = "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"
OK = httpx.Response(200, json={"data": []})
MODES = ["value", "none", "omitted"]


def _kw(values: Dict[str, Any], combo: Tuple[str, ...]) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    for (field, value), mode in zip(values.items(), combo, strict=True):
        if mode != "omitted":
            out[field] = None if mode == "none" else value
    return out


def _body(route: Any) -> Dict[str, Any]:
    return json.loads(route.calls.last.request.read())


def _assert_fields(body: Dict[str, Any], values: Dict[str, Any], combo: Tuple[str, ...]) -> None:
    for (field, value), mode in zip(values.items(), combo, strict=True):
        if mode == "omitted":
            assert field not in body
        else:
            assert body[field] == (None if mode == "none" else value)


PRESET_ARGS: Dict[str, Any] = {"project_id": ID, "agent_id": ID, "prompt_preset_id": ID, "dataset_name": "d"}
DOC_ARGS: Dict[str, Any] = {"project_id": ID, "agent_id": ID, "knowledge_base_id": ID}
PRESET_VALUES: Dict[str, Any] = {"target_path": "$.response.content", "dataset_id": ID}
DOC_VALUES: Dict[str, Any] = {"target_path": "$.response.content", "dataset_id": ID}
COMBOS = list(itertools.product(MODES, repeat=2))


@pytest.mark.parametrize("combo", COMBOS, ids="-".join)
@pytest.mark.respx(base_url=base_url)
def test_generate_preset_based_sends_target_path(
    client: HubClient, respx_mock: MockRouter, combo: Tuple[str, ...]
) -> None:
    route = respx_mock.post("/v2/datasets/generate-preset-based").mock(return_value=OK)
    client.datasets.with_raw_response.generate_preset_based(**PRESET_ARGS, **_kw(PRESET_VALUES, combo))
    _assert_fields(_body(route), PRESET_VALUES, combo)


@pytest.mark.parametrize("combo", COMBOS, ids="-".join)
@pytest.mark.respx(base_url=base_url)
def test_generate_document_based_sends_dataset_id(
    client: HubClient, respx_mock: MockRouter, combo: Tuple[str, ...]
) -> None:
    route = respx_mock.post("/v2/datasets/generate-document-based").mock(return_value=OK)
    client.datasets.with_raw_response.generate_document_based(**DOC_ARGS, **_kw(DOC_VALUES, combo))
    _assert_fields(_body(route), DOC_VALUES, combo)


@pytest.mark.parametrize("combo", COMBOS, ids="-".join)
@pytest.mark.respx(base_url=base_url)
async def test_async_generate_methods(
    async_client: AsyncHubClient, respx_mock: MockRouter, combo: Tuple[str, ...]
) -> None:
    preset = respx_mock.post("/v2/datasets/generate-preset-based").mock(return_value=OK)
    doc = respx_mock.post("/v2/datasets/generate-document-based").mock(return_value=OK)
    await async_client.datasets.with_raw_response.generate_preset_based(**PRESET_ARGS, **_kw(PRESET_VALUES, combo))
    await async_client.datasets.with_raw_response.generate_document_based(**DOC_ARGS, **_kw(DOC_VALUES, combo))
    _assert_fields(_body(preset), PRESET_VALUES, combo)
    _assert_fields(_body(doc), DOC_VALUES, combo)


Turn = Tuple[Mapping[str, Any], Mapping[str, Any], Optional[Mapping[str, Any]]]
TURNS: List[Turn] = [
    ({"messages": [{"role": "user", "content": "a"}]}, {"response": {"role": "assistant", "content": "b"}}, None),
    ({"messages": [{"role": "user", "content": "c"}]}, {"response": {"role": "assistant", "content": "d"}}, {"k": 1}),
]
EXPECTED_TURNS = [[dict(i), dict(o), None if m is None else dict(m)] for i, o, m in TURNS]


def _interactions_variants() -> List[Tuple[str, Callable[[], Any], Any]]:
    """(id, factory of the value passed to the SDK, expected JSON in the body).
    Factories, so a one-shot generator is not shared between parametrized runs."""
    return [
        ("list-of-tuples", lambda: TURNS, EXPECTED_TURNS),
        ("generator", lambda: (t for t in TURNS), EXPECTED_TURNS),
        ("list-of-lists", lambda: [list(t) for t in TURNS], EXPECTED_TURNS),
        ("empty", lambda: [], []),
        (
            "MappingProxyType",
            lambda: [tuple(None if x is None else types.MappingProxyType(dict(x)) for x in t) for t in TURNS],
            EXPECTED_TURNS,
        ),
        (
            "OrderedDict",
            lambda: [tuple(None if x is None else collections.OrderedDict(x) for x in t) for t in TURNS],
            EXPECTED_TURNS,
        ),
    ]


RUN_ARGS: Dict[str, Any] = {
    "project_id": ID,
    "checks": [{"identifier": "string_matching"}],
    "input_data": {"q": 1},
    "agent_output": "x",
}


@pytest.mark.parametrize("agent_mode", MODES)
@pytest.mark.parametrize("variant", [*_interactions_variants(), ("omitted", lambda: None, None)], ids=lambda v: v[0])
@pytest.mark.respx(base_url=base_url)
def test_run_single_sends_agent_id_and_interactions(
    client: HubClient, respx_mock: MockRouter, variant: Tuple[str, Callable[[], Any], Any], agent_mode: str
) -> None:
    route = respx_mock.post("/v2/evaluations/run-interaction-checks").mock(return_value=OK)
    name, make_value, expected = variant
    kw = _kw({"agent_id": ID}, (agent_mode,))
    if name != "omitted":
        kw["interactions"] = make_value()
    client.evaluations.with_raw_response.run_single(**RUN_ARGS, **kw)
    body = _body(route)
    _assert_fields(body, {"agent_id": ID}, (agent_mode,))
    if name == "omitted":
        assert "interactions" not in body
    else:
        assert body["interactions"] == expected
    assert body["checks"] == [{"identifier": "string_matching"}]


@pytest.mark.respx(base_url=base_url)
async def test_async_run_single_sends_agent_id_and_interactions(
    async_client: AsyncHubClient, respx_mock: MockRouter
) -> None:
    route = respx_mock.post("/v2/evaluations/run-interaction-checks").mock(return_value=OK)
    interactions: Iterable[Turn] = (t for t in TURNS)
    await async_client.evaluations.with_raw_response.run_single(**RUN_ARGS, agent_id=ID, interactions=interactions)
    body = _body(route)
    assert body["agent_id"] == ID
    assert body["interactions"] == EXPECTED_TURNS


@pytest.mark.parametrize("options", [["issues"], ["valid"], ["issues", "valid"]])
@pytest.mark.parametrize("match_mode", ["include", "exclude"])
@pytest.mark.respx(base_url=base_url)
def test_search_scenarios_schema_issues_filter(
    client: HubClient, respx_mock: MockRouter, options: List[str], match_mode: Literal["include", "exclude"]
) -> None:
    route = respx_mock.post(f"/v2/datasets/{ID}/scenarios/search").mock(return_value=OK)
    filters: ScenarioFiltersParam = {"schema_issues": {"selected_options": options, "match_mode": match_mode}}
    client.datasets.with_raw_response.search_scenarios(ID, filters=filters)
    assert _body(route)["filters"] == {"schema_issues": {"selected_options": options, "match_mode": match_mode}}
