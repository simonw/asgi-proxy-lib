from setuptools import setup
import os

VERSION = "0.2a0"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="asgi-proxy-lib",
    description="An ASGI function for proxying to a backend over HTTP",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/asgi-proxy-lib",
    project_urls={
        "Issues": "https://github.com/simonw/asgi-proxy-lib/issues",
        "CI": "https://github.com/simonw/asgi-proxy-lib/actions",
        "Changelog": "https://github.com/simonw/asgi-proxy-lib/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["asgi_proxy"],
    install_requires=["httpx"],
    extras_require={"test": ["pytest", "pytest-asyncio", "pytest-httpx"]},
    python_requires=">=3.9",
)
