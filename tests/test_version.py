import importlib.metadata

import giskard_hub


def test_version_matches_pyproject():
    """Verify that _version.py __version__ matches the version declared in pyproject.toml."""
    pyproject_version = importlib.metadata.version("giskard-hub")
    assert giskard_hub.__version__ == pyproject_version
