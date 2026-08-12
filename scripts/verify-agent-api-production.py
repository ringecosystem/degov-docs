#!/usr/bin/env python3
"""Explicit production smoke test; do not run on every ordinary PR build."""

from __future__ import annotations

import json
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

BASE = "https://agent-api.degov.ai"


def get(path: str) -> tuple[int, dict[str, str], bytes]:
    request = Request(BASE + path, headers={"User-Agent": "degov-docs-production-smoke"})
    for attempt in range(2):
        try:
            with urlopen(request, timeout=30) as response:
                return response.status, dict(response.headers.items()), response.read()
        except HTTPError as error:
            return error.code, dict(error.headers.items()), error.read()
        except URLError:
            if attempt == 1:
                raise
            time.sleep(1)
    raise AssertionError("unreachable")


def main() -> None:
    for path in ("/health", "/v2/meta/pricing", "/v2/meta/data-status", "/v2/daos?limit=1"):
        status, _, body = get(path)
        assert status == 200, (path, status)
        json.loads(body)

    minimum_operations = {"agent-v1": 10, "agent-v2": 18, "atlas": 17}
    for name, minimum in minimum_operations.items():
        status, _, body = get(f"/openapi/{name}.json")
        assert status == 200, (name, status)
        spec = json.loads(body)
        operation_count = sum(
            method.lower() in {"get", "post", "put", "patch", "delete"}
            for path_item in spec.get("paths", {}).values()
            for method in path_item
        )
        assert operation_count >= minimum, (name, operation_count, minimum)

    status, headers, _ = get("/v2/proposals?limit=1")
    normalized_headers = {key.lower(): value for key, value in headers.items()}
    assert status == 402, status
    assert "payment-required" in normalized_headers

    preflight = Request(
        BASE + "/v2/proposals?limit=1",
        method="OPTIONS",
        headers={
            "User-Agent": "degov-docs-production-smoke",
            "Origin": "https://docs.degov.ai",
            "Access-Control-Request-Method": "GET",
            "Access-Control-Request-Headers": "x-degov-api-token",
        },
    )
    with urlopen(preflight, timeout=20) as response:
        headers = {key.lower(): value for key, value in response.headers.items()}
        assert response.status == 204
        assert headers.get("access-control-allow-origin") == "https://docs.degov.ai"
        assert "x-degov-api-token" in headers.get("access-control-allow-headers", "").lower()

    print("Production Agent API smoke test passed.")


if __name__ == "__main__":
    main()
