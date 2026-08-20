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
from ...types.prompt_preset import (
    PromptPreset,
    PromptPresetPreview,
    PromptPresetCreateParams,
    PromptPresetUpdateParams,
    PromptPresetPreviewParams,
)

__all__ = ["PromptPresetsResource", "AsyncPromptPresetsResource"]


class PromptPresetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromptPresetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return PromptPresetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptPresetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return PromptPresetsResourceWithStreamingResponse(self)

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
    ) -> PromptPreset:
        """Create a new prompt preset within a project.

        Parameters
        ----------
        project_id : str
            The ID of the project.
        name : str
            The name of the prompt preset.
        description : str
            The description of the prompt preset.
        rules : SequenceNotStr[str]
            The rules of the prompt preset.

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
        PromptPreset
            The newly created prompt preset.

        Raises
        ------
        ValueError
            If `project_id` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        response = self._post(
            f"/v2/projects/{project_id}/prompt-presets",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "rules": rules,
                },
                PromptPresetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[PromptPreset],
        )

        return self._unwrap(response)

    def retrieve(
        self,
        prompt_preset_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptPreset:
        """Retrieve a prompt preset by its ID within a project.

        Parameters
        ----------
        prompt_preset_id : str
            The ID of the prompt preset.
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
        PromptPreset
            The requested prompt preset.

        Raises
        ------
        ValueError
            If `project_id` or `prompt_preset_id` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not prompt_preset_id:
            raise ValueError(f"Expected a non-empty value for `prompt_preset_id` but received {prompt_preset_id!r}")
        response = self._get(
            f"/v2/projects/{project_id}/prompt-presets/{prompt_preset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[PromptPreset],
        )

        return self._unwrap(response)

    def update(
        self,
        prompt_preset_id: str,
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
    ) -> PromptPreset:
        """Update an existing prompt preset's definition.

        Parameters
        ----------
        prompt_preset_id : str
            The ID of the prompt preset.
        project_id : str
            The ID of the project.
        name : str or None
            Name of the prompt preset.
        description : str or None
            Description of the prompt preset.
        rules : SequenceNotStr[str] or None
            The rules of the prompt preset.

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
        PromptPreset
            The updated prompt preset.

        Raises
        ------
        ValueError
            If `project_id` or `prompt_preset_id` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not prompt_preset_id:
            raise ValueError(f"Expected a non-empty value for `prompt_preset_id` but received {prompt_preset_id!r}")
        response = self._patch(
            f"/v2/projects/{project_id}/prompt-presets/{prompt_preset_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "rules": rules,
                },
                PromptPresetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[PromptPreset],
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
    ) -> List[PromptPreset]:
        """List all prompt presets for a project.

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
        list of PromptPreset
            A list of all prompt presets for the project.

        Raises
        ------
        ValueError
            If `project_id` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        response = self._get(
            f"/v2/projects/{project_id}/prompt-presets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[PromptPreset]],
        )

        return self._unwrap(response)

    def delete(
        self,
        prompt_preset_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a prompt preset from a project.

        Parameters
        ----------
        prompt_preset_id : str
            The ID of the prompt preset.
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
            If `project_id` or `prompt_preset_id` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not prompt_preset_id:
            raise ValueError(f"Expected a non-empty value for `prompt_preset_id` but received {prompt_preset_id!r}")
        response = self._delete(
            f"/v2/projects/{project_id}/prompt-presets/{prompt_preset_id}",
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
        description: str,
        rules: SequenceNotStr[str] | Omit = omit,
        agent_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptPresetPreview:
        """Generate a preview conversation for a prompt preset without persisting it.

        Parameters
        ----------
        project_id : str
            The ID of the project.
        description : str
            Description of the prompt preset.
        rules : SequenceNotStr[str]
            Rules to use for preview.
        agent_id : str or None
            Agent ID to use for preview.

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
        PromptPresetPreview
            The generated preview conversation.

        Raises
        ------
        ValueError
            If `project_id` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        response = self._post(
            f"/v2/projects/{project_id}/prompt-presets/preview",
            body=maybe_transform(
                {
                    "description": description,
                    "rules": rules,
                },
                PromptPresetPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"agent_id": agent_id}, PromptPresetPreviewParams),
            ),
            cast_to=APIResponse[PromptPresetPreview],
        )

        return self._unwrap(response)


class AsyncPromptPresetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromptPresetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPromptPresetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptPresetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncPromptPresetsResourceWithStreamingResponse(self)

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
    ) -> PromptPreset:
        """Create a new prompt preset within a project.

        Parameters
        ----------
        project_id : str
            The ID of the project.
        name : str
            The name of the prompt preset.
        description : str
            The description of the prompt preset.
        rules : SequenceNotStr[str]
            The rules of the prompt preset.

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
        PromptPreset
            The newly created prompt preset.

        Raises
        ------
        ValueError
            If `project_id` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        response = await self._post(
            f"/v2/projects/{project_id}/prompt-presets",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "rules": rules,
                },
                PromptPresetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[PromptPreset],
        )

        return self._unwrap(response)

    async def retrieve(
        self,
        prompt_preset_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptPreset:
        """Retrieve a prompt preset by its ID within a project.

        Parameters
        ----------
        prompt_preset_id : str
            The ID of the prompt preset.
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
        PromptPreset
            The requested prompt preset.

        Raises
        ------
        ValueError
            If `project_id` or `prompt_preset_id` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not prompt_preset_id:
            raise ValueError(f"Expected a non-empty value for `prompt_preset_id` but received {prompt_preset_id!r}")
        response = await self._get(
            f"/v2/projects/{project_id}/prompt-presets/{prompt_preset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[PromptPreset],
        )

        return self._unwrap(response)

    async def update(
        self,
        prompt_preset_id: str,
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
    ) -> PromptPreset:
        """Update an existing prompt preset's definition.

        Parameters
        ----------
        prompt_preset_id : str
            The ID of the prompt preset.
        project_id : str
            The ID of the project.
        name : str or None
            Name of the prompt preset.
        description : str or None
            Description of the prompt preset.
        rules : SequenceNotStr[str] or None
            The rules of the prompt preset.

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
        PromptPreset
            The updated prompt preset.

        Raises
        ------
        ValueError
            If `project_id` or `prompt_preset_id` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not prompt_preset_id:
            raise ValueError(f"Expected a non-empty value for `prompt_preset_id` but received {prompt_preset_id!r}")
        response = await self._patch(
            f"/v2/projects/{project_id}/prompt-presets/{prompt_preset_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "rules": rules,
                },
                PromptPresetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[PromptPreset],
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
    ) -> List[PromptPreset]:
        """List all prompt presets for a project.

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
        list of PromptPreset
            A list of all prompt presets for the project.

        Raises
        ------
        ValueError
            If `project_id` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        response = await self._get(
            f"/v2/projects/{project_id}/prompt-presets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[PromptPreset]],
        )

        return self._unwrap(response)

    async def delete(
        self,
        prompt_preset_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a prompt preset from a project.

        Parameters
        ----------
        prompt_preset_id : str
            The ID of the prompt preset.
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
            If `project_id` or `prompt_preset_id` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not prompt_preset_id:
            raise ValueError(f"Expected a non-empty value for `prompt_preset_id` but received {prompt_preset_id!r}")
        response = await self._delete(
            f"/v2/projects/{project_id}/prompt-presets/{prompt_preset_id}",
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
        description: str,
        rules: SequenceNotStr[str] | Omit = omit,
        agent_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromptPresetPreview:
        """Generate a preview conversation for a prompt preset without persisting it.

        Parameters
        ----------
        project_id : str
            The ID of the project.
        description : str
            Description of the prompt preset.
        rules : SequenceNotStr[str]
            Rules to use for preview.
        agent_id : str or None
            Agent ID to use for preview.

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
        PromptPresetPreview
            The generated preview conversation.

        Raises
        ------
        ValueError
            If `project_id` is empty.
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        response = await self._post(
            f"/v2/projects/{project_id}/prompt-presets/preview",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "rules": rules,
                },
                PromptPresetPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"agent_id": agent_id}, PromptPresetPreviewParams),
            ),
            cast_to=APIResponse[PromptPresetPreview],
        )

        return self._unwrap(response)


class PromptPresetsResourceWithRawResponse:
    def __init__(self, prompt_presets: PromptPresetsResource) -> None:
        self._prompt_presets = prompt_presets

        self.create = to_raw_response_wrapper(
            prompt_presets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            prompt_presets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            prompt_presets.update,
        )
        self.list = to_raw_response_wrapper(
            prompt_presets.list,
        )
        self.delete = to_raw_response_wrapper(
            prompt_presets.delete,
        )
        self.preview = to_raw_response_wrapper(
            prompt_presets.preview,
        )


class AsyncPromptPresetsResourceWithRawResponse:
    def __init__(self, prompt_presets: AsyncPromptPresetsResource) -> None:
        self._prompt_presets = prompt_presets

        self.create = async_to_raw_response_wrapper(
            prompt_presets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            prompt_presets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            prompt_presets.update,
        )
        self.list = async_to_raw_response_wrapper(
            prompt_presets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            prompt_presets.delete,
        )
        self.preview = async_to_raw_response_wrapper(
            prompt_presets.preview,
        )


class PromptPresetsResourceWithStreamingResponse:
    def __init__(self, prompt_presets: PromptPresetsResource) -> None:
        self._prompt_presets = prompt_presets

        self.create = to_streamed_response_wrapper(
            prompt_presets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            prompt_presets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            prompt_presets.update,
        )
        self.list = to_streamed_response_wrapper(
            prompt_presets.list,
        )
        self.delete = to_streamed_response_wrapper(
            prompt_presets.delete,
        )
        self.preview = to_streamed_response_wrapper(
            prompt_presets.preview,
        )


class AsyncPromptPresetsResourceWithStreamingResponse:
    def __init__(self, prompt_presets: AsyncPromptPresetsResource) -> None:
        self._prompt_presets = prompt_presets

        self.create = async_to_streamed_response_wrapper(
            prompt_presets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            prompt_presets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            prompt_presets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            prompt_presets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            prompt_presets.delete,
        )
        self.preview = async_to_streamed_response_wrapper(
            prompt_presets.preview,
        )
