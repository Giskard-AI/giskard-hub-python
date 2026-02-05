from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    dataset_list_params,
    dataset_create_params,
    dataset_update_params,
    dataset_export_params,
    dataset_bulk_delete_params,
    dataset_export_selected_params,
    dataset_generate_document_based_params,
    dataset_generate_scenario_based_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.api_response_none import APIResponseNone
from ..types.task_progress_param import TaskProgressParam
from ..types.api_response_dataset import APIResponseDataset
from ..types.dataset_list_response import DatasetListResponse
from ..types.dataset_list_tags_response import DatasetListTagsResponse
from ..types.api_response_list_test_case import APIResponseListTestCase
from ..types.export_chat_test_cases_request import ExportChatTestCasesRequest

__all__ = ["DatasetsResource", "AsyncDatasetsResource"]


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
    ) -> APIResponseDataset:
        """
        Create Dataset

        Args:
          name: Name of the dataset to create

          project_id: Project ID to create the dataset in

          description: Description of the dataset to create

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/datasets",
            body=maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "description": description,
                },
                dataset_create_params.DatasetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseDataset,
        )

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
    ) -> APIResponseDataset:
        """
        Retrieve Dataset

        Args:
          dataset_id: ID of the dataset to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._get(
            f"/v2/datasets/{dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseDataset,
        )

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
    ) -> APIResponseDataset:
        """
        Update Dataset

        Args:
          dataset_id: ID of the dataset to update

          description: Description of the dataset to update

          name: Name of the dataset to update

          status: Status of the dataset to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._patch(
            f"/v2/datasets/{dataset_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "status": status,
                },
                dataset_update_params.DatasetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseDataset,
        )

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
    ) -> DatasetListResponse:
        """
        List Datasets

        Args:
          project_id: Project ID to list datasets for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/datasets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, dataset_list_params.DatasetListParams),
            ),
            cast_to=DatasetListResponse,
        )

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
    ) -> APIResponseNone:
        """
        Delete Dataset

        Args:
          dataset_id: ID of the dataset to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._delete(
            f"/v2/datasets/{dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseNone,
        )

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
    ) -> APIResponseNone:
        """
        Bulk Delete Datasets

        Args:
          dataset_ids: IDs of the datasets to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v2/datasets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dataset_ids": dataset_ids}, dataset_bulk_delete_params.DatasetBulkDeleteParams),
            ),
            cast_to=APIResponseNone,
        )

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
    ) -> APIResponseDataset:
        """
        Generate Scenario Based Dataset

        Args:
          project_id: The ID of the project

          agent_id: The ID of the agent to use for generation

          scenario_id: The ID of the scenario to use

          n_examples: Total number of examples to generate

          dataset_id: The ID of the dataset to use (required when dataset_name is not provided)

          dataset_name: Name for the generated dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """

        if dataset_id is omit and dataset_name is omit:
            raise ValueError("'dataset_name' is required when 'dataset_id' is not provided")

        return self._post(
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
                dataset_generate_scenario_based_params.DatasetGenerateScenarioBasedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseDataset,
        )

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
    ) -> APIResponseDataset:
        """
        Generate Document Based Dataset

        Args:
          agent_id: The ID of the agent to use for generation

          knowledge_base_id: The ID of the knowledge base to use for generation

          project_id: The ID of the project to use for generation

          dataset_name: Name for the generated dataset

          description: Description of the generated dataset

          n_examples: Total number of examples to generate

          topic_ids: IDs of the topics to use for generation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
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
                dataset_generate_document_based_params.DatasetGenerateDocumentBasedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseDataset,
        )

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
    ) -> DatasetListTagsResponse:
        """
        List Dataset Tags

        Args:
          dataset_id: The ID of the dataset to list tags for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._get(
            f"/v2/datasets/{dataset_id}/tags",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetListTagsResponse,
        )

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
    ) -> APIResponseListTestCase:
        """
        List Dataset Test Cases

        Args:
          dataset_id: The ID of the dataset to list test cases for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._get(
            f"/v2/datasets/{dataset_id}/test-cases",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseListTestCase,
        )

    def export(
        self,
        dataset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Export Dataset Chat Test Cases

        Args:
          dataset_id: The ID of the dataset to export

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._get(
            f"/v2/datasets/{dataset_id}/export",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def export_selected(
        self,
        dataset_id: str,
        *,
        test_case_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Export Selected Dataset Chat Test Cases

        Args:
          dataset_id: The ID of the dataset to export

          test_case_ids: IDs of the test cases to export

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._post(
            f"/v2/datasets/{dataset_id}/export",
            body=maybe_transform(
                {"test_case_ids": test_case_ids}, dataset_export_selected_params.DatasetExportSelectedParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


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
    ) -> APIResponseDataset:
        """
        Create Dataset

        Args:
          name: Name of the dataset to create

          project_id: Project ID to create the dataset in

          description: Description of the dataset to create

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/datasets",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "description": description,
                },
                dataset_create_params.DatasetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseDataset,
        )

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
    ) -> APIResponseDataset:
        """
        Retrieve Dataset

        Args:
          dataset_id: ID of the dataset to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._get(
            f"/v2/datasets/{dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseDataset,
        )

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
    ) -> APIResponseDataset:
        """
        Update Dataset

        Args:
          dataset_id: ID of the dataset to update

          description: Description of the dataset to update

          name: Name of the dataset to update

          status: Status of the dataset to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._patch(
            f"/v2/datasets/{dataset_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "status": status,
                },
                dataset_update_params.DatasetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseDataset,
        )

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
    ) -> DatasetListResponse:
        """
        List Datasets

        Args:
          project_id: Project ID to list datasets for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/datasets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"project_id": project_id}, dataset_list_params.DatasetListParams),
            ),
            cast_to=DatasetListResponse,
        )

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
    ) -> APIResponseNone:
        """
        Delete Dataset

        Args:
          dataset_id: ID of the dataset to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._delete(
            f"/v2/datasets/{dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseNone,
        )

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
    ) -> APIResponseNone:
        """
        Bulk Delete Datasets

        Args:
          dataset_ids: IDs of the datasets to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v2/datasets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"dataset_ids": dataset_ids}, dataset_bulk_delete_params.DatasetBulkDeleteParams
                ),
            ),
            cast_to=APIResponseNone,
        )

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
    ) -> APIResponseDataset:
        """
        Generate Scenario Based Dataset

        Args:
          project_id: The ID of the project

          agent_id: The ID of the agent to use for generation

          scenario_id: The ID of the scenario to use

          n_examples: Total number of examples to generate

          dataset_id: The ID of the dataset to use

          dataset_name: Name for the generated dataset (required when dataset_id is not provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """

        if dataset_id is omit and dataset_name is omit:
            raise ValueError("'dataset_name' is required when 'dataset_id' is not provided")

        return await self._post(
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
                dataset_generate_scenario_based_params.DatasetGenerateScenarioBasedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseDataset,
        )

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
    ) -> APIResponseDataset:
        """
        Generate Document Based Dataset

        Args:
          agent_id: The ID of the agent to use for generation

          knowledge_base_id: The ID of the knowledge base to use for generation

          project_id: The ID of the project to use for generation

          dataset_name: Name for the generated dataset

          description: Description of the generated dataset

          n_examples: Total number of examples to generate

          topic_ids: IDs of the topics to use for generation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
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
                dataset_generate_document_based_params.DatasetGenerateDocumentBasedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseDataset,
        )

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
    ) -> DatasetListTagsResponse:
        """
        List Dataset Tags

        Args:
          dataset_id: The ID of the dataset to list test cases for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._get(
            f"/v2/datasets/{dataset_id}/tags",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetListTagsResponse,
        )

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
    ) -> APIResponseListTestCase:
        """
        List Dataset Test Cases

        Args:
          dataset_id: The ID of the dataset to list test cases for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._get(
            f"/v2/datasets/{dataset_id}/test-cases",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseListTestCase,
        )

    async def export(
        self,
        dataset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Export Dataset Chat Test Cases

        Args:
          dataset_id: The ID of the dataset to export

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._get(
            f"/v2/datasets/{dataset_id}/export",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def export_selected(
        self,
        dataset_id: str,
        *,
        test_case_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Export Selected Dataset Chat Test Cases

        Args:
          dataset_id: The ID of the dataset to export

          test_case_ids: IDs of the test cases to export

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._post(
            f"/v2/datasets/{dataset_id}/export",
            body=await async_maybe_transform(
                {"test_case_ids": test_case_ids}, dataset_export_selected_params.DatasetExportSelectedParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class DatasetsResourceWithRawResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.create = to_raw_response_wrapper(
            datasets.create,
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
        self.export = to_raw_response_wrapper(
            datasets.export,
        )
        self.export_selected = to_raw_response_wrapper(
            datasets.export_selected,
        )


class AsyncDatasetsResourceWithRawResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.create = async_to_raw_response_wrapper(
            datasets.create,
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
        self.export = async_to_raw_response_wrapper(
            datasets.export,
        )
        self.export_selected = async_to_raw_response_wrapper(
            datasets.export_selected,
        )


class DatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.create = to_streamed_response_wrapper(
            datasets.create,
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
        self.export = to_streamed_response_wrapper(
            datasets.export,
        )
        self.export_selected = to_streamed_response_wrapper(
            datasets.export_selected,
        )


class AsyncDatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.create = async_to_streamed_response_wrapper(
            datasets.create,
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
        self.export = async_to_streamed_response_wrapper(
            datasets.export,
        )
        self.export_selected = async_to_streamed_response_wrapper(
            datasets.export_selected,
        )
