import importlib.metadata

import giskard_hub


def test_version_is_resolved():
    """Verify that __version__ is resolved from package metadata and is not 'unknown'."""
    pyproject_version = importlib.metadata.version("giskard-hub")
    assert giskard_hub.__version__ == pyproject_version
    assert giskard_hub.__version__ != "unknown"
