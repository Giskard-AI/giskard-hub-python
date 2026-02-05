from __future__ import annotations

from typing import Any, Dict, List, Optional

import httpx

from ..types import (
    AuditAPIResource,
    APIPaginatedResponse,
    AuditDisplayAPIResponse,
    audit_search_params,
    audit_list_entity_params,
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

__all__ = ["AuditResource", "AsyncAuditResource"]


class AuditResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuditResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AuditResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuditResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AuditResourceWithStreamingResponse(self)

    def search(
        self,
        *,
        search: Optional[str] | Omit = omit,
        order_by: SequenceNotStr[Dict[str, Any]] | Omit = omit,
        filters: Dict[str, Dict[str, Any]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIPaginatedResponse[List[AuditAPIResource], None]:
        """
        Search Audit Logs By Filters

        Args:
          search: Search query for audit logs

          order_by: Order by criteria for audit logs

          filters: Filter criteria for audit logs

          limit: Maximum number of results to return

          offset: Number of results to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/audit/search",
            body=maybe_transform(
                {
                    "filters": filters,
                    "order_by": order_by,
                    "search": search,
                },
                audit_search_params.AuditSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    audit_search_params.AuditSearchParams,
                ),
            ),
            cast_to=APIPaginatedResponse[List[AuditAPIResource], None],
        )

    def list_entities(
        self,
        entity_id: str,
        entity_type: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIPaginatedResponse[List[AuditDisplayAPIResponse], None]:
        """
        List Entity Audit Display Logs

        Args:
          entity_id: The UUID of the entity

          entity_type: The type of the entity

          limit: Maximum number of results to return

          offset: Number of results to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_type:
            raise ValueError(f"Expected a non-empty value for `entity_type` but received {entity_type!r}")
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._get(
            f"/v2/audit/{entity_type}/{entity_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    audit_list_entity_params.AuditListEntityParams,
                ),
            ),
            cast_to=APIPaginatedResponse[List[AuditDisplayAPIResponse], None],
        )


class AsyncAuditResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuditResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuditResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuditResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncAuditResourceWithStreamingResponse(self)

    async def search(
        self,
        *,
        search: Optional[str] | Omit = omit,
        order_by: SequenceNotStr[Dict[str, Any]] | Omit = omit,
        filters: Dict[str, Dict[str, Any]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIPaginatedResponse[List[AuditAPIResource], None]:
        """
        Search Audit Logs By Filters

        Args:
          search: Search query for audit logs

          order_by: Order by criteria for audit logs

          filters: Filter criteria for audit logs

          limit: Maximum number of results to return

          offset: Number of results to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/audit/search",
            body=await async_maybe_transform(
                {
                    "filters": filters,
                    "order_by": order_by,
                    "search": search,
                },
                audit_search_params.AuditSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    audit_search_params.AuditSearchParams,
                ),
            ),
            cast_to=APIPaginatedResponse[List[AuditAPIResource], None],
        )

    async def list_entities(
        self,
        entity_id: str,
        entity_type: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIPaginatedResponse[List[AuditDisplayAPIResponse], None]:
        """
        List Entity Audit Display Logs

        Args:
          entity_id: The UUID of the entity

          entity_type: The type of the entity

          limit: Maximum number of results to return

          offset: Number of results to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_type:
            raise ValueError(f"Expected a non-empty value for `entity_type` but received {entity_type!r}")
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._get(
            f"/v2/audit/{entity_type}/{entity_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    audit_list_entity_params.AuditListEntityParams,
                ),
            ),
            cast_to=APIPaginatedResponse[List[AuditDisplayAPIResponse], None],
        )


class AuditResourceWithRawResponse:
    def __init__(self, audit: AuditResource) -> None:
        self._audit = audit

        self.search = to_raw_response_wrapper(
            audit.search,
        )
        self.list_entities = to_raw_response_wrapper(
            audit.list_entities,
        )


class AsyncAuditResourceWithRawResponse:
    def __init__(self, audit: AsyncAuditResource) -> None:
        self._audit = audit

        self.search = async_to_raw_response_wrapper(
            audit.search,
        )
        self.list_entities = async_to_raw_response_wrapper(
            audit.list_entities,
        )


class AuditResourceWithStreamingResponse:
    def __init__(self, audit: AuditResource) -> None:
        self._audit = audit

        self.search = to_streamed_response_wrapper(
            audit.search,
        )
        self.list_entities = to_streamed_response_wrapper(
            audit.list_entities,
        )


class AsyncAuditResourceWithStreamingResponse:
    def __init__(self, audit: AsyncAuditResource) -> None:
        self._audit = audit

        self.search = async_to_streamed_response_wrapper(
            audit.search,
        )
        self.list_entities = async_to_streamed_response_wrapper(
            audit.list_entities,
        )
