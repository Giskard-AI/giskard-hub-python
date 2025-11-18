## Setting up the environment

### With uv

We use [uv](https://docs.astral.sh/uv/getting-started/installation/) to manage dependencies because it will automatically provision a Python environment with the expected Python version. To set it up, run:

```sh
$ uv sync --all-extras
```

You can then run scripts using `uv run python script.py` or by activating the virtual environment:

```sh
# Activate the virtual environment - https://docs.python.org/3/library/venv.html#how-venvs-work
$ source .venv/bin/activate

# now you can omit the `uv run` prefix
$ python script.py
```

### Without uv

Alternatively if you don't want to install `uv`, you can stick with the standard `pip` setup by ensuring you have the Python version specified in `.python-version`, create a virtual environment however you desire and then install dependencies using this command:

```sh
$ pip install -e ".[dev]"
```

## Modifying/Adding code

The SDK code in `src/giskard_hub/` can be freely modified. The `src/giskard_hub/lib/` and `examples/` directories are for custom code and examples.

## Adding and running examples

All files in the `examples/` directory can be freely edited or added to.

```py
# add an example to examples/<your-example>.py

#!/usr/bin/env -S uv run python
…
```

```sh
$ chmod +x examples/<your-example>.py
# run the example against your api
$ ./examples/<your-example>.py
```

## Using the repository from source

If you’d like to use the repository from source, you can either install from git or link to a cloned repository:

To install via git:

```sh
$ pip install git+https://github.com/Giskard-AI/giskard-hub-python.git
```

Alternatively, you can build from source and install the wheel file:

Building this package will create two files in the `dist/` directory, a `.tar.gz` containing the source files and a `.whl` that can be used to install the package efficiently.

To create a distributable version of the library, all you have to do is run this command:

```sh
$ uv build
# or
$ python -m build
```

Then to install:

```sh
$ pip install ./path-to-wheel-file.whl
```

## Running tests

```sh
$ uv run pytest
```

## Linting and formatting

This repository uses [ruff](https://github.com/astral-sh/ruff) to format and lint the code in the repository.

To lint:

```sh
$ uv run ruff check .
uv run pyright
uv run mypy .
uv run python -c 'import giskard_hub'
```

To format and fix all ruff issues automatically:

```sh
$ uv run ruff format
```

## Publishing and releases

### Publish manually

If you need to manually release a package, you can run the `bin/publish-pypi` script with a `PYPI_TOKEN` set on
the environment.
