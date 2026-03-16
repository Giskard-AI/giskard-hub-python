from __future__ import annotations

from typing import List, Optional

import httpx

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
from ...types.common import APIResponse
from ...types.scenario import (
    Scenario,
    ScenarioPreview,
    ScenarioCreateParams,
    ScenarioUpdateParams,
    ScenarioPreviewParams,
)

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
        description: str,
        rules: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Scenario:
        """Create a new scenario within a project.

        Parameters
        ----------
        project_id : str
            The ID of the project.
        name : str
            The name of the scenario.
        description : str
            The description of the scenario.
        rules : SequenceNotStr[str]
            The rules of the scenario.

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
        Scenario
            The newly created scenario.

        Raises
        ------
        ValueError
            If ``project_id`` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        response = self._post(
            f"/v2/projects/{project_id}/scenarios",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "rules": rules,
                },
                ScenarioCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Scenario],
        )

        return self._unwrap(response)

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
    ) -> Scenario:
        """Retrieve a scenario by its ID within a project.

        Parameters
        ----------
        scenario_id : str
            The ID of the scenario.
        project_id : str
            The ID of the project.

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
        Scenario
            The requested scenario.

        Raises
        ------
        ValueError
            If ``project_id`` or ``scenario_id`` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")
        response = self._get(
            f"/v2/projects/{project_id}/scenarios/{scenario_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Scenario],
        )

        return self._unwrap(response)

    def update(
        self,
        scenario_id: str,
        *,
        project_id: str,
        name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        rules: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Scenario:
        """Update an existing scenario's definition.

        Parameters
        ----------
        scenario_id : str
            The ID of the scenario.
        project_id : str
            The ID of the project.
        name : str or None
            Name of the scenario.
        description : str or None
            Description of the scenario.
        rules : SequenceNotStr[str] or None
            The rules of the scenario.

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
        Scenario
            The updated scenario.

        Raises
        ------
        ValueError
            If ``project_id`` or ``scenario_id`` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")
        response = self._patch(
            f"/v2/projects/{project_id}/scenarios/{scenario_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "rules": rules,
                },
                ScenarioUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Scenario],
        )

        return self._unwrap(response)

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
    ) -> List[Scenario]:
        """List all scenarios for a project.

        Parameters
        ----------
        project_id : str
            The ID of the project.

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
        list of Scenario
            A list of all scenarios for the project.

        Raises
        ------
        ValueError
            If ``project_id`` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        response = self._get(
            f"/v2/projects/{project_id}/scenarios",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[Scenario]],
        )

        return self._unwrap(response)

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
    ) -> None:
        """Delete a scenario from a project.

        Parameters
        ----------
        scenario_id : str
            The ID of the scenario.
        project_id : str
            The ID of the project.

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
            If ``project_id`` or ``scenario_id`` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")
        response = self._delete(
            f"/v2/projects/{project_id}/scenarios/{scenario_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    def preview(
        self,
        project_id: str,
        *,
        agent_id: Optional[str] | Omit = omit,
        description: str,
        rules: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScenarioPreview:
        """Generate a preview conversation for a scenario without persisting it.

        Parameters
        ----------
        project_id : str
            The ID of the project.
        agent_id : str or None
            Agent ID to use for preview.
        description : str
            Description of the scenario.
        rules : SequenceNotStr[str]
            Rules to use for preview.

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
        ScenarioPreview
            The generated preview conversation.

        Raises
        ------
        ValueError
            If ``project_id`` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        response = self._post(
            f"/v2/projects/{project_id}/scenarios/preview",
            body=maybe_transform(
                {
                    "description": description,
                    "rules": rules,
                },
                ScenarioPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"agent_id": agent_id}, ScenarioPreviewParams),
            ),
            cast_to=APIResponse[ScenarioPreview],
        )

        return self._unwrap(response)


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
        description: str,
        rules: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Scenario:
        """Create a new scenario within a project.

        Parameters
        ----------
        project_id : str
            The ID of the project.
        name : str
            The name of the scenario.
        description : str
            The description of the scenario.
        rules : SequenceNotStr[str]
            The rules of the scenario.

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
        Scenario
            The newly created scenario.

        Raises
        ------
        ValueError
            If ``project_id`` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        response = await self._post(
            f"/v2/projects/{project_id}/scenarios",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "rules": rules,
                },
                ScenarioCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Scenario],
        )

        return self._unwrap(response)

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
    ) -> Scenario:
        """Retrieve a scenario by its ID within a project.

        Parameters
        ----------
        scenario_id : str
            The ID of the scenario.
        project_id : str
            The ID of the project.

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
        Scenario
            The requested scenario.

        Raises
        ------
        ValueError
            If ``project_id`` or ``scenario_id`` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")
        response = await self._get(
            f"/v2/projects/{project_id}/scenarios/{scenario_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Scenario],
        )

        return self._unwrap(response)

    async def update(
        self,
        scenario_id: str,
        *,
        project_id: str,
        name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        rules: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Scenario:
        """Update an existing scenario's definition.

        Parameters
        ----------
        scenario_id : str
            The ID of the scenario.
        project_id : str
            The ID of the project.
        name : str or None
            Name of the scenario.
        description : str or None
            Description of the scenario.
        rules : SequenceNotStr[str] or None
            The rules of the scenario.

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
        Scenario
            The updated scenario.

        Raises
        ------
        ValueError
            If ``project_id`` or ``scenario_id`` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")
        response = await self._patch(
            f"/v2/projects/{project_id}/scenarios/{scenario_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "rules": rules,
                },
                ScenarioUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Scenario],
        )

        return self._unwrap(response)

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
    ) -> List[Scenario]:
        """List all scenarios for a project.

        Parameters
        ----------
        project_id : str
            The ID of the project.

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
        list of Scenario
            A list of all scenarios for the project.

        Raises
        ------
        ValueError
            If ``project_id`` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        response = await self._get(
            f"/v2/projects/{project_id}/scenarios",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[Scenario]],
        )

        return self._unwrap(response)

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
    ) -> None:
        """Delete a scenario from a project.

        Parameters
        ----------
        scenario_id : str
            The ID of the scenario.
        project_id : str
            The ID of the project.

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
            If ``project_id`` or ``scenario_id`` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")
        response = await self._delete(
            f"/v2/projects/{project_id}/scenarios/{scenario_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    async def preview(
        self,
        project_id: str,
        *,
        agent_id: Optional[str] | Omit = omit,
        description: str,
        rules: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScenarioPreview:
        """Generate a preview conversation for a scenario without persisting it.

        Parameters
        ----------
        project_id : str
            The ID of the project.
        agent_id : str or None
            Agent ID to use for preview.
        description : str
            Description of the scenario.
        rules : SequenceNotStr[str]
            Rules to use for preview.

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
        ScenarioPreview
            The generated preview conversation.

        Raises
        ------
        ValueError
            If ``project_id`` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        response = await self._post(
            f"/v2/projects/{project_id}/scenarios/preview",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "rules": rules,
                },
                ScenarioPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"agent_id": agent_id}, ScenarioPreviewParams),
            ),
            cast_to=APIResponse[ScenarioPreview],
        )

        return self._unwrap(response)


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
