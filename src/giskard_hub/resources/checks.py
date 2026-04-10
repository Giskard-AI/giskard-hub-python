from __future__ import annotations

from typing import List, Optional

import httpx

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
from ..types.check import (
    Check,
    CheckListParams,
    CheckCreateParams,
    CheckUpdateParams,
    FlatCheckSpecParam,
    CheckBulkDeleteParams,
)
from .._base_client import make_request_options
from ..types.common import APIResponse

__all__ = ["ChecksResource", "AsyncChecksResource"]


class ChecksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return ChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return ChecksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        spec: FlatCheckSpecParam,
        identifier: str,
        name: str,
        project_id: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Check:
        """Create a new check in the specified project.

        Parameters
        ----------
        spec : FlatCheckSpecParam
            Check specification.
        identifier : str
            Unique identifier of the check.
        name : str
            Display name of the check.
        project_id : str
            Project ID to create the check in.
        description : str | None | Omit
            Human-readable description of the check.

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
        Check
            The newly created check.
        """
        response = self._post(
            "/v2/checks",
            body=maybe_transform(
                {
                    "spec": spec,
                    "description": description,
                    "identifier": identifier,
                    "name": name,
                    "project_id": project_id,
                },
                CheckCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Check],
        )

        return self._unwrap(response)

    def retrieve(
        self,
        check_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Check:
        """Retrieve a check by its ID.

        Parameters
        ----------
        check_id : str
            ID of the check to retrieve.

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
        Check
            The requested check.

        Raises
        ------
        ValueError
            If ``check_id`` is empty.
        """
        if not check_id:
            raise ValueError(f"Expected a non-empty value for `check_id` but received {check_id!r}")
        response = self._get(
            f"/v2/checks/{check_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Check],
        )

        return self._unwrap(response)

    def update(
        self,
        check_id: str,
        *,
        spec: Optional[FlatCheckSpecParam] | Omit = omit,
        description: Optional[str] | Omit = omit,
        identifier: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Check:
        """Update an existing check.

        Parameters
        ----------
        check_id : str
            ID of the check to update.
        spec : FlatCheckSpecParam | None | Omit
            Updated check specification.
        description : str | None | Omit
            Updated description of the check.
        identifier : str | None | Omit
            Updated identifier of the check.
        name : str | None | Omit
            Updated display name of the check.

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
        Check
            The updated check.

        Raises
        ------
        ValueError
            If ``check_id`` is empty.
        """
        if not check_id:
            raise ValueError(f"Expected a non-empty value for `check_id` but received {check_id!r}")
        response = self._patch(
            f"/v2/checks/{check_id}",
            body=maybe_transform(
                {
                    "spec": spec,
                    "description": description,
                    "identifier": identifier,
                    "name": name,
                },
                CheckUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Check],
        )

        return self._unwrap(response)

    def list(
        self,
        *,
        project_id: str,
        filter_builtin: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[Check]:
        """List all checks for a project.

        Parameters
        ----------
        project_id : str
            Project ID to list checks for.
        filter_builtin : bool | Omit
            Whether to filter out built-in checks. Default value is True.

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
        list[Check]
            List of checks for the project.
        """
        response = self._get(
            "/v2/checks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "project_id": project_id,
                        "filter_builtin": filter_builtin,
                    },
                    CheckListParams,
                ),
            ),
            cast_to=APIResponse[List[Check]],
        )

        return self._unwrap(response)

    def delete(
        self,
        check_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a check by its ID.

        Parameters
        ----------
        check_id : str
            ID of the check to delete.

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

        Raises
        ------
        ValueError
            If ``check_id`` is empty.
        """
        if not check_id:
            raise ValueError(f"Expected a non-empty value for `check_id` but received {check_id!r}")
        response = self._delete(
            f"/v2/checks/{check_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    def bulk_delete(
        self,
        *,
        check_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete multiple checks at once.

        Parameters
        ----------
        check_ids : SequenceNotStr[str]
            IDs of the checks to delete.

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
        """
        response = self._delete(
            "/v2/checks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"check_ids": check_ids}, CheckBulkDeleteParams),
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)


class AsyncChecksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncChecksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        spec: FlatCheckSpecParam,
        identifier: str,
        name: str,
        project_id: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Check:
        """Create a new check in the specified project.

        Parameters
        ----------
        spec : FlatCheckSpecParam
            Check specification.
        identifier : str
            Unique identifier of the check.
        name : str
            Display name of the check.
        project_id : str
            Project ID to create the check in.
        description : str | None | Omit
            Human-readable description of the check.

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
        Check
            The newly created check.
        """
        response = await self._post(
            "/v2/checks",
            body=await async_maybe_transform(
                {
                    "spec": spec,
                    "description": description,
                    "identifier": identifier,
                    "name": name,
                    "project_id": project_id,
                },
                CheckCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Check],
        )

        return self._unwrap(response)

    async def retrieve(
        self,
        check_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Check:
        """Retrieve a check by its ID.

        Parameters
        ----------
        check_id : str
            ID of the check to retrieve.

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
        Check
            The requested check.

        Raises
        ------
        ValueError
            If ``check_id`` is empty.
        """
        if not check_id:
            raise ValueError(f"Expected a non-empty value for `check_id` but received {check_id!r}")
        response = await self._get(
            f"/v2/checks/{check_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Check],
        )

        return self._unwrap(response)

    async def update(
        self,
        check_id: str,
        *,
        spec: Optional[FlatCheckSpecParam] | Omit = omit,
        description: Optional[str] | Omit = omit,
        identifier: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Check:
        """Update an existing check.

        Parameters
        ----------
        check_id : str
            ID of the check to update.
        spec : FlatCheckSpecParam | None | Omit
            Updated check specification.
        description : str | None | Omit
            Updated description of the check.
        identifier : str | None | Omit
            Updated identifier of the check.
        name : str | None | Omit
            Updated display name of the check.

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
        Check
            The updated check.

        Raises
        ------
        ValueError
            If ``check_id`` is empty.
        """
        if not check_id:
            raise ValueError(f"Expected a non-empty value for `check_id` but received {check_id!r}")
        response = await self._patch(
            f"/v2/checks/{check_id}",
            body=await async_maybe_transform(
                {
                    "spec": spec,
                    "description": description,
                    "identifier": identifier,
                    "name": name,
                },
                CheckUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Check],
        )

        return self._unwrap(response)

    async def list(
        self,
        *,
        project_id: str,
        filter_builtin: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[Check]:
        """List all checks for a project.

        Parameters
        ----------
        project_id : str
            Project ID to list checks for.
        filter_builtin : bool | Omit
            Whether to filter out built-in checks. Default value is True.

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
        list[Check]
            List of checks for the project.
        """
        response = await self._get(
            "/v2/checks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "project_id": project_id,
                        "filter_builtin": filter_builtin,
                    },
                    CheckListParams,
                ),
            ),
            cast_to=APIResponse[List[Check]],
        )

        return self._unwrap(response)

    async def delete(
        self,
        check_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a check by its ID.

        Parameters
        ----------
        check_id : str
            ID of the check to delete.

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

        Raises
        ------
        ValueError
            If ``check_id`` is empty.
        """
        if not check_id:
            raise ValueError(f"Expected a non-empty value for `check_id` but received {check_id!r}")
        response = await self._delete(
            f"/v2/checks/{check_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    async def bulk_delete(
        self,
        *,
        check_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete multiple checks at once.

        Parameters
        ----------
        check_ids : SequenceNotStr[str]
            IDs of the checks to delete.

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
        """
        response = await self._delete(
            "/v2/checks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"check_ids": check_ids}, CheckBulkDeleteParams),
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)


class ChecksResourceWithRawResponse:
    def __init__(self, checks: ChecksResource) -> None:
        self._checks = checks

        self.create = to_raw_response_wrapper(
            checks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            checks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            checks.update,
        )
        self.list = to_raw_response_wrapper(
            checks.list,
        )
        self.delete = to_raw_response_wrapper(
            checks.delete,
        )
        self.bulk_delete = to_raw_response_wrapper(
            checks.bulk_delete,
        )


class AsyncChecksResourceWithRawResponse:
    def __init__(self, checks: AsyncChecksResource) -> None:
        self._checks = checks

        self.create = async_to_raw_response_wrapper(
            checks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            checks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            checks.update,
        )
        self.list = async_to_raw_response_wrapper(
            checks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            checks.delete,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            checks.bulk_delete,
        )


class ChecksResourceWithStreamingResponse:
    def __init__(self, checks: ChecksResource) -> None:
        self._checks = checks

        self.create = to_streamed_response_wrapper(
            checks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            checks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            checks.update,
        )
        self.list = to_streamed_response_wrapper(
            checks.list,
        )
        self.delete = to_streamed_response_wrapper(
            checks.delete,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            checks.bulk_delete,
        )


class AsyncChecksResourceWithStreamingResponse:
    def __init__(self, checks: AsyncChecksResource) -> None:
        self._checks = checks

        self.create = async_to_streamed_response_wrapper(
            checks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            checks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            checks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            checks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            checks.delete,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            checks.bulk_delete,
        )
