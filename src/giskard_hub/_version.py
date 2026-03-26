import importlib.metadata

__title__ = "giskard_hub"
try:
    __version__ = importlib.metadata.version("giskard-hub")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"
