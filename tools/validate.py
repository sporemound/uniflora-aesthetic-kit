#!/usr/bin/env python3
"""SPDX-License-Identifier: Unlicense. Check the editable v0.1 package; stdlib only."""
import argparse
import json
import re
import sys
from datetime import datetime, timezone
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
BRANCHES = ("isometric-idm", "engraved-architecture", "crt-worlds",
            "nocturnal-optics", "kilim-burdock", "botanical-specimen")
errors = []
checks = 0


def check(condition, message):
    global checks
    checks += 1
    if not condition:
        errors.append(message)


def contrast(a, b):
    def luminance(color):
        rgb = [int(color[i:i+2], 16) / 255 for i in (1, 3, 5)]
        linear = [v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4 for v in rgb]
        return sum(c * w for c, w in zip(linear, (.2126, .7152, .0722)))
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + .05) / (lo + .05)


def local_link(path, link):
    parts = urlsplit(link)
    if parts.scheme or parts.netloc or not parts.path:
        return
    target = (path.parent / unquote(parts.path)).resolve()
    check(target.is_relative_to(ROOT), f"Link escapes project: {path.name}: {link}")
    check(target.exists(), f"Missing link: {path.relative_to(ROOT)}: {link}")


class DemoParser(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.branches, self.images, self.ids, self.labels = path, [], 0, [], []

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        check(tag not in ("script", "iframe", "object", "embed"), f"Unexpected active element: {tag}")
        check(not any(k.startswith("on") for k in data), "Unexpected inline event handler")
        if "id" in data:
            self.ids.append(data["id"])
        if "data-uniflora" in data:
            self.branches.append(data["data-uniflora"])
        if tag == "label":
            self.labels.append(data.get("for"))
        if tag == "img":
            self.images += 1
            check(bool(data.get("alt")), "Artwork needs descriptive alt text")
        for attr in ("src", "href"):
            if data.get(attr):
                local_link(self.path, data[attr])
                if tag != "a":
                    check(not urlsplit(data[attr]).scheme, "Demo must not fetch external assets")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", action="store_true", help="Write docs/VALIDATION.md after checking")
    args = parser.parse_args()
    tokens = json.loads((ROOT / "presets/tokens.json").read_text())
    css = (ROOT / "presets/tokens.css").read_text()
    check(set(tokens["branches"]) == set(BRANCHES), "Tokens must cover exactly six branches")
    ratios = []
    for branch, record in tokens["branches"].items():
        roles = record["roles"]
        block = re.search(r'\[data-uniflora="' + re.escape(branch) + r'"\]\s*\{([^}]+)\}', css)
        check(bool(block), f"Missing CSS preset {branch}")
        for name, value in roles.items():
            check(bool(re.fullmatch(r"#[0-9a-fA-F]{6}", value)), f"Invalid hex {branch}/{name}")
            if block:
                check(f"--uf-{name}: {value};" in block[1], f"JSON/CSS mismatch {branch}/{name}")
        pairs = {(fg, bg): contrast(roles[fg], roles[bg])
                 for fg in ("text", "muted", "accent") for bg in ("bg", "surface")}
        for pair, ratio in pairs.items():
            check(ratio >= 4.5, f"Text contrast {branch}/{pair}: {ratio:.3f}:1")
        ratios.append((branch, min(pairs.values())))
    check(not tokens.get("bundledFonts"), "v0.1 must not bundle fonts")
    for path in ROOT.rglob("*.json"):
        json.loads(path.read_text())
    examples = json.loads((ROOT / "prompts/examples.json").read_text())
    records = examples if isinstance(examples, list) else examples.get("examples", [])
    check(len(records) == 6, "Provide six prompt examples")
    check({e.get("branch") for e in records} == set(BRANCHES), "Prompts must cover six branches")
    for path in ROOT.rglob("*.md"):
        text = path.read_text()
        for target in re.findall(r'\]\(([^)\s]+)\)', text):
            local_link(path, target)
    namespace = "{http://www.w3.org/2000/svg}"
    svgs = list((ROOT / "assets/svg").glob("*.svg"))
    check(len(svgs) == 6, "Provide six original SVG motifs")
    for path in svgs:
        node = ET.parse(path).getroot()
        check(node.tag == namespace + "svg", f"Invalid SVG root {path.name}")
        check(node.get("viewBox") == "0 0 480 360", f"Unexpected viewBox {path.name}")
        check(node.find(namespace + "title") is not None, f"Missing SVG title {path.name}")
        check(node.find(namespace + "desc") is not None, f"Missing SVG description {path.name}")
        ids = [n.get("id") for n in node.iter() if n.get("id")]
        check(len(ids) == len(set(ids)), f"Duplicate SVG ids {path.name}")
        for n in node.iter():
            check(n.tag.split("}")[-1] not in ("script", "image", "foreignObject"), f"External/active SVG element {path.name}")
            for key, value in n.attrib.items():
                check(not key.lower().startswith("on"), f"Event attribute {path.name}")
                if key.split("}")[-1] == "href":
                    check(value.startswith("#") and value[1:] in ids, f"Nonlocal or missing SVG reference {path.name}")
        for ref in re.findall(r"url\(#([^)]+)\)", path.read_text()):
            check(ref in ids, f"Missing SVG paint reference {path.name}/{ref}")
    register = json.loads((ROOT / "attribution.json").read_text())
    check({a["path"] for a in register["assets"]} == {str(p.relative_to(ROOT)) for p in svgs}, "SVG attribution inventory mismatch")
    check(not register["fonts"]["bundled"], "Font attribution inventory must be empty")
    check(not register["includedThirdPartyVisualAssets"], "v0.1 must not silently add external visuals")
    for extra in (ROOT / "demo").glob("*.html"):
        if extra.name != "index.html":
            parsed = DemoParser(extra)
            parsed.feed(extra.read_text())
    html_path = ROOT / "demo/index.html"
    demo = DemoParser(html_path)
    demo.feed(html_path.read_text())
    check(tuple(demo.branches) == BRANCHES, "Demo preset order/coverage mismatch")
    check(demo.images == 6, "Demo must show six motifs")
    check(len(demo.ids) == len(set(demo.ids)), "Duplicate HTML ids")
    check(all(v in demo.ids for v in demo.labels), "Input label target missing")
    demo_css = (ROOT / "demo/demo.css").read_text()
    check("prefers-reduced-motion: reduce" in demo_css, "Reduced-motion fallback missing")
    check(".crt-toggle:checked" in demo_css, "Motion must be explicit opt-in")
    check("overflow: hidden" in demo_css, "Screen clipping missing")
    for path in (ROOT / "demo/demo.css", ROOT / "presets/tokens.css"):
        text = path.read_text()
        check(not re.search(r"@import|@font-face|https?://", text), "External CSS/font dependency")
    check(not list(ROOT.rglob("*.woff*")) and not list(ROOT.rglob("*.ttf")) and not list(ROOT.rglob("*.otf")), "Bundled font found")
    result = "PASS" if not errors else "FAIL"
    print(f"{result}: {checks} checks; {len(errors)} failures")
    for message in errors:
        print("- " + message)
    if args.report:
        report = ["# Validation record", "", f"Portable validator: **{result}**, {checks} checks, {len(errors)} failures.", "",
                  f"Executed {datetime.now(timezone.utc).date()} UTC. Uses Python standard library; no paid dependencies.", "",
                  "## Readable token pairs", "", "Minimum across text, muted, and accent against both bg and surface. Threshold checked without rounding: 4.5:1.", "",
                  "| Branch | Minimum ratio |", "| --- | --- |"]
        report += [f"| `{branch}` | {ratio:.2f}:1 |" for branch, ratio in ratios]
        report += ["", "## Scope", "", "Checks JSON/CSS synchronization, all six demo/prompt/SVG branches, internal links, SVG parse and references, absence of font files and external demo resources, and declared opt-in/reduced-motion CSS.", "",
                   "Six SVGs were rendered and visually inspected separately. No complete browser interaction, assistive-technology, or botanical expert certification is claimed. A local browser runtime download failed in this environment; inspect the HTML in your target browser before publication. Static CSS checks do not prove animation confinement at runtime. No hosted website deployment has occurred. The creator authorized publishing the reviewed v0.1 to the existing GitHub repository.", "",
                   "Decorative swatches are not approved text colors. This record is not a full WCAG conformance or legal clearance report."]
        if errors:
            report += ["", "## Failures", ""] + ["- " + e for e in errors]
        (ROOT / "docs/VALIDATION.md").write_text("\n".join(report) + "\n")
    return bool(errors)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, ET.ParseError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
