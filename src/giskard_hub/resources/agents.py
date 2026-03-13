from __future__ import annotations

from typing import Dict, List, Iterable, Optional

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
        headers: Iterable[HeaderParam],
        name: str,
        project_id: str,
        supported_languages: SequenceNotStr[str],
        url: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """
        Create Agent

        Args:
          headers: Headers to use for the agent

          name: Name of the agent

          project_id: Project ID to use for the agent

          supported_languages: Supported languages for the agent

          url: URL of the agent

          description: Description of the agent

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        response = self._post(
            "/v2/agents",
            body=maybe_transform(
                {
                    "headers": headers,
                    "name": name,
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

        return response.data

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
        """
        Retrieve Agent

        Args:
          agent_id: Agent ID to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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

        return response.data

    def update(
        self,
        agent_id: str,
        *,
        description: Optional[str] | Omit = omit,
        headers: Optional[Iterable[HeaderParam]] | Omit = omit,
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
        """
        Update Agent

        Args:
          agent_id: Agent ID to update

          description: Description of the agent

          headers: Headers to use for the agent

          name: Name of the agent

          supported_languages: Supported languages for the agent

          url: URL of the agent

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        response = self._patch(
            f"/v2/agents/{agent_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "headers": headers,
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

        return response.data

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
        """
        List Agents

        Args:
          project_id: Project ID to list agents for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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

        return response.data

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
        """
        Delete Agent

        Args:
          agent_id: Agent ID to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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

        return response.data

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
        """
        Bulk Delete Agents

        Args:
          agent_ids: Agent IDs to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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

        return response.data

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
        """
        Generate Agent Completion

        Args:
          agent_id: Agent ID to generate completion for

          messages: Messages to generate completion for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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

        return response.data

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
        """
        Test Agent Connection

        Args:
          url: URL to test the connection for

          headers: Headers to use for the connection test

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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

        return response.data

    def autofill_description(
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
        """
        Autofill Agent Description

        Args:
          agent_id: Agent ID to autofill description for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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

        return response.data


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
        headers: Iterable[HeaderParam],
        name: str,
        project_id: str,
        supported_languages: SequenceNotStr[str],
        url: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """
        Create Agent

        Args:
          headers: Headers to use for the agent

          name: Name of the agent

          project_id: Project ID to use for the agent

          supported_languages: Supported languages for the agent

          url: URL of the agent

          description: Description of the agent

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        response = await self._post(
            "/v2/agents",
            body=await async_maybe_transform(
                {
                    "headers": headers,
                    "name": name,
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

        return response.data

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
        """
        Retrieve Agent

        Args:
          agent_id: Agent ID to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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

        return response.data

    async def update(
        self,
        agent_id: str,
        *,
        description: Optional[str] | Omit = omit,
        headers: Optional[Iterable[HeaderParam]] | Omit = omit,
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
        """
        Update Agent

        Args:
          agent_id: Agent ID to update

          description: Description of the agent

          headers: Headers to use for the agent

          name: Name of the agent

          supported_languages: Supported languages for the agent

          url: URL of the agent

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        response = await self._patch(
            f"/v2/agents/{agent_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "headers": headers,
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

        return response.data

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
        """
        List Agents

        Args:
          project_id: Project ID to list agents for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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

        return response.data

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
        """
        Delete Agent

        Args:
          agent_id: Agent ID to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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

        return response.data

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
        """
        Bulk Delete Agents

        Args:
          agent_ids: Agent IDs to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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

        return response.data

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
        """
        Generate Agent Completion

        Args:
          agent_id: Agent ID to generate completion for

          messages: Messages to generate completion for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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

        return response.data

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
        """
        Test Agent Connection

        Args:
          url: URL to test the connection for

          headers: Headers to use for the connection test

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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

        return response.data

    async def autofill_description(
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
        """
        Autofill Agent Description

        Args:
          agent_id: Agent ID to autofill description for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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

        return response.data


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
        self.autofill_description = to_raw_response_wrapper(
            agents.autofill_description,
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
        self.autofill_description = async_to_raw_response_wrapper(
            agents.autofill_description,
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
        self.autofill_description = to_streamed_response_wrapper(
            agents.autofill_description,
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
        self.autofill_description = async_to_streamed_response_wrapper(
            agents.autofill_description,
        )
