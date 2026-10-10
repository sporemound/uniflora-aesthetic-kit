# Uniflora plugin source

[Open the existing Uniflora plugin](https://chatgpt.com/plugins/plugin_02aa24827e008191b1976328c2633fe8). The linked account plugin was private when exported; opening that link requires access to it. The public source below is independently reusable under the repository's license map. Adding the files to GitHub does not change the hosted plugin's audience or create automatic synchronization.

## Included release

`uniflora/` contains the six original editable files from plugin version **0.1.2**, release `pluginrel_6ac9eb292c8c8191af2ef0bb1553ed4f`, exported on 2026-10-10 UTC. The archive bytes are preserved, including CRLF line endings in the bundled reference. Git attributes disable line-ending conversion for the imported files so hashes remain stable on Windows as well. The package's generated internal name and `GPT Creator` presentation fields are retained export metadata, not a claim of external authorship. [EXPORT.json](EXPORT.json) records the source, file hashes, known limits, and the 36 original kit files embedded at commit `92acf469da1a832c0bad510472dd2a31a832acd8`.

| File relative to `uniflora/` | Purpose |
| --- | --- |
| `plugin.json` | Portable Agent Plugins manifest and presentation |
| `.codex-plugin/plugin.json` | Existing Codex compatibility manifest |
| `skills/instructions/SKILL.md` | Subject preservation, branch selection, botany, output and attribution rules |
| `skills/instructions/agents/openai.yaml` | Skill presentation |
| `skills/instructions/lookup/knowledge-index.json` | Route to the bundled reference |
| `skills/instructions/references/uniflora-gpt-reference.md` | Concatenated instructions and complete v0.1 kit source |

The reference's `===== BEGIN FILE ... =====` / `===== END FILE ... =====` markers identify each source section. Paths such as `snapshot/docs/STYLE-GUIDE.md` inside those sections describe the earlier skill package. They are section names here, not separate files on disk. The embedded `SOURCE-SNAPSHOT.md` also mentions a `SHA256SUMS.txt` which is not included in this export; use this repository's [EXPORT.json](EXPORT.json) for verification. Do not resolve copied relative Markdown links against the reference file's directory.

## Use in ChatGPT or Codex

For the existing hosted plugin, open the link above, install or select it where available, and start a new chat with Uniflora selected. Account and workspace availability still apply. Ordinary use of the packaged reference does not need GitHub access. The aesthetic kit itself remains free, offline, and platform-neutral; this optional integration does not make an OpenAI account or subscription a kit requirement.

For repository-based discovery in supported local clients, the catalog is [.agents/plugins/marketplace.json](../.agents/plugins/marketplace.json). Open this repository as a local project and look for **Uniflora** under the **Uniflora Aesthetic Kit** marketplace in the desktop Plugins view. Install it deliberately; the catalog does not enable it automatically. Alternatively, register the GitHub marketplace using current Codex CLI:

```sh
codex plugin marketplace add sporemound/uniflora-aesthetic-kit --ref main
```

Then use the desktop Plugins view to install and test the listed plugin. See the official [package and marketplace guide](https://developers.openai.com/plugins/build/plugins). Availability differs by host; neither catalog creation nor source checks establish a successful host installation. No MCP server, app binding, credentials, hooks, paid font, or third-party runtime is included.

## Review before a new upload

This is an exact source export, not a newly submitted public-directory release. Both exported manifest subtitles exceed the current 30-character authoring limit; the skill's UI subtitle is visibly truncated. Before preparing a fresh upload, shorten those presentation strings, bump and synchronize the two manifest versions, and verify host behavior. Preserve every default prompt's text, type, and order. Keep the imported snapshot unchanged until an explicitly reviewed refresh. Changes made in this repository do not update the existing hosted plugin.

## Validate and contribute

```sh
python tools/validate.py
python tools/validate_plugin.py
```

The plugin check verifies six exported file hashes, manifest agreement, catalog paths, lookup routing, and all 36 embedded source blobs against the recorded Git commit. It reports the preserved metadata limitations separately. It does not certify host installation or botanical identification. To refresh, inspect the selected plugin's current release, review changes and rights, replace all affected files, update `EXPORT.json`, and run both checks. See [CONTRIBUTING.md](../CONTRIBUTING.md).

## Rights

Code and configuration use Unlicense; authored instructions, presentation prose, and this guide use CC BY 4.0, credited to **Uniflora contributors**. The aggregate reference contains multiple material types: original source sections retain the exact scope and notices of the v0.1 kit, including CC0 for Creative Commons' legal-code text. The wrapper does not relicense its contents. See [licenses/README.md](../licenses/README.md) and [ATTRIBUTION.md](../ATTRIBUTION.md). No historical artwork or bundled fonts were introduced.
