#!/usr/bin/env python3
"""Public-site UX/UI smoke checks for the resume and portfolio."""

from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ScriptCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_json_ld = False
        self.buffer: list[str] = []
        self.blocks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = dict(attrs)
        if tag == "script" and attr.get("type") == "application/ld+json":
            self.in_json_ld = True
            self.buffer = []

    def handle_data(self, data: str) -> None:
        if self.in_json_ld:
            self.buffer.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self.in_json_ld:
            self.blocks.append("".join(self.buffer))
            self.in_json_ld = False


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def section_order(html: str) -> list[str]:
    return re.findall(r'<section[^>]+data-section="([^"]+)"', html)


def json_ld_blocks(html: str) -> list[dict]:
    parser = ScriptCollector()
    parser.feed(html)
    return [json.loads(block) for block in parser.blocks]


def main() -> None:
    index = read("index.html")
    portfolio = read("portfolio.html")
    robots = read("robots.txt")
    sitemap = read("sitemap.xml")
    llms = read("llms.txt")

    sections = section_order(index)
    expected = [
        "summary",
        "competencies",
        "affiliation",
        "career",
        "projects",
        "education",
        "certifications",
        "additional",
        "links",
    ]
    assert_true(sections == expected, f"Unexpected resume section order: {sections}")

    for text in [
        "vvorotilov.au@gmail.com",
        "linkedin.com/in/vladimir-vorotilov",
        "Available immediately",
        "Resume",
        "Portfolio",
    ]:
        assert_true(text in index, f"Missing contact or navigation cue: {text}")

    competencies_pos = index.index("Core Competencies")
    affiliation_pos = index.index("AITAI Associate, AITAI - AI Institute")
    career_pos = index.index("Career History")
    assert_true(
        competencies_pos < affiliation_pos < career_pos,
        "AITAI affiliation is not between competencies and career history",
    )

    assert_true(
        "AITAI Associate, Anthropic Academy, and WA driver" not in portfolio,
        "Portfolio still contains the combined credentials card",
    )
    assert_true("Selected Projects" in portfolio, "Portfolio project heading is missing")
    assert_true("View Resume" in portfolio, "Portfolio needs a clear resume path")

    for name, html in [("index.html", index), ("portfolio.html", portfolio)]:
        blocks = json_ld_blocks(html)
        assert_true(blocks, f"{name} has no JSON-LD")

    assert_true(
        "Sitemap: https://vvorotilov-ai-au.github.io/cv-2026/sitemap.xml" in robots,
        "robots.txt does not expose the sitemap",
    )
    assert_true(
        "https://vvorotilov-ai-au.github.io/cv-2026/portfolio.html" in sitemap,
        "sitemap.xml does not include the portfolio page",
    )
    assert_true(
        "Resume: https://vvorotilov-ai-au.github.io/cv-2026/" in llms,
        "llms.txt does not include the canonical resume URL",
    )

    print("UX/UI smoke checks passed")


if __name__ == "__main__":
    main()
