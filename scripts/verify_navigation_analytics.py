from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "docs/resource/javascripts/navigation-analytics.js"
MKDOCS_PATH = ROOT / "mkdocs.yml"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


source = SCRIPT_PATH.read_text()
mkdocs = MKDOCS_PATH.read_text()

require("degov_docs_navigation" in source, "event name must be defined")
require(
    "resource/javascripts/navigation-analytics.js" in mkdocs,
    "mkdocs.yml must load docs navigation analytics",
)
require("source_surface: 'docs'" in source, "source surface must be docs")
for field in [
    "topic_id",
    "target_path_class",
    "channel_group",
    "locale",
]:
    require(field in source, f"allowed parameter {field} must be present")

for field in [
    "private_dao_id",
    "wallet_address",
    "proposal_draft",
    "window.location.search",
    "window.location.href",
]:
    require(field not in source, f"sensitive field {field} must not be present")

for expected in [
    "return 'direct-unknown'",
    "ai-search-assistant-referral",
    "organic-search",
    "social-organic",
    "documentation-referral",
    "cross-product-degov-referral",
    "other-external-referral",
]:
    require(expected in source, f"channel classification {expected} must be present")

require(
    "[EVENT_NAME, params.topic_id, params.target_path_class].join(':')" in source,
    "dedupe key must use session plus topic id plus target path class",
)
require("typeof window.gtag !== 'function'" in source, "script must not send without gtag")
require("targetHost !== currentHost && targetHost !== 'docs.degov.ai'" in source, "script must not track unrelated external links")

print("Docs navigation analytics verification passed.")
