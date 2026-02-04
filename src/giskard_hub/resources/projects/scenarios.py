from __future__ import annotations

from typing import Any, Dict, Optional

import httpx

from ...types import scenario_create_params, scenario_update_params, scenario_preview_params
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.api_response_none import APIResponseNone
from ...types.api_response_scenario import APIResponseScenario
from ...types.api_response_list_scenario import APIResponseListScenario
from ...types.api_response_scenario_preview import APIResponseScenarioPreview

__all__ = ["ScenariosResource", "AsyncScenariosResource"]


class ScenariosResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScenariosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return ScenariosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScenariosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return ScenariosResourceWithStreamingResponse(self)

    def create(
        self,
        project_id: str,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        config: Optional[Dict[str, Any]] | Omit = omit,
        agent_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseScenario:
        """
        Create Scenario

        Args:
          name: Name of the scenario

          description: Description of the scenario

          config: Configuration for the scenario

          agent_id: Associated agent ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            f"/v2/projects/{project_id}/scenarios",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "config": config,
                    "agent_id": agent_id,
                },
                scenario_create_params.ScenarioCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseScenario,
        )

    def retrieve(
        self,
        scenario_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseScenario:
        """
        Retrieve Scenario

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")
        return self._get(
            f"/v2/projects/{project_id}/scenarios/{scenario_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseScenario,
        )

    def update(
        self,
        scenario_id: str,
        *,
        project_id: str,
        name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        config: Optional[Dict[str, Any]] | Omit = omit,
        agent_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseScenario:
        """
        Update Scenario

        Args:
          name: Name of the scenario

          description: Description of the scenario

          config: Configuration for the scenario

          agent_id: Associated agent ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")
        return self._patch(
            f"/v2/projects/{project_id}/scenarios/{scenario_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "config": config,
                    "agent_id": agent_id,
                },
                scenario_update_params.ScenarioUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseScenario,
        )

    def list(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseListScenario:
        """
        List Scenarios

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            f"/v2/projects/{project_id}/scenarios",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseListScenario,
        )

    def delete(
        self,
        scenario_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseNone:
        """
        Delete Scenario

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")
        return self._delete(
            f"/v2/projects/{project_id}/scenarios/{scenario_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseNone,
        )

    def preview(
        self,
        project_id: str,
        *,
        agent_id: str,
        description: str,
        rules: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseScenarioPreview:
        """
        Preview Scenario

        Args:
          project_id: Project ID

          agent_id: Agent ID to use for preview

          description: Description of the scenario

          rules: Rules to use for preview

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            f"/v2/projects/{project_id}/scenarios/preview",
            body=maybe_transform(
                {
                    "description": description,
                    "rules": rules,
                },
                scenario_preview_params.ScenarioPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"agent_id": agent_id}, scenario_preview_params.ScenarioPreviewParams),
            ),
            cast_to=APIResponseScenarioPreview,
        )


class AsyncScenariosResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScenariosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScenariosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScenariosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncScenariosResourceWithStreamingResponse(self)

    async def create(
        self,
        project_id: str,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        config: Optional[Dict[str, Any]] | Omit = omit,
        agent_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseScenario:
        """
        Create Scenario

        Args:
          name: Name of the scenario

          description: Description of the scenario

          config: Configuration for the scenario

          agent_id: Associated agent ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            f"/v2/projects/{project_id}/scenarios",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "config": config,
                    "agent_id": agent_id,
                },
                scenario_create_params.ScenarioCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseScenario,
        )

    async def retrieve(
        self,
        scenario_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseScenario:
        """
        Retrieve Scenario

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")
        return await self._get(
            f"/v2/projects/{project_id}/scenarios/{scenario_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseScenario,
        )

    async def update(
        self,
        scenario_id: str,
        *,
        project_id: str,
        name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        config: Optional[Dict[str, Any]] | Omit = omit,
        agent_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseScenario:
        """
        Update Scenario

        Args:
          name: Name of the scenario

          description: Description of the scenario

          config: Configuration for the scenario

          agent_id: Associated agent ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")
        return await self._patch(
            f"/v2/projects/{project_id}/scenarios/{scenario_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "config": config,
                    "agent_id": agent_id,
                },
                scenario_update_params.ScenarioUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseScenario,
        )

    async def list(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseListScenario:
        """
        List Scenarios

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            f"/v2/projects/{project_id}/scenarios",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseListScenario,
        )

    async def delete(
        self,
        scenario_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseNone:
        """
        Delete Scenario

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")
        return await self._delete(
            f"/v2/projects/{project_id}/scenarios/{scenario_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseNone,
        )

    async def preview(
        self,
        project_id: str,
        *,
        agent_id: str,
        description: str,
        rules: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseScenarioPreview:
        """
        Preview Scenario

        Args:
          project_id: Project ID

          agent_id: Agent ID to use for preview

          description: Description of the scenario

          rules: Rules to use for preview

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            f"/v2/projects/{project_id}/scenarios/preview",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "rules": rules,
                },
                scenario_preview_params.ScenarioPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"agent_id": agent_id}, scenario_preview_params.ScenarioPreviewParams
                ),
            ),
            cast_to=APIResponseScenarioPreview,
        )


class ScenariosResourceWithRawResponse:
    def __init__(self, scenarios: ScenariosResource) -> None:
        self._scenarios = scenarios

        self.create = to_raw_response_wrapper(
            scenarios.create,
        )
        self.retrieve = to_raw_response_wrapper(
            scenarios.retrieve,
        )
        self.update = to_raw_response_wrapper(
            scenarios.update,
        )
        self.list = to_raw_response_wrapper(
            scenarios.list,
        )
        self.delete = to_raw_response_wrapper(
            scenarios.delete,
        )
        self.preview = to_raw_response_wrapper(
            scenarios.preview,
        )


class AsyncScenariosResourceWithRawResponse:
    def __init__(self, scenarios: AsyncScenariosResource) -> None:
        self._scenarios = scenarios

        self.create = async_to_raw_response_wrapper(
            scenarios.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            scenarios.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            scenarios.update,
        )
        self.list = async_to_raw_response_wrapper(
            scenarios.list,
        )
        self.delete = async_to_raw_response_wrapper(
            scenarios.delete,
        )
        self.preview = async_to_raw_response_wrapper(
            scenarios.preview,
        )


class ScenariosResourceWithStreamingResponse:
    def __init__(self, scenarios: ScenariosResource) -> None:
        self._scenarios = scenarios

        self.create = to_streamed_response_wrapper(
            scenarios.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            scenarios.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            scenarios.update,
        )
        self.list = to_streamed_response_wrapper(
            scenarios.list,
        )
        self.delete = to_streamed_response_wrapper(
            scenarios.delete,
        )
        self.preview = to_streamed_response_wrapper(
            scenarios.preview,
        )


class AsyncScenariosResourceWithStreamingResponse:
    def __init__(self, scenarios: AsyncScenariosResource) -> None:
        self._scenarios = scenarios

        self.create = async_to_streamed_response_wrapper(
            scenarios.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            scenarios.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            scenarios.update,
        )
        self.list = async_to_streamed_response_wrapper(
            scenarios.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            scenarios.delete,
        )
        self.preview = async_to_streamed_response_wrapper(
            scenarios.preview,
        )
