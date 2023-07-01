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
async def test_asgi_proxy(mock_backend, url, expected_status, expected_body):
    app = asgi_proxy("https://datasette.io/")
    async with httpx.AsyncClient(
        app=app,
        follow_redirects=False,
    ) as client:
        response = await client.get(url)
    assert response.status_code == expected_status
    assert response.text == expected_body
    assert len(mock_backend.get_requests()) == 1
    assert mock_backend.get_requests()[0].url == url
