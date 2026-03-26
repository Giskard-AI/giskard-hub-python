from __future__ import annotations

from typing import Any, Dict, List, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.common import APIResponse
from ...types.table_view import (
    TableView,
    TableViewListParams,
    TableViewCreateParams,
    TableViewUpdateParams,
)

__all__ = ["TableViewsResource", "AsyncTableViewsResource"]


class TableViewsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TableViewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return TableViewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TableViewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return TableViewsResourceWithStreamingResponse(self)

    def create(
        self,
        project_id: str,
        *,
        entity_type: str,
        name: str,
        settings: Dict[str, Any],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TableView:
        """Create a new table view for a project.

        Parameters
        ----------
        project_id : str
            The ID of the project to create the table view in.
        entity_type : str
            The entity type for the table view.
        name : str
            The name of the table view.
        settings : Dict[str, Any]
            The settings for the table view.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float or httpx.Timeout or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        TableView
            The newly created table view.

        Raises
        ------
        ValueError
            If ``project_id`` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        response = self._post(
            f"/v2/projects/{project_id}/table-views",
            body=maybe_transform(
                {
                    "entity_type": entity_type,
                    "name": name,
                    "settings": settings,
                },
                TableViewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[TableView],
        )

        return self._unwrap(response)

    def list(
        self,
        project_id: str,
        *,
        entity_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[TableView]:
        """List all table views for a project filtered by entity type.

        Parameters
        ----------
        project_id : str
            The ID of the project to list table views for.
        entity_type : str
            The entity type to filter table views by.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float or httpx.Timeout or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        list[TableView]
            A list of table views for the project.

        Raises
        ------
        ValueError
            If ``project_id`` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        response = self._get(
            f"/v2/projects/{project_id}/table-views",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"entity_type": entity_type}, TableViewListParams),
            ),
            cast_to=APIResponse[List[TableView]],
        )

        return self._unwrap(response)

    def update(
        self,
        view_id: str,
        *,
        project_id: str,
        name: Optional[str] | Omit = omit,
        settings: Optional[Dict[str, Any]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TableView:
        """Update an existing table view.

        Parameters
        ----------
        view_id : str
            The ID of the table view to update.
        project_id : str
            The ID of the project the table view belongs to.
        name : str or None
            The updated name of the table view.
        settings : Dict[str, Any] or None
            The updated settings for the table view.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float or httpx.Timeout or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        TableView
            The updated table view.

        Raises
        ------
        ValueError
            If ``project_id`` or ``view_id`` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        response = self._patch(
            f"/v2/projects/{project_id}/table-views/{view_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "settings": settings,
                },
                TableViewUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[TableView],
        )

        return self._unwrap(response)

    def delete(
        self,
        view_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a table view by its ID.

        Parameters
        ----------
        view_id : str
            The ID of the table view to delete.
        project_id : str
            The ID of the project the table view belongs to.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float or httpx.Timeout or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If ``project_id`` or ``view_id`` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        response = self._delete(
            f"/v2/projects/{project_id}/table-views/{view_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)


class AsyncTableViewsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTableViewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTableViewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTableViewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncTableViewsResourceWithStreamingResponse(self)

    async def create(
        self,
        project_id: str,
        *,
        entity_type: str,
        name: str,
        settings: Dict[str, Any],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TableView:
        """Create a new table view for a project.

        Parameters
        ----------
        project_id : str
            The ID of the project to create the table view in.
        entity_type : str
            The entity type for the table view.
        name : str
            The name of the table view.
        settings : Dict[str, Any]
            The settings for the table view.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float or httpx.Timeout or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        TableView
            The newly created table view.

        Raises
        ------
        ValueError
            If ``project_id`` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        response = await self._post(
            f"/v2/projects/{project_id}/table-views",
            body=await async_maybe_transform(
                {
                    "entity_type": entity_type,
                    "name": name,
                    "settings": settings,
                },
                TableViewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[TableView],
        )

        return self._unwrap(response)

    async def list(
        self,
        project_id: str,
        *,
        entity_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[TableView]:
        """List all table views for a project filtered by entity type.

        Parameters
        ----------
        project_id : str
            The ID of the project to list table views for.
        entity_type : str
            The entity type to filter table views by.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float or httpx.Timeout or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        list[TableView]
            A list of table views for the project.

        Raises
        ------
        ValueError
            If ``project_id`` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        response = await self._get(
            f"/v2/projects/{project_id}/table-views",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"entity_type": entity_type}, TableViewListParams),
            ),
            cast_to=APIResponse[List[TableView]],
        )

        return self._unwrap(response)

    async def update(
        self,
        view_id: str,
        *,
        project_id: str,
        name: Optional[str] | Omit = omit,
        settings: Optional[Dict[str, Any]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TableView:
        """Update an existing table view.

        Parameters
        ----------
        view_id : str
            The ID of the table view to update.
        project_id : str
            The ID of the project the table view belongs to.
        name : str or None
            The updated name of the table view.
        settings : Dict[str, Any] or None
            The updated settings for the table view.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float or httpx.Timeout or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        TableView
            The updated table view.

        Raises
        ------
        ValueError
            If ``project_id`` or ``view_id`` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        response = await self._patch(
            f"/v2/projects/{project_id}/table-views/{view_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "settings": settings,
                },
                TableViewUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[TableView],
        )

        return self._unwrap(response)

    async def delete(
        self,
        view_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a table view by its ID.

        Parameters
        ----------
        view_id : str
            The ID of the table view to delete.
        project_id : str
            The ID of the project the table view belongs to.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float or httpx.Timeout or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If ``project_id`` or ``view_id`` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        response = await self._delete(
            f"/v2/projects/{project_id}/table-views/{view_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)


class TableViewsResourceWithRawResponse:
    def __init__(self, table_views: TableViewsResource) -> None:
        self._table_views = table_views

        self.create = to_raw_response_wrapper(
            table_views.create,
        )
        self.list = to_raw_response_wrapper(
            table_views.list,
        )
        self.update = to_raw_response_wrapper(
            table_views.update,
        )
        self.delete = to_raw_response_wrapper(
            table_views.delete,
        )


class AsyncTableViewsResourceWithRawResponse:
    def __init__(self, table_views: AsyncTableViewsResource) -> None:
        self._table_views = table_views

        self.create = async_to_raw_response_wrapper(
            table_views.create,
        )
        self.list = async_to_raw_response_wrapper(
            table_views.list,
        )
        self.update = async_to_raw_response_wrapper(
            table_views.update,
        )
        self.delete = async_to_raw_response_wrapper(
            table_views.delete,
        )


class TableViewsResourceWithStreamingResponse:
    def __init__(self, table_views: TableViewsResource) -> None:
        self._table_views = table_views

        self.create = to_streamed_response_wrapper(
            table_views.create,
        )
        self.list = to_streamed_response_wrapper(
            table_views.list,
        )
        self.update = to_streamed_response_wrapper(
            table_views.update,
        )
        self.delete = to_streamed_response_wrapper(
            table_views.delete,
        )


class AsyncTableViewsResourceWithStreamingResponse:
    def __init__(self, table_views: AsyncTableViewsResource) -> None:
        self._table_views = table_views

        self.create = async_to_streamed_response_wrapper(
            table_views.create,
        )
        self.list = async_to_streamed_response_wrapper(
            table_views.list,
        )
        self.update = async_to_streamed_response_wrapper(
            table_views.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            table_views.delete,
        )
