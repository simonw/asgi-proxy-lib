from . import asgi_proxy
import argparse
import sys


if __name__ == "__main__":
    try:
        import uvicorn
    except ImportError:
        print("Install uvicorn with: pip install uvicorn")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Start a proxy server")
    parser.add_argument("url", help="The backend URL to proxy to")
    parser.add_argument(
        "-p", "--port", type=int, default=8000, help="Port to use (default: 8000)"
    )
    parser.add_argument(
        "--host", default="0.0.0.0", help="Host to bind to (default: 0.0.0.0)"
    )
    parser.add_argument(
        "--timeout", type=float, default=None, help="Timeout in seconds"
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose logging")
    parser.add_argument(
        "-b",
        "--bodies",
        action="store_true",
        help="Log full request and response bodies",
    )

    args = parser.parse_args()

    if args.verbose or args.bodies:
        import logging

        logging.basicConfig(level=logging.INFO)
        log_request_body = None
        log_response_body = None
        if args.bodies:
            log_request_body = logging.info
            log_response_body = logging.info
        app = asgi_proxy(
            args.url,
            log=logging,
            timeout=args.timeout,
            log_request_body=log_request_body,
            log_response_body=log_response_body,
        )
    else:
        app = asgi_proxy(args.url, timeout=args.timeout)

    uvicorn.run(app, host=args.host, port=args.port)
