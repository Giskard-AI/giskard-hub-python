from __future__ import annotations

import warnings
from typing import List, Literal, Iterable, Optional, cast

import httpx

from ...types import BulkMoveScenariosParams
from ..._types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    SequenceNotStr,
    omit,
    not_given,
)
from ..._utils import maybe_transform, async_maybe_transform
from .comments import (
    CommentsResource,
    AsyncCommentsResource,
    CommentsResourceWithRawResponse,
    AsyncCommentsResourceWithRawResponse,
    CommentsResourceWithStreamingResponse,
    AsyncCommentsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.chat import ChatMessageParam, ChatMessageWithMetadataParam
from ...types.check import CheckConfigParam, InteractionParam
from ..._base_client import make_request_options
from ...types.common import APIResponse
from ...types.scenario import (
    Scenario,
    ScenarioCreateParams,
    ScenarioUpdateParams,
    ScenarioBulkDeleteParams,
    ScenarioBulkUpdateParams,
)
from .._interaction_helpers import (
    normalize_interactions,
    build_legacy_interaction,
)

__all__ = ["ScenariosResource", "AsyncScenariosResource"]

DemoOutput = ChatMessageWithMetadataParam | str


_LEGACY_SCENARIO_PARAM_NAMES = ("messages", "checks", "demo_output")


def _resolve_interaction_source(
    *,
    method: str,
    require_one: bool,
    interactions: Iterable[InteractionParam] | None | Omit,
    messages: Iterable[ChatMessageParam] | None | Omit,
    checks: Iterable[CheckConfigParam] | None | Omit,
    demo_output: Optional[DemoOutput] | Omit,
) -> Literal["interactions", "legacy", "none"]:
    """Decide whether the call is using the new `interactions=` form, the
    deprecated legacy form, or nothing.

    Raises if both forms are mixed, or if neither is provided when
    `require_one=True` (i.e. on `create`).
    Emits a `DeprecationWarning` when the legacy form is selected.
    """
    using_interactions = not isinstance(interactions, Omit) and interactions is not None
    using_legacy = any(not isinstance(value, Omit) for value in (messages, checks, demo_output))

    if using_interactions and using_legacy:
        raise ValueError(
            "Cannot mix `interactions` with legacy parameters "
            f"({', '.join(repr(n) for n in _LEGACY_SCENARIO_PARAM_NAMES)}). Pick one."
        )
    if require_one and not using_interactions and not using_legacy:
        raise ValueError("Must provide either `interactions=` (recommended) or legacy `messages` (deprecated).")

    if using_legacy:
        warnings.warn(
            f"Passing `messages` / `checks` / `demo_output` to "
            f"`scenarios.{method}` is deprecated. Pass `interactions=[{{...}}]` instead.",
            DeprecationWarning,
            stacklevel=3,
        )
        return "legacy"
    return "interactions" if using_interactions else "none"


class ScenariosResource(SyncAPIResource):
    @cached_property
    def comments(self) -> CommentsResource:
        return CommentsResource(self._client)

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
        *,
        dataset_id: str,
        interactions: Iterable[InteractionParam] | Omit = omit,
        status: Optional[Literal["active", "draft"]] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        source_probe_attempt_id: Optional[str] | Omit = omit,
        messages: Iterable[ChatMessageParam] | Omit = omit,
        checks: Iterable[CheckConfigParam] | Omit = omit,
        demo_output: Optional[DemoOutput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Scenario:
        """Create a new scenario in a dataset.

        Parameters
        ----------
        dataset_id : str
            Dataset ID to create the scenario in.
        interactions : Iterable[InteractionParam] | Omit
            Interactions to attach to the scenario. Each interaction needs a
            structured `input` matching the agent's `input_schema`, and
            optionally an `output` and a `checks` list. `position` defaults to
            the interaction's index in the list when omitted.
        status : Literal["active", "draft"] | None | Omit
            Status of the scenario.
        tags : SequenceNotStr[str] | Omit
            Tags to apply to the scenario.
        source_probe_attempt_id : str | None | Omit
            ID of the scan probe attempt this scenario was created from, if
            any.
        messages : Iterable[ChatMessageParam] | Omit
            (Deprecated) Conversation messages. Translated into a single
            interaction against the dataset's default role with
            `input={"messages": [...]}`.
        checks : Iterable[CheckConfigParam] | Omit
            (Deprecated) Checks attached to the synthesized interaction.
            Each `identifier` is resolved to a `check_id`.
        demo_output : DemoOutput | None | Omit
            (Deprecated) Reference output for the synthesized interaction.

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
        Scenario
            The newly created scenario.

        Raises
        ------
        ValueError
            If `interactions` is mixed with legacy parameters, or if neither
            is provided.
        """
        source = _resolve_interaction_source(
            method="create",
            require_one=True,
            interactions=interactions,
            messages=messages,
            checks=checks,
            demo_output=demo_output,
        )
        if source == "legacy":
            interactions = [
                build_legacy_interaction(
                    messages=messages,
                    demo_output=demo_output,
                    checks=checks,
                )
            ]
        elif source == "interactions":
            interactions = normalize_interactions(cast("Iterable[InteractionParam]", interactions))

        response = self._post(
            "/v2/scenarios",
            body=maybe_transform(
                {
                    "dataset_id": dataset_id,
                    "interactions": interactions,
                    "status": status,
                    "tags": tags,
                    "source_probe_attempt_id": source_probe_attempt_id,
                },
                ScenarioCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponse[Scenario],
        )

        return self._unwrap(response)

    def retrieve(
        self,
        scenario_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Scenario:
        """
        Retrieve a scenario by its ID.

        Parameters
        ----------
        scenario_id : str
            Scenario ID to retrieve.

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
        Scenario
            The retrieved scenario.

        Raises
        ------
        ValueError
            If `scenario_id` is empty.
        """
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")
        response = self._get(
            f"/v2/scenarios/{scenario_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponse[Scenario],
        )

        return self._unwrap(response)

    def update(
        self,
        scenario_id: str,
        *,
        interactions: Optional[Iterable[InteractionParam]] | Omit = omit,
        dataset_id: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        status: Optional[Literal["active", "draft"]] | Omit = omit,
        messages: Optional[Iterable[ChatMessageParam]] | Omit = omit,
        checks: Optional[Iterable[CheckConfigParam]] | Omit = omit,
        demo_output: Optional[DemoOutput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Scenario:
        """Update an existing scenario.

        Parameters
        ----------
        scenario_id : str
            Scenario ID to update.
        interactions : Iterable[InteractionParam] | None | Omit
            Replace the scenario's interactions.
        dataset_id : str | None | Omit
            Move the scenario to this dataset.
        tags : SequenceNotStr[str] | None | Omit
            Tags to set on the scenario.
        status : Literal["active", "draft"] | None | Omit
            New status of the scenario.
        messages : Iterable[ChatMessageParam] | None | Omit
            (Deprecated) Conversation messages. Translated into a single
            interaction against the dataset's default role with
            `input={"messages": [...]}`.
        checks : Iterable[CheckConfigParam] | None | Omit
            (Deprecated) Checks attached to the synthesized interaction.
            Each `identifier` is resolved to a `check_id`.
        demo_output : DemoOutput | None | Omit
            (Deprecated) Reference output for the synthesized interaction.

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
        Scenario
            The updated scenario.

        Raises
        ------
        ValueError
            If `scenario_id` is empty, or if `interactions` is mixed with
            legacy parameters.
        """
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")

        source = _resolve_interaction_source(
            method="update",
            require_one=False,
            interactions=interactions,
            messages=messages,
            checks=checks,
            demo_output=demo_output,
        )
        if source == "legacy":
            interactions = [
                build_legacy_interaction(
                    messages=messages,
                    demo_output=demo_output,
                    checks=checks,
                )
            ]
        elif source == "interactions":
            interactions = normalize_interactions(cast("Iterable[InteractionParam]", interactions))

        response = self._patch(
            f"/v2/scenarios/{scenario_id}",
            body=maybe_transform(
                {
                    "dataset_id": dataset_id,
                    "interactions": interactions,
                    "tags": tags,
                    "status": status,
                },
                ScenarioUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponse[Scenario],
        )

        return self._unwrap(response)

    def delete(
        self,
        scenario_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a scenario by its ID.

        Parameters
        ----------
        scenario_id : str
            Scenario ID to delete.

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
        None

        Raises
        ------
        ValueError
            If `scenario_id` is empty.
        """
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")
        response = self._delete(
            f"/v2/scenarios/{scenario_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    def bulk_delete(
        self,
        *,
        scenario_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete multiple scenarios at once.

        Parameters
        ----------
        scenario_ids : SequenceNotStr[str]
            Scenario IDs to delete.

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
        None
        """
        response = self._delete(
            "/v2/scenarios",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"scenario_ids": scenario_ids}, ScenarioBulkDeleteParams),
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    def bulk_update(
        self,
        *,
        scenario_ids: SequenceNotStr[str],
        disabled_checks: Optional[SequenceNotStr[str]] | Omit = omit,
        enabled_checks: Optional[SequenceNotStr[str]] | Omit = omit,
        added_tags: Optional[SequenceNotStr[str]] | Omit = omit,
        removed_tags: Optional[SequenceNotStr[str]] | Omit = omit,
        status: Optional[Literal["active", "draft"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[Scenario]:
        """
        Bulk update multiple scenarios' checks, tags, or status.

        Parameters
        ----------
        scenario_ids : SequenceNotStr[str]
            Scenario IDs to update.
        disabled_checks : Optional[SequenceNotStr[str]] | Omit
            Partial list of checks to be disabled.
        enabled_checks : Optional[SequenceNotStr[str]] | Omit
            Partial list of checks to be enabled.
        added_tags : Optional[SequenceNotStr[str]] | Omit
            Tags to be added to the scenarios.
        removed_tags : Optional[SequenceNotStr[str]] | Omit
            Tags to be removed from the scenarios.
        status : Optional[Literal["active", "draft"]] | Omit
            Status of the scenarios.

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
        List[Scenario]
            The updated scenarios.
        """
        response = self._patch(
            "/v2/scenarios",
            body=maybe_transform(
                {
                    "ids": scenario_ids,
                    "disabled_checks": disabled_checks,
                    "enabled_checks": enabled_checks,
                    "added_tags": added_tags,
                    "removed_tags": removed_tags,
                    "status": status,
                },
                ScenarioBulkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponse[List[Scenario]],
        )

        return self._unwrap(response)

    def bulk_move(
        self,
        *,
        scenario_ids: List[str],
        target_dataset_id: str,
        duplicate: Optional[bool] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Move or copy scenarios between datasets.

        Parameters
        ----------
        scenario_ids : List[str]
            List of scenario IDs to move.
        target_dataset_id : str
            Target dataset ID to move scenarios to.
        duplicate : Optional[bool] | Omit
            If true, keep a copy of the scenarios in the original dataset. Default is true.

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
        None
        """
        response = self._post(
            "/v2/scenarios/bulk-move",
            body=maybe_transform(
                {
                    "scenario_ids": scenario_ids,
                    "dataset_id": target_dataset_id,
                    "duplicate": duplicate,
                },
                BulkMoveScenariosParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)


class AsyncScenariosResource(AsyncAPIResource):
    @cached_property
    def comments(self) -> AsyncCommentsResource:
        return AsyncCommentsResource(self._client)

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
        *,
        dataset_id: str,
        interactions: Iterable[InteractionParam] | Omit = omit,
        status: Optional[Literal["active", "draft"]] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        source_probe_attempt_id: Optional[str] | Omit = omit,
        messages: Iterable[ChatMessageParam] | Omit = omit,
        checks: Iterable[CheckConfigParam] | Omit = omit,
        demo_output: Optional[DemoOutput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Scenario:
        """Create a new scenario in a dataset.

        Parameters
        ----------
        dataset_id : str
            Dataset ID to create the scenario in.
        interactions : Iterable[InteractionParam] | Omit
            Interactions to attach to the scenario. Each interaction needs a
            structured `input` matching the agent's `input_schema`, and
            optionally an `output` and a `checks` list. `position` defaults to
            the interaction's index in the list when omitted.
        status : Literal["active", "draft"] | None | Omit
            Status of the scenario.
        tags : SequenceNotStr[str] | Omit
            Tags to apply to the scenario.
        source_probe_attempt_id : str | None | Omit
            ID of the scan probe attempt this scenario was created from, if
            any.
        messages : Iterable[ChatMessageParam] | Omit
            (Deprecated) Conversation messages. Translated into a single
            interaction against the dataset's default role with
            `input={"messages": [...]}`.
        checks : Iterable[CheckConfigParam] | Omit
            (Deprecated) Checks attached to the synthesized interaction.
            Each `identifier` is resolved to a `check_id`.
        demo_output : DemoOutput | None | Omit
            (Deprecated) Reference output for the synthesized interaction.

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
        Scenario
            The newly created scenario.

        Raises
        ------
        ValueError
            If `interactions` is mixed with legacy parameters, or if neither
            is provided.
        """
        source = _resolve_interaction_source(
            method="create",
            require_one=True,
            interactions=interactions,
            messages=messages,
            checks=checks,
            demo_output=demo_output,
        )
        if source == "legacy":
            interactions = [
                build_legacy_interaction(
                    messages=messages,
                    demo_output=demo_output,
                    checks=checks,
                )
            ]
        elif source == "interactions":
            interactions = normalize_interactions(cast("Iterable[InteractionParam]", interactions))

        response = await self._post(
            "/v2/scenarios",
            body=await async_maybe_transform(
                {
                    "dataset_id": dataset_id,
                    "interactions": interactions,
                    "status": status,
                    "tags": tags,
                    "source_probe_attempt_id": source_probe_attempt_id,
                },
                ScenarioCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponse[Scenario],
        )

        return self._unwrap(response)

    async def retrieve(
        self,
        scenario_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Scenario:
        """
        Retrieve a scenario by its ID.

        Parameters
        ----------
        scenario_id : str
            Scenario ID to retrieve.

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
        Scenario
            The retrieved scenario.

        Raises
        ------
        ValueError
            If `scenario_id` is empty.
        """
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")
        response = await self._get(
            f"/v2/scenarios/{scenario_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponse[Scenario],
        )

        return self._unwrap(response)

    async def update(
        self,
        scenario_id: str,
        *,
        interactions: Optional[Iterable[InteractionParam]] | Omit = omit,
        dataset_id: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        status: Optional[Literal["active", "draft"]] | Omit = omit,
        messages: Optional[Iterable[ChatMessageParam]] | Omit = omit,
        checks: Optional[Iterable[CheckConfigParam]] | Omit = omit,
        demo_output: Optional[DemoOutput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Scenario:
        """Update an existing scenario.

        Parameters
        ----------
        scenario_id : str
            Scenario ID to update.
        interactions : Iterable[InteractionParam] | None | Omit
            Replace the scenario's interactions.
        dataset_id : str | None | Omit
            Move the scenario to this dataset.
        tags : SequenceNotStr[str] | None | Omit
            Tags to set on the scenario.
        status : Literal["active", "draft"] | None | Omit
            New status of the scenario.
        messages : Iterable[ChatMessageParam] | None | Omit
            (Deprecated) Conversation messages. Translated into a single
            interaction against the dataset's default role with
            `input={"messages": [...]}`.
        checks : Iterable[CheckConfigParam] | None | Omit
            (Deprecated) Checks attached to the synthesized interaction.
            Each `identifier` is resolved to a `check_id`.
        demo_output : DemoOutput | None | Omit
            (Deprecated) Reference output for the synthesized interaction.

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
        Scenario
            The updated scenario.

        Raises
        ------
        ValueError
            If `scenario_id` is empty, or if `interactions` is mixed with
            legacy parameters.
        """
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")

        source = _resolve_interaction_source(
            method="update",
            require_one=False,
            interactions=interactions,
            messages=messages,
            checks=checks,
            demo_output=demo_output,
        )
        if source == "legacy":
            interactions = [
                build_legacy_interaction(
                    messages=messages,
                    demo_output=demo_output,
                    checks=checks,
                )
            ]
        elif source == "interactions":
            interactions = normalize_interactions(cast("Iterable[InteractionParam]", interactions))

        response = await self._patch(
            f"/v2/scenarios/{scenario_id}",
            body=await async_maybe_transform(
                {
                    "dataset_id": dataset_id,
                    "interactions": interactions,
                    "tags": tags,
                    "status": status,
                },
                ScenarioUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponse[Scenario],
        )

        return self._unwrap(response)

    async def delete(
        self,
        scenario_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a scenario by its ID.

        Parameters
        ----------
        scenario_id : str
            Scenario ID to delete.

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
        None

        Raises
        ------
        ValueError
            If `scenario_id` is empty.
        """
        if not scenario_id:
            raise ValueError(f"Expected a non-empty value for `scenario_id` but received {scenario_id!r}")
        response = await self._delete(
            f"/v2/scenarios/{scenario_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    async def bulk_delete(
        self,
        *,
        scenario_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete multiple scenarios at once.

        Parameters
        ----------
        scenario_ids : SequenceNotStr[str]
            Scenario IDs to delete.

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
        None
        """
        response = await self._delete(
            "/v2/scenarios",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"scenario_ids": scenario_ids}, ScenarioBulkDeleteParams),
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    async def bulk_update(
        self,
        *,
        scenario_ids: SequenceNotStr[str],
        disabled_checks: Optional[SequenceNotStr[str]] | Omit = omit,
        enabled_checks: Optional[SequenceNotStr[str]] | Omit = omit,
        added_tags: Optional[SequenceNotStr[str]] | Omit = omit,
        removed_tags: Optional[SequenceNotStr[str]] | Omit = omit,
        status: Optional[Literal["active", "draft"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[Scenario]:
        """
        Bulk update multiple scenarios' checks, tags, or status.

        Parameters
        ----------
        scenario_ids : SequenceNotStr[str]
            Scenario IDs to update.
        disabled_checks : Optional[SequenceNotStr[str]] | Omit
            Partial list of checks to be disabled.
        enabled_checks : Optional[SequenceNotStr[str]] | Omit
            Partial list of checks to be enabled.
        added_tags : Optional[SequenceNotStr[str]] | Omit
            Tags to be added to the scenarios.
        removed_tags : Optional[SequenceNotStr[str]] | Omit
            Tags to be removed from the scenarios.
        status : Optional[Literal["active", "draft"]] | Omit
            Status of the scenarios.

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
        List[Scenario]
            The updated scenarios.
        """
        response = await self._patch(
            "/v2/scenarios",
            body=await async_maybe_transform(
                {
                    "ids": scenario_ids,
                    "disabled_checks": disabled_checks,
                    "enabled_checks": enabled_checks,
                    "added_tags": added_tags,
                    "removed_tags": removed_tags,
                    "status": status,
                },
                ScenarioBulkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponse[List[Scenario]],
        )

        return self._unwrap(response)

    async def bulk_move(
        self,
        *,
        scenario_ids: List[str],
        target_dataset_id: str,
        duplicate: Optional[bool] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Move or copy scenarios between datasets.

        Parameters
        ----------
        scenario_ids : List[str]
            List of scenario IDs to move.
        target_dataset_id : str
            Target dataset ID to move scenarios to.
        duplicate : Optional[bool] | Omit
            If true, keep a copy of the scenarios in the original dataset. Default is true.

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
        None
        """
        response = await self._post(
            "/v2/scenarios/bulk-move",
            body=await async_maybe_transform(
                {
                    "scenario_ids": scenario_ids,
                    "dataset_id": target_dataset_id,
                    "duplicate": duplicate,
                },
                BulkMoveScenariosParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponse[None],
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
        self.delete = to_raw_response_wrapper(
            scenarios.delete,
        )
        self.bulk_delete = to_raw_response_wrapper(
            scenarios.bulk_delete,
        )
        self.bulk_update = to_raw_response_wrapper(
            scenarios.bulk_update,
        )
        self.bulk_move = to_raw_response_wrapper(
            scenarios.bulk_move,
        )

    @cached_property
    def comments(self) -> CommentsResourceWithRawResponse:
        return CommentsResourceWithRawResponse(self._scenarios.comments)


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
        self.delete = async_to_raw_response_wrapper(
            scenarios.delete,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            scenarios.bulk_delete,
        )
        self.bulk_update = async_to_raw_response_wrapper(
            scenarios.bulk_update,
        )
        self.bulk_move = async_to_raw_response_wrapper(
            scenarios.bulk_move,
        )

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithRawResponse:
        return AsyncCommentsResourceWithRawResponse(self._scenarios.comments)


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
        self.delete = to_streamed_response_wrapper(
            scenarios.delete,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            scenarios.bulk_delete,
        )
        self.bulk_update = to_streamed_response_wrapper(
            scenarios.bulk_update,
        )
        self.bulk_move = to_streamed_response_wrapper(
            scenarios.bulk_move,
        )

    @cached_property
    def comments(self) -> CommentsResourceWithStreamingResponse:
        return CommentsResourceWithStreamingResponse(self._scenarios.comments)


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
        self.delete = async_to_streamed_response_wrapper(
            scenarios.delete,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            scenarios.bulk_delete,
        )
        self.bulk_update = async_to_streamed_response_wrapper(
            scenarios.bulk_update,
        )
        self.bulk_move = async_to_streamed_response_wrapper(
            scenarios.bulk_move,
        )

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithStreamingResponse:
        return AsyncCommentsResourceWithStreamingResponse(self._scenarios.comments)
