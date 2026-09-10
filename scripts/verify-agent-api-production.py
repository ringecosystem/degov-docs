#!/usr/bin/env python3
"""Read-only v0.9.1 production smoke; no credentials, signing, or settlement."""

from __future__ import annotations

import base64
import importlib.util
import json
from pathlib import Path
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

BASE = "https://agent-api.degov.ai"
module_spec = importlib.util.spec_from_file_location("docs_contract", Path(__file__).with_name("verify-agent-api-docs.py"))
contract = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(contract)


def request(path: str, method: str = "GET", body: dict | None = None) -> tuple[int, dict, dict]:
    headers = {"User-Agent": "Mozilla/5.0 (compatible; DeGovDocsVerification/1.0)"}
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode()
    req = Request(BASE + path, data=data, headers=headers, method=method)
    for attempt in range(2):
        try:
            response = urlopen(req, timeout=30)
        except HTTPError as error:
            response = error
        except URLError:
            if attempt:
                raise
            time.sleep(1)
            continue
        with response:
            return response.status, {k.lower(): v for k, v in response.headers.items()}, json.load(response)
    raise AssertionError("unreachable")


def require_error(path: str, status: int, code: str, **kwargs: object) -> None:
    actual, _, body = request(path, **kwargs)
    assert actual == status, (path, actual, status)
    assert body["error"]["code"] == code, (path, body)
    assert body["requestId"], path


def require_offer(path: str, **kwargs: object) -> None:
    status, headers, _ = request(path, **kwargs)
    assert status == 402, f"{path}: expected anonymous v0.9.1 discovery status 402, received {status}"
    offer = json.loads(base64.b64decode(headers["payment-required"]))
    assert offer["x402Version"] == 2 and offer["accepts"], path
    assert "resource" in offer, f"{path}: missing v0.9.1 resource metadata; check deployment version"
    resource = offer["resource"]
    assert resource["url"] == BASE + path, resource
    assert resource["description"] and resource["mimeType"] == "application/json", resource
    bazaar = offer.get("extensions", {}).get("bazaar")
    assert bazaar, f"{path}: missing v0.9.1 Bazaar discovery schema"
    assert bazaar["info"]["input"]["type"] == "http", bazaar
    assert bazaar["info"]["input"]["method"] == kwargs.get("method", "GET"), bazaar
    assert bazaar["info"]["output"]["type"] == "json", bazaar
    assert "data" in bazaar["schema"]["properties"]["output"]["properties"]["example"]["properties"], path
    for accepted in offer["accepts"]:
        assert {"scheme", "network", "amount", "asset", "payTo"} <= accepted.keys(), accepted
        assert accepted["scheme"] == "exact" and int(accepted["amount"]) > 0, accepted
    assert any(a["network"] == "eip155:8453" for a in offer["accepts"]), path
    assert "payment-response" not in headers, "An unsigned request must not settle a payment"


def main() -> None:
    status, _, spec = request("/openapi.json")
    assert status == 200 and spec["openapi"].startswith("3."), status
    operations = {(method.upper(), path) for path, item in spec["paths"].items()
                  for method in item if method in {"get", "post", "put", "patch", "delete"}}
    assert operations == contract.PUBLIC_OPERATIONS, operations
    ids = [op["operationId"] for item in spec["paths"].values() for op in item.values()]
    assert len(set(ids)) == 11, ids
    status, _, alias = request("/openapi/agent-v2.json")
    assert status == 200 and alias == spec, "OpenAPI alias differs"
    for path, item in spec["paths"].items():
        for op in item.values():
            assert op["responses"]["200"]["content"]["application/json"]["schema"], path
            if op.get("security"):
                assert "x-payment-info" in op and "402" in op["responses"], path

    status, _, listing = request("/v2/daos?limit=1")
    assert status == 200 and set(listing) == {"data", "page"} and listing["data"], listing
    assert isinstance(listing["data"], list) and isinstance(listing["page"]["hasMore"], bool)
    dao_id = listing["data"][0]["daoId"]
    status, _, detail = request("/v2/daos/" + quote(dao_id, safe=""))
    assert status == 200 and set(detail) == {"data"} and detail["data"]["daoId"] == dao_id, detail
    assert "availableData" in detail["data"] and "dataAsOf" in detail["data"], detail
    if listing["page"]["hasMore"]:
        status, _, following = request("/v2/daos?" + urlencode({"limit": 1, "cursor": listing["page"]["nextCursor"]}))
        assert status == 200 and following["data"][0]["daoId"] != dao_id, following

    require_error("/v2/daos?limit=0", 400, "INVALID_ARGUMENT")
    require_error("/v2/daos?unknown=true", 400, "INVALID_ARGUMENT")
    print("Public operation inventory, free DAO access, pagination, and free-route validation passed.", flush=True)
    paid = [(method, path) for method, path in operations if spec["paths"][path][method.lower()].get("security")]
    assert len(paid) == 9, paid
    for method, path in sorted(paid):
        require_offer(quote(path, safe="/"), method=method)
    require_offer("/v2/proposals?limit=1")
    require_offer("/v2/proposals/resolve", method="POST", body={"by": "url"})
    resolver = spec["paths"]["/v2/proposals/resolve"]["post"]["requestBody"]["content"]["application/json"]["schema"]
    source_url = resolver["anyOf"][0]["properties"]["url"]["examples"][0]
    require_offer("/v2/proposals/resolve", method="POST", body={"by": "url", "url": source_url})
    print("Production v0.9.1 contract verified: 11 operations, spec alias, free discovery/detail/pagination, validation, and all nine anonymous x402 discovery challenges with resource and Bazaar schemas. No payment was signed or settled.")


if __name__ == "__main__":
    main()
