from __future__ import annotations

from typing import List, Literal, Optional

import httpx

from .probes import (
    ProbesResource,
    AsyncProbesResource,
    ProbesResourceWithRawResponse,
    AsyncProbesResourceWithRawResponse,
    ProbesResourceWithStreamingResponse,
    AsyncProbesResourceWithStreamingResponse,
)
from ...types import (
    Agent,
    ScanResult,
    ScanCategory,
    KnowledgeBase,
    ScanProbeResult,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .attempts import (
    AttemptsResource,
    AsyncAttemptsResource,
    AttemptsResourceWithRawResponse,
    AsyncAttemptsResourceWithRawResponse,
    AttemptsResourceWithStreamingResponse,
    AsyncAttemptsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.scan import (
    ScanListParams,
    ScanCreateParams,
    ScanRetrieveParams,
    ScanBulkDeleteParams,
)
from ..._base_client import make_request_options
from ...types.common import APIResponse, APIResponseWithIncluded

__all__ = ["ScansResource", "AsyncScansResource"]


class ScansResource(SyncAPIResource):
    @cached_property
    def probes(self) -> ProbesResource:
        return ProbesResource(self._client)

    @cached_property
    def attempts(self) -> AttemptsResource:
        return AttemptsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ScansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return ScansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return ScansResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: str,
        agent_id: str,
        knowledge_base_id: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[ScanResult]:
        """
        Create Scan

        Args:
          project_id: Project ID to use for the scan

          agent_id: Agent ID to use for the scan

          knowledge_base_id: Knowledge Base ID to use for the scan

          tags: List of category tags to apply to the scan; use `list_categories` to get the available categories.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/scans",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "project_id": project_id,
                    "knowledge_base_id": knowledge_base_id,
                    "tags": tags,
                },
                ScanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[ScanResult],
        )

    def retrieve(
        self,
        scan_result_id: str,
        *,
        include: Optional[List[Literal["agent", "knowledge_base"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseWithIncluded[ScanResult, APIResponse[Agent | KnowledgeBase]]:
        """
        Retrieve Scan

        Args:
          scan_result_id: Scan Result ID

          include: Related resources to include in response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_result_id:
            raise ValueError(f"Expected a non-empty value for `scan_result_id` but received {scan_result_id!r}")
        return self._get(
            f"/v2/scans/{scan_result_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include": include}, ScanRetrieveParams),
            ),
            cast_to=APIResponseWithIncluded[ScanResult, APIResponse[Agent | KnowledgeBase]],
        )

    def list(
        self,
        *,
        project_id: Optional[str] | Omit = omit,
        include: Optional[List[Literal["agent", "knowledge_base"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseWithIncluded[List[ScanResult], APIResponse[Agent | KnowledgeBase]]:
        """
        List Scans

        Args:
          project_id: Project ID to use for the scan

          include: Related resources to include in response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/scans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include": include,
                        "project_id": project_id,
                    },
                    ScanListParams,
                ),
            ),
            cast_to=APIResponseWithIncluded[List[ScanResult], APIResponse[Agent | KnowledgeBase]],
        )

    def delete(
        self,
        scan_result_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[None]:
        """
        Delete Scan

        Args:
          scan_result_id: Scan Result ID to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_result_id:
            raise ValueError(f"Expected a non-empty value for `scan_result_id` but received {scan_result_id!r}")
        return self._delete(
            f"/v2/scans/{scan_result_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

    def bulk_delete(
        self,
        *,
        scan_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[None]:
        """
        Bulk Delete Scans

        Args:
          scan_ids: List of scan IDs to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v2/scans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"scan_ids": scan_ids}, ScanBulkDeleteParams),
            ),
            cast_to=APIResponse[None],
        )

    def list_categories(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[List[ScanCategory]]:
        """
        List Scan Categories

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/scan-categories",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[ScanCategory]],
        )

    def list_probes(
        self,
        scan_result_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[List[ScanProbeResult]]:
        """
        List Scan Probes

        Args:
          scan_result_id: Scan Result ID to list probes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_result_id:
            raise ValueError(f"Expected a non-empty value for `scan_result_id` but received {scan_result_id!r}")
        return self._get(
            f"/v2/scans/{scan_result_id}/probes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[ScanProbeResult]],
        )


class AsyncScansResource(AsyncAPIResource):
    @cached_property
    def probes(self) -> AsyncProbesResource:
        return AsyncProbesResource(self._client)

    @cached_property
    def attempts(self) -> AsyncAttemptsResource:
        return AsyncAttemptsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncScansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncScansResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: str,
        agent_id: str,
        knowledge_base_id: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[ScanResult]:
        """
        Create Scan

        Args:
          project_id: Project ID to use for the scan

          agent_id: Agent ID to use for the scan

          knowledge_base_id: Knowledge Base ID to use for the scan

          tags: List of category tags to apply to the scan; use `list_categories` to get the available categories.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/scans",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "project_id": project_id,
                    "knowledge_base_id": knowledge_base_id,
                    "tags": tags,
                },
                ScanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[ScanResult],
        )

    async def retrieve(
        self,
        scan_result_id: str,
        *,
        include: Optional[List[Literal["agent", "knowledge_base"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseWithIncluded[ScanResult, APIResponse[Agent | KnowledgeBase]]:
        """
        Retrieve Scan

        Args:
          scan_result_id: Scan Result ID to retrieve

          include: Related resources to include in response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_result_id:
            raise ValueError(f"Expected a non-empty value for `scan_result_id` but received {scan_result_id!r}")
        return await self._get(
            f"/v2/scans/{scan_result_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"include": include}, ScanRetrieveParams),
            ),
            cast_to=APIResponseWithIncluded[ScanResult, APIResponse[Agent | KnowledgeBase]],
        )

    async def list(
        self,
        *,
        project_id: Optional[str] | Omit = omit,
        include: Optional[List[Literal["agent", "knowledge_base"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseWithIncluded[List[ScanResult], APIResponse[Agent | KnowledgeBase]]:
        """
        List Scans

        Args:
          project_id: Project ID to use for the scan

          include: Related resources to include in response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/scans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include": include,
                        "project_id": project_id,
                    },
                    ScanListParams,
                ),
            ),
            cast_to=APIResponseWithIncluded[List[ScanResult], APIResponse[Agent | KnowledgeBase]],
        )

    async def delete(
        self,
        scan_result_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[None]:
        """
        Delete Scan

        Args:
          scan_result_id: Scan Result ID to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_result_id:
            raise ValueError(f"Expected a non-empty value for `scan_result_id` but received {scan_result_id!r}")
        return await self._delete(
            f"/v2/scans/{scan_result_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

    async def bulk_delete(
        self,
        *,
        scan_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[None]:
        """
        Bulk Delete Scans

        Args:
          scan_result_id: Scan Result ID to list categories

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v2/scans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"scan_ids": scan_ids}, ScanBulkDeleteParams),
            ),
            cast_to=APIResponse[None],
        )

    async def list_categories(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[List[ScanCategory]]:
        """
        List Scan Categories

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/scan-categories",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[ScanCategory]],
        )

    async def list_probes(
        self,
        scan_result_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[List[ScanProbeResult]]:
        """
        List Scan Probes

        Args:
          scan_result_id: Scan Result ID to list probes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_result_id:
            raise ValueError(f"Expected a non-empty value for `scan_result_id` but received {scan_result_id!r}")
        return await self._get(
            f"/v2/scans/{scan_result_id}/probes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[ScanProbeResult]],
        )


class ScansResourceWithRawResponse:
    def __init__(self, scans: ScansResource) -> None:
        self._scans = scans

        self.create = to_raw_response_wrapper(
            scans.create,
        )
        self.retrieve = to_raw_response_wrapper(
            scans.retrieve,
        )
        self.list = to_raw_response_wrapper(
            scans.list,
        )
        self.delete = to_raw_response_wrapper(
            scans.delete,
        )
        self.bulk_delete = to_raw_response_wrapper(
            scans.bulk_delete,
        )
        self.list_categories = to_raw_response_wrapper(
            scans.list_categories,
        )
        self.list_probes = to_raw_response_wrapper(
            scans.list_probes,
        )

    @cached_property
    def probes(self) -> ProbesResourceWithRawResponse:
        return ProbesResourceWithRawResponse(self._scans.probes)

    @cached_property
    def attempts(self) -> AttemptsResourceWithRawResponse:
        return AttemptsResourceWithRawResponse(self._scans.attempts)


class AsyncScansResourceWithRawResponse:
    def __init__(self, scans: AsyncScansResource) -> None:
        self._scans = scans

        self.create = async_to_raw_response_wrapper(
            scans.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            scans.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            scans.list,
        )
        self.delete = async_to_raw_response_wrapper(
            scans.delete,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            scans.bulk_delete,
        )
        self.list_categories = async_to_raw_response_wrapper(
            scans.list_categories,
        )
        self.list_probes = async_to_raw_response_wrapper(
            scans.list_probes,
        )

    @cached_property
    def probes(self) -> AsyncProbesResourceWithRawResponse:
        return AsyncProbesResourceWithRawResponse(self._scans.probes)

    @cached_property
    def attempts(self) -> AsyncAttemptsResourceWithRawResponse:
        return AsyncAttemptsResourceWithRawResponse(self._scans.attempts)


class ScansResourceWithStreamingResponse:
    def __init__(self, scans: ScansResource) -> None:
        self._scans = scans

        self.create = to_streamed_response_wrapper(
            scans.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            scans.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            scans.list,
        )
        self.delete = to_streamed_response_wrapper(
            scans.delete,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            scans.bulk_delete,
        )
        self.list_categories = to_streamed_response_wrapper(
            scans.list_categories,
        )
        self.list_probes = to_streamed_response_wrapper(
            scans.list_probes,
        )

    @cached_property
    def probes(self) -> ProbesResourceWithStreamingResponse:
        return ProbesResourceWithStreamingResponse(self._scans.probes)

    @cached_property
    def attempts(self) -> AttemptsResourceWithStreamingResponse:
        return AttemptsResourceWithStreamingResponse(self._scans.attempts)


class AsyncScansResourceWithStreamingResponse:
    def __init__(self, scans: AsyncScansResource) -> None:
        self._scans = scans

        self.create = async_to_streamed_response_wrapper(
            scans.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            scans.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            scans.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            scans.delete,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            scans.bulk_delete,
        )
        self.list_categories = async_to_streamed_response_wrapper(
            scans.list_categories,
        )
        self.list_probes = async_to_streamed_response_wrapper(
            scans.list_probes,
        )

    @cached_property
    def probes(self) -> AsyncProbesResourceWithStreamingResponse:
        return AsyncProbesResourceWithStreamingResponse(self._scans.probes)

    @cached_property
    def attempts(self) -> AsyncAttemptsResourceWithStreamingResponse:
        return AsyncAttemptsResourceWithStreamingResponse(self._scans.attempts)
