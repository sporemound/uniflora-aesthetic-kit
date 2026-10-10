#!/usr/bin/env python3
"""SPDX-License-Identifier: Unlicense. Verify the pinned plugin export; stdlib only."""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    errors, checks = [], 0

    def check(condition, message):
        nonlocal checks
        checks += 1
        if not condition:
            errors.append(message)

    record = json.loads((ROOT / "plugins/EXPORT.json").read_text(encoding="utf-8"))
    plugin = (ROOT / record["pluginRoot"]).resolve()
    check(plugin.is_relative_to(ROOT), "Plugin root escapes repository")
    expected = {item["path"]: item for item in record["files"]}
    actual = {p.relative_to(plugin).as_posix() for p in plugin.rglob("*") if p.is_file()}
    check(actual == set(expected), "Export file inventory changed")
    for relative, item in expected.items():
        path = plugin / relative
        check(path.resolve().is_relative_to(plugin), f"Export path escapes: {relative}")
        check(not path.is_symlink(), f"Symlink in export: {relative}")
        data = path.read_bytes()
        data.decode("utf-8")
        check(len(data) == item["bytes"], f"Export size changed: {relative}")
        check(hashlib.sha256(data).hexdigest() == item["sha256"], f"Export hash changed: {relative}")
    manifest = json.loads((plugin / "plugin.json").read_text(encoding="utf-8"))
    legacy = json.loads((plugin / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    for key in ("name", "version", "description", "author"):
        check(manifest[key] == legacy[key], f"Manifest mismatch: {key}")
    check(manifest["name"] == record["packageName"], "Package identity changed")
    check(manifest["version"] == record["version"], "Export version mismatch")
    interface = manifest["extensions"]["com.openai"]["interface"]
    check(interface == legacy["interface"], "Manifest presentation mismatch")
    prompts = interface["defaultPrompt"]
    check(isinstance(prompts, str) or (isinstance(prompts, list) and 1 <= len(prompts) <= 3
          and all(isinstance(p, str) for p in prompts)), "Invalid default prompts")
    check(not any((plugin / name).exists() for name in ("mcp.json", ".app.json", "hooks")),
          "Unexpected integration added to skills-only export")
    skill_root = plugin / "skills/instructions"
    skill = (skill_root / "SKILL.md").read_text(encoding="utf-8")
    check(skill.startswith("---\n") and "\nname: instructions\n" in skill,
          "Skill identity/frontmatter missing")
    check(record["sourceCommit"] in skill, "Skill source commit changed")
    index = json.loads((skill_root / "lookup/knowledge-index.json").read_text(encoding="utf-8"))
    for item in index["files"]:
        target = (skill_root / item["path"]).resolve()
        check(target.is_relative_to(plugin) and target.is_file(), "Missing/unsafe knowledge route")
    reference = (skill_root / "references/uniflora-gpt-reference.md").read_text(encoding="utf-8")
    check("Commit: " + record["sourceCommit"] in reference, "Reference commit changed")
    pairs = re.findall(r"^===== BEGIN FILE (.+?) =====\n(.*?)^===== END FILE \1 =====",
                       reference, re.MULTILINE | re.DOTALL)
    check(len(pairs) == 38 and len(dict(pairs)) == 38, "Embedded section inventory changed")
    bundled = {name[9:]: content for name, content in pairs if name.startswith("snapshot/")}
    expected_blobs = {item["path"]: item["gitBlobSha"] for item in record["bundledFiles"]}
    check(set(bundled) == set(expected_blobs) and len(bundled) == 36,
          "Bundled kit must contain the 36 pinned source files")
    for name, content in bundled.items():
        # One LF separator follows each embedded file. read_text normalizes the
        # reference's CRLF transport to the source kit's LF before verification.
        check(content.endswith("\n"), f"Missing section separator: {name}")
        data = content[:-1].encode("utf-8")
        blob = hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()
        check(blob == expected_blobs.get(name), f"Embedded source differs from pinned Git blob: {name}")
    catalog = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
    check(len(catalog["plugins"]) == 1, "Unexpected marketplace entries")
    entry = catalog["plugins"][0]
    check(entry["name"] == manifest["name"], "Catalog/plugin identity mismatch")
    check(entry["source"]["source"] == "local"
          and (ROOT / entry["source"]["path"]).resolve() == plugin, "Catalog path mismatch")
    check(entry["policy"]["installation"] == "AVAILABLE", "Plugin must remain optional")
    print(f"Plugin export {'FAIL' if errors else 'PASS'}: {checks} checks; {len(errors)} failures")
    for message in errors:
        print("- " + message)
    for message in record["knownMetadataIssues"]:
        print("Preserved export note: " + message)
    return bool(errors)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, IndexError) as exc:
        print(f"Plugin export FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
