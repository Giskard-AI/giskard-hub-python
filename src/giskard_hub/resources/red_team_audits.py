from __future__ import annotations

from typing import List, Mapping, Optional, cast

import httpx

from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._analytics import capture_event, make_distinct_id
from .._base_client import make_request_options
from ..types.common import APIResponse
from ..types.credit import CreditEstimate
from ..types.red_team_audit import (
    RedTeamAudit,
    RedTeamAuditLogs,
    RedTeamAuditContent,
    RedTeamAuditScanType,
    RedTeamAuditListParams,
    RedTeamAuditCoverageMode,
    RedTeamAuditCreateParams,
    RedTeamAuditUploadParams,
    RedTeamAuditEstimateParams,
    RedTeamAuditRetrieveLogsParams,
)

__all__ = ["RedTeamAuditsResource", "AsyncRedTeamAuditsResource"]


class RedTeamAuditsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RedTeamAuditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return RedTeamAuditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RedTeamAuditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return RedTeamAuditsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: str,
        target_agent_id: str,
        input_evaluation_ids: SequenceNotStr[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        scan_types: Optional[List[RedTeamAuditScanType]] | Omit = omit,
        mode: RedTeamAuditCoverageMode | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamAudit:
        """Launch a new red team audit of an agent.

        Parameters
        ----------
        project_id : str
            Project ID to run the audit in.
        target_agent_id : str
            ID of the agent to audit. The agent must belong to the project.
        input_evaluation_ids : SequenceNotStr[str] | Omit
            IDs of existing evaluations of the same project to use as input for the audit.
        name : str | None | Omit
            Name of the audit.
        scan_types : List[Literal["vulnerability", "garak", "deepteam", "lidar"]] | None | Omit
            Scan suites to run during the audit. When omitted, the server runs its default
            scan suites if no ``input_evaluation_ids`` are given, and no scan suite otherwise.
        mode : Literal["regular", "light"] | Omit
            Coverage mode of the audit. Defaults to ``regular`` on the server when omitted.

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
        RedTeamAudit
            The newly created red team audit.
        """
        response = self._post(
            "/v2/red-team-audits",
            body=maybe_transform(
                {
                    "project_id": project_id,
                    "target_agent_id": target_agent_id,
                    "input_evaluation_ids": input_evaluation_ids,
                    "name": name,
                    "scan_types": scan_types,
                    "mode": mode,
                },
                RedTeamAuditCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[RedTeamAudit],
        )

        result = self._unwrap(response)
        capture_event(
            make_distinct_id(self._client.api_key), "red_team_audit_created", {"red_team_audit_id": result.id}
        )
        return result

    def upload(
        self,
        *,
        project_id: str,
        target_agent_id: str,
        content: FileTypes,
        name: Optional[str] | Omit = omit,
        report: FileTypes | Omit = omit,
        risk_model: FileTypes | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamAudit:
        """Import the results of a red team audit that ran outside of the Hub.

        Parameters
        ----------
        project_id : str
            Project ID to import the audit into.
        target_agent_id : str
            ID of the audited agent. The agent must belong to the project.
        content : FileTypes
            JSON file with the audit report content.
        name : str | None | Omit
            Name of the audit.
        report : FileTypes | Omit
            PDF file with the audit report.
        risk_model : FileTypes | Omit
            JSON file with the risk model of the audit.

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
        RedTeamAudit
            The imported red team audit.
        """
        body = deepcopy_minimal(
            {
                "project_id": project_id,
                "target_agent_id": target_agent_id,
                "name": name,
                "content": content,
                "report": report,
                "risk_model": risk_model,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["content"], ["report"], ["risk_model"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        response = self._post(
            "/v2/red-team-audits/import",
            body=maybe_transform(body, RedTeamAuditUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[RedTeamAudit],
        )

        return self._unwrap(response)

    def retrieve(
        self,
        audit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamAudit:
        """Retrieve a red team audit by its ID.

        Parameters
        ----------
        audit_id : str
            Red team audit ID.

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
        RedTeamAudit
            The requested red team audit.

        Raises
        ------
        ValueError
            If `audit_id` is empty.
        """
        if not audit_id:
            raise ValueError(f"Expected a non-empty value for `audit_id` but received {audit_id!r}")
        response = self._get(
            f"/v2/red-team-audits/{audit_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[RedTeamAudit],
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
    ) -> List[RedTeamAudit]:
        """List all red team audits, optionally filtered by project.

        Parameters
        ----------
        project_id : str | None | Omit
            Project ID to filter the audits by.

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
        List[RedTeamAudit]
            A list of red team audits.
        """
        response = self._get(
            "/v2/red-team-audits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, RedTeamAuditListParams),
            ),
            cast_to=APIResponse[List[RedTeamAudit]],
        )

        return self._unwrap(response)

    def delete(
        self,
        audit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a red team audit by its ID. If the audit is still running, it is canceled first.

        Parameters
        ----------
        audit_id : str
            Red team audit ID to delete.

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
            If `audit_id` is empty.
        """
        if not audit_id:
            raise ValueError(f"Expected a non-empty value for `audit_id` but received {audit_id!r}")
        response = self._delete(
            f"/v2/red-team-audits/{audit_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    def retrieve_content(
        self,
        audit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamAuditContent:
        """Retrieve the findings, remediations, and trust level of a red team audit.

        The content is available only when ``RedTeamAudit.has_audit_content`` is true.

        Parameters
        ----------
        audit_id : str
            Red team audit ID.

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
        RedTeamAuditContent
            The content of the red team audit.

        Raises
        ------
        ValueError
            If `audit_id` is empty.
        """
        if not audit_id:
            raise ValueError(f"Expected a non-empty value for `audit_id` but received {audit_id!r}")
        response = self._get(
            f"/v2/red-team-audits/{audit_id}/content",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[RedTeamAuditContent],
        )

        return self._unwrap(response)

    def retrieve_logs(
        self,
        audit_id: str,
        *,
        after: int | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamAuditLogs:
        """Retrieve a page of the execution logs of a red team audit.

        Parameters
        ----------
        audit_id : str
            Red team audit ID.
        after : int | Omit
            Return only the log chunks with a sequence number greater than this value.
            To get the next page, use the ``next_cursor`` of the previous page.
            Defaults to ``0`` on the server when omitted.
        limit : int | Omit
            Maximum number of log chunks to return, from 1 to 1000.
            Defaults to ``500`` on the server when omitted.

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
        RedTeamAuditLogs
            The log chunks, the audit status, and the cursor for the next page.

        Raises
        ------
        ValueError
            If `audit_id` is empty.
        """
        if not audit_id:
            raise ValueError(f"Expected a non-empty value for `audit_id` but received {audit_id!r}")
        response = self._get(
            f"/v2/red-team-audits/{audit_id}/logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    RedTeamAuditRetrieveLogsParams,
                ),
            ),
            cast_to=APIResponse[RedTeamAuditLogs],
        )

        return self._unwrap(response)

    def estimate(
        self,
        *,
        mode: RedTeamAuditCoverageMode | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditEstimate:
        """Estimate the credit cost of a red team audit.

        Parameters
        ----------
        mode : Literal["regular", "light"] | Omit
            Coverage mode to price. Defaults to ``regular`` on the server when omitted.

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
        CreditEstimate
            Estimated credit cost of the audit.
        """
        response = self._post(
            "/v2/red-team-audits/estimate",
            body=maybe_transform(
                {
                    "mode": mode,
                },
                RedTeamAuditEstimateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[CreditEstimate],
        )

        return self._unwrap(response)


class AsyncRedTeamAuditsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRedTeamAuditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRedTeamAuditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRedTeamAuditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncRedTeamAuditsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: str,
        target_agent_id: str,
        input_evaluation_ids: SequenceNotStr[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        scan_types: Optional[List[RedTeamAuditScanType]] | Omit = omit,
        mode: RedTeamAuditCoverageMode | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamAudit:
        """Launch a new red team audit of an agent.

        Parameters
        ----------
        project_id : str
            Project ID to run the audit in.
        target_agent_id : str
            ID of the agent to audit. The agent must belong to the project.
        input_evaluation_ids : SequenceNotStr[str] | Omit
            IDs of existing evaluations of the same project to use as input for the audit.
        name : str | None | Omit
            Name of the audit.
        scan_types : List[Literal["vulnerability", "garak", "deepteam", "lidar"]] | None | Omit
            Scan suites to run during the audit. When omitted, the server runs its default
            scan suites if no ``input_evaluation_ids`` are given, and no scan suite otherwise.
        mode : Literal["regular", "light"] | Omit
            Coverage mode of the audit. Defaults to ``regular`` on the server when omitted.

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
        RedTeamAudit
            The newly created red team audit.
        """
        response = await self._post(
            "/v2/red-team-audits",
            body=await async_maybe_transform(
                {
                    "project_id": project_id,
                    "target_agent_id": target_agent_id,
                    "input_evaluation_ids": input_evaluation_ids,
                    "name": name,
                    "scan_types": scan_types,
                    "mode": mode,
                },
                RedTeamAuditCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[RedTeamAudit],
        )

        result = self._unwrap(response)
        capture_event(
            make_distinct_id(self._client.api_key), "red_team_audit_created", {"red_team_audit_id": result.id}
        )
        return result

    async def upload(
        self,
        *,
        project_id: str,
        target_agent_id: str,
        content: FileTypes,
        name: Optional[str] | Omit = omit,
        report: FileTypes | Omit = omit,
        risk_model: FileTypes | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamAudit:
        """Import the results of a red team audit that ran outside of the Hub.

        Parameters
        ----------
        project_id : str
            Project ID to import the audit into.
        target_agent_id : str
            ID of the audited agent. The agent must belong to the project.
        content : FileTypes
            JSON file with the audit report content.
        name : str | None | Omit
            Name of the audit.
        report : FileTypes | Omit
            PDF file with the audit report.
        risk_model : FileTypes | Omit
            JSON file with the risk model of the audit.

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
        RedTeamAudit
            The imported red team audit.
        """
        body = deepcopy_minimal(
            {
                "project_id": project_id,
                "target_agent_id": target_agent_id,
                "name": name,
                "content": content,
                "report": report,
                "risk_model": risk_model,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["content"], ["report"], ["risk_model"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        response = await self._post(
            "/v2/red-team-audits/import",
            body=await async_maybe_transform(body, RedTeamAuditUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[RedTeamAudit],
        )

        return self._unwrap(response)

    async def retrieve(
        self,
        audit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamAudit:
        """Retrieve a red team audit by its ID.

        Parameters
        ----------
        audit_id : str
            Red team audit ID.

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
        RedTeamAudit
            The requested red team audit.

        Raises
        ------
        ValueError
            If `audit_id` is empty.
        """
        if not audit_id:
            raise ValueError(f"Expected a non-empty value for `audit_id` but received {audit_id!r}")
        response = await self._get(
            f"/v2/red-team-audits/{audit_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[RedTeamAudit],
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
    ) -> List[RedTeamAudit]:
        """List all red team audits, optionally filtered by project.

        Parameters
        ----------
        project_id : str | None | Omit
            Project ID to filter the audits by.

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
        List[RedTeamAudit]
            A list of red team audits.
        """
        response = await self._get(
            "/v2/red-team-audits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"project_id": project_id}, RedTeamAuditListParams),
            ),
            cast_to=APIResponse[List[RedTeamAudit]],
        )

        return self._unwrap(response)

    async def delete(
        self,
        audit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a red team audit by its ID. If the audit is still running, it is canceled first.

        Parameters
        ----------
        audit_id : str
            Red team audit ID to delete.

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
            If `audit_id` is empty.
        """
        if not audit_id:
            raise ValueError(f"Expected a non-empty value for `audit_id` but received {audit_id!r}")
        response = await self._delete(
            f"/v2/red-team-audits/{audit_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    async def retrieve_content(
        self,
        audit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamAuditContent:
        """Retrieve the findings, remediations, and trust level of a red team audit.

        The content is available only when ``RedTeamAudit.has_audit_content`` is true.

        Parameters
        ----------
        audit_id : str
            Red team audit ID.

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
        RedTeamAuditContent
            The content of the red team audit.

        Raises
        ------
        ValueError
            If `audit_id` is empty.
        """
        if not audit_id:
            raise ValueError(f"Expected a non-empty value for `audit_id` but received {audit_id!r}")
        response = await self._get(
            f"/v2/red-team-audits/{audit_id}/content",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[RedTeamAuditContent],
        )

        return self._unwrap(response)

    async def retrieve_logs(
        self,
        audit_id: str,
        *,
        after: int | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamAuditLogs:
        """Retrieve a page of the execution logs of a red team audit.

        Parameters
        ----------
        audit_id : str
            Red team audit ID.
        after : int | Omit
            Return only the log chunks with a sequence number greater than this value.
            To get the next page, use the ``next_cursor`` of the previous page.
            Defaults to ``0`` on the server when omitted.
        limit : int | Omit
            Maximum number of log chunks to return, from 1 to 1000.
            Defaults to ``500`` on the server when omitted.

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
        RedTeamAuditLogs
            The log chunks, the audit status, and the cursor for the next page.

        Raises
        ------
        ValueError
            If `audit_id` is empty.
        """
        if not audit_id:
            raise ValueError(f"Expected a non-empty value for `audit_id` but received {audit_id!r}")
        response = await self._get(
            f"/v2/red-team-audits/{audit_id}/logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    RedTeamAuditRetrieveLogsParams,
                ),
            ),
            cast_to=APIResponse[RedTeamAuditLogs],
        )

        return self._unwrap(response)

    async def estimate(
        self,
        *,
        mode: RedTeamAuditCoverageMode | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditEstimate:
        """Estimate the credit cost of a red team audit.

        Parameters
        ----------
        mode : Literal["regular", "light"] | Omit
            Coverage mode to price. Defaults to ``regular`` on the server when omitted.

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
        CreditEstimate
            Estimated credit cost of the audit.
        """
        response = await self._post(
            "/v2/red-team-audits/estimate",
            body=await async_maybe_transform(
                {
                    "mode": mode,
                },
                RedTeamAuditEstimateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[CreditEstimate],
        )

        return self._unwrap(response)


class RedTeamAuditsResourceWithRawResponse:
    def __init__(self, red_team_audits: RedTeamAuditsResource) -> None:
        self._red_team_audits = red_team_audits

        self.create = to_raw_response_wrapper(
            red_team_audits.create,
        )
        self.upload = to_raw_response_wrapper(
            red_team_audits.upload,
        )
        self.retrieve = to_raw_response_wrapper(
            red_team_audits.retrieve,
        )
        self.list = to_raw_response_wrapper(
            red_team_audits.list,
        )
        self.delete = to_raw_response_wrapper(
            red_team_audits.delete,
        )
        self.retrieve_content = to_raw_response_wrapper(
            red_team_audits.retrieve_content,
        )
        self.retrieve_logs = to_raw_response_wrapper(
            red_team_audits.retrieve_logs,
        )
        self.estimate = to_raw_response_wrapper(
            red_team_audits.estimate,
        )


class AsyncRedTeamAuditsResourceWithRawResponse:
    def __init__(self, red_team_audits: AsyncRedTeamAuditsResource) -> None:
        self._red_team_audits = red_team_audits

        self.create = async_to_raw_response_wrapper(
            red_team_audits.create,
        )
        self.upload = async_to_raw_response_wrapper(
            red_team_audits.upload,
        )
        self.retrieve = async_to_raw_response_wrapper(
            red_team_audits.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            red_team_audits.list,
        )
        self.delete = async_to_raw_response_wrapper(
            red_team_audits.delete,
        )
        self.retrieve_content = async_to_raw_response_wrapper(
            red_team_audits.retrieve_content,
        )
        self.retrieve_logs = async_to_raw_response_wrapper(
            red_team_audits.retrieve_logs,
        )
        self.estimate = async_to_raw_response_wrapper(
            red_team_audits.estimate,
        )


class RedTeamAuditsResourceWithStreamingResponse:
    def __init__(self, red_team_audits: RedTeamAuditsResource) -> None:
        self._red_team_audits = red_team_audits

        self.create = to_streamed_response_wrapper(
            red_team_audits.create,
        )
        self.upload = to_streamed_response_wrapper(
            red_team_audits.upload,
        )
        self.retrieve = to_streamed_response_wrapper(
            red_team_audits.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            red_team_audits.list,
        )
        self.delete = to_streamed_response_wrapper(
            red_team_audits.delete,
        )
        self.retrieve_content = to_streamed_response_wrapper(
            red_team_audits.retrieve_content,
        )
        self.retrieve_logs = to_streamed_response_wrapper(
            red_team_audits.retrieve_logs,
        )
        self.estimate = to_streamed_response_wrapper(
            red_team_audits.estimate,
        )


class AsyncRedTeamAuditsResourceWithStreamingResponse:
    def __init__(self, red_team_audits: AsyncRedTeamAuditsResource) -> None:
        self._red_team_audits = red_team_audits

        self.create = async_to_streamed_response_wrapper(
            red_team_audits.create,
        )
        self.upload = async_to_streamed_response_wrapper(
            red_team_audits.upload,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            red_team_audits.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            red_team_audits.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            red_team_audits.delete,
        )
        self.retrieve_content = async_to_streamed_response_wrapper(
            red_team_audits.retrieve_content,
        )
        self.retrieve_logs = async_to_streamed_response_wrapper(
            red_team_audits.retrieve_logs,
        )
        self.estimate = async_to_streamed_response_wrapper(
            red_team_audits.estimate,
        )
