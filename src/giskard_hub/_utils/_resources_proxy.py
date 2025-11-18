from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `giskard_hub.resources` module.

    This is used so that we can lazily import `giskard_hub.resources` only when
    needed *and* so that users can just import `giskard_hub` and reference `giskard_hub.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("giskard_hub.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
