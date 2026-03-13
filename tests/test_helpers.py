from __future__ import annotations

from typing import List, Iterable

import pytest

from giskard_hub.resources.helpers import StatefulEntity, HelpersResource, AsyncHelpersResource


class DummyStateful(StatefulEntity):
    def __init__(self, id: str, state: str) -> None:
        self.id = id
        self.state = state  # type: ignore[assignment]


class DummySyncResource:
    def __init__(self, states: Iterable[str]) -> None:
        self._states: List[str] = list(states)
        self._index = 0

    def retrieve(self, _id: str) -> DummyStateful:
        # Return successive states until we run out, then repeat last state
        if self._index < len(self._states) - 1:
            state = self._states[self._index]
            self._index += 1
        else:
            state = self._states[-1]
        return DummyStateful(_id, state)


class DummyAsyncResource:
    def __init__(self, states: Iterable[str]) -> None:
        self._states: List[str] = list(states)
        self._index = 0

    async def retrieve(self, _id: str) -> DummyStateful:
        if self._index < len(self._states) - 1:
            state = self._states[self._index]
            self._index += 1
        else:
            state = self._states[-1]
        return DummyStateful(_id, state)


class DummySyncHelpers(HelpersResource):
    def __init__(self, resource: DummySyncResource) -> None:
        # bypass parent init; we don't need a real client
        self._resource = resource

    def _map_entity_to_resource(self, _: DummyStateful) -> DummySyncResource:  # type: ignore[override]
        return self._resource


class DummyAsyncHelpers(AsyncHelpersResource):
    def __init__(self, resource: DummyAsyncResource) -> None:
        # bypass parent init; we don't need a real client
        self._resource = resource

    def _map_entity_to_resource(self, _: DummyStateful) -> DummyAsyncResource:  # type: ignore[override]
        return self._resource


def test_wait_for_completion_sync_success() -> None:
    helper = DummySyncHelpers(DummySyncResource(["running", "running", "finished"]))
    entity = DummyStateful("id-1", "running")

    result = helper.wait_for_completion(
        entity,
        poll_interval=0,
        max_retries=5,
        running_states={"running"},
        error_states={"error"},
    )

    assert isinstance(result, DummyStateful)
    assert result.state == "finished"  # type: ignore[comparison-overlap]


def test_wait_for_completion_sync_error_state_raises() -> None:
    helper = DummySyncHelpers(DummySyncResource(["running", "error"]))
    entity = DummyStateful("id-1", "running")

    with pytest.raises(ValueError):
        helper.wait_for_completion(
            entity,
            poll_interval=0,
            max_retries=3,
            running_states={"running"},
            error_states={"error"},
            raise_on_error=True,
        )


@pytest.mark.asyncio
async def test_wait_for_completion_async_success() -> None:
    helper = DummyAsyncHelpers(DummyAsyncResource(["running", "finished"]))
    entity = DummyStateful("id-1", "running")

    result = await helper.wait_for_completion(
        entity,
        poll_interval=0,
        max_retries=5,
        running_states={"running"},
        error_states={"error"},
    )

    assert isinstance(result, DummyStateful)
    assert result.state == "finished"  # type: ignore[comparison-overlap]


@pytest.mark.asyncio
async def test_wait_for_completion_async_error_state_raises() -> None:
    helper = DummyAsyncHelpers(DummyAsyncResource(["running", "error"]))
    entity = DummyStateful("id-1", "running")

    with pytest.raises(ValueError):
        await helper.wait_for_completion(
            entity,
            poll_interval=0,
            max_retries=3,
            running_states={"running"},
            error_states={"error"},
            raise_on_error=True,
        )
