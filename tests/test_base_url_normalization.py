from giskard_hub import HubClient, AsyncHubClient
from giskard_hub._client import _normalize_base_url

API_KEY = "test-key"


class TestNormalizeBaseUrl:
    def test_appends_suffix_when_missing(self) -> None:
        assert _normalize_base_url("http://localhost:8080", auto_add_api_suffix=True) == "http://localhost:8080/_api"

    def test_does_not_double_append_suffix(self) -> None:
        assert (
            _normalize_base_url("http://localhost:8080/_api", auto_add_api_suffix=True) == "http://localhost:8080/_api"
        )

    def test_strips_trailing_slash_before_appending(self) -> None:
        assert _normalize_base_url("http://localhost:8080/", auto_add_api_suffix=True) == "http://localhost:8080/_api"

    def test_strips_trailing_slash_without_appending(self) -> None:
        assert _normalize_base_url("http://localhost:8080/", auto_add_api_suffix=False) == "http://localhost:8080"

    def test_disabled_does_not_append_suffix(self) -> None:
        assert _normalize_base_url("http://localhost:8080", auto_add_api_suffix=False) == "http://localhost:8080"


class TestHubClientBaseUrl:
    def test_suffix_added_by_default(self) -> None:
        client = HubClient(base_url="http://localhost:8080", api_key=API_KEY)
        assert str(client.base_url).rstrip("/") == "http://localhost:8080/_api"

    def test_suffix_not_duplicated(self) -> None:
        client = HubClient(base_url="http://localhost:8080/_api", api_key=API_KEY)
        assert str(client.base_url).rstrip("/") == "http://localhost:8080/_api"

    def test_suffix_not_added_when_disabled(self) -> None:
        client = HubClient(base_url="http://localhost:8080", api_key=API_KEY, auto_add_api_suffix=False)
        assert str(client.base_url).rstrip("/") == "http://localhost:8080"

    def test_trailing_slash_stripped(self) -> None:
        client = HubClient(base_url="http://localhost:8080/", api_key=API_KEY)
        assert str(client.base_url).rstrip("/") == "http://localhost:8080/_api"


class TestAsyncHubClientBaseUrl:
    def test_suffix_added_by_default(self) -> None:
        client = AsyncHubClient(base_url="http://localhost:8080", api_key=API_KEY)
        assert str(client.base_url).rstrip("/") == "http://localhost:8080/_api"

    def test_suffix_not_duplicated(self) -> None:
        client = AsyncHubClient(base_url="http://localhost:8080/_api", api_key=API_KEY)
        assert str(client.base_url).rstrip("/") == "http://localhost:8080/_api"

    def test_suffix_not_added_when_disabled(self) -> None:
        client = AsyncHubClient(base_url="http://localhost:8080", api_key=API_KEY, auto_add_api_suffix=False)
        assert str(client.base_url).rstrip("/") == "http://localhost:8080"

    def test_trailing_slash_stripped(self) -> None:
        client = AsyncHubClient(base_url="http://localhost:8080/", api_key=API_KEY)
        assert str(client.base_url).rstrip("/") == "http://localhost:8080/_api"
