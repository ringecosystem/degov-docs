#!/usr/bin/env python3
"""Check public operation coverage, retired-contract drift, examples, and redirects."""

from decimal import Decimal
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_OPERATIONS = {
    ("GET", "/v2/daos"),
    ("GET", "/v2/daos/{daoId}"),
    ("GET", "/v2/daos/{daoId}/participants"),
    ("GET", "/v2/proposals"),
    ("POST", "/v2/proposals/resolve"),
    ("GET", "/v2/proposals/{proposalId}"),
    ("GET", "/v2/proposals/{proposalId}/vote-summary"),
    ("GET", "/v2/proposals/{proposalId}/votes"),
    ("GET", "/v2/forum-topics"),
    ("GET", "/v2/voters/{voterId}"),
    ("GET", "/v2/voters/{voterId}/votes"),
}
RETIRED = (
    "/v1/", "/openapi/agent-v1.json", "/openapi/atlas.json",
    "/v2/meta/", "/v2/events", "/v2/signals", "/votes/summary",
    "proposalKey", "topicKey", "voterIdentity", "data.items", "meta.page",
    "lifecycleStatus", "endingSoon", "repliesDesc", "governanceRelated=true",
    "hasVoteData", "hasForumData", "coverageStatus", "servingRevision",
    "x-degov-internal-token", "GET /v2/proposals/resolve", "/proposals/resolve?",
)


def check_example(value: object, label: str, failures: list[str]) -> None:
    if not isinstance(value, dict):
        return
    if isinstance(value.get("data"), list):
        page = value.get("page", {})
        if not isinstance(page.get("hasMore"), bool):
            failures.append(f"{label}: list needs a top-level page.hasMore boolean")
        elif page["hasMore"] != bool(page.get("nextCursor")):
            failures.append(f"{label}: hasMore and nextCursor disagree")
        if "nextCursor" not in page:
            failures.append(f"{label}: list is missing nextCursor")
    if "choices" in value and "totals" in value:
        choices, totals = value["choices"], value["totals"]
        if sum(c["voteCount"] for c in choices) != totals["voteCount"]:
            failures.append(f"{label}: choice vote counts do not equal the total")
        power = sum(Decimal(c["knownVotingPower"]) for c in choices)
        if power != Decimal(totals["knownVotingPower"]):
            failures.append(f"{label}: choice voting power does not equal the total")
    if value.get("by") in {"url", "source_id"}:
        expected = {"by", "url"} if value["by"] == "url" else {"by", "daoId", "provider", "externalId"}
        if set(value) != expected:
            failures.append(f"{label}: resolver example mixes lookup forms or omits a field")
    for child in value.values():
        if isinstance(child, dict):
            check_example(child, label, failures)


def main() -> int:
    failures: list[str] = []
    paths = sorted((ROOT / "docs/agent-api").rglob("*.md"))
    paths += sorted((ROOT / "docs/agent-skills").rglob("*.md"))
    paths.append(ROOT / "docs/llms.txt")
    for path in paths:
        text = path.read_text(encoding="utf-8")
        label = str(path.relative_to(ROOT))
        for phrase in RETIRED:
            if phrase in text:
                failures.append(f"{label}: retired contract text {phrase!r}")
        for number, raw in enumerate(re.findall(r"```json\s*\n(.*?)\n```", text, re.S), 1):
            try:
                value = json.loads(raw)
                check_example(value, f"{label} example {number}", failures)
            except (ValueError, KeyError, TypeError) as error:
                failures.append(f"{label} example {number}: {error}")

    reference = (ROOT / "docs/agent-api/reference/index.md").read_text()
    documented = re.findall(r"\| (GET|POST) \| `([^`]+)`", reference)
    if set(documented) != PUBLIC_OPERATIONS or len(documented) != len(PUBLIC_OPERATIONS):
        failures.append("Reference table must contain exactly the 11 current method/path pairs")
    detailed = []
    for path in (ROOT / "docs/agent-api/reference").glob("v2-*.md"):
        detailed.extend(re.findall(r"^## `(GET|POST) ([^`]+)`", path.read_text(), re.M))
    if set(detailed) != PUBLIC_OPERATIONS or len(detailed) != len(PUBLIC_OPERATIONS):
        failures.append("Detailed reference must describe every current method/path pair once")

    nav = (ROOT / "mkdocs.yml").read_text()
    for page in ("agent-api/concepts/proposal-and-topic-keys.md", "agent-api/concepts/readiness-and-coverage.md",
                 "agent-api/reference/index.md", "agent-skills/index.md", "atlas/atlas-vs-agent-api.md"):
        if page not in nav:
            failures.append(f"Navigation is missing {page}")
    config = json.loads((ROOT / "vercel.json").read_text())
    for redirect in config["redirects"]:
        destination = redirect["destination"]
        if destination.startswith("/") and not (ROOT / "site" / destination.strip("/") / "index.html").exists():
            failures.append(f"Redirect destination was not built: {destination}")
    for obsolete in ("agent-api/reference/v1/index.html", "agent-api/migration-v1-to-v2/index.html",
                     "agent-api/reference/v2-metadata/index.html", "agent-api/reference/v2-feeds/index.html"):
        if (ROOT / "site" / obsolete).exists():
            failures.append(f"Retired page still appears in the build: {obsolete}")
    if not (ROOT / "site/llms.txt").exists():
        failures.append("Agent navigation file was not included in the build")
    if failures:
        print("Agent API documentation verification failed:\n" + "\n".join(f"- {f}" for f in failures))
        return 1
    print("Agent API documentation verification passed: 11 operations, current examples, discovery, and redirects.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
