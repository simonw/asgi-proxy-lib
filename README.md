# asgi-proxy

[![PyPI](https://img.shields.io/pypi/v/asgi-proxy.svg)](https://pypi.org/project/asgi-proxy/)
[![Changelog](https://img.shields.io/github/v/release/simonw/asgi-proxy?include_prereleases&label=changelog)](https://github.com/simonw/asgi-proxy/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/asgi-proxy/blob/main/LICENSE)

An ASGI function for proxying to a backend over HTTP

**⚠️ Warning: this is an early alpha.**

## Installation

Install this library using `pip`:

    pip install asgi-proxy

## Usage

This library provides a single ASGI function called `asgi_proxy`. You can use it like this:

```python
from asgi_proxy import asgi_proxy

app = asgi_proxy("https://datasette.io")
```
Now `app` is an ASGI application that will proxy all incoming HTTP requests to the equivalent URL on `https://datasette.io`.

The function takes an optional second argument, `log=` - set this to a Python logger, or any object that has `.info(msg)` and `.error(msg)` methods, and the proxy will log information about each request it proxies.

## CLI tool

You can try this module out like so:

```bash
python -m asgi_proxy https://datasette.io
```
This will start a server on port 8000 that proxies to `https://datasette.io`.

Add `-p PORT` to specify a different port, `--verbose` to see debug logging, and `--host 127.0.0.1` to listen on a different host (the default is `0.0.0.0`).

## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:

    cd asgi-proxy
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
