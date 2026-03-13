from __future__ import annotations

import time
from typing import TYPE_CHECKING, Any, cast

import anyio

from ._response import BaseAPIResponse

if TYPE_CHECKING:
    from ._client import HubClient, AsyncHubClient


class SyncAPIResource:
    _client: HubClient

    def __init__(self, client: HubClient) -> None:
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._put = client.put
        self._delete = client.delete
        self._get_api_list = client.get_api_list

    def _sleep(self, seconds: float) -> None:
        time.sleep(seconds)

    def _unwrap(self, result: Any) -> Any:
        """Unwrap a JSON:API response wrapper, returning ``result.data``.

        When the request was made via ``.with_raw_response`` or
        ``.with_streaming_response``, *result* is an HTTP-level
        ``BaseAPIResponse`` and is returned as-is so the raw-response
        contract is preserved.
        """
        if isinstance(result, BaseAPIResponse):
            return cast(Any, result)
        return result.data

    def _unwrap_paginated(self, result: Any, include_metadata: bool) -> Any:
        """Unwrap a paginated JSON:API response wrapper.

        When *include_metadata* is true the return value is a
        ``(data, metadata)`` tuple; otherwise only ``data`` is returned.

        Raw / streaming responses are passed through unchanged.
        """
        if isinstance(result, BaseAPIResponse):
            return cast(Any, result)
        if include_metadata:
            return result.data, result.metadata
        return result.data


class AsyncAPIResource:
    _client: AsyncHubClient

    def __init__(self, client: AsyncHubClient) -> None:
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._put = client.put
        self._delete = client.delete
        self._get_api_list = client.get_api_list

    async def _sleep(self, seconds: float) -> None:
        await anyio.sleep(seconds)

    def _unwrap(self, result: Any) -> Any:
        """Unwrap a JSON:API response wrapper, returning ``result.data``.

        When the request was made via ``.with_raw_response`` or
        ``.with_streaming_response``, *result* is an HTTP-level
        ``BaseAPIResponse`` and is returned as-is so the raw-response
        contract is preserved.
        """
        if isinstance(result, BaseAPIResponse):
            return cast(Any, result)
        return result.data

    def _unwrap_paginated(self, result: Any, include_metadata: bool) -> Any:
        """Unwrap a paginated JSON:API response wrapper.

        When *include_metadata* is true the return value is a
        ``(data, metadata)`` tuple; otherwise only ``data`` is returned.

        Raw / streaming responses are passed through unchanged.
        """
        if isinstance(result, BaseAPIResponse):
            return cast(Any, result)
        if include_metadata:
            return result.data, result.metadata
        return result.data
