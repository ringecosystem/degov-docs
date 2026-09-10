#!/usr/bin/env python3
import argparse
import html
import json
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
        self.json_ld = []
        self._in_json_ld = False
        self._script_chunks = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta":
            key = attrs.get("property") or attrs.get("name")
            if key and "content" in attrs:
                self.meta[key] = attrs["content"]
        if tag == "link" and attrs.get("rel"):
            self.links[attrs["rel"]] = attrs.get("href", "")
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self._in_json_ld = True
            self._script_chunks = []

    def handle_data(self, data):
        if self._in_json_ld:
            self._script_chunks.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self._in_json_ld:
            self.json_ld.append(json.loads("".join(self._script_chunks)))
            self._in_json_ld = False
            self._script_chunks = []


class BreadcrumbParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self._in_breadcrumbs = False
        self._current_href = None
        self._current_text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "nav" and attrs.get("aria-label") == "Breadcrumb":
            self._in_breadcrumbs = True
        elif self._in_breadcrumbs and tag == "a":
            self._current_href = attrs.get("href")
            self._current_text = []

    def handle_data(self, data):
        if self._current_href is not None:
            self._current_text.append(data)

    def handle_endtag(self, tag):
        if self._in_breadcrumbs and tag == "a" and self._current_href is not None:
            text = re.sub(r"\s+", " ", "".join(self._current_text)).strip()
            self.links.append({"href": self._current_href, "text": text})
            self._current_href = None
            self._current_text = []
        elif tag == "nav" and self._in_breadcrumbs:
            self._in_breadcrumbs = False


def read_head(path):
    parser = HeadParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def visible_text(path):
    source = path.read_text(encoding="utf-8")
    source = re.sub(r"<script\b[^>]*>.*?</script>", " ", source, flags=re.I | re.S)
    source = re.sub(r"<style\b[^>]*>.*?</style>", " ", source, flags=re.I | re.S)
    source = re.sub(r"<[^>]+>", " ", source)
    return re.sub(r"\s+", " ", html.unescape(source)).strip()


def verify_content_provenance(site_dir):
    index_path = site_dir / "index.html"
    text = visible_text(index_path)
    for phrase in [
        "Canonical owner: DeGov Docs.",
        "Editorial review: 2026-09-10.",
        "Primary sources:",
        "The review date describes this explanatory page, not a deploy or build timestamp.",
    ]:
        require(phrase in text, f"index.html missing provenance phrase: {phrase}")


def visible_breadcrumb_links(path):
    parser = BreadcrumbParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser.links


def find_json_ld(parsed, type_name):
    for item in parsed.json_ld:
        candidates = item if isinstance(item, list) else [item]
        for candidate in candidates:
            item_type = candidate.get("@type")
            if item_type == type_name or (isinstance(item_type, list) and type_name in item_type):
                return candidate
    return None


def verify_breadcrumbs(path, parsed, relative_path):
    canonical = parsed.links.get("canonical")
    if relative_path == "index.html":
        require(not visible_breadcrumb_links(path), "index.html should not render a self breadcrumb")
        require(not find_json_ld(parsed, "BreadcrumbList"), "index.html should not emit BreadcrumbList")
        return

    links = visible_breadcrumb_links(path)
    require(
        links == [
            {"href": "https://docs.degov.ai/", "text": "DeGov.AI Docs"},
            {"href": canonical, "text": parsed.meta["og:title"].removesuffix(" | DeGov.AI Docs")},
        ],
        f"{relative_path} visible breadcrumbs must match canonical URLs",
    )

    breadcrumb = find_json_ld(parsed, "BreadcrumbList")
    require(breadcrumb, f"{relative_path} missing BreadcrumbList JSON-LD")
    items = breadcrumb.get("itemListElement", [])
    require(len(items) == len(links), f"{relative_path} BreadcrumbList item count")
    for index, (item, link) in enumerate(zip(items, links), start=1):
        require(item.get("@type") == "ListItem", f"{relative_path} breadcrumb item type {index}")
        require(item.get("position") == index, f"{relative_path} breadcrumb position {index}")
        require(item.get("name") == link["text"], f"{relative_path} breadcrumb name {index}")
        require(item.get("item") == link["href"], f"{relative_path} breadcrumb URL {index}")
        require(item.get("item", "").startswith("https://docs.degov.ai/"), f"{relative_path} breadcrumb host {index}")


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
    verify_breadcrumbs(path, parsed, relative_path)


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
    verify_content_provenance(site_dir)

    if args.fetch_image:
        verify_remote_image()

    print("Verified DeGov Docs social metadata.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"social metadata verification failed: {error}", file=sys.stderr)
        sys.exit(1)
