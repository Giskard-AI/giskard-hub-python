from __future__ import annotations

from typing import Dict, List, Iterable, Optional, cast

import httpx

from ..types import AgentOutput
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
from ..types.chat import HeaderParam, ChatMessageParam
from ..types.agent import (
    Agent,
    AgentListParams,
    AgentCreateParams,
    AgentUpdateParams,
    AgentBulkDeleteParams,
    AgentTestConnectionParams,
    AgentGenerateCompletionParams,
    AgentAutofillDescriptionParams,
)
from .._base_client import make_request_options
from ..types.common import APIResponse

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        project_id: str,
        supported_languages: SequenceNotStr[str],
        url: str,
        headers: Dict[str, str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """Create a new agent in the specified project.

        Parameters
        ----------
        name : str
            Name of the agent.
        project_id : str
            Project ID to create the agent in.
        supported_languages : SequenceNotStr[str]
            Supported languages for the agent.
        url : str
            URL endpoint of the agent.
        headers : Dict[str, str] | Omit
            HTTP headers to include when calling the agent.
        description : str | None | Omit
            Human-readable description of the agent.

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
        Agent
            The newly created agent.
        """
        headers_api: list[HeaderParam] = []

        if headers is not omit:
            headers_api = [
                HeaderParam(name=header_name, value=header_value)
                for header_name, header_value in cast(Dict[str, str], headers).items()
            ]

        response = self._post(
            "/v2/agents",
            body=maybe_transform(
                {
                    "name": name,
                    "headers": headers_api,
                    "project_id": project_id,
                    "supported_languages": supported_languages,
                    "url": url,
                    "description": description,
                },
                AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Agent],
        )

        return self._unwrap(response)

    def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """Retrieve an agent by its ID.

        Parameters
        ----------
        agent_id : str
            ID of the agent to retrieve.

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
        Agent
            The requested agent.

        Raises
        ------
        ValueError
            If ``agent_id`` is empty.
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        response = self._get(
            f"/v2/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Agent],
        )

        return self._unwrap(response)

    def update(
        self,
        agent_id: str,
        *,
        description: Optional[str] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        supported_languages: Optional[SequenceNotStr[str]] | Omit = omit,
        url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """Update an existing agent's configuration.

        Parameters
        ----------
        agent_id : str
            ID of the agent to update.
        description : str | None | Omit
            Updated description of the agent.
        headers : Dict[str, str] | Omit
            Updated HTTP headers for agent calls.
        name : str | None | Omit
            Updated name of the agent.
        supported_languages : SequenceNotStr[str] | None | Omit
            Updated supported languages.
        url : str | None | Omit
            Updated URL endpoint of the agent.

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
        Agent
            The updated agent.

        Raises
        ------
        ValueError
            If ``agent_id`` is empty.
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")

        headers_api: list[HeaderParam] | Omit
        if headers is omit:
            headers_api = omit
        else:
            headers_api = [
                HeaderParam(name=header_name, value=header_value)
                for header_name, header_value in cast(Dict[str, str], headers).items()
            ]

        response = self._patch(
            f"/v2/agents/{agent_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "headers": headers_api,
                    "name": name,
                    "supported_languages": supported_languages,
                    "url": url,
                },
                AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Agent],
        )

        return self._unwrap(response)

    def list(
        self,
        *,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[Agent]:
        """List all agents, optionally filtered by project.

        Parameters
        ----------
        project_id : str | None | Omit
            Project ID to filter agents by.

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
        list[Agent]
            List of agents matching the criteria.
        """
        response = self._get(
            "/v2/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, AgentListParams),
            ),
            cast_to=APIResponse[List[Agent]],
        )

        return self._unwrap(response)

    def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete an agent by its ID.

        Parameters
        ----------
        agent_id : str
            ID of the agent to delete.

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
            If ``agent_id`` is empty.
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        response = self._delete(
            f"/v2/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    def bulk_delete(
        self,
        *,
        agent_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete multiple agents at once.

        Parameters
        ----------
        agent_ids : SequenceNotStr[str]
            IDs of the agents to delete.

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
            "/v2/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"agent_ids": agent_ids}, AgentBulkDeleteParams),
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    def generate_completion(
        self,
        agent_id: str,
        *,
        messages: Iterable[ChatMessageParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentOutput:
        """Send a chat conversation to the agent and get a completion response.

        Parameters
        ----------
        agent_id : str
            ID of the agent to generate a completion from.
        messages : Iterable[ChatMessageParam]
            Conversation messages to send to the agent.

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
        AgentOutput
            The agent's completion response.

        Raises
        ------
        ValueError
            If ``agent_id`` is empty.
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        response = self._post(
            f"/v2/agents/{agent_id}/generate-completion",
            body=maybe_transform({"messages": messages}, AgentGenerateCompletionParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[AgentOutput],
        )

        return self._unwrap(response)

    def test_connection(
        self,
        *,
        url: str,
        headers: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentOutput:
        """Test the connection to an agent endpoint without persisting it.

        Parameters
        ----------
        url : str
            URL endpoint to test the connection to.
        headers : Dict[str, str] | Omit
            HTTP headers to include in the test request.

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
        AgentOutput
            The agent's test response.
        """
        response = self._post(
            "/v2/agents/test-connection",
            body=maybe_transform(
                {
                    "url": url,
                    "headers": headers,
                },
                AgentTestConnectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[AgentOutput],
        )

        return self._unwrap(response)

    def generate_description(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Auto-generate a description for an agent by probing its capabilities.

        Discovers the agent's tone, features, goals, and constraints, then
        formats the findings into a human-readable description.

        Parameters
        ----------
        agent_id : str
            ID of the agent to generate a description for.

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
        str
            The generated agent description.

        Raises
        ------
        ValueError
            If ``agent_id`` is empty.
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        response = self._post(
            f"/v2/agents/{agent_id}/autofill-description",
            body=maybe_transform({}, AgentAutofillDescriptionParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[str],
        )

        return self._unwrap(response)


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        project_id: str,
        supported_languages: SequenceNotStr[str],
        url: str,
        headers: Dict[str, str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """Create a new agent in the specified project.

        Parameters
        ----------
        name : str
            Name of the agent.
        project_id : str
            Project ID to create the agent in.
        supported_languages : SequenceNotStr[str]
            Supported languages for the agent.
        url : str
            URL endpoint of the agent.
        headers : Dict[str, str] | Omit
            HTTP headers to include when calling the agent.
        description : str | None | Omit
            Human-readable description of the agent.

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
        Agent
            The newly created agent.
        """
        headers_api: list[HeaderParam] = []

        if headers is not omit:
            headers_api = [
                HeaderParam(name=header_name, value=header_value)
                for header_name, header_value in cast(Dict[str, str], headers).items()
            ]

        response = await self._post(
            "/v2/agents",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "headers": headers_api,
                    "project_id": project_id,
                    "supported_languages": supported_languages,
                    "url": url,
                    "description": description,
                },
                AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Agent],
        )

        return self._unwrap(response)

    async def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """Retrieve an agent by its ID.

        Parameters
        ----------
        agent_id : str
            ID of the agent to retrieve.

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
        Agent
            The requested agent.

        Raises
        ------
        ValueError
            If ``agent_id`` is empty.
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        response = await self._get(
            f"/v2/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Agent],
        )

        return self._unwrap(response)

    async def update(
        self,
        agent_id: str,
        *,
        description: Optional[str] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        supported_languages: Optional[SequenceNotStr[str]] | Omit = omit,
        url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """Update an existing agent's configuration.

        Parameters
        ----------
        agent_id : str
            ID of the agent to update.
        description : str | None | Omit
            Updated description of the agent.
        headers : Dict[str, str] | Omit
            Updated HTTP headers for agent calls.
        name : str | None | Omit
            Updated name of the agent.
        supported_languages : SequenceNotStr[str] | None | Omit
            Updated supported languages.
        url : str | None | Omit
            Updated URL endpoint of the agent.

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
        Agent
            The updated agent.

        Raises
        ------
        ValueError
            If ``agent_id`` is empty.
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")

        headers_api: list[HeaderParam] | Omit
        if headers is omit:
            headers_api = omit
        else:
            headers_api = [
                HeaderParam(name=header_name, value=header_value)
                for header_name, header_value in cast(Dict[str, str], headers).items()
            ]

        response = await self._patch(
            f"/v2/agents/{agent_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "headers": headers_api,
                    "name": name,
                    "supported_languages": supported_languages,
                    "url": url,
                },
                AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Agent],
        )

        return self._unwrap(response)

    async def list(
        self,
        *,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[Agent]:
        """List all agents, optionally filtered by project.

        Parameters
        ----------
        project_id : str | None | Omit
            Project ID to filter agents by.

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
        list[Agent]
            List of agents matching the criteria.
        """
        response = await self._get(
            "/v2/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"project_id": project_id}, AgentListParams),
            ),
            cast_to=APIResponse[List[Agent]],
        )

        return self._unwrap(response)

    async def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete an agent by its ID.

        Parameters
        ----------
        agent_id : str
            ID of the agent to delete.

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
            If ``agent_id`` is empty.
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        response = await self._delete(
            f"/v2/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    async def bulk_delete(
        self,
        *,
        agent_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete multiple agents at once.

        Parameters
        ----------
        agent_ids : SequenceNotStr[str]
            IDs of the agents to delete.

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
            "/v2/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"agent_ids": agent_ids}, AgentBulkDeleteParams),
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    async def generate_completion(
        self,
        agent_id: str,
        *,
        messages: Iterable[ChatMessageParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentOutput:
        """Send a chat conversation to the agent and get a completion response.

        Parameters
        ----------
        agent_id : str
            ID of the agent to generate a completion from.
        messages : Iterable[ChatMessageParam]
            Conversation messages to send to the agent.

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
        AgentOutput
            The agent's completion response.

        Raises
        ------
        ValueError
            If ``agent_id`` is empty.
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        response = await self._post(
            f"/v2/agents/{agent_id}/generate-completion",
            body=await async_maybe_transform({"messages": messages}, AgentGenerateCompletionParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[AgentOutput],
        )

        return self._unwrap(response)

    async def test_connection(
        self,
        *,
        url: str,
        headers: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentOutput:
        """Test the connection to an agent endpoint without persisting it.

        Parameters
        ----------
        url : str
            URL endpoint to test the connection to.
        headers : Dict[str, str] | Omit
            HTTP headers to include in the test request.

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
        AgentOutput
            The agent's test response.
        """
        response = await self._post(
            "/v2/agents/test-connection",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "headers": headers,
                },
                AgentTestConnectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[AgentOutput],
        )

        return self._unwrap(response)

    async def generate_description(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Auto-generate a description for an agent by probing its capabilities.

        Discovers the agent's tone, features, goals, and constraints, then
        formats the findings into a human-readable description.

        Parameters
        ----------
        agent_id : str
            ID of the agent to generate a description for.

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
        str
            The generated agent description.

        Raises
        ------
        ValueError
            If ``agent_id`` is empty.
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        response = await self._post(
            f"/v2/agents/{agent_id}/autofill-description",
            body=await async_maybe_transform({}, AgentAutofillDescriptionParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[str],
        )

        return self._unwrap(response)


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = to_raw_response_wrapper(
            agents.update,
        )
        self.list = to_raw_response_wrapper(
            agents.list,
        )
        self.delete = to_raw_response_wrapper(
            agents.delete,
        )
        self.bulk_delete = to_raw_response_wrapper(
            agents.bulk_delete,
        )
        self.generate_completion = to_raw_response_wrapper(
            agents.generate_completion,
        )
        self.test_connection = to_raw_response_wrapper(
            agents.test_connection,
        )
        self.generate_description = to_raw_response_wrapper(
            agents.generate_description,
        )


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            agents.update,
        )
        self.list = async_to_raw_response_wrapper(
            agents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            agents.delete,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            agents.bulk_delete,
        )
        self.generate_completion = async_to_raw_response_wrapper(
            agents.generate_completion,
        )
        self.test_connection = async_to_raw_response_wrapper(
            agents.test_connection,
        )
        self.generate_description = async_to_raw_response_wrapper(
            agents.generate_description,
        )


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            agents.update,
        )
        self.list = to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = to_streamed_response_wrapper(
            agents.delete,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            agents.bulk_delete,
        )
        self.generate_completion = to_streamed_response_wrapper(
            agents.generate_completion,
        )
        self.test_connection = to_streamed_response_wrapper(
            agents.test_connection,
        )
        self.generate_description = to_streamed_response_wrapper(
            agents.generate_description,
        )


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            agents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            agents.delete,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            agents.bulk_delete,
        )
        self.generate_completion = async_to_streamed_response_wrapper(
            agents.generate_completion,
        )
        self.test_connection = async_to_streamed_response_wrapper(
            agents.test_connection,
        )
        self.generate_description = async_to_streamed_response_wrapper(
            agents.generate_description,
        )
