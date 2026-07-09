import json
from typing import Tuple, cast
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

from giskard_hub import HubClient, AsyncHubClient
from giskard_hub.resources.datasets import _prepare_upload_data_sync

base_url = "http://127.0.0.1:4010"
api_key = "test-api-key"


def test_datasets_upload_converts_str_to_path(tmp_path: Path) -> None:
    json_file = tmp_path / "test.json"
    json_file.write_text('[{"col1": "val1", "col2": "val2"}]')

    client = HubClient(base_url=base_url, api_key=api_key, auto_add_api_suffix=False)

    with patch.object(client.datasets, "_post", return_value=MagicMock()) as mock_post:
        client.datasets.upload(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data=str(json_file),
        )

        files = mock_post.call_args.kwargs["files"]
        assert len(files) == 1
        assert files[0][0] == "file"
        assert isinstance(files[0][1], Path)
        assert files[0][1] == json_file


def test_knowledge_bases_create_converts_str_to_path(tmp_path: Path) -> None:
    jsonl_file = tmp_path / "documents.jsonl"
    jsonl_file.write_text('{"text": "doc1", "topic": "topic1"}\n')

    client = HubClient(base_url=base_url, api_key=api_key, auto_add_api_suffix=False)

    with patch.object(client.knowledge_bases, "_post", return_value=MagicMock()) as mock_post:
        client.knowledge_bases.create(
            name="test-kb",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data=str(jsonl_file),
        )

        files = mock_post.call_args.kwargs["files"]
        assert len(files) == 1
        assert files[0][0] == "file"
        assert isinstance(files[0][1], Path)
        assert files[0][1] == jsonl_file


async def test_async_datasets_upload_converts_str_to_path(tmp_path: Path) -> None:
    json_file = tmp_path / "test.json"
    json_file.write_text('[{"col1": "val1", "col2": "val2"}]')

    async with AsyncHubClient(base_url=base_url, api_key=api_key, auto_add_api_suffix=False) as client:
        with patch.object(client.datasets, "_post", new_callable=AsyncMock, return_value=MagicMock()) as mock_post:
            await client.datasets.upload(
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                data=str(json_file),
            )

            files = mock_post.call_args.kwargs["files"]
            assert len(files) == 1
            assert files[0][0] == "file"
            assert isinstance(files[0][1], Path)
            assert files[0][1] == json_file


def test_upload_list_defaults_interaction_positions() -> None:
    # New-shape items with omitted `position` get the interaction's list index.
    data = [{"interactions": [{"input": {"a": 1}}, {"position": 5, "input": {"b": 2}}, {"input": {"c": 3}}]}]
    name, payload = cast("Tuple[str, bytes]", _prepare_upload_data_sync(MagicMock(), data, project_id="p"))
    assert name == "test_cases.json"
    items = json.loads(payload)
    assert [i["position"] for i in items[0]["interactions"]] == [0, 5, 2]
    # Caller's dicts are not mutated.
    assert "position" not in data[0]["interactions"][0]


def test_upload_file_defaults_interaction_positions(tmp_path: Path) -> None:
    json_file = tmp_path / "tc.json"
    json_file.write_text(json.dumps([{"interactions": [{"input": {"a": 1}}, {"input": {"b": 2}}]}]))
    result = _prepare_upload_data_sync(MagicMock(), json_file, project_id="p")
    assert isinstance(result, tuple)  # re-encoded, not passed through
    items = json.loads(cast("bytes", result[1]))
    assert [i["position"] for i in items[0]["interactions"]] == [0, 1]


def test_upload_file_without_interactions_passes_through(tmp_path: Path) -> None:
    json_file = tmp_path / "plain.json"
    json_file.write_text(json.dumps([{"col1": "val1"}]))
    # Nothing to translate or fill -> the original Path is forwarded unchanged.
    assert _prepare_upload_data_sync(MagicMock(), json_file, project_id="p") == json_file


async def test_async_knowledge_bases_create_converts_str_to_path(tmp_path: Path) -> None:
    jsonl_file = tmp_path / "documents.jsonl"
    jsonl_file.write_text('{"text": "doc1", "topic": "topic1"}\n')

    async with AsyncHubClient(base_url=base_url, api_key=api_key, auto_add_api_suffix=False) as client:
        with patch.object(
            client.knowledge_bases, "_post", new_callable=AsyncMock, return_value=MagicMock()
        ) as mock_post:
            await client.knowledge_bases.create(
                name="test-kb",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                data=str(jsonl_file),
            )

            files = mock_post.call_args.kwargs["files"]
            assert len(files) == 1
            assert files[0][0] == "file"
            assert isinstance(files[0][1], Path)
            assert files[0][1] == jsonl_file
