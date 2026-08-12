#!/usr/bin/env python3
"""Fail when known Agent API documentation drift patterns return."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN = {
    "docs/agent-api": (
        "Proposed Agent API v2",
        "not yet available",
        "not live yet",
        "x-degov-internal-token",
        '"deadlineAtMs"',
        '"eventTimeConfidence"',
        '"data": [',
    ),
    "docs/agent-skills": (
        "bundled CLI",
        "dedicated local wallet",
        "explicit user consent",
        "web-search-only",
    ),
}

REQUIRED_PATHS = {
    "/v2/meta/pricing",
    "/v2/meta/data-status",
    "/v2/daos",
    "/v2/proposals",
    "/v2/forum-topics",
    "/v2/events",
    "/v2/signals",
}


def main() -> int:
    failures: list[str] = []
    all_text = ""

    for relative_dir, phrases in FORBIDDEN.items():
        for path in sorted((ROOT / relative_dir).rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            all_text += "\n" + text
            for phrase in phrases:
                if phrase in text:
                    failures.append(f"{path.relative_to(ROOT)} contains forbidden text: {phrase}")

    documented_paths = set(re.findall(r"/v2/[A-Za-z0-9_:/.-]+", all_text))
    missing = REQUIRED_PATHS - documented_paths
    if missing:
        failures.append(f"required production paths are undocumented: {sorted(missing)}")

    nav = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    for required_page in (
        "agent-api/concepts/index.md",
        "agent-api/guides/index.md",
        "agent-api/reference/index.md",
        "atlas/atlas-vs-agent-api.md",
    ):
        if required_page not in nav:
            failures.append(f"navigation is missing {required_page}")

    if failures:
        print("Agent API documentation verification failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Agent API documentation verification passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
