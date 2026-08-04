#!/usr/bin/env python3
import argparse
import re
import struct
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen


EXPECTED_IMAGE_URL = "https://degov.ai/images/degov-social-card.png"
EXPECTED_IMAGE_WIDTH = "1200"
EXPECTED_IMAGE_HEIGHT = "630"
EXPECTED_IMAGE_TYPE = "image/png"
EXPECTED_TWITTER_SITE = "@ai_degov"


class HeadParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta = {}
        self.links = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta":
            key = attrs.get("property") or attrs.get("name")
            if key and "content" in attrs:
                self.meta[key] = attrs["content"]
        if tag == "link" and attrs.get("rel"):
            self.links[attrs["rel"]] = attrs.get("href", "")


def read_head(path):
    parser = HeadParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def verify_page(site_dir, relative_path):
    path = site_dir / relative_path
    require(path.exists(), f"{relative_path} must exist")

    parsed = read_head(path)
    canonical = parsed.links.get("canonical")
    require(canonical and canonical.startswith("https://docs.degov.ai"), f"{relative_path} canonical host")
    require(parsed.meta.get("og:url") == canonical, f"{relative_path} og:url must match canonical")

    for key in [
        "og:title",
        "og:type",
        "og:url",
        "og:image",
        "og:description",
        "og:site_name",
        "og:locale",
        "og:image:type",
        "og:image:width",
        "og:image:height",
        "og:image:alt",
        "twitter:card",
        "twitter:site",
        "twitter:creator",
        "twitter:title",
        "twitter:description",
        "twitter:image",
        "twitter:image:alt",
    ]:
        require(parsed.meta.get(key), f"{relative_path} missing {key}")

    require(parsed.meta["og:image"] == EXPECTED_IMAGE_URL, f"{relative_path} og:image")
    require(parsed.meta["twitter:image"] == EXPECTED_IMAGE_URL, f"{relative_path} twitter:image")
    require(parsed.meta["og:image:type"] == EXPECTED_IMAGE_TYPE, f"{relative_path} image type")
    require(parsed.meta["og:image:width"] == EXPECTED_IMAGE_WIDTH, f"{relative_path} image width")
    require(parsed.meta["og:image:height"] == EXPECTED_IMAGE_HEIGHT, f"{relative_path} image height")
    require(parsed.meta["twitter:card"] == "summary_large_image", f"{relative_path} Twitter card")
    require(parsed.meta["twitter:site"] == EXPECTED_TWITTER_SITE, f"{relative_path} Twitter site")
    require(parsed.meta["twitter:creator"] == EXPECTED_TWITTER_SITE, f"{relative_path} Twitter creator")
    require(parsed.meta["og:title"] == parsed.meta["twitter:title"], f"{relative_path} social titles")
    require(
        parsed.meta["og:description"] == parsed.meta["twitter:description"],
        f"{relative_path} social descriptions",
    )
    require(parsed.meta["og:image:alt"] == parsed.meta["twitter:image:alt"], f"{relative_path} image alt")
    require(not re.search(r"https://[^\"']+vercel\\.app", path.read_text(encoding="utf-8")), f"{relative_path} dev host leak")


def verify_remote_image():
    request = Request(EXPECTED_IMAGE_URL, headers={"User-Agent": "degov-docs-social-preview-check"})
    with urlopen(request, timeout=20) as response:
        content_type = response.headers.get("content-type", "")
        cache_control = response.headers.get("cache-control", "")
        body = response.read()
        status = response.status

    require(status == 200, "social image must return HTTP 200")
    require(content_type.startswith(EXPECTED_IMAGE_TYPE), "social image must be PNG")
    require(cache_control, "social image must declare cache behavior")
    require(body.startswith(b"\x89PNG\r\n\x1a\n"), "social image must be a PNG")

    width, height = struct.unpack(">II", body[16:24])
    require(width == int(EXPECTED_IMAGE_WIDTH), "social image width")
    require(height == int(EXPECTED_IMAGE_HEIGHT), "social image height")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-dir", default="site")
    parser.add_argument("--fetch-image", action="store_true")
    args = parser.parse_args()

    site_dir = Path(args.site_dir)
    for page in ["index.html", "integration/overview/index.html"]:
        verify_page(site_dir, page)

    if args.fetch_image:
        verify_remote_image()

    print("Verified DeGov Docs social metadata.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"social metadata verification failed: {error}", file=sys.stderr)
        sys.exit(1)
