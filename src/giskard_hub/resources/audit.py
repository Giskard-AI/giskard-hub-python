from __future__ import annotations

from typing import List, Tuple, Literal, Optional, overload

import httpx

from ..types import (
    Audit,
    AuditDisplay,
    AuditFiltersParam,
    AuditOrderByParam,
    AuditSearchParams,
    APIPaginatedResponse,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.audit import AuditListEntityParams
from .._base_client import make_request_options
from ..types.common import APIPaginatedMetadata

__all__ = ["AuditLogsResource", "AsyncAuditLogsResource"]


class AuditLogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuditLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AuditLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuditLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AuditLogsResourceWithStreamingResponse(self)

    @overload
    def search(
        self,
        *,
        query: Optional[str] | Omit = omit,
        order_by: List[AuditOrderByParam] | Omit = omit,
        filters: AuditFiltersParam | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: bool = False,
    ) -> List[Audit]: ...

    @overload
    def search(
        self,
        *,
        query: Optional[str] | Omit = omit,
        order_by: List[AuditOrderByParam] | Omit = omit,
        filters: AuditFiltersParam | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: Literal[True],
    ) -> Tuple[List[Audit], APIPaginatedMetadata]: ...

    def search(
        self,
        *,
        query: Optional[str] | Omit = omit,
        order_by: List[AuditOrderByParam] | Omit = omit,
        filters: AuditFiltersParam | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: bool = False,
    ) -> List[Audit] | Tuple[List[Audit], APIPaginatedMetadata]:
        """Search audit logs using filters, sorting, and pagination.

        Parameters
        ----------
        query : str | None | Omit
            Free-text search query for audit logs.
        order_by : list[AuditOrderByParam] | Omit
            Sorting criteria for audit logs.
        filters : AuditFiltersParam | Omit
            Filter criteria for audit logs.
        limit : int | Omit
            Maximum number of results to return.
        offset : int | Omit
            Number of results to skip for pagination.
        include_metadata : bool
            If ``True``, return a tuple of ``(data, metadata)`` with pagination info.

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
        list[Audit] | tuple[list[Audit], APIPaginatedMetadata]
            Audit logs, optionally with pagination metadata.
        """
        response = self._post(
            "/v2/audit/search",
            body=maybe_transform(
                {
                    "filters": filters,
                    "order_by": order_by,
                    "search": query,
                },
                AuditSearchParams,
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
                    AuditSearchParams,
                ),
            ),
            cast_to=APIPaginatedResponse[Audit, None],
        )

        return self._unwrap_paginated(response, include_metadata)

    @overload
    def list_entities(
        self,
        entity_id: str,
        entity_type: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: bool = False,
    ) -> List[AuditDisplay]: ...

    @overload
    def list_entities(
        self,
        entity_id: str,
        entity_type: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: Literal[True],
    ) -> Tuple[List[AuditDisplay], APIPaginatedMetadata]: ...

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
        include_metadata: bool = False,
    ) -> List[AuditDisplay] | Tuple[List[AuditDisplay], APIPaginatedMetadata]:
        """List audit display logs for a specific entity.

        Parameters
        ----------
        entity_id : str
            UUID of the entity to list audit logs for.
        entity_type : str
            Type of the entity (e.g. ``"project"``, ``"agent"``).
        limit : int | Omit
            Maximum number of results to return.
        offset : int | Omit
            Number of results to skip for pagination.
        include_metadata : bool
            If ``True``, return a tuple of ``(data, metadata)`` with pagination info.

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
        list[AuditDisplay] | tuple[list[AuditDisplay], APIPaginatedMetadata]
            Audit display logs, optionally with pagination metadata.

        Raises
        ------
        ValueError
            If ``entity_type`` or ``entity_id`` is empty.
        """
        if not entity_type:
            raise ValueError(f"Expected a non-empty value for `entity_type` but received {entity_type!r}")
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        response = self._get(
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
                    AuditListEntityParams,
                ),
            ),
            cast_to=APIPaginatedResponse[AuditDisplay, None],
        )

        return self._unwrap_paginated(response, include_metadata)


class AsyncAuditLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuditLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuditLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuditLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncAuditLogsResourceWithStreamingResponse(self)

    @overload
    async def search(
        self,
        *,
        query: Optional[str] | Omit = omit,
        order_by: Optional[List[AuditOrderByParam]] | Omit = omit,
        filters: Optional[AuditFiltersParam] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: bool = False,
    ) -> List[Audit]: ...

    @overload
    async def search(
        self,
        *,
        query: Optional[str] | Omit = omit,
        order_by: Optional[List[AuditOrderByParam]] | Omit = omit,
        filters: Optional[AuditFiltersParam] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: Literal[True],
    ) -> Tuple[List[Audit], APIPaginatedMetadata]: ...

    async def search(
        self,
        *,
        query: Optional[str] | Omit = omit,
        order_by: Optional[List[AuditOrderByParam]] | Omit = omit,
        filters: Optional[AuditFiltersParam] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: bool = False,
    ) -> List[Audit] | Tuple[List[Audit], APIPaginatedMetadata]:
        """Search audit logs using filters, sorting, and pagination.

        Parameters
        ----------
        query : str | None | Omit
            Free-text search query for audit logs.
        order_by : list[AuditOrderByParam] | Omit
            Sorting criteria for audit logs.
        filters : AuditFiltersParam | Omit
            Filter criteria for audit logs.
        limit : int | Omit
            Maximum number of results to return.
        offset : int | Omit
            Number of results to skip for pagination.
        include_metadata : bool
            If ``True``, return a tuple of ``(data, metadata)`` with pagination info.

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
        list[Audit] | tuple[list[Audit], APIPaginatedMetadata]
            Audit logs, optionally with pagination metadata.
        """
        response = await self._post(
            "/v2/audit/search",
            body=await async_maybe_transform(
                {
                    "filters": filters,
                    "order_by": order_by,
                    "search": query,
                },
                AuditSearchParams,
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
                    AuditSearchParams,
                ),
            ),
            cast_to=APIPaginatedResponse[Audit, None],
        )

        return self._unwrap_paginated(response, include_metadata)

    @overload
    async def list_entities(
        self,
        entity_id: str,
        entity_type: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: bool = False,
    ) -> List[AuditDisplay]: ...

    @overload
    async def list_entities(
        self,
        entity_id: str,
        entity_type: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: Literal[True],
    ) -> Tuple[List[AuditDisplay], APIPaginatedMetadata]: ...

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
        include_metadata: bool = False,
    ) -> List[AuditDisplay] | Tuple[List[AuditDisplay], APIPaginatedMetadata]:
        """List audit display logs for a specific entity.

        Parameters
        ----------
        entity_id : str
            UUID of the entity to list audit logs for.
        entity_type : str
            Type of the entity (e.g. ``"project"``, ``"agent"``).
        limit : int | Omit
            Maximum number of results to return.
        offset : int | Omit
            Number of results to skip for pagination.
        include_metadata : bool
            If ``True``, return a tuple of ``(data, metadata)`` with pagination info.

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
        list[AuditDisplay] | tuple[list[AuditDisplay], APIPaginatedMetadata]
            Audit display logs, optionally with pagination metadata.

        Raises
        ------
        ValueError
            If ``entity_type`` or ``entity_id`` is empty.
        """
        if not entity_type:
            raise ValueError(f"Expected a non-empty value for `entity_type` but received {entity_type!r}")
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        response = await self._get(
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
                    AuditListEntityParams,
                ),
            ),
            cast_to=APIPaginatedResponse[AuditDisplay, None],
        )

        return self._unwrap_paginated(response, include_metadata)


class AuditLogsResourceWithRawResponse:
    def __init__(self, audit: AuditLogsResource) -> None:
        self._audit = audit

        self.search = to_raw_response_wrapper(
            audit.search,
        )
        self.list_entities = to_raw_response_wrapper(
            audit.list_entities,
        )


class AsyncAuditLogsResourceWithRawResponse:
    def __init__(self, audit: AsyncAuditLogsResource) -> None:
        self._audit = audit

        self.search = async_to_raw_response_wrapper(
            audit.search,
        )
        self.list_entities = async_to_raw_response_wrapper(
            audit.list_entities,
        )


class AuditLogsResourceWithStreamingResponse:
    def __init__(self, audit: AuditLogsResource) -> None:
        self._audit = audit

        self.search = to_streamed_response_wrapper(
            audit.search,
        )
        self.list_entities = to_streamed_response_wrapper(
            audit.list_entities,
        )


class AsyncAuditLogsResourceWithStreamingResponse:
    def __init__(self, audit: AsyncAuditLogsResource) -> None:
        self._audit = audit

        self.search = async_to_streamed_response_wrapper(
            audit.search,
        )
        self.list_entities = async_to_streamed_response_wrapper(
            audit.list_entities,
        )
