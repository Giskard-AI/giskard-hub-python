from __future__ import annotations

import warnings
from typing import List, Literal, Iterable, Optional

import httpx

from ...types import BulkMoveTestCasesParams
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
from ...types.test_case import (
    TestCase,
    TestCaseCreateParams,
    TestCaseUpdateParams,
    TestCaseBulkDeleteParams,
    TestCaseBulkUpdateParams,
)
from .._interaction_helpers import (
    build_legacy_interaction_sync,
    build_legacy_interaction_async,
)

__all__ = ["TestCasesResource", "AsyncTestCasesResource"]

DemoOutput = ChatMessageWithMetadataParam | str


_LEGACY_TC_PARAM_NAMES = ("messages", "checks", "demo_output")


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
            f"({', '.join(repr(n) for n in _LEGACY_TC_PARAM_NAMES)}). Pick one."
        )
    if require_one and not using_interactions and not using_legacy:
        raise ValueError("Must provide either `interactions=` (recommended) or legacy `messages` (deprecated).")

    if using_legacy:
        warnings.warn(
            f"Passing `messages` / `checks` / `demo_output` to "
            f"`test_cases.{method}` is deprecated. Pass `interactions=[{{...}}]` instead.",
            DeprecationWarning,
            stacklevel=3,
        )
        return "legacy"
    return "interactions" if using_interactions else "none"


class TestCasesResource(SyncAPIResource):
    __test__ = False

    @cached_property
    def comments(self) -> CommentsResource:
        return CommentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TestCasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return TestCasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestCasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return TestCasesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        dataset_id: str,
        interactions: Iterable[InteractionParam] | Omit = omit,
        status: Optional[Literal["active", "draft"]] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        messages: Iterable[ChatMessageParam] | Omit = omit,
        checks: Iterable[CheckConfigParam] | Omit = omit,
        demo_output: Optional[DemoOutput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCase:
        """Create a new test case in a dataset.

        Parameters
        ----------
        dataset_id : str
            Dataset ID to create the test case in.
        interactions : Iterable[InteractionParam] | Omit
            Interactions to attach to the test case. Each interaction needs a
            a `position`, a structured `input` matching the agent's
            `input_schema`, and optionally an `output` and a `checks` list.
        status : Literal["active", "draft"] | None | Omit
            Status of the test case.
        tags : SequenceNotStr[str] | Omit
            Tags to apply to the test case.
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
        TestCase
            The newly created test case.

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
                build_legacy_interaction_sync(
                    self._client,
                    dataset_id=dataset_id,
                    messages=messages,
                    demo_output=demo_output,
                    checks=checks,
                )
            ]

        response = self._post(
            "/v2/test-cases",
            body=maybe_transform(
                {
                    "dataset_id": dataset_id,
                    "interactions": interactions,
                    "status": status,
                    "tags": tags,
                },
                TestCaseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponse[TestCase],
        )

        return self._unwrap(response)

    def retrieve(
        self,
        test_case_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCase:
        """
        Retrieve a test case by its ID.

        Parameters
        ----------
        test_case_id : str
            Test Case ID to retrieve.

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
        TestCase
            The retrieved test case.

        Raises
        ------
        ValueError
            If `test_case_id` is empty.
        """
        if not test_case_id:
            raise ValueError(f"Expected a non-empty value for `test_case_id` but received {test_case_id!r}")
        response = self._get(
            f"/v2/test-cases/{test_case_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponse[TestCase],
        )

        return self._unwrap(response)

    def update(
        self,
        test_case_id: str,
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
    ) -> TestCase:
        """Update an existing test case.

        Parameters
        ----------
        test_case_id : str
            Test Case ID to update.
        interactions : Iterable[InteractionParam] | None | Omit
            Replace the test case's interactions.
        dataset_id : str | None | Omit
            Move the test case to this dataset.
        tags : SequenceNotStr[str] | None | Omit
            Tags to set on the test case.
        status : Literal["active", "draft"] | None | Omit
            New status of the test case.
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
        TestCase
            The updated test case.

        Raises
        ------
        ValueError
            If `test_case_id` is empty, or if `interactions` is mixed with
            legacy parameters.
        """
        if not test_case_id:
            raise ValueError(f"Expected a non-empty value for `test_case_id` but received {test_case_id!r}")

        source = _resolve_interaction_source(
            method="update",
            require_one=False,
            interactions=interactions,
            messages=messages,
            checks=checks,
            demo_output=demo_output,
        )
        if source == "legacy":
            target_dataset_id = dataset_id if isinstance(dataset_id, str) else self.retrieve(test_case_id).dataset_id
            interactions = [
                build_legacy_interaction_sync(
                    self._client,
                    dataset_id=target_dataset_id,
                    messages=messages,
                    demo_output=demo_output,
                    checks=checks,
                )
            ]

        response = self._patch(
            f"/v2/test-cases/{test_case_id}",
            body=maybe_transform(
                {
                    "dataset_id": dataset_id,
                    "interactions": interactions,
                    "tags": tags,
                    "status": status,
                },
                TestCaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponse[TestCase],
        )

        return self._unwrap(response)

    def delete(
        self,
        test_case_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a test case by its ID.

        Parameters
        ----------
        test_case_id : str
            Test Case ID to delete.

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
            If `test_case_id` is empty.
        """
        if not test_case_id:
            raise ValueError(f"Expected a non-empty value for `test_case_id` but received {test_case_id!r}")
        response = self._delete(
            f"/v2/test-cases/{test_case_id}",
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
        test_case_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete multiple test cases at once.

        Parameters
        ----------
        test_case_ids : SequenceNotStr[str]
            Test Case IDs to delete.

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
            "/v2/test-cases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"test_case_ids": test_case_ids}, TestCaseBulkDeleteParams),
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    def bulk_update(
        self,
        *,
        test_case_ids: SequenceNotStr[str],
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
    ) -> List[TestCase]:
        """
        Bulk update multiple test cases' checks, tags, or status.

        Parameters
        ----------
        test_case_ids : SequenceNotStr[str]
            Test Case IDs to update.
        disabled_checks : Optional[SequenceNotStr[str]] | Omit
            Partial list of checks to be disabled.
        enabled_checks : Optional[SequenceNotStr[str]] | Omit
            Partial list of checks to be enabled.
        added_tags : Optional[SequenceNotStr[str]] | Omit
            Tags to be added to the test cases.
        removed_tags : Optional[SequenceNotStr[str]] | Omit
            Tags to be removed from the test cases.
        status : Optional[Literal["active", "draft"]] | Omit
            Status of the test cases.

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
        List[TestCase]
            The updated test cases.
        """
        response = self._patch(
            "/v2/test-cases",
            body=maybe_transform(
                {
                    "ids": test_case_ids,
                    "disabled_checks": disabled_checks,
                    "enabled_checks": enabled_checks,
                    "added_tags": added_tags,
                    "removed_tags": removed_tags,
                    "status": status,
                },
                TestCaseBulkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponse[List[TestCase]],
        )

        return self._unwrap(response)

    def bulk_move(
        self,
        *,
        test_case_ids: List[str],
        target_dataset_id: str,
        duplicate: Optional[bool] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Move or copy test cases between datasets.

        Parameters
        ----------
        test_case_ids : List[str]
            List of test case IDs to move.
        target_dataset_id : str
            Target dataset ID to move test cases to.
        duplicate : Optional[bool] | Omit
            If true, keep a copy of the test cases in the original dataset. Default is true.

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
            "/v2/test-cases/bulk-move",
            body=maybe_transform(
                {
                    "test_case_ids": test_case_ids,
                    "dataset_id": target_dataset_id,
                    "duplicate": duplicate,
                },
                BulkMoveTestCasesParams,
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


class AsyncTestCasesResource(AsyncAPIResource):
    @cached_property
    def comments(self) -> AsyncCommentsResource:
        return AsyncCommentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTestCasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTestCasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestCasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncTestCasesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        dataset_id: str,
        interactions: Iterable[InteractionParam] | Omit = omit,
        status: Optional[Literal["active", "draft"]] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        messages: Iterable[ChatMessageParam] | Omit = omit,
        checks: Iterable[CheckConfigParam] | Omit = omit,
        demo_output: Optional[DemoOutput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCase:
        """Create a new test case in a dataset.

        Parameters
        ----------
        dataset_id : str
            Dataset ID to create the test case in.
        interactions : Iterable[InteractionParam] | Omit
            Interactions to attach to the test case. Each interaction needs a
            `position`, a structured `input` matching the agent's
            `input_schema`, and optionally an `output` and a `checks` list.
        status : Literal["active", "draft"] | None | Omit
            Status of the test case.
        tags : SequenceNotStr[str] | Omit
            Tags to apply to the test case.
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
        TestCase
            The newly created test case.

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
                await build_legacy_interaction_async(
                    self._client,
                    dataset_id=dataset_id,
                    messages=messages,
                    demo_output=demo_output,
                    checks=checks,
                )
            ]

        response = await self._post(
            "/v2/test-cases",
            body=await async_maybe_transform(
                {
                    "dataset_id": dataset_id,
                    "interactions": interactions,
                    "status": status,
                    "tags": tags,
                },
                TestCaseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponse[TestCase],
        )

        return self._unwrap(response)

    async def retrieve(
        self,
        test_case_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCase:
        """
        Retrieve a test case by its ID.

        Parameters
        ----------
        test_case_id : str
            Test Case ID to retrieve.

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
        TestCase
            The retrieved test case.

        Raises
        ------
        ValueError
            If `test_case_id` is empty.
        """
        if not test_case_id:
            raise ValueError(f"Expected a non-empty value for `test_case_id` but received {test_case_id!r}")
        response = await self._get(
            f"/v2/test-cases/{test_case_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponse[TestCase],
        )

        return self._unwrap(response)

    async def update(
        self,
        test_case_id: str,
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
    ) -> TestCase:
        """Update an existing test case.

        Parameters
        ----------
        test_case_id : str
            Test Case ID to update.
        interactions : Iterable[InteractionParam] | None | Omit
            Replace the test case's interactions.
        dataset_id : str | None | Omit
            Move the test case to this dataset.
        tags : SequenceNotStr[str] | None | Omit
            Tags to set on the test case.
        status : Literal["active", "draft"] | None | Omit
            New status of the test case.
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
        TestCase
            The updated test case.

        Raises
        ------
        ValueError
            If `test_case_id` is empty, or if `interactions` is mixed with
            legacy parameters.
        """
        if not test_case_id:
            raise ValueError(f"Expected a non-empty value for `test_case_id` but received {test_case_id!r}")

        source = _resolve_interaction_source(
            method="update",
            require_one=False,
            interactions=interactions,
            messages=messages,
            checks=checks,
            demo_output=demo_output,
        )
        if source == "legacy":
            target_dataset_id = (
                dataset_id if isinstance(dataset_id, str) else (await self.retrieve(test_case_id)).dataset_id
            )
            interactions = [
                await build_legacy_interaction_async(
                    self._client,
                    dataset_id=target_dataset_id,
                    messages=messages,
                    demo_output=demo_output,
                    checks=checks,
                )
            ]

        response = await self._patch(
            f"/v2/test-cases/{test_case_id}",
            body=await async_maybe_transform(
                {
                    "dataset_id": dataset_id,
                    "interactions": interactions,
                    "tags": tags,
                    "status": status,
                },
                TestCaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponse[TestCase],
        )

        return self._unwrap(response)

    async def delete(
        self,
        test_case_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a test case by its ID.

        Parameters
        ----------
        test_case_id : str
            Test Case ID to delete.

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
            If `test_case_id` is empty.
        """
        if not test_case_id:
            raise ValueError(f"Expected a non-empty value for `test_case_id` but received {test_case_id!r}")
        response = await self._delete(
            f"/v2/test-cases/{test_case_id}",
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
        test_case_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete multiple test cases at once.

        Parameters
        ----------
        test_case_ids : SequenceNotStr[str]
            Test Case IDs to delete.

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
            "/v2/test-cases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"test_case_ids": test_case_ids}, TestCaseBulkDeleteParams),
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    async def bulk_update(
        self,
        *,
        test_case_ids: SequenceNotStr[str],
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
    ) -> List[TestCase]:
        """
        Bulk update multiple test cases' checks, tags, or status.

        Parameters
        ----------
        test_case_ids : SequenceNotStr[str]
            Test Case IDs to update.
        disabled_checks : Optional[SequenceNotStr[str]] | Omit
            Partial list of checks to be disabled.
        enabled_checks : Optional[SequenceNotStr[str]] | Omit
            Partial list of checks to be enabled.
        added_tags : Optional[SequenceNotStr[str]] | Omit
            Tags to be added to the test cases.
        removed_tags : Optional[SequenceNotStr[str]] | Omit
            Tags to be removed from the test cases.
        status : Optional[Literal["active", "draft"]] | Omit
            Status of the test cases.

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
        List[TestCase]
            The updated test cases.
        """
        response = await self._patch(
            "/v2/test-cases",
            body=await async_maybe_transform(
                {
                    "ids": test_case_ids,
                    "disabled_checks": disabled_checks,
                    "enabled_checks": enabled_checks,
                    "added_tags": added_tags,
                    "removed_tags": removed_tags,
                    "status": status,
                },
                TestCaseBulkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponse[List[TestCase]],
        )

        return self._unwrap(response)

    async def bulk_move(
        self,
        *,
        test_case_ids: List[str],
        target_dataset_id: str,
        duplicate: Optional[bool] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Move or copy test cases between datasets.

        Parameters
        ----------
        test_case_ids : List[str]
            List of test case IDs to move.
        target_dataset_id : str
            Target dataset ID to move test cases to.
        duplicate : Optional[bool] | Omit
            If true, keep a copy of the test cases in the original dataset. Default is true.

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
            "/v2/test-cases/bulk-move",
            body=await async_maybe_transform(
                {
                    "test_case_ids": test_case_ids,
                    "dataset_id": target_dataset_id,
                    "duplicate": duplicate,
                },
                BulkMoveTestCasesParams,
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


class TestCasesResourceWithRawResponse:
    __test__ = False

    def __init__(self, test_cases: TestCasesResource) -> None:
        self._test_cases = test_cases

        self.create = to_raw_response_wrapper(
            test_cases.create,
        )
        self.retrieve = to_raw_response_wrapper(
            test_cases.retrieve,
        )
        self.update = to_raw_response_wrapper(
            test_cases.update,
        )
        self.delete = to_raw_response_wrapper(
            test_cases.delete,
        )
        self.bulk_delete = to_raw_response_wrapper(
            test_cases.bulk_delete,
        )
        self.bulk_update = to_raw_response_wrapper(
            test_cases.bulk_update,
        )
        self.bulk_move = to_raw_response_wrapper(
            test_cases.bulk_move,
        )

    @cached_property
    def comments(self) -> CommentsResourceWithRawResponse:
        return CommentsResourceWithRawResponse(self._test_cases.comments)


class AsyncTestCasesResourceWithRawResponse:
    def __init__(self, test_cases: AsyncTestCasesResource) -> None:
        self._test_cases = test_cases

        self.create = async_to_raw_response_wrapper(
            test_cases.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            test_cases.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            test_cases.update,
        )
        self.delete = async_to_raw_response_wrapper(
            test_cases.delete,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            test_cases.bulk_delete,
        )
        self.bulk_update = async_to_raw_response_wrapper(
            test_cases.bulk_update,
        )
        self.bulk_move = async_to_raw_response_wrapper(
            test_cases.bulk_move,
        )

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithRawResponse:
        return AsyncCommentsResourceWithRawResponse(self._test_cases.comments)


class TestCasesResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, test_cases: TestCasesResource) -> None:
        self._test_cases = test_cases

        self.create = to_streamed_response_wrapper(
            test_cases.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            test_cases.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            test_cases.update,
        )
        self.delete = to_streamed_response_wrapper(
            test_cases.delete,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            test_cases.bulk_delete,
        )
        self.bulk_update = to_streamed_response_wrapper(
            test_cases.bulk_update,
        )
        self.bulk_move = to_streamed_response_wrapper(
            test_cases.bulk_move,
        )

    @cached_property
    def comments(self) -> CommentsResourceWithStreamingResponse:
        return CommentsResourceWithStreamingResponse(self._test_cases.comments)


class AsyncTestCasesResourceWithStreamingResponse:
    def __init__(self, test_cases: AsyncTestCasesResource) -> None:
        self._test_cases = test_cases

        self.create = async_to_streamed_response_wrapper(
            test_cases.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            test_cases.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            test_cases.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            test_cases.delete,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            test_cases.bulk_delete,
        )
        self.bulk_update = async_to_streamed_response_wrapper(
            test_cases.bulk_update,
        )
        self.bulk_move = async_to_streamed_response_wrapper(
            test_cases.bulk_move,
        )

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithStreamingResponse:
        return AsyncCommentsResourceWithStreamingResponse(self._test_cases.comments)
