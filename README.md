# Giskard Hub Python SDK

<!-- prettier-ignore -->
[![PyPI version](https://img.shields.io/pypi/v/giskard-hub.svg?label=pypi%20(stable))](https://pypi.org/project/giskard-hub/)

The official Python SDK for Giskard Hub. Use it to define agents, manage projects and datasets,
run evaluations and vulnerability scans, schedule recurring runs, and automate your LLM quality
workflow from Python.

The package includes type definitions for all request params and response fields, and offers both
synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

It was initially generated with [Stainless](https://www.stainless.com/).

## Documentation

- [Documentation website](https://docs.giskard.ai/hub/sdk)
- [Quickstart](https://docs.giskard.ai/hub/sdk/quickstart)
- [How-to guides](https://docs.giskard.ai/hub/sdk/guides/projects)
- [API reference](https://docs.giskard.ai/hub/sdk/reference)
- [Migration guide (for SDK v2 users)](https://docs.giskard.ai/hub/sdk/migration)

## Installation

```sh
pip install giskard-hub
```

To install the latest unreleased changes directly from GitHub:

```sh
pip install git+ssh://git@github.com/Giskard-AI/giskard-hub-python.git
```

## Configuration

Set the Hub base URL and API key before creating a client:

```sh
export GISKARD_HUB_BASE_URL="https://your-hub-instance"
export GISKARD_HUB_API_KEY="your-api-key"
```

`HubClient()` and `AsyncHubClient()` automatically read these environment variables.

## Quickstart

```python
from giskard_hub import HubClient

hub = HubClient()

project = hub.projects.list()[0]

scan = hub.scans.create(
    project_id=project.id,
    agent_id="<agent-id>",
    dataset_id="<dataset-id>",
)

print(scan)
```

If you prefer, you can also pass `api_key` and `base_url` directly to the client constructor.
For local development, we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
to load `GISKARD_HUB_BASE_URL` and `GISKARD_HUB_API_KEY` from a local `.env` file
so that secrets are not stored in source control.

## Helpers

The SDK exposes convenience helpers on `hub.helpers` for common workflows such as running
evaluations over a dataset, waiting for asynchronous jobs to finish, and printing evaluation or
scan metrics.

For example, to run an evaluation with a local Python callable:

```python
from giskard_hub import HubClient
from giskard_hub.type import ChatMessage

hub = HubClient()

def my_agent(messages: list[ChatMessage]) -> str:
    # Your agent logic here
    return "Hello from my agent"

evaluation = hub.helpers.evaluate(
    agent=my_agent,
    dataset="dataset-id",
    name="My local evaluation",
)

completed = hub.helpers.wait_for_completion(evaluation)
hub.helpers.print_metrics(completed)
```

## Async usage

Simply import `AsyncHubClient` instead of `HubClient` and use `await` with each API call:

```python
import asyncio
from giskard_hub import AsyncHubClient

client = AsyncHubClient()


async def main() -> None:
    projects = await client.projects.list()
    print(projects)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

### With aiohttp

By default, the async client uses `httpx` for HTTP requests. However, for improved concurrency performance you may also use `aiohttp` as the HTTP backend.

You can enable this by installing `aiohttp`:

```sh
# install from pypi
pip install 'giskard-hub[aiohttp]'
```

Then you can enable it by instantiating the client with `http_client=DefaultAioHttpClient()`:

```python
import asyncio
from giskard_hub import DefaultAioHttpClient
from giskard_hub import AsyncHubClient


async def main() -> None:
    async with AsyncHubClient(
        http_client=DefaultAioHttpClient(),
    ) as client:
        projects = await client.projects.list()
        print(projects.data)


asyncio.run(main())
```

## Using types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev) which also provide helper methods for things like:

- Serializing back into JSON, `model.to_json()`
- Converting to a dictionary, `model.to_dict()`

Typed requests and responses provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `basic`.

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from giskard_hub import HubClient

client = HubClient()

updated_dataset = client.datasets.update(
    dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    status={"total": 0},
)
print(updated_dataset.status)
```

## File uploads

Request parameters that correspond to file uploads can be passed as `bytes`, or a [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) instance or a tuple of `(filename, contents, media type)`.

```python
from pathlib import Path
from giskard_hub import HubClient

client = HubClient()

client.knowledge_bases.create(
    name="My Knowledge Base",
    project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
    file=Path("/path/to/file.jsonl"),
)
```

The async client uses the exact same interface. If you pass a [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) instance, the file contents will be read asynchronously automatically.

## Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `giskard_hub.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `giskard_hub.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `giskard_hub.APIError`.

```python
import giskard_hub
from giskard_hub import HubClient

client = HubClient()

try:
    client.projects.list()
except giskard_hub.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except giskard_hub.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except giskard_hub.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as follows:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from giskard_hub import HubClient

# Configure the default for all requests:
client = HubClient(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).projects.list()
```

### Timeouts

By default requests time out after 1 minute. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration) object:

```python
from giskard_hub import HubClient

# Configure the default for all requests:
client = HubClient(
    # 20 seconds (default is 1 minute)
    timeout=20.0,
)

# More granular control:
client = HubClient(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).projects.list()
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

## Advanced

### Logging

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `GISKARD_HUB_LOG` to `info`.

```shell
$ export GISKARD_HUB_LOG=info
```

Or to `debug` for more verbose logging.

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Accessing raw response data (e.g. headers)

The "raw" Response object can be accessed by prefixing `.with_raw_response.` to any HTTP method call, e.g.,

```py
from giskard_hub import HubClient

client = HubClient()
response = client.projects.with_raw_response.list()
print(response.headers.get('X-My-Header'))

projects = response.parse()  # get the object that `projects.list()` would have returned
print(projects)
```

These methods return an [`APIResponse`](https://github.com/stainless-sdks/giskard-hub-python/tree/main/src/giskard_hub/_response.py) object.

The async client returns an [`AsyncAPIResponse`](https://github.com/stainless-sdks/giskard-hub-python/tree/main/src/giskard_hub/_response.py) with the same structure, the only difference being `await`able methods for reading the response content.

#### `.with_streaming_response`

The above interface eagerly reads the full response body when you make the request, which may not always be what you want.

To stream the response body, use `.with_streaming_response` instead, which requires a context manager and only reads the response body once you call `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` or `.parse()`. In the async client, these are async methods.

```python
with client.projects.with_streaming_response.list() as response:
    print(response.headers.get("X-My-Header"))

    for line in response.iter_lines():
        print(line)
```

The context manager is required so that the response will reliably be closed.

### Making custom/undocumented requests

This library is typed for convenient access to the documented API.

If you need to access undocumented endpoints, params, or response properties, the library can still be used.

#### Undocumented endpoints

To make requests to undocumented endpoints, you can make requests using `client.get`, `client.post`, and other
http verbs. Options on the client will be respected (such as retries) when making this request.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Undocumented request params

If you want to explicitly send an extra param, you can do so with the `extra_query`, `extra_body`, and `extra_headers` request
options.

#### Undocumented response properties

To access undocumented response properties, you can access the extra fields like `response.unknown_prop`. You
can also get all the extra fields on the Pydantic model as a dict with
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for [proxies](https://www.python-httpx.org/advanced/proxies/)
- Custom [transports](https://www.python-httpx.org/advanced/transports/)
- Additional [advanced](https://www.python-httpx.org/advanced/clients/) functionality

```python
import httpx
from giskard_hub import HubClient, DefaultHttpxClient

client = HubClient(
    # Or use the `GISKARD_HUB_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

You can also customize the client on a per-request basis by using `with_options()`:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Managing HTTP resources

By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

```py
from giskard_hub import HubClient

with HubClient() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals.)_
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/Giskard-AI/giskard-hub-python/issues) with questions, bugs, or suggestions.

### Determining the installed version

If you've upgraded to the latest version but aren't seeing any new features you were expecting then your python environment is likely still using an older version.

You can determine the version that is being used at runtime with:

```py
import giskard_hub
print(giskard_hub.__version__)
```

## Requirements

Python 3.10 or higher.

## Contributing

See [the contributing documentation](./CONTRIBUTING.md).
