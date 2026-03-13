from __future__ import annotations

from .._models import BaseModel
from .._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["HelpersResource", "AsyncHelpersResource"]


class HelpersResource(SyncAPIResource):
    def wait_for_completion(self, entity: BaseModel, *, poll_interval: float = 1.0) -> BaseModel:
        """
        Wait for the given entity to reach a non running state and return the refreshed entity.
        """
        pass

    def print_metrics(self, entity: BaseModel) -> None:
        """
        Pretty-print metrics for the given entity.

        Implementation is intentionally left for future versions.
        """
        pass

    def evaluate(self, *args: object, **kwargs: object) -> None:
        """
        Run a combined remote and local evaluation.

        Implementation is intentionally left for future versions.
        """
        pass


class AsyncHelpersResource(AsyncAPIResource):
    async def wait_for_completion(self, entity: BaseModel, *, poll_interval: float = 1.0) -> BaseModel:
        """
        Async variant of ``HelpersResource.wait_for_completion``.
        """
        pass

    async def print_metrics(self, entity: BaseModel) -> None:
        """
        Async variant of ``HelpersResource.print_metrics``.
        """
        pass

    async def evaluate(self, *args: object, **kwargs: object) -> None:
        """
        Async variant of ``HelpersResource.evaluate``.
        """
        pass
