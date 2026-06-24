from __future__ import annotations

import json
import warnings
from typing import Any, List, Tuple, Literal, Mapping, Optional, cast, overload
from pathlib import Path

import httpx

from ..types import (
    TestCaseFiltersParam,
    TestCaseOrderByParam,
    DatasetSearchTestCasesParams,
)
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.common import APIResponse, TaskProgressParam, APIPaginatedMetadata, APIPaginatedResponse
from ..types.dataset import (
    Dataset,
    DatasetListParams,
    DatasetCreateParams,
    DatasetImportParams,
    DatasetUpdateParams,
    DatasetBulkDeleteParams,
    DatasetGenerateDocumentBasedParams,
    DatasetGenerateScenarioBasedParams,
)
from ..types.test_case import TestCase
from ._interaction_helpers import is_legacy_upload_item, translate_legacy_upload_item

__all__ = ["DatasetsResource", "AsyncDatasetsResource"]


_LEGACY_UPLOAD_DEPRECATION = (
    "Passing legacy `messages` / `checks` / `demo_output` items to "
    "`datasets.upload` is deprecated. Use the new "
    "`{interactions: [{position, input, output, checks}]}` shape."
)


def _read_dataset_file(path: Path) -> Optional[Tuple[List[dict[str, Any]], Literal["json", "jsonl"]]]:
    """Read a `.json` / `.jsonl` dataset file into a list of dicts.

    Returns `(items, format)` or `None` if the file is not a recognized
    JSON dataset (binary, unsupported extension, malformed, etc) — in that
    case the caller should pass the file through unchanged so the backend
    can return a clear error.
    """
    suffix = path.suffix.lower()
    if suffix not in (".json", ".jsonl"):
        return None
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    try:
        if suffix == ".json":
            data = json.loads(text)
            if not isinstance(data, list):
                return None
            return cast(List[dict[str, Any]], data), "json"
        items: List[dict[str, Any]] = []
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            if not isinstance(obj, dict):
                return None
            items.append(cast(dict[str, Any], obj))
        return items, "jsonl"
    except json.JSONDecodeError:
        return None


def _encode_items(items: List[dict[str, Any]], fmt: Literal["json", "jsonl"]) -> bytes:
    """Re-encode a list of dicts back into the original JSON/JSONL format."""
    if fmt == "jsonl":
        return ("\n".join(json.dumps(it) for it in items) + "\n").encode("utf-8")
    return json.dumps(items).encode("utf-8")


def _maybe_translate_items(items: List[dict[str, Any]], identifier_to_id: Mapping[str, str]) -> List[dict[str, Any]]:
    """Translate any legacy items in the list, leaving new-shape items alone."""
    return [translate_legacy_upload_item(it, identifier_to_id) if is_legacy_upload_item(it) else it for it in items]


def _checks_lookup_needed(items: List[dict[str, Any]]) -> bool:
    return any(item.get("checks") for item in items if is_legacy_upload_item(item))


def _prepare_upload_data_sync(
    resource: "DatasetsResource",
    data: "FileTypes | list[dict[str, Any]] | str | Path",
    *,
    project_id: str,
) -> "FileTypes | Tuple[str, bytes]":
    """Translate legacy `data` (list, .json file, or .jsonl file) into the
    new import shape; pass other `FileTypes` through unchanged."""
    if isinstance(data, str):
        data = Path(data)

    if isinstance(data, list):
        items: List[dict[str, Any]] = data
        needs_translation = any(is_legacy_upload_item(it) for it in items)
        if needs_translation:
            warnings.warn(_LEGACY_UPLOAD_DEPRECATION, DeprecationWarning, stacklevel=4)
            identifier_to_id: dict[str, str] = {}
            if _checks_lookup_needed(items):
                identifier_to_id = {
                    c.identifier: c.id
                    for c in resource._client.checks.list(project_id=project_id, filter_builtin=False)
                }
            items = _maybe_translate_items(items, identifier_to_id)
        return ("test_cases.json", _encode_items(items, "json"))

    if isinstance(data, Path):
        parsed = _read_dataset_file(data)
        if parsed is None:
            # Not a JSON/JSONL dataset we can introspect — pass through.
            return data
        items, fmt = parsed
        needs_translation = any(is_legacy_upload_item(it) for it in items)
        if not needs_translation:
            return data
        warnings.warn(_LEGACY_UPLOAD_DEPRECATION, DeprecationWarning, stacklevel=4)
        identifier_to_id = {}
        if _checks_lookup_needed(items):
            identifier_to_id = {
                c.identifier: c.id for c in resource._client.checks.list(project_id=project_id, filter_builtin=False)
            }
        items = _maybe_translate_items(items, identifier_to_id)
        return (data.name, _encode_items(items, fmt))

    return data


async def _prepare_upload_data_async(
    resource: "AsyncDatasetsResource",
    data: "FileTypes | list[dict[str, Any]] | str | Path",
    *,
    project_id: str,
) -> "FileTypes | Tuple[str, bytes]":
    """Async variant of :func:`_prepare_upload_data_sync`."""
    if isinstance(data, str):
        data = Path(data)

    if isinstance(data, list):
        items: List[dict[str, Any]] = data
        needs_translation = any(is_legacy_upload_item(it) for it in items)
        if needs_translation:
            warnings.warn(_LEGACY_UPLOAD_DEPRECATION, DeprecationWarning, stacklevel=4)
            identifier_to_id: dict[str, str] = {}
            if _checks_lookup_needed(items):
                identifier_to_id = {
                    c.identifier: c.id
                    for c in await resource._client.checks.list(project_id=project_id, filter_builtin=False)
                }
            items = _maybe_translate_items(items, identifier_to_id)
        return ("test_cases.json", _encode_items(items, "json"))

    if isinstance(data, Path):
        parsed = _read_dataset_file(data)
        if parsed is None:
            return data
        items, fmt = parsed
        needs_translation = any(is_legacy_upload_item(it) for it in items)
        if not needs_translation:
            return data
        warnings.warn(_LEGACY_UPLOAD_DEPRECATION, DeprecationWarning, stacklevel=4)
        identifier_to_id = {}
        if _checks_lookup_needed(items):
            identifier_to_id = {
                c.identifier: c.id
                for c in await resource._client.checks.list(project_id=project_id, filter_builtin=False)
            }
        items = _maybe_translate_items(items, identifier_to_id)
        return (data.name, _encode_items(items, fmt))

    return data


class DatasetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return DatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return DatasetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        project_id: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dataset:
        """Create a new empty dataset in the specified project.

        Parameters
        ----------
        name : str
            Name of the dataset to create.
        project_id : str
            Project ID to create the dataset in.
        description : Optional[str]
            Description of the dataset to create.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        Dataset
            The newly created dataset.
        """
        response = self._post(
            "/v2/datasets",
            body=maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "description": description,
                },
                DatasetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Dataset],
        )

        return self._unwrap(response)

    def upload(
        self,
        *,
        project_id: str,
        data: FileTypes | list[dict[str, Any]] | str,
        dataset_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dataset:
        """Upload a dataset from a file or a list of dictionaries.

        Parameters
        ----------
        project_id : str
            Project ID to import the dataset into.
        data : FileTypes | list[dict[str, Any]] | str
            Data to upload. Accepts a list of dicts, a path to a `.json` /
            `.jsonl` file, or any binary file-like supported by `FileTypes`.
            Items in the legacy `messages` / `checks` / `demo_output` shape
            are translated client-side to the new `interactions` format.
        dataset_id : str | None | Omit
            Dataset ID to merge the items into. If omitted, a new dataset is
            created.
        name : str | None | Omit
            Name of the dataset. Used when creating a new dataset.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        Dataset
            The uploaded dataset.
        """
        data = _prepare_upload_data_sync(self, data, project_id=project_id)

        body = deepcopy_minimal(
            {
                "file": data,
            }
        )

        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])

        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}

        response = self._post(
            "/v2/datasets/import",
            body=maybe_transform(body, DatasetImportParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "project_id": project_id,
                        "dataset_id": dataset_id,
                        "name": name,
                    },
                    DatasetImportParams,
                ),
            ),
            cast_to=APIResponse[Dataset],
        )

        return self._unwrap(response)

    def retrieve(
        self,
        dataset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dataset:
        """Retrieve a dataset by its ID.

        Parameters
        ----------
        dataset_id : str
            ID of the dataset to retrieve.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        Dataset
            The retrieved dataset.

        Raises
        ------
        ValueError
            If `dataset_id` is empty.
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        response = self._get(
            f"/v2/datasets/{dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Dataset],
        )

        return self._unwrap(response)

    def update(
        self,
        dataset_id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        status: Optional[TaskProgressParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dataset:
        """Update an existing dataset's metadata.

        Parameters
        ----------
        dataset_id : str
            ID of the dataset to update.
        description : Optional[str]
            Description of the dataset to update.
        name : Optional[str]
            Name of the dataset to update.
        status : Optional[TaskProgressParam]
            Status of the dataset to update.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        Dataset
            The updated dataset.

        Raises
        ------
        ValueError
            If `dataset_id` is empty.
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        response = self._patch(
            f"/v2/datasets/{dataset_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "status": status,
                },
                DatasetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Dataset],
        )

        return self._unwrap(response)

    def list(
        self,
        *,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[Dataset]:
        """List all datasets, optionally filtered by project.

        Parameters
        ----------
        project_id : Optional[str]
            Project ID to list datasets for.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        List[Dataset]
            A list of datasets.
        """
        response = self._get(
            "/v2/datasets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, DatasetListParams),
            ),
            cast_to=APIResponse[List[Dataset]],
        )

        return self._unwrap(response)

    def delete(
        self,
        dataset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a dataset by its ID.

        Parameters
        ----------
        dataset_id : str
            ID of the dataset to delete.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If `dataset_id` is empty.
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        response = self._delete(
            f"/v2/datasets/{dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    def bulk_delete(
        self,
        *,
        dataset_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete multiple datasets at once.

        Parameters
        ----------
        dataset_ids : SequenceNotStr[str]
            IDs of the datasets to delete.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        None
        """
        response = self._delete(
            "/v2/datasets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dataset_ids": dataset_ids}, DatasetBulkDeleteParams),
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    def generate_scenario_based(
        self,
        *,
        project_id: str,
        agent_id: str,
        scenario_id: str,
        n_examples: int | Omit = omit,
        dataset_id: Optional[str] | Omit = omit,
        dataset_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dataset:
        """Generate a dataset of test cases from scenario definitions.

        Parameters
        ----------
        project_id : str
            The ID of the project.
        agent_id : str
            The ID of the agent to use for generation.
        scenario_id : str
            The ID of the scenario to use.
        n_examples : int
            Total number of examples to generate.
        dataset_id : Optional[str]
            The ID of the dataset to use (required when dataset_name is not provided).
        dataset_name : Optional[str]
            Name for the generated dataset.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        Dataset
            The generated dataset.

        Raises
        ------
        ValueError
            If neither `dataset_id` nor `dataset_name` is provided.
        """

        if dataset_id is omit and dataset_name is omit:
            raise ValueError("'dataset_name' is required when 'dataset_id' is not provided")

        response = self._post(
            "/v2/datasets/generate-scenario-based",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "project_id": project_id,
                    "scenario_id": scenario_id,
                    "dataset_name": dataset_name,
                    "num_examples": n_examples,
                    "dataset_id": dataset_id,
                },
                DatasetGenerateScenarioBasedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Dataset],
        )

        return self._unwrap(response)

    def generate_document_based(
        self,
        *,
        agent_id: str,
        knowledge_base_id: str,
        project_id: str,
        dataset_name: str | Omit = omit,
        description: Optional[str] | Omit = omit,
        n_examples: int | Omit = omit,
        topic_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dataset:
        """Generate a dataset of test cases from knowledge base documents.

        Parameters
        ----------
        agent_id : str
            The ID of the agent to use for generation.
        knowledge_base_id : str
            The ID of the knowledge base to use for generation.
        project_id : str
            The ID of the project to use for generation.
        dataset_name : str
            Name for the generated dataset.
        description : Optional[str]
            Description of the generated dataset.
        n_examples : int
            Total number of examples to generate.
        topic_ids : SequenceNotStr[str]
            IDs of the topics to use for generation.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        Dataset
            The generated dataset.
        """
        response = self._post(
            "/v2/datasets/generate-document-based",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "knowledge_base_id": knowledge_base_id,
                    "project_id": project_id,
                    "dataset_name": dataset_name,
                    "description": description,
                    "n_examples": n_examples,
                    "topic_ids": topic_ids,
                },
                DatasetGenerateDocumentBasedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Dataset],
        )

        return self._unwrap(response)

    def list_tags(
        self,
        dataset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[str]:
        """List all tags associated with a dataset.

        Parameters
        ----------
        dataset_id : str
            The ID of the dataset to list tags for.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        List[str]
            A list of tag strings.

        Raises
        ------
        ValueError
            If `dataset_id` is empty.
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        response = self._get(
            f"/v2/datasets/{dataset_id}/tags",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[str]],
        )

        return self._unwrap(response)

    def list_test_cases(
        self,
        dataset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[TestCase]:
        """List all test cases belonging to a dataset.

        Fetches every page via :meth:`search_test_cases` (same as an unfiltered search).

        Parameters
        ----------
        dataset_id : str
            The ID of the dataset to list test cases for.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        List[TestCase]
            A list of test cases.

        Raises
        ------
        ValueError
            If `dataset_id` is empty.
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        page_limit = 100
        all_items: List[TestCase] = []
        offset = 0
        while True:
            page, meta = self.search_test_cases(
                dataset_id,
                limit=page_limit,
                offset=offset,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                include_metadata=True,
            )
            all_items.extend(page)
            next_offset = meta.offset + meta.count
            if next_offset >= meta.total or not page:
                break
            offset = next_offset
        return all_items

    @overload
    def search_test_cases(
        self,
        dataset_id: str,
        *,
        query: Optional[str] | Omit = omit,
        order_by: Optional[List[TestCaseOrderByParam]] | Omit = omit,
        filters: Optional[TestCaseFiltersParam] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: Literal[False] = False,
    ) -> List[TestCase]: ...

    @overload
    def search_test_cases(
        self,
        dataset_id: str,
        *,
        query: Optional[str] | Omit = omit,
        order_by: Optional[List[TestCaseOrderByParam]] | Omit = omit,
        filters: Optional[TestCaseFiltersParam] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: Literal[True] = True,
    ) -> Tuple[List[TestCase], APIPaginatedMetadata]: ...

    def search_test_cases(
        self,
        dataset_id: str,
        *,
        query: Optional[str] | Omit = omit,
        order_by: Optional[List[TestCaseOrderByParam]] | Omit = omit,
        filters: Optional[TestCaseFiltersParam] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: bool = False,
    ) -> List[TestCase] | Tuple[List[TestCase], APIPaginatedMetadata]:
        """Search test cases in a dataset using filters, sorting, and pagination.

        Parameters
        ----------
        dataset_id : str
            The ID of the dataset to search test cases in.
        query : Optional[str]
            Search query for test cases.
        order_by : Optional[List[TestCaseOrderByParam]]
            Order by criteria for test cases.
        filters : Optional[TestCaseFiltersParam]
            Search filters to apply.
        limit : int
            Maximum number of results to return.
        offset : int
            Number of results to skip.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        List[TestCase] | Tuple[List[TestCase], APIPaginatedMetadata]
            A list of matching test cases, optionally with pagination metadata.

        Raises
        ------
        ValueError
            If `dataset_id` is empty.
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        response = self._post(
            f"/v2/datasets/{dataset_id}/test-cases/search",
            body=maybe_transform(
                {
                    "filters": filters,
                    "order_by": order_by,
                    "search": query,
                },
                DatasetSearchTestCasesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit, "offset": offset},
                    DatasetSearchTestCasesParams,
                ),
            ),
            cast_to=APIPaginatedResponse[TestCase, None],
        )

        return self._unwrap_paginated(response, include_metadata)


class AsyncDatasetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncDatasetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        project_id: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dataset:
        """Create a new empty dataset in the specified project.

        Parameters
        ----------
        name : str
            Name of the dataset to create.
        project_id : str
            Project ID to create the dataset in.
        description : Optional[str]
            Description of the dataset to create.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        Dataset
            The newly created dataset.
        """
        response = await self._post(
            "/v2/datasets",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "description": description,
                },
                DatasetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Dataset],
        )

        return self._unwrap(response)

    async def upload(
        self,
        *,
        project_id: str,
        data: FileTypes | list[dict[str, Any]] | str,
        dataset_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dataset:
        """Upload a dataset from a file or a list of dictionaries.

        Parameters
        ----------
        project_id : str
            Project ID to import the dataset into.
        data : FileTypes | list[dict[str, Any]] | str
            Data to upload. Accepts a list of dicts, a path to a `.json` /
            `.jsonl` file, or any binary file-like supported by `FileTypes`.
            Items in the legacy `messages` / `checks` / `demo_output` shape
            are translated client-side to the new `interactions` format.
        dataset_id : str | None | Omit
            Dataset ID to merge the items into. If omitted, a new dataset is
            created.
        name : str | None | Omit
            Name of the dataset. Used when creating a new dataset.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        Dataset
            The uploaded dataset.
        """
        data = await _prepare_upload_data_async(self, data, project_id=project_id)

        body = deepcopy_minimal(
            {
                "file": data,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        response = await self._post(
            "/v2/datasets/import",
            body=await async_maybe_transform(body, DatasetImportParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "project_id": project_id,
                        "dataset_id": dataset_id,
                        "name": name,
                    },
                    DatasetImportParams,
                ),
            ),
            cast_to=APIResponse[Dataset],
        )

        return self._unwrap(response)

    async def retrieve(
        self,
        dataset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dataset:
        """Retrieve a dataset by its ID.

        Parameters
        ----------
        dataset_id : str
            ID of the dataset to retrieve.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        Dataset
            The retrieved dataset.

        Raises
        ------
        ValueError
            If `dataset_id` is empty.
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        response = await self._get(
            f"/v2/datasets/{dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Dataset],
        )

        return self._unwrap(response)

    async def update(
        self,
        dataset_id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        status: Optional[TaskProgressParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dataset:
        """Update an existing dataset's metadata.

        Parameters
        ----------
        dataset_id : str
            ID of the dataset to update.
        description : Optional[str]
            Description of the dataset to update.
        name : Optional[str]
            Name of the dataset to update.
        status : Optional[TaskProgressParam]
            Status of the dataset to update.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        Dataset
            The updated dataset.

        Raises
        ------
        ValueError
            If `dataset_id` is empty.
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        response = await self._patch(
            f"/v2/datasets/{dataset_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "status": status,
                },
                DatasetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Dataset],
        )

        return self._unwrap(response)

    async def list(
        self,
        *,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[Dataset]:
        """List all datasets, optionally filtered by project.

        Parameters
        ----------
        project_id : Optional[str]
            Project ID to list datasets for.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        List[Dataset]
            A list of datasets.
        """
        response = await self._get(
            "/v2/datasets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"project_id": project_id}, DatasetListParams),
            ),
            cast_to=APIResponse[List[Dataset]],
        )

        return self._unwrap(response)

    async def delete(
        self,
        dataset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a dataset by its ID.

        Parameters
        ----------
        dataset_id : str
            ID of the dataset to delete.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If `dataset_id` is empty.
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        response = await self._delete(
            f"/v2/datasets/{dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    async def bulk_delete(
        self,
        *,
        dataset_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete multiple datasets at once.

        Parameters
        ----------
        dataset_ids : SequenceNotStr[str]
            IDs of the datasets to delete.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        None
        """
        response = await self._delete(
            "/v2/datasets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"dataset_ids": dataset_ids}, DatasetBulkDeleteParams),
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    async def generate_scenario_based(
        self,
        *,
        project_id: str,
        agent_id: str,
        scenario_id: str,
        n_examples: int | Omit = omit,
        dataset_id: Optional[str] | Omit = omit,
        dataset_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dataset:
        """Generate a dataset of test cases from scenario definitions.

        Parameters
        ----------
        project_id : str
            The ID of the project.
        agent_id : str
            The ID of the agent to use for generation.
        scenario_id : str
            The ID of the scenario to use.
        n_examples : int
            Total number of examples to generate.
        dataset_id : Optional[str]
            The ID of the dataset to use (required when dataset_name is not provided).
        dataset_name : Optional[str]
            Name for the generated dataset.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        Dataset
            The generated dataset.

        Raises
        ------
        ValueError
            If neither `dataset_id` nor `dataset_name` is provided.
        """

        if dataset_id is omit and dataset_name is omit:
            raise ValueError("'dataset_name' is required when 'dataset_id' is not provided")

        response = await self._post(
            "/v2/datasets/generate-scenario-based",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "project_id": project_id,
                    "scenario_id": scenario_id,
                    "dataset_name": dataset_name,
                    "num_examples": n_examples,
                    "dataset_id": dataset_id,
                },
                DatasetGenerateScenarioBasedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Dataset],
        )

        return self._unwrap(response)

    async def generate_document_based(
        self,
        *,
        agent_id: str,
        knowledge_base_id: str,
        project_id: str,
        dataset_name: str | Omit = omit,
        description: Optional[str] | Omit = omit,
        n_examples: int | Omit = omit,
        topic_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dataset:
        """Generate a dataset of test cases from knowledge base documents.

        Parameters
        ----------
        agent_id : str
            The ID of the agent to use for generation.
        knowledge_base_id : str
            The ID of the knowledge base to use for generation.
        project_id : str
            The ID of the project to use for generation.
        dataset_name : str
            Name for the generated dataset.
        description : Optional[str]
            Description of the generated dataset.
        n_examples : int
            Total number of examples to generate.
        topic_ids : SequenceNotStr[str]
            IDs of the topics to use for generation.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        Dataset
            The generated dataset.
        """
        response = await self._post(
            "/v2/datasets/generate-document-based",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "knowledge_base_id": knowledge_base_id,
                    "project_id": project_id,
                    "dataset_name": dataset_name,
                    "description": description,
                    "n_examples": n_examples,
                    "topic_ids": topic_ids,
                },
                DatasetGenerateDocumentBasedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Dataset],
        )

        return self._unwrap(response)

    async def list_tags(
        self,
        dataset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[str]:
        """List all tags associated with a dataset.

        Parameters
        ----------
        dataset_id : str
            The ID of the dataset to list tags for.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        List[str]
            A list of tag strings.

        Raises
        ------
        ValueError
            If `dataset_id` is empty.
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        response = await self._get(
            f"/v2/datasets/{dataset_id}/tags",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[str]],
        )

        return self._unwrap(response)

    async def list_test_cases(
        self,
        dataset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[TestCase]:
        """List all test cases belonging to a dataset.

        Fetches every page via :meth:`search_test_cases` (same as an unfiltered search).

        Parameters
        ----------
        dataset_id : str
            The ID of the dataset to list test cases for.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        List[TestCase]
            A list of test cases.

        Raises
        ------
        ValueError
            If `dataset_id` is empty.
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        page_limit = 100
        all_items: List[TestCase] = []
        offset = 0
        while True:
            page, meta = await self.search_test_cases(
                dataset_id,
                limit=page_limit,
                offset=offset,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                include_metadata=True,
            )
            all_items.extend(page)
            next_offset = meta.offset + meta.count
            if next_offset >= meta.total or not page:
                break
            offset = next_offset
        return all_items

    @overload
    async def search_test_cases(
        self,
        dataset_id: str,
        *,
        query: Optional[str] | Omit = omit,
        order_by: Optional[List[TestCaseOrderByParam]] | Omit = omit,
        filters: Optional[TestCaseFiltersParam] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: Literal[False] = False,
    ) -> List[TestCase]: ...

    @overload
    async def search_test_cases(
        self,
        dataset_id: str,
        *,
        query: Optional[str] | Omit = omit,
        order_by: Optional[List[TestCaseOrderByParam]] | Omit = omit,
        filters: Optional[TestCaseFiltersParam] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: Literal[True] = True,
    ) -> Tuple[List[TestCase], APIPaginatedMetadata]: ...

    async def search_test_cases(
        self,
        dataset_id: str,
        *,
        query: Optional[str] | Omit = omit,
        order_by: Optional[List[TestCaseOrderByParam]] | Omit = omit,
        filters: Optional[TestCaseFiltersParam] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: bool = False,
    ) -> List[TestCase] | Tuple[List[TestCase], APIPaginatedMetadata]:
        """Search test cases in a dataset using filters, sorting, and pagination.

        Parameters
        ----------
        dataset_id : str
            The ID of the dataset to search test cases in.
        query : Optional[str]
            Search query for test cases.
        order_by : Optional[List[TestCaseOrderByParam]]
            Order by criteria for test cases.
        filters : Optional[TestCaseFiltersParam]
            Search filters to apply.
        limit : int
            Maximum number of results to return.
        offset : int
            Number of results to skip.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        List[TestCase] | Tuple[List[TestCase], APIPaginatedMetadata]
            A list of matching test cases, optionally with pagination metadata.

        Raises
        ------
        ValueError
            If `dataset_id` is empty.
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        response = await self._post(
            f"/v2/datasets/{dataset_id}/test-cases/search",
            body=await async_maybe_transform(
                {
                    "filters": filters,
                    "order_by": order_by,
                    "search": query,
                },
                DatasetSearchTestCasesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit, "offset": offset},
                    DatasetSearchTestCasesParams,
                ),
            ),
            cast_to=APIPaginatedResponse[TestCase, None],
        )

        return self._unwrap_paginated(response, include_metadata)


class DatasetsResourceWithRawResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.create = to_raw_response_wrapper(
            datasets.create,
        )
        self.upload = to_raw_response_wrapper(
            datasets.upload,
        )
        self.retrieve = to_raw_response_wrapper(
            datasets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            datasets.update,
        )
        self.list = to_raw_response_wrapper(
            datasets.list,
        )
        self.delete = to_raw_response_wrapper(
            datasets.delete,
        )
        self.bulk_delete = to_raw_response_wrapper(
            datasets.bulk_delete,
        )
        self.generate_scenario_based = to_raw_response_wrapper(
            datasets.generate_scenario_based,
        )
        self.generate_document_based = to_raw_response_wrapper(
            datasets.generate_document_based,
        )
        self.list_tags = to_raw_response_wrapper(
            datasets.list_tags,
        )
        self.list_test_cases = to_raw_response_wrapper(
            datasets.list_test_cases,
        )
        self.search_test_cases = to_raw_response_wrapper(
            datasets.search_test_cases,
        )


class AsyncDatasetsResourceWithRawResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.create = async_to_raw_response_wrapper(
            datasets.create,
        )
        self.upload = async_to_raw_response_wrapper(
            datasets.upload,
        )
        self.retrieve = async_to_raw_response_wrapper(
            datasets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            datasets.update,
        )
        self.list = async_to_raw_response_wrapper(
            datasets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            datasets.delete,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            datasets.bulk_delete,
        )
        self.generate_scenario_based = async_to_raw_response_wrapper(
            datasets.generate_scenario_based,
        )
        self.generate_document_based = async_to_raw_response_wrapper(
            datasets.generate_document_based,
        )
        self.list_tags = async_to_raw_response_wrapper(
            datasets.list_tags,
        )
        self.list_test_cases = async_to_raw_response_wrapper(
            datasets.list_test_cases,
        )
        self.search_test_cases = async_to_raw_response_wrapper(
            datasets.search_test_cases,
        )


class DatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.create = to_streamed_response_wrapper(
            datasets.create,
        )
        self.upload = to_streamed_response_wrapper(
            datasets.upload,
        )
        self.retrieve = to_streamed_response_wrapper(
            datasets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            datasets.update,
        )
        self.list = to_streamed_response_wrapper(
            datasets.list,
        )
        self.delete = to_streamed_response_wrapper(
            datasets.delete,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            datasets.bulk_delete,
        )
        self.generate_scenario_based = to_streamed_response_wrapper(
            datasets.generate_scenario_based,
        )
        self.generate_document_based = to_streamed_response_wrapper(
            datasets.generate_document_based,
        )
        self.list_tags = to_streamed_response_wrapper(
            datasets.list_tags,
        )
        self.list_test_cases = to_streamed_response_wrapper(
            datasets.list_test_cases,
        )
        self.search_test_cases = to_streamed_response_wrapper(
            datasets.search_test_cases,
        )


class AsyncDatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.create = async_to_streamed_response_wrapper(
            datasets.create,
        )
        self.upload = async_to_streamed_response_wrapper(
            datasets.upload,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            datasets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            datasets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            datasets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            datasets.delete,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            datasets.bulk_delete,
        )
        self.generate_scenario_based = async_to_streamed_response_wrapper(
            datasets.generate_scenario_based,
        )
        self.generate_document_based = async_to_streamed_response_wrapper(
            datasets.generate_document_based,
        )
        self.list_tags = async_to_streamed_response_wrapper(
            datasets.list_tags,
        )
        self.list_test_cases = async_to_streamed_response_wrapper(
            datasets.list_test_cases,
        )
        self.search_test_cases = async_to_streamed_response_wrapper(
            datasets.search_test_cases,
        )
