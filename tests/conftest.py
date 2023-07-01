import pytest


@pytest.fixture
def assert_all_responses_were_requested() -> bool:
    return False


@pytest.fixture(autouse=True)
def mock_backend(httpx_mock):
    httpx_mock.add_response(url="https://datasette.io/", text="<h1>datasette.io</h1>")
    httpx_mock.add_response(url="https://datasette.io/faq", text="FAQ goes here")
    httpx_mock.add_response(
        url="https://datasette.io/404", status_code=404, text="Not Found"
    )
    return httpx_mock
