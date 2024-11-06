from asgi_proxy import asgi_proxy
import httpx
import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "url,expected_status,expected_body",
    (
        (
            "https://datasette.io/",
            200,
            "<h1>datasette.io</h1>",
        ),
        (
            "https://datasette.io/faq",
            200,
            "FAQ goes here",
        ),
        (
            "https://datasette.io/404",
            404,
            "Not Found",
        ),
    ),
)
@pytest.mark.httpx_mock(assert_all_responses_were_requested=False)
async def test_asgi_proxy(mock_backend, url, expected_status, expected_body):
    app = asgi_proxy("https://datasette.io")
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app),
    ) as client:
        response = await client.get(url)
    assert response.status_code == expected_status
    assert response.text == expected_body
    assert len(mock_backend.get_requests()) == 1
    assert mock_backend.get_requests()[0].url == url


@pytest.mark.asyncio
@pytest.mark.httpx_mock(assert_all_responses_were_requested=False)
async def test_asgi_proxy_timeout(httpx_mock):
    httpx_mock.add_exception(httpx.ReadTimeout("Unable to read within timeout"))
    app = asgi_proxy("https://datasette.io", timeout=0.1)
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app),
    ) as client:
        response = await client.get("https://datasette.io/")
        assert response.status_code == 504
        assert response.text == "Gateway timeout"
