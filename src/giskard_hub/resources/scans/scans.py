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
    Scan,
    Agent,
    ScanProbe,
    ScanCategory,
    KnowledgeBase,
    ScanAvailableProbe,
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
from .._included import embed_included_list, embed_included_single
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._analytics import capture_event, make_distinct_id
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
        probe_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Scan:
        """Launch a new vulnerability scan of an agent.

        Parameters
        ----------
        project_id : str
            Project ID to use for the scan.
        agent_id : str
            Agent ID to use for the scan.
        knowledge_base_id : str or None
            Knowledge Base ID to use for the scan.
        probe_ids : list of str or None
            List of specific probe IDs to run in the scan.
        tags : list of str or None
            List of category tags to apply to the scan; use ``list_categories``
            to get the available categories.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        Scan
            The newly created scan object.
        """
        response = self._post(
            "/v2/scans",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "project_id": project_id,
                    "knowledge_base_id": knowledge_base_id,
                    "probe_ids": probe_ids,
                    "tags": tags,
                },
                ScanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Scan],
        )

        result = self._unwrap(response)
        capture_event(
            make_distinct_id(self._client.api_key),
            "scan_created",
            {"scan_id": result.id, "has_knowledge_base": knowledge_base_id is not omit and knowledge_base_id is not None},
        )
        return result

    def retrieve(
        self,
        scan_id: str,
        *,
        include: Optional[List[Literal["agent", "knowledge_base"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Scan:
        """Retrieve a scan result by its ID, with optional related resource inclusion.

        Parameters
        ----------
        scan_id : str
            Scan Result ID.
        include : list of {'agent', 'knowledge_base'} or None
            Related resources to include in response.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        Scan
            The requested scan object.

        Raises
        ------
        ValueError
            If ``scan_id`` is empty.
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        response = self._get(
            f"/v2/scans/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include": include}, ScanRetrieveParams),
            ),
            cast_to=APIResponseWithIncluded[Scan, APIResponse[Agent | KnowledgeBase]],
        )

        if include is not omit and include:
            response = embed_included_single(response, id_getter=lambda scan_result: scan_result.id)

        return self._unwrap(response)

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
    ) -> List[Scan]:
        """List all scan results, optionally filtered by project.

        Parameters
        ----------
        project_id : str or None
            Project ID to use for the scan.
        include : list of {'agent', 'knowledge_base'} or None
            Related resources to include in response.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        list of Scan
            A list of scan objects.
        """
        response = self._get(
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
            cast_to=APIResponseWithIncluded[List[Scan], APIResponse[Agent | KnowledgeBase]],
        )

        if include is not omit and include:
            response = embed_included_list(response, id_getter=lambda scan_result: scan_result.id)

        return self._unwrap(response)

    def delete(
        self,
        scan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a scan result by its ID.

        Parameters
        ----------
        scan_id : str
            Scan Result ID to delete.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If ``scan_id`` is empty.
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        response = self._delete(
            f"/v2/scans/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

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
    ) -> None:
        """Delete multiple scan results at once.

        Parameters
        ----------
        scan_ids : list of str
            List of scan IDs to delete.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        None
        """
        response = self._delete(
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

        return self._unwrap(response)

    def list_categories(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[ScanCategory]:
        """List all available scan vulnerability categories.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        list of ScanCategory
            A list of scan vulnerability categories.
        """
        response = self._get(
            "/v2/scan-categories",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[ScanCategory]],
        )

        return self._unwrap(response)

    def list_probes(
        self,
        scan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[ScanProbe]:
        """List all probes for a given scan result.

        Parameters
        ----------
        scan_id : str
            Scan Result ID to list probes.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        list of ScanProbe
            A list of scan probes for the given scan.

        Raises
        ------
        ValueError
            If ``scan_id`` is empty.
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        response = self._get(
            f"/v2/scans/{scan_id}/probes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[ScanProbe]],
        )

        return self._unwrap(response)

    def list_available_probes(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[ScanAvailableProbe]:
        """List all available probes that can be used for scanning.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        list of ScanAvailableProbe
            A list of available scan probes.
        """
        response = self._get(
            "/v2/scan-available-probes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[ScanAvailableProbe]],
        )

        return self._unwrap(response)


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
        probe_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Scan:
        """Launch a new vulnerability scan of an agent.

        Parameters
        ----------
        project_id : str
            Project ID to use for the scan.
        agent_id : str
            Agent ID to use for the scan.
        knowledge_base_id : str or None
            Knowledge Base ID to use for the scan.
        probe_ids : list of str or None
            List of specific probe IDs to run in the scan.
        tags : list of str or None
            List of category tags to apply to the scan; use ``list_categories``
            to get the available categories.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        Scan
            The newly created scan object.
        """
        response = await self._post(
            "/v2/scans",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "project_id": project_id,
                    "knowledge_base_id": knowledge_base_id,
                    "probe_ids": probe_ids,
                    "tags": tags,
                },
                ScanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Scan],
        )

        result = self._unwrap(response)
        capture_event(
            make_distinct_id(self._client.api_key),
            "scan_created",
            {"scan_id": result.id, "has_knowledge_base": knowledge_base_id is not omit and knowledge_base_id is not None},
        )
        return result

    async def retrieve(
        self,
        scan_id: str,
        *,
        include: Optional[List[Literal["agent", "knowledge_base"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Scan:
        """Retrieve a scan result by its ID, with optional related resource inclusion.

        Parameters
        ----------
        scan_id : str
            Scan Result ID to retrieve.
        include : list of {'agent', 'knowledge_base'} or None
            Related resources to include in response.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        Scan
            The requested scan object.

        Raises
        ------
        ValueError
            If ``scan_id`` is empty.
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")

        response = await self._get(
            f"/v2/scans/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"include": include}, ScanRetrieveParams),
            ),
            cast_to=APIResponseWithIncluded[Scan, APIResponse[Agent | KnowledgeBase]],
        )

        if include is not omit and include:
            response = embed_included_single(response, id_getter=lambda scan_result: scan_result.id)

        return self._unwrap(response)

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
    ) -> List[Scan]:
        """List all scan results, optionally filtered by project.

        Parameters
        ----------
        project_id : str or None
            Project ID to use for the scan.
        include : list of {'agent', 'knowledge_base'} or None
            Related resources to include in response.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        list of Scan
            A list of scan objects.
        """
        response = await self._get(
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
            cast_to=APIResponseWithIncluded[List[Scan], APIResponse[Agent | KnowledgeBase]],
        )

        if include is not omit and include:
            response = embed_included_list(response, id_getter=lambda scan_result: scan_result.id)

        return self._unwrap(response)

    async def delete(
        self,
        scan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a scan result by its ID.

        Parameters
        ----------
        scan_id : str
            Scan Result ID to delete.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If ``scan_id`` is empty.
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        response = await self._delete(
            f"/v2/scans/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

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
    ) -> None:
        """Delete multiple scan results at once.

        Parameters
        ----------
        scan_ids : list of str
            List of scan IDs to delete.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        None
        """
        response = await self._delete(
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

        return self._unwrap(response)

    async def list_categories(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[ScanCategory]:
        """List all available scan vulnerability categories.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        list of ScanCategory
            A list of scan vulnerability categories.
        """
        response = await self._get(
            "/v2/scan-categories",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[ScanCategory]],
        )

        return self._unwrap(response)

    async def list_probes(
        self,
        scan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[ScanProbe]:
        """List all probes for a given scan result.

        Parameters
        ----------
        scan_id : str
            Scan Result ID to list probes.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        list of ScanProbe
            A list of scan probes for the given scan.

        Raises
        ------
        ValueError
            If ``scan_id`` is empty.
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        response = await self._get(
            f"/v2/scans/{scan_id}/probes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[ScanProbe]],
        )

        return self._unwrap(response)

    async def list_available_probes(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[ScanAvailableProbe]:
        """List all available probes that can be used for scanning.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        list of ScanAvailableProbe
            A list of available scan probes.
        """
        response = await self._get(
            "/v2/scan-available-probes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[ScanAvailableProbe]],
        )

        return self._unwrap(response)


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
        self.list_available_probes = to_raw_response_wrapper(
            scans.list_available_probes,
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
        self.list_available_probes = async_to_raw_response_wrapper(
            scans.list_available_probes,
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
        self.list_available_probes = to_streamed_response_wrapper(
            scans.list_available_probes,
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
        self.list_available_probes = async_to_streamed_response_wrapper(
            scans.list_available_probes,
        )

    @cached_property
    def probes(self) -> AsyncProbesResourceWithStreamingResponse:
        return AsyncProbesResourceWithStreamingResponse(self._scans.probes)

    @cached_property
    def attempts(self) -> AsyncAttemptsResourceWithStreamingResponse:
        return AsyncAttemptsResourceWithStreamingResponse(self._scans.attempts)
