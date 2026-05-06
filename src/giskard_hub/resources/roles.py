from typing import Any, Dict, List

import httpx

from ..types import Role, RoleListParams, RoleCreateParams, RoleUpdateParams
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
from .._base_client import make_request_options
from ..types.common import APIResponse

__all__ = ["RolesResource", "AsyncRolesResource"]


class RolesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> "RolesResourceWithRawResponse":
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return RolesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> "RolesResourceWithStreamingResponse":
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return RolesResourceWithStreamingResponse(self)

    def create(
        self,
        dataset_id: str,
        /,
        *,
        project_id: str,
        name: str,
        input_schema: Dict[str, Any],
        output_schema: Dict[str, Any],
        source_agent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Role:
        """Create a new role in a dataset.

        Parameters
        ----------
        dataset_id : str
            ID of the dataset to create the role in.
        project_id : str
            Project ID for the role.
        name : str
            Name of the role.
        input_schema : Dict[str, Any]
            JSON schema describing the role's input payload.
        output_schema : Dict[str, Any]
            JSON schema describing the role's output payload.
        source_agent_id : str | Omit
            Optional source agent to clone the schemas from.

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
        Role
            The newly created role.

        Raises
        ------
        ValueError
            If `dataset_id` is empty.
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        response = self._post(
            f"/v2/roles/datasets/{dataset_id}/roles",
            body=maybe_transform(
                {
                    "name": name,
                    "input_schema": input_schema,
                    "output_schema": output_schema,
                    "source_agent_id": source_agent_id,
                },
                RoleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, RoleListParams),
            ),
            cast_to=APIResponse[Role],
        )

        return self._unwrap(response)

    def list(
        self,
        dataset_id: str,
        /,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[Role]:
        """List all roles in a dataset.

        Parameters
        ----------
        dataset_id : str
            ID of the dataset to list roles for.
        project_id : str
            Project ID to filter by.

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
        List[Role]
            List of roles in the dataset.

        Raises
        ------
        ValueError
            If `dataset_id` is empty.
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        response = self._get(
            f"/v2/roles/datasets/{dataset_id}/roles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, RoleListParams),
            ),
            cast_to=APIResponse[List[Role]],
        )

        return self._unwrap(response)

    def update(
        self,
        role_id: str,
        /,
        *,
        project_id: str,
        name: str | Omit = omit,
        input_schema: Dict[str, Any] | Omit = omit,
        output_schema: Dict[str, Any] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Role:
        """Update an existing role.

        Parameters
        ----------
        role_id : str
            ID of the role to update.
        project_id : str
            Project ID for the role.
        name : str | Omit
            Updated name of the role.
        input_schema : Dict[str, Any] | Omit
            Updated input schema for the role.
        output_schema : Dict[str, Any] | Omit
            Updated output schema for the role.

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
        Role
            The updated role.

        Raises
        ------
        ValueError
            If `role_id` is empty.
        """
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        response = self._patch(
            f"/v2/roles/{role_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "input_schema": input_schema,
                    "output_schema": output_schema,
                },
                RoleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, RoleListParams),
            ),
            cast_to=APIResponse[Role],
        )

        return self._unwrap(response)

    def delete(
        self,
        role_id: str,
        /,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a role by its ID.

        Parameters
        ----------
        role_id : str
            ID of the role to delete.
        project_id : str
            Project ID for the role.

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
            If `role_id` is empty.
        """
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        response = self._delete(
            f"/v2/roles/{role_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, RoleListParams),
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)


class AsyncRolesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> "AsyncRolesResourceWithRawResponse":
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRolesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> "AsyncRolesResourceWithStreamingResponse":
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncRolesResourceWithStreamingResponse(self)

    async def create(
        self,
        dataset_id: str,
        /,
        *,
        project_id: str,
        name: str,
        input_schema: Dict[str, Any],
        output_schema: Dict[str, Any],
        source_agent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Role:
        """Create a new role in a dataset.

        Parameters
        ----------
        dataset_id : str
            ID of the dataset to create the role in.
        project_id : str
            Project ID for the role.
        name : str
            Name of the role.
        input_schema : Dict[str, Any]
            JSON schema describing the role's input payload.
        output_schema : Dict[str, Any]
            JSON schema describing the role's output payload.
        source_agent_id : str | Omit
            Optional source agent to clone the schemas from.

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
        Role
            The newly created role.

        Raises
        ------
        ValueError
            If `dataset_id` is empty.
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        response = await self._post(
            f"/v2/roles/datasets/{dataset_id}/roles",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "input_schema": input_schema,
                    "output_schema": output_schema,
                    "source_agent_id": source_agent_id,
                },
                RoleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"project_id": project_id}, RoleListParams),
            ),
            cast_to=APIResponse[Role],
        )

        return self._unwrap(response)

    async def list(
        self,
        dataset_id: str,
        /,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[Role]:
        """List all roles in a dataset.

        Parameters
        ----------
        dataset_id : str
            ID of the dataset to list roles for.
        project_id : str
            Project ID to filter by.

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
        List[Role]
            List of roles in the dataset.

        Raises
        ------
        ValueError
            If `dataset_id` is empty.
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        response = await self._get(
            f"/v2/roles/datasets/{dataset_id}/roles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"project_id": project_id}, RoleListParams),
            ),
            cast_to=APIResponse[List[Role]],
        )

        return self._unwrap(response)

    async def update(
        self,
        role_id: str,
        /,
        *,
        project_id: str,
        name: str | Omit = omit,
        input_schema: Dict[str, Any] | Omit = omit,
        output_schema: Dict[str, Any] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Role:
        """Update an existing role.

        Parameters
        ----------
        role_id : str
            ID of the role to update.
        project_id : str
            Project ID for the role.
        name : str | Omit
            Updated name of the role.
        input_schema : Dict[str, Any] | Omit
            Updated input schema for the role.
        output_schema : Dict[str, Any] | Omit
            Updated output schema for the role.

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
        Role
            The updated role.

        Raises
        ------
        ValueError
            If `role_id` is empty.
        """
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        response = await self._patch(
            f"/v2/roles/{role_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "input_schema": input_schema,
                    "output_schema": output_schema,
                },
                RoleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"project_id": project_id}, RoleListParams),
            ),
            cast_to=APIResponse[Role],
        )

        return self._unwrap(response)

    async def delete(
        self,
        role_id: str,
        /,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a role by its ID.

        Parameters
        ----------
        role_id : str
            ID of the role to delete.
        project_id : str
            Project ID for the role.

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
            If `role_id` is empty.
        """
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        response = await self._delete(
            f"/v2/roles/{role_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"project_id": project_id}, RoleListParams),
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)


class RolesResourceWithRawResponse:
    def __init__(self, roles: RolesResource) -> None:
        self._roles = roles

        self.create = to_raw_response_wrapper(
            roles.create,
        )
        self.list = to_raw_response_wrapper(
            roles.list,
        )
        self.update = to_raw_response_wrapper(
            roles.update,
        )
        self.delete = to_raw_response_wrapper(
            roles.delete,
        )


class AsyncRolesResourceWithRawResponse:
    def __init__(self, roles: AsyncRolesResource) -> None:
        self._roles = roles

        self.create = async_to_raw_response_wrapper(
            roles.create,
        )
        self.list = async_to_raw_response_wrapper(
            roles.list,
        )
        self.update = async_to_raw_response_wrapper(
            roles.update,
        )
        self.delete = async_to_raw_response_wrapper(
            roles.delete,
        )


class RolesResourceWithStreamingResponse:
    def __init__(self, roles: RolesResource) -> None:
        self._roles = roles

        self.create = to_streamed_response_wrapper(
            roles.create,
        )
        self.list = to_streamed_response_wrapper(
            roles.list,
        )
        self.update = to_streamed_response_wrapper(
            roles.update,
        )
        self.delete = to_streamed_response_wrapper(
            roles.delete,
        )


class AsyncRolesResourceWithStreamingResponse:
    def __init__(self, roles: AsyncRolesResource) -> None:
        self._roles = roles

        self.create = async_to_streamed_response_wrapper(
            roles.create,
        )
        self.list = async_to_streamed_response_wrapper(
            roles.list,
        )
        self.update = async_to_streamed_response_wrapper(
            roles.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            roles.delete,
        )
