from typing import Any, List, Iterable

import pytest

from giskard_hub.types.chat import ChatMessage
from giskard_hub.types.common import TaskState
from giskard_hub.types.test_case import TestCase
from giskard_hub.types.evaluation import Evaluation
from giskard_hub.resources.helpers import HelpersResource, AsyncHelpersResource


class DummyStateful:
    def __init__(self, id: str, state: TaskState) -> None:
        self.id = id
        self._state: TaskState = state

    @property
    def state(self) -> TaskState:
        return self._state


class DummySyncResource:
    def __init__(self, states: Iterable[TaskState]) -> None:
        self._states: List[TaskState] = list(states)
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
    def __init__(self, states: Iterable[TaskState]) -> None:
        self._states: List[TaskState] = list(states)
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

    def _make_retriever(self, _: Any) -> Any:  # type: ignore[override]
        return self._resource.retrieve


class DummyAsyncHelpers(AsyncHelpersResource):
    def __init__(self, resource: DummyAsyncResource) -> None:
        # bypass parent init; we don't need a real client
        self._resource = resource

    def _make_retriever(self, _: Any) -> Any:  # type: ignore[override]
        return self._resource.retrieve


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


def test_wait_for_completion_sync_timeout() -> None:
    states: List[TaskState] = ["running"] * 3
    helper = DummySyncHelpers(DummySyncResource(states))
    entity = DummyStateful("id-1", "running")

    with pytest.raises(RuntimeError):
        helper.wait_for_completion(
            entity,
            poll_interval=0,
            max_retries=2,
        )


@pytest.mark.asyncio
async def test_wait_for_completion_async_timeout() -> None:
    states: List[TaskState] = ["running"] * 3
    helper = DummyAsyncHelpers(DummyAsyncResource(states))
    entity = DummyStateful("id-1", "running")

    with pytest.raises(RuntimeError):
        await helper.wait_for_completion(
            entity,
            poll_interval=0,
            max_retries=2,
        )


def test_wait_for_completion_sync_error_no_raise() -> None:
    helper = DummySyncHelpers(DummySyncResource(["running", "error"]))
    entity = DummyStateful("id-1", "running")

    result = helper.wait_for_completion(
        entity,
        poll_interval=0,
        max_retries=3,
        error_states={"error"},
        raise_on_error=False,
    )
    assert result.state == "error"


@pytest.mark.asyncio
async def test_wait_for_completion_async_error_no_raise() -> None:
    helper = DummyAsyncHelpers(DummyAsyncResource(["running", "error"]))
    entity = DummyStateful("id-1", "running")

    result = await helper.wait_for_completion(
        entity,
        poll_interval=0,
        max_retries=3,
        error_states={"error"},
        raise_on_error=False,
    )
    assert result.state == "error"


def test_wait_for_completion_sync_with_extra_retrieve_kwargs() -> None:
    """Verify that a retriever requiring extra kwargs (e.g. evaluation_id) works."""
    captured_kwargs: List[dict[str, Any]] = []

    class ResourceWithExtraKwargs:
        def __init__(self, states: Iterable[TaskState]) -> None:
            self._states = list(states)
            self._index = 0

        def retrieve(self, _id: str, *, evaluation_id: str) -> DummyStateful:
            captured_kwargs.append({"evaluation_id": evaluation_id})
            if self._index < len(self._states) - 1:
                state = self._states[self._index]
                self._index += 1
            else:
                state = self._states[-1]
            return DummyStateful(_id, state)

    from functools import partial

    resource = ResourceWithExtraKwargs(["running", "finished"])
    retriever = partial(resource.retrieve, evaluation_id="eval-42")

    class HelperWithPartial(HelpersResource):
        def __init__(self) -> None:
            pass

        def _make_retriever(self, _: Any) -> Any:  # type: ignore[override]
            return retriever

    helper = HelperWithPartial()
    entity = DummyStateful("id-1", "running")

    result = helper.wait_for_completion(entity, poll_interval=0, max_retries=5)

    assert result.state == "finished"  # type: ignore[comparison-overlap]
    assert all(kw["evaluation_id"] == "eval-42" for kw in captured_kwargs)


@pytest.mark.asyncio
async def test_wait_for_completion_async_with_extra_retrieve_kwargs() -> None:
    """Verify that an async retriever requiring extra kwargs (e.g. evaluation_id) works."""
    captured_kwargs: List[dict[str, Any]] = []

    class AsyncResourceWithExtraKwargs:
        def __init__(self, states: Iterable[TaskState]) -> None:
            self._states = list(states)
            self._index = 0

        async def retrieve(self, _id: str, *, evaluation_id: str) -> DummyStateful:
            captured_kwargs.append({"evaluation_id": evaluation_id})
            if self._index < len(self._states) - 1:
                state = self._states[self._index]
                self._index += 1
            else:
                state = self._states[-1]
            return DummyStateful(_id, state)

    from functools import partial

    resource = AsyncResourceWithExtraKwargs(["running", "finished"])
    retriever = partial(resource.retrieve, evaluation_id="eval-42")

    class AsyncHelperWithPartial(AsyncHelpersResource):
        def __init__(self) -> None:
            pass

        def _make_retriever(self, _: Any) -> Any:  # type: ignore[override]
            return retriever

    helper = AsyncHelperWithPartial()
    entity = DummyStateful("id-1", "running")

    result = await helper.wait_for_completion(entity, poll_interval=0, max_retries=5)

    assert result.state == "finished"  # type: ignore[comparison-overlap]
    assert all(kw["evaluation_id"] == "eval-42" for kw in captured_kwargs)


# ---------------------------------------------------------------------------
# evaluate helpers (unit-style tests with fake clients)
# ---------------------------------------------------------------------------


class DummyEvaluations:
    def __init__(self, remote_eval: Evaluation, local_eval: Evaluation, entries: list[Any]) -> None:
        self.remote_eval = remote_eval
        self.local_eval = local_eval
        self.entries = entries
        self.create_kwargs: dict[str, Any] | None = None
        self.create_local_kwargs: dict[str, Any] | None = None

        class _Results:
            def __init__(self, outer: "DummyEvaluations") -> None:
                self._outer = outer
                self.submissions: list[dict[str, Any]] = []

            def list(self, *, evaluation_id: str, include: list[str]) -> list[Any]:
                assert "test_case" in include
                assert evaluation_id == outer.local_eval.id  # type: ignore[union-attr]
                return outer.entries

            def submit_local_output(self, *, result_id: str, evaluation_id: str, agent_output: dict[str, Any]) -> None:
                self.submissions.append(
                    {
                        "result_id": result_id,
                        "evaluation_id": evaluation_id,
                        "agent_output": agent_output,
                    }
                )

        outer = self
        self.results = _Results(outer)

    def create(self, **kwargs: Any) -> Evaluation:
        self.create_kwargs = kwargs
        return self.remote_eval

    def create_local(self, **kwargs: Any) -> Evaluation:
        self.create_local_kwargs = kwargs
        return self.local_eval


class AsyncDummyEvaluations:
    def __init__(self, remote_eval: Evaluation, local_eval: Evaluation, entries: list[Any]) -> None:
        self.remote_eval = remote_eval
        self.local_eval = local_eval
        self.entries = entries
        self.create_kwargs: dict[str, Any] | None = None
        self.create_local_kwargs: dict[str, Any] | None = None

        class _Results:
            def __init__(self, outer: "AsyncDummyEvaluations") -> None:
                self._outer = outer
                self.submissions: list[dict[str, Any]] = []

            async def list(self, *, evaluation_id: str, include: list[str]) -> list[Any]:
                assert "test_case" in include
                assert evaluation_id == outer.local_eval.id  # type: ignore[union-attr]
                return outer.entries

            async def submit_local_output(
                self, *, result_id: str, evaluation_id: str, agent_output: dict[str, Any]
            ) -> None:
                self.submissions.append(
                    {
                        "result_id": result_id,
                        "evaluation_id": evaluation_id,
                        "agent_output": agent_output,
                    }
                )

        outer = self
        self.results = _Results(outer)

    async def create(self, **kwargs: Any) -> Evaluation:
        self.create_kwargs = kwargs
        return self.remote_eval

    async def create_local(self, **kwargs: Any) -> Evaluation:
        self.create_local_kwargs = kwargs
        return self.local_eval


class DummyClient:
    def __init__(self, evaluations: DummyEvaluations) -> None:
        self.evaluations = evaluations


class AsyncDummyClient:
    def __init__(self, evaluations: AsyncDummyEvaluations) -> None:
        self.evaluations = evaluations


class HelpersWithDummyClient(HelpersResource):
    _client: Any

    def __init__(self, client: DummyClient) -> None:  # type: ignore[override]
        # Bypass parent initialisation; only `_client` is used in `evaluate`.
        object.__setattr__(self, "_client", client)


class AsyncHelpersWithDummyClient(AsyncHelpersResource):
    _client: Any

    def __init__(self, client: AsyncDummyClient) -> None:  # type: ignore[override]
        object.__setattr__(self, "_client", client)


def _make_evaluation(eval_id: str = "eval-1") -> Evaluation:
    # Use minimal construction; other fields aren't inspected in these tests.
    return Evaluation.model_construct(id=eval_id)  # type: ignore[arg-type]


def _make_test_case(messages: list[ChatMessage]) -> TestCase:
    return TestCase.model_construct(id="tc-1", messages=messages)  # type: ignore[arg-type]


def _make_result_entry(test_case: TestCase, result_id: str = "res-1") -> Any:
    class Entry:
        def __init__(self, id: str, test_case: TestCase) -> None:
            self.id = id
            self.test_case = test_case

    return Entry(result_id, test_case)


def test_evaluate_remote_with_ids() -> None:
    remote_eval = _make_evaluation("remote-eval")
    local_eval = _make_evaluation("local-eval")
    evaluations = DummyEvaluations(remote_eval, local_eval, entries=[])
    client = DummyClient(evaluations)
    helpers = HelpersWithDummyClient(client)  # type: ignore[arg-type]

    result = helpers.evaluate(
        agent="agent-1",
        dataset="ds-1",
        project="proj-1",
        name="my-eval",
        tags=["tag-1"],
    )

    assert result is remote_eval
    assert evaluations.create_kwargs is not None
    assert evaluations.create_kwargs["project_id"] == "proj-1"
    assert evaluations.create_kwargs["agent_id"] == "agent-1"
    assert evaluations.create_kwargs["name"] == "my-eval"
    assert evaluations.create_kwargs["dataset_id"] == "ds-1"
    assert evaluations.create_kwargs["tags"] == ["tag-1"]


def test_evaluate_remote_missing_project_raises() -> None:
    remote_eval = _make_evaluation()
    local_eval = _make_evaluation()
    evaluations = DummyEvaluations(remote_eval, local_eval, entries=[])
    client = DummyClient(evaluations)
    helpers = HelpersWithDummyClient(client)  # type: ignore[arg-type]

    with pytest.raises(ValueError, match="Project is required"):
        helpers.evaluate(
            agent="agent-1",
            dataset="ds-1",
            project=None,
        )


def test_evaluate_local_with_callable_str_output() -> None:
    remote_eval = _make_evaluation()
    local_eval = _make_evaluation("local-eval")

    messages = [ChatMessage(role="user", content="hi")]
    test_case = _make_test_case(messages)
    entry = _make_result_entry(test_case, "res-1")

    evaluations = DummyEvaluations(remote_eval, local_eval, entries=[entry])
    client = DummyClient(evaluations)
    helpers = HelpersWithDummyClient(client)  # type: ignore[arg-type]

    def agent_fn(msgs: list[ChatMessage]) -> str:
        assert msgs == messages
        return "hello"

    result = helpers.evaluate(
        agent=agent_fn,
        dataset="ds-1",
        name="local-eval",
        tags=["tag-1"],
    )

    assert result is local_eval
    assert evaluations.create_local_kwargs is not None
    assert evaluations.create_local_kwargs["agent_info"]["name"] == agent_fn.__name__

    submissions = evaluations.results.submissions
    assert len(submissions) == 1
    submitted = submissions[0]["agent_output"]
    assert submitted["response"]["content"] == "hello"
    assert submitted["response"]["role"] == "assistant"


def test_evaluate_local_with_callable_agent_output_dict() -> None:
    remote_eval = _make_evaluation()
    local_eval = _make_evaluation("local-eval")

    messages = [ChatMessage(role="user", content="hi")]
    test_case = _make_test_case(messages)
    entry = _make_result_entry(test_case, "res-1")

    evaluations = DummyEvaluations(remote_eval, local_eval, entries=[entry])
    client = DummyClient(evaluations)
    helpers = HelpersWithDummyClient(client)  # type: ignore[arg-type]

    def agent_fn(msgs: list[ChatMessage]) -> dict[str, Any]:
        assert msgs == messages
        # Dict with AgentOutput-like shape; should be accepted by the helper.
        return {
            "response": {
                "role": "assistant",
                "content": "dict response",
            }
        }

    result = helpers.evaluate(
        agent=agent_fn,  # type: ignore[arg-type]
        dataset="ds-1",
    )

    assert result is local_eval
    submissions = evaluations.results.submissions
    assert len(submissions) == 1
    submitted = submissions[0]["agent_output"]
    assert submitted["response"]["content"] == "dict response"
    assert submitted["response"]["role"] == "assistant"


# ---------------------------------------------------------------------------
# async evaluate helpers
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_evaluate_remote_with_ids_async() -> None:
    remote_eval = _make_evaluation("remote-eval")
    local_eval = _make_evaluation("local-eval")
    evaluations = AsyncDummyEvaluations(remote_eval, local_eval, entries=[])
    client = AsyncDummyClient(evaluations)
    helpers = AsyncHelpersWithDummyClient(client)  # type: ignore[arg-type]

    result = await helpers.evaluate(
        agent="agent-1",
        dataset="ds-1",
        project="proj-1",
        name="my-eval",
        tags=["tag-1"],
    )

    assert result is remote_eval
    assert evaluations.create_kwargs is not None
    assert evaluations.create_kwargs["project_id"] == "proj-1"
    assert evaluations.create_kwargs["agent_id"] == "agent-1"
    assert evaluations.create_kwargs["name"] == "my-eval"
    assert evaluations.create_kwargs["dataset_id"] == "ds-1"
    assert evaluations.create_kwargs["tags"] == ["tag-1"]


@pytest.mark.asyncio
async def test_evaluate_remote_missing_project_raises_async() -> None:
    remote_eval = _make_evaluation()
    local_eval = _make_evaluation()
    evaluations = AsyncDummyEvaluations(remote_eval, local_eval, entries=[])
    client = AsyncDummyClient(evaluations)
    helpers = AsyncHelpersWithDummyClient(client)  # type: ignore[arg-type]

    with pytest.raises(ValueError, match="Project is required"):
        await helpers.evaluate(
            agent="agent-1",
            dataset="ds-1",
            project=None,
        )


@pytest.mark.asyncio
async def test_evaluate_local_with_callable_str_output_async() -> None:
    remote_eval = _make_evaluation()
    local_eval = _make_evaluation("local-eval")

    messages = [ChatMessage(role="user", content="hi")]
    test_case = _make_test_case(messages)
    entry = _make_result_entry(test_case, "res-1")

    evaluations = AsyncDummyEvaluations(remote_eval, local_eval, entries=[entry])
    client = AsyncDummyClient(evaluations)
    helpers = AsyncHelpersWithDummyClient(client)  # type: ignore[arg-type]

    def agent_fn(msgs: list[ChatMessage]) -> str:
        assert msgs == messages
        return "hello"

    result = await helpers.evaluate(
        agent=agent_fn,
        dataset="ds-1",
        name="local-eval",
        tags=["tag-1"],
    )

    assert result is local_eval
    assert evaluations.create_local_kwargs is not None
    assert evaluations.create_local_kwargs["agent_info"]["name"] == agent_fn.__name__

    submissions = evaluations.results.submissions
    assert len(submissions) == 1
    submitted = submissions[0]["agent_output"]
    assert submitted["response"]["content"] == "hello"
    assert submitted["response"]["role"] == "assistant"


@pytest.mark.asyncio
async def test_evaluate_local_with_callable_agent_output_dict_async() -> None:
    remote_eval = _make_evaluation()
    local_eval = _make_evaluation("local-eval")

    messages = [ChatMessage(role="user", content="hi")]
    test_case = _make_test_case(messages)
    entry = _make_result_entry(test_case, "res-1")

    evaluations = AsyncDummyEvaluations(remote_eval, local_eval, entries=[entry])
    client = AsyncDummyClient(evaluations)
    helpers = AsyncHelpersWithDummyClient(client)  # type: ignore[arg-type]

    def agent_fn(msgs: list[ChatMessage]) -> dict[str, Any]:
        assert msgs == messages
        return {
            "response": {
                "role": "assistant",
                "content": "dict response",
            }
        }

    result = await helpers.evaluate(
        agent=agent_fn,  # type: ignore[arg-type]
        dataset="ds-1",
    )

    assert result is local_eval
    submissions = evaluations.results.submissions
    assert len(submissions) == 1
    submitted = submissions[0]["agent_output"]
    assert submitted["response"]["content"] == "dict response"
    assert submitted["response"]["role"] == "assistant"
