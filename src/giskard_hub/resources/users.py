from __future__ import annotations

from typing import List, Literal, Optional

import httpx

from ..types import (
    UserListParams,
    InviteUserRequest,
    UpdateUserGroupsRequest,
    UpdateNotificationPreferencesRequest,
)
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.common import APIResponse, APIResponseWithIncluded
from ..types.user_api_resource import UserAPIResource
from ..types.user_detail_api_resource import UserDetailAPIResource
from ..types.user_preferences_api_resource import UserPreferencesAPIResource
from ..types.group_api_resource import GroupAPIResource

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[List[UserAPIResource]]:
        """
        List Users

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/users",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[UserAPIResource]],
        )

    def current(
        self,
        *,
        include: Optional[List[Literal["groups"]]] | NotGiven = not_given,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseWithIncluded[UserDetailAPIResource, object]:
        """
        Get Current User

        Args:
          include: Related resources to include in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/users/current",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include": include}, UserListParams),
            ),
            cast_to=APIResponseWithIncluded[UserDetailAPIResource, object],
        )

    def current_preferences(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[UserPreferencesAPIResource]:
        """
        Get Current User Preferences

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/users/current/preferences",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[UserPreferencesAPIResource],
        )

    def update_notification_preferences(
        self,
        *,
        email_notifications: Optional[bool] | NotGiven = not_given,
        push_notifications: Optional[bool] | NotGiven = not_given,
        evaluation_notifications: Optional[bool] | NotGiven = not_given,
        scan_notifications: Optional[bool] | NotGiven = not_given,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[UserPreferencesAPIResource]:
        """
        Update Notification Preferences

        Args:
          email_notifications: Enable or disable email notifications

          push_notifications: Enable or disable push notifications

          evaluation_notifications: Enable or disable evaluation notifications

          scan_notifications: Enable or disable scan notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/v2/users/current/preferences/notifications",
            body=maybe_transform(
                {
                    "email_notifications": email_notifications,
                    "push_notifications": push_notifications,
                    "evaluation_notifications": evaluation_notifications,
                    "scan_notifications": scan_notifications,
                },
                UpdateNotificationPreferencesRequest,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[UserPreferencesAPIResource],
        )

    def invite(
        self,
        *,
        email: str,
        name: str,
        role: Optional[str] | NotGiven = not_given,
        permissions: Optional[List[str]] | NotGiven = not_given,
        group_ids: Optional[List[str]] | NotGiven = not_given,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[UserDetailAPIResource]:
        """
        Invite User

        Args:
          email: Email address of the user to invite

          name: Name of the user to invite

          role: Role to assign to the user

          permissions: Permissions to assign to the user

          group_ids: Group IDs to assign to the user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/users/invite",
            body=maybe_transform(
                {
                    "email": email,
                    "name": name,
                    "role": role,
                    "permissions": permissions,
                    "group_ids": group_ids,
                },
                InviteUserRequest,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[UserDetailAPIResource],
        )

    def retrieve(
        self,
        user_id: str,
        *,
        include: Optional[List[Literal["groups"]]] | NotGiven = not_given,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseWithIncluded[UserDetailAPIResource, object]:
        """
        Get User Detail

        Args:
          user_id: User ID to retrieve

          include: Related resources to include in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/v2/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include": include}, UserListParams),
            ),
            cast_to=APIResponseWithIncluded[UserDetailAPIResource, object],
        )

    def delete(
        self,
        user_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[None]:
        """
        Delete User

        Args:
          user_id: User ID to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._delete(
            f"/v2/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

    def update_permissions(
        self,
        user_id: str,
        *,
        permissions: List[str],
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[UserDetailAPIResource]:
        """
        Update User Permissions

        Args:
          user_id: User ID to update

          permissions: Permissions to assign to the user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._patch(
            f"/v2/users/permissions/{user_id}",
            body=permissions,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[UserDetailAPIResource],
        )

    def get_groups(
        self,
        user_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[List[GroupAPIResource]]:
        """
        Get User Groups

        Args:
          user_id: User ID to retrieve groups for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/v2/users/{user_id}/groups",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[GroupAPIResource]],
        )

    def update_groups(
        self,
        user_id: str,
        *,
        group_ids: List[str],
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[List[GroupAPIResource]]:
        """
        Update User Groups

        Args:
          user_id: User ID to update

          group_ids: Group IDs to assign to the user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._patch(
            f"/v2/users/{user_id}/groups",
            body=maybe_transform({"group_ids": group_ids}, UpdateUserGroupsRequest),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[GroupAPIResource]],
        )

    def request_password_reset(
        self,
        user_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[None]:
        """
        Request Password Reset

        Args:
          user_id: User ID to request password reset for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._put(
            f"/v2/users/{user_id}/request-reset-password",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[List[UserAPIResource]]:
        """List Users"""
        return await self._get(
            "/v2/users",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[UserAPIResource]],
        )

    async def current(
        self,
        *,
        include: Optional[List[Literal["groups"]]] | NotGiven = not_given,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseWithIncluded[UserDetailAPIResource, object]:
        """Get Current User"""
        return await self._get(
            "/v2/users/current",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"include": include}, UserListParams),
            ),
            cast_to=APIResponseWithIncluded[UserDetailAPIResource, object],
        )

    async def current_preferences(
        self,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[UserPreferencesAPIResource]:
        """Get Current User Preferences"""
        return await self._get(
            "/v2/users/current/preferences",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[UserPreferencesAPIResource],
        )

    async def update_notification_preferences(
        self,
        *,
        email_notifications: Optional[bool] | NotGiven = not_given,
        push_notifications: Optional[bool] | NotGiven = not_given,
        evaluation_notifications: Optional[bool] | NotGiven = not_given,
        scan_notifications: Optional[bool] | NotGiven = not_given,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[UserPreferencesAPIResource]:
        """Update Notification Preferences"""
        return await self._patch(
            "/v2/users/current/preferences/notifications",
            body=await async_maybe_transform(
                {
                    "email_notifications": email_notifications,
                    "push_notifications": push_notifications,
                    "evaluation_notifications": evaluation_notifications,
                    "scan_notifications": scan_notifications,
                },
                UpdateNotificationPreferencesRequest,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[UserPreferencesAPIResource],
        )

    async def invite(
        self,
        *,
        email: str,
        name: str,
        role: Optional[str] | NotGiven = not_given,
        permissions: Optional[List[str]] | NotGiven = not_given,
        group_ids: Optional[List[str]] | NotGiven = not_given,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[UserDetailAPIResource]:
        """Invite User"""
        return await self._post(
            "/v2/users/invite",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "name": name,
                    "role": role,
                    "permissions": permissions,
                    "group_ids": group_ids,
                },
                InviteUserRequest,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[UserDetailAPIResource],
        )

    async def retrieve(
        self,
        user_id: str,
        *,
        include: Optional[List[Literal["groups"]]] | NotGiven = not_given,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseWithIncluded[UserDetailAPIResource, object]:
        """Get User Detail"""
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/v2/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"include": include}, UserListParams),
            ),
            cast_to=APIResponseWithIncluded[UserDetailAPIResource, object],
        )

    async def delete(
        self,
        user_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[None]:
        """Delete User"""
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._delete(
            f"/v2/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

    async def update_permissions(
        self,
        user_id: str,
        *,
        permissions: List[str],
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[UserDetailAPIResource]:
        """Update User Permissions"""
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._patch(
            f"/v2/users/permissions/{user_id}",
            body=permissions,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[UserDetailAPIResource],
        )

    async def get_groups(
        self,
        user_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[List[GroupAPIResource]]:
        """Get User Groups"""
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/v2/users/{user_id}/groups",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[GroupAPIResource]],
        )

    async def update_groups(
        self,
        user_id: str,
        *,
        group_ids: List[str],
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[List[GroupAPIResource]]:
        """Update User Groups"""
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._patch(
            f"/v2/users/{user_id}/groups",
            body=await async_maybe_transform({"group_ids": group_ids}, UpdateUserGroupsRequest),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[GroupAPIResource]],
        )

    async def request_password_reset(
        self,
        user_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[None]:
        """Request Password Reset"""
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._put(
            f"/v2/users/{user_id}/request-reset-password",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.current = to_raw_response_wrapper(
            users.current,
        )
        self.current_preferences = to_raw_response_wrapper(
            users.current_preferences,
        )
        self.update_notification_preferences = to_raw_response_wrapper(
            users.update_notification_preferences,
        )
        self.invite = to_raw_response_wrapper(
            users.invite,
        )
        self.retrieve = to_raw_response_wrapper(
            users.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            users.delete,
        )
        self.update_permissions = to_raw_response_wrapper(
            users.update_permissions,
        )
        self.get_groups = to_raw_response_wrapper(
            users.get_groups,
        )
        self.update_groups = to_raw_response_wrapper(
            users.update_groups,
        )
        self.request_password_reset = to_raw_response_wrapper(
            users.request_password_reset,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.current = async_to_raw_response_wrapper(
            users.current,
        )
        self.current_preferences = async_to_raw_response_wrapper(
            users.current_preferences,
        )
        self.update_notification_preferences = async_to_raw_response_wrapper(
            users.update_notification_preferences,
        )
        self.invite = async_to_raw_response_wrapper(
            users.invite,
        )
        self.retrieve = async_to_raw_response_wrapper(
            users.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            users.delete,
        )
        self.update_permissions = async_to_raw_response_wrapper(
            users.update_permissions,
        )
        self.get_groups = async_to_raw_response_wrapper(
            users.get_groups,
        )
        self.update_groups = async_to_raw_response_wrapper(
            users.update_groups,
        )
        self.request_password_reset = async_to_raw_response_wrapper(
            users.request_password_reset,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.current = to_streamed_response_wrapper(
            users.current,
        )
        self.current_preferences = to_streamed_response_wrapper(
            users.current_preferences,
        )
        self.update_notification_preferences = to_streamed_response_wrapper(
            users.update_notification_preferences,
        )
        self.invite = to_streamed_response_wrapper(
            users.invite,
        )
        self.retrieve = to_streamed_response_wrapper(
            users.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            users.delete,
        )
        self.update_permissions = to_streamed_response_wrapper(
            users.update_permissions,
        )
        self.get_groups = to_streamed_response_wrapper(
            users.get_groups,
        )
        self.update_groups = to_streamed_response_wrapper(
            users.update_groups,
        )
        self.request_password_reset = to_streamed_response_wrapper(
            users.request_password_reset,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.current = async_to_streamed_response_wrapper(
            users.current,
        )
        self.current_preferences = async_to_streamed_response_wrapper(
            users.current_preferences,
        )
        self.update_notification_preferences = async_to_streamed_response_wrapper(
            users.update_notification_preferences,
        )
        self.invite = async_to_streamed_response_wrapper(
            users.invite,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            users.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            users.delete,
        )
        self.update_permissions = async_to_streamed_response_wrapper(
            users.update_permissions,
        )
        self.get_groups = async_to_streamed_response_wrapper(
            users.get_groups,
        )
        self.update_groups = async_to_streamed_response_wrapper(
            users.update_groups,
        )
        self.request_password_reset = async_to_streamed_response_wrapper(
            users.request_password_reset,
        )
