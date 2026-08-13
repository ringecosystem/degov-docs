import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MEASUREMENT_ID = "G-P1X6QLGZX6"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


parser = argparse.ArgumentParser()
parser.add_argument("--expect-enabled", action="store_true")
parser.add_argument("--expect-disabled", action="store_true")
args = parser.parse_args()

require(
    args.expect_enabled != args.expect_disabled,
    "choose exactly one of --expect-enabled or --expect-disabled",
)

base_config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
production_config = (ROOT / "mkdocs.production.yml").read_text(encoding="utf-8")
prod_workflow = (ROOT / ".github/workflows/deploy-prd.yml").read_text(encoding="utf-8")
stg_workflow = (ROOT / ".github/workflows/deploy-stg.yml").read_text(encoding="utf-8")
dev_workflow = (ROOT / ".github/workflows/deploy-dev.yml").read_text(encoding="utf-8")
site_index = ROOT / "site/index.html"

require(
    "provider: google" not in base_config,
    "base MkDocs config must not enable the Google analytics provider",
)
require(
    MEASUREMENT_ID not in base_config,
    "base MkDocs config must not include production GA4 property",
)
require(
    "INHERIT: mkdocs.yml" in production_config
    and "provider: google" in production_config
    and f"property: {MEASUREMENT_ID}" in production_config,
    "production MkDocs overlay must set GA4 measurement ID",
)
require(
    "mkdocs.production.yml" in prod_workflow,
    "production workflow must build with production MkDocs overlay",
)
require(
    "mkdocs.production.yml" not in stg_workflow,
    "staging workflow must not build with production MkDocs overlay",
)
require(
    "mkdocs.production.yml" not in dev_workflow,
    "PR workflow must not build with production MkDocs overlay",
)

if site_index.exists():
    site_html = site_index.read_text(encoding="utf-8")
    if args.expect_enabled:
        require(MEASUREMENT_ID in site_html, "production artifact must include GA4 measurement ID")
        require(
            "consent.analytics&&__md_analytics()" in site_html,
            "production analytics must remain behind Material analytics consent",
        )
    else:
        require("googletagmanager.com/gtag/js" not in site_html, "non-production artifact must not load GA")
        require("id=\"__analytics\"" not in site_html, "non-production artifact must not initialize GA")

print("GA4 activation verification passed.")
