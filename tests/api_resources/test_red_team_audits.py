# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, List, cast

import pytest

from giskard_hub import HubClient, AsyncHubClient
from tests.utils import assert_matches_type
from giskard_hub.types import (
    RedTeamAudit,
    CreditEstimate,
    RedTeamAuditLogs,
    RedTeamAuditContent,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRedTeamAudits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubClient) -> None:
        red_team_audit = client.red_team_audits.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RedTeamAudit, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubClient) -> None:
        red_team_audit = client.red_team_audits.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input_evaluation_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="name",
            scan_types=["vulnerability"],
            mode="light",
        )
        assert_matches_type(RedTeamAudit, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubClient) -> None:
        response = client.red_team_audits.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        red_team_audit = response.parse()
        assert_matches_type(RedTeamAudit, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubClient) -> None:
        with client.red_team_audits.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            red_team_audit = response.parse()
            assert_matches_type(RedTeamAudit, red_team_audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload(self, client: HubClient) -> None:
        red_team_audit = client.red_team_audits.upload(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content=b"raw file contents",
        )
        assert_matches_type(RedTeamAudit, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: HubClient) -> None:
        red_team_audit = client.red_team_audits.upload(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content=b"raw file contents",
            name="name",
            report=b"raw file contents",
            risk_model=b"raw file contents",
        )
        assert_matches_type(RedTeamAudit, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: HubClient) -> None:
        response = client.red_team_audits.with_raw_response.upload(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        red_team_audit = response.parse()
        assert_matches_type(RedTeamAudit, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: HubClient) -> None:
        with client.red_team_audits.with_streaming_response.upload(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            red_team_audit = response.parse()
            assert_matches_type(RedTeamAudit, red_team_audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: HubClient) -> None:
        red_team_audit = client.red_team_audits.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RedTeamAudit, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: HubClient) -> None:
        response = client.red_team_audits.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        red_team_audit = response.parse()
        assert_matches_type(RedTeamAudit, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: HubClient) -> None:
        with client.red_team_audits.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            red_team_audit = response.parse()
            assert_matches_type(RedTeamAudit, red_team_audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: HubClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audit_id` but received ''"):
            client.red_team_audits.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubClient) -> None:
        red_team_audit = client.red_team_audits.list()
        assert_matches_type(List[RedTeamAudit], red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubClient) -> None:
        red_team_audit = client.red_team_audits.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(List[RedTeamAudit], red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubClient) -> None:
        response = client.red_team_audits.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        red_team_audit = response.parse()
        assert_matches_type(List[RedTeamAudit], red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubClient) -> None:
        with client.red_team_audits.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            red_team_audit = response.parse()
            assert_matches_type(List[RedTeamAudit], red_team_audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubClient) -> None:
        red_team_audit = client.red_team_audits.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(None, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubClient) -> None:
        response = client.red_team_audits.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        red_team_audit = response.parse()
        assert_matches_type(None, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubClient) -> None:
        with client.red_team_audits.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            red_team_audit = response.parse()
            assert_matches_type(None, red_team_audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audit_id` but received ''"):
            client.red_team_audits.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_content(self, client: HubClient) -> None:
        red_team_audit = client.red_team_audits.retrieve_content(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RedTeamAuditContent, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_content(self, client: HubClient) -> None:
        response = client.red_team_audits.with_raw_response.retrieve_content(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        red_team_audit = response.parse()
        assert_matches_type(RedTeamAuditContent, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_content(self, client: HubClient) -> None:
        with client.red_team_audits.with_streaming_response.retrieve_content(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            red_team_audit = response.parse()
            assert_matches_type(RedTeamAuditContent, red_team_audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_content(self, client: HubClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audit_id` but received ''"):
            client.red_team_audits.with_raw_response.retrieve_content(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_logs(self, client: HubClient) -> None:
        red_team_audit = client.red_team_audits.retrieve_logs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RedTeamAuditLogs, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_logs_with_all_params(self, client: HubClient) -> None:
        red_team_audit = client.red_team_audits.retrieve_logs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after=0,
            limit=1,
        )
        assert_matches_type(RedTeamAuditLogs, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_logs(self, client: HubClient) -> None:
        response = client.red_team_audits.with_raw_response.retrieve_logs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        red_team_audit = response.parse()
        assert_matches_type(RedTeamAuditLogs, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_logs(self, client: HubClient) -> None:
        with client.red_team_audits.with_streaming_response.retrieve_logs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            red_team_audit = response.parse()
            assert_matches_type(RedTeamAuditLogs, red_team_audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_logs(self, client: HubClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audit_id` but received ''"):
            client.red_team_audits.with_raw_response.retrieve_logs(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_estimate(self, client: HubClient) -> None:
        estimate = client.red_team_audits.estimate()
        assert_matches_type(CreditEstimate, estimate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_estimate_with_all_params(self, client: HubClient) -> None:
        estimate = client.red_team_audits.estimate(
            mode="light",
        )
        assert_matches_type(CreditEstimate, estimate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_estimate(self, client: HubClient) -> None:
        response = client.red_team_audits.with_raw_response.estimate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        estimate = response.parse()
        assert_matches_type(CreditEstimate, estimate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_estimate(self, client: HubClient) -> None:
        with client.red_team_audits.with_streaming_response.estimate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            estimate = response.parse()
            assert_matches_type(CreditEstimate, estimate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRedTeamAudits:
    parametrize = pytest.mark.parametrize(
        "async_client",
        [False, True, {"http_client": "aiohttp"}],
        indirect=True,
        ids=["loose", "strict", "aiohttp"],
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubClient) -> None:
        red_team_audit = await async_client.red_team_audits.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RedTeamAudit, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubClient) -> None:
        red_team_audit = await async_client.red_team_audits.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input_evaluation_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="name",
            scan_types=["vulnerability"],
            mode="light",
        )
        assert_matches_type(RedTeamAudit, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubClient) -> None:
        response = await async_client.red_team_audits.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        red_team_audit = await response.parse()
        assert_matches_type(RedTeamAudit, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubClient) -> None:
        async with async_client.red_team_audits.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            red_team_audit = await response.parse()
            assert_matches_type(RedTeamAudit, red_team_audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncHubClient) -> None:
        red_team_audit = await async_client.red_team_audits.upload(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content=b"raw file contents",
        )
        assert_matches_type(RedTeamAudit, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncHubClient) -> None:
        red_team_audit = await async_client.red_team_audits.upload(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content=b"raw file contents",
            name="name",
            report=b"raw file contents",
            risk_model=b"raw file contents",
        )
        assert_matches_type(RedTeamAudit, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncHubClient) -> None:
        response = await async_client.red_team_audits.with_raw_response.upload(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        red_team_audit = await response.parse()
        assert_matches_type(RedTeamAudit, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncHubClient) -> None:
        async with async_client.red_team_audits.with_streaming_response.upload(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            red_team_audit = await response.parse()
            assert_matches_type(RedTeamAudit, red_team_audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHubClient) -> None:
        red_team_audit = await async_client.red_team_audits.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RedTeamAudit, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHubClient) -> None:
        response = await async_client.red_team_audits.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        red_team_audit = await response.parse()
        assert_matches_type(RedTeamAudit, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHubClient) -> None:
        async with async_client.red_team_audits.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            red_team_audit = await response.parse()
            assert_matches_type(RedTeamAudit, red_team_audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audit_id` but received ''"):
            await async_client.red_team_audits.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubClient) -> None:
        red_team_audit = await async_client.red_team_audits.list()
        assert_matches_type(List[RedTeamAudit], red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubClient) -> None:
        red_team_audit = await async_client.red_team_audits.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(List[RedTeamAudit], red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubClient) -> None:
        response = await async_client.red_team_audits.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        red_team_audit = await response.parse()
        assert_matches_type(List[RedTeamAudit], red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubClient) -> None:
        async with async_client.red_team_audits.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            red_team_audit = await response.parse()
            assert_matches_type(List[RedTeamAudit], red_team_audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubClient) -> None:
        red_team_audit = await async_client.red_team_audits.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(None, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubClient) -> None:
        response = await async_client.red_team_audits.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        red_team_audit = await response.parse()
        assert_matches_type(None, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubClient) -> None:
        async with async_client.red_team_audits.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            red_team_audit = await response.parse()
            assert_matches_type(None, red_team_audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audit_id` but received ''"):
            await async_client.red_team_audits.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_content(self, async_client: AsyncHubClient) -> None:
        red_team_audit = await async_client.red_team_audits.retrieve_content(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RedTeamAuditContent, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_content(self, async_client: AsyncHubClient) -> None:
        response = await async_client.red_team_audits.with_raw_response.retrieve_content(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        red_team_audit = await response.parse()
        assert_matches_type(RedTeamAuditContent, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_content(self, async_client: AsyncHubClient) -> None:
        async with async_client.red_team_audits.with_streaming_response.retrieve_content(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            red_team_audit = await response.parse()
            assert_matches_type(RedTeamAuditContent, red_team_audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_content(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audit_id` but received ''"):
            await async_client.red_team_audits.with_raw_response.retrieve_content(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_logs(self, async_client: AsyncHubClient) -> None:
        red_team_audit = await async_client.red_team_audits.retrieve_logs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RedTeamAuditLogs, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_logs_with_all_params(self, async_client: AsyncHubClient) -> None:
        red_team_audit = await async_client.red_team_audits.retrieve_logs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after=0,
            limit=1,
        )
        assert_matches_type(RedTeamAuditLogs, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_logs(self, async_client: AsyncHubClient) -> None:
        response = await async_client.red_team_audits.with_raw_response.retrieve_logs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        red_team_audit = await response.parse()
        assert_matches_type(RedTeamAuditLogs, red_team_audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_logs(self, async_client: AsyncHubClient) -> None:
        async with async_client.red_team_audits.with_streaming_response.retrieve_logs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            red_team_audit = await response.parse()
            assert_matches_type(RedTeamAuditLogs, red_team_audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_logs(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audit_id` but received ''"):
            await async_client.red_team_audits.with_raw_response.retrieve_logs(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_estimate(self, async_client: AsyncHubClient) -> None:
        estimate = await async_client.red_team_audits.estimate()
        assert_matches_type(CreditEstimate, estimate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_estimate_with_all_params(self, async_client: AsyncHubClient) -> None:
        estimate = await async_client.red_team_audits.estimate(
            mode="regular",
        )
        assert_matches_type(CreditEstimate, estimate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_estimate(self, async_client: AsyncHubClient) -> None:
        response = await async_client.red_team_audits.with_raw_response.estimate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        estimate = await response.parse()
        assert_matches_type(CreditEstimate, estimate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_estimate(self, async_client: AsyncHubClient) -> None:
        async with async_client.red_team_audits.with_streaming_response.estimate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            estimate = await response.parse()
            assert_matches_type(CreditEstimate, estimate, path=["response"])

        assert cast(Any, response.is_closed) is True
