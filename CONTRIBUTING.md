# Contributing

This project is an initial v0.1 release for review. Keep changes small enough to compare visually and explain their purpose. A new subject is welcome; it must retain its meaning when translated into the visual language.

1. Identify the affected branch and the subject invariant. Explain what the change does to composition, spatial relationships, rhythm, form, or material.
2. Distinguish recovered user choices from your new interpretation. An example phrase, font treatment, palette, or generated image is not a universal Uniflora rule. Add evidence to the history register before claiming a historical requirement.
3. Preserve branch differences. Glitch exclusions belong to the brief that requested them. CRT distortion is allowed in the CRT branch; effects must preserve a fixed screen, scene continuity, a static alternative, and reduced-motion behavior.
4. For identifiable plants, name the species and life stage and check an institutional botanical source. Record the source. Avoid mushroom substitutions, invented leaf anatomy, and unsupported ecological labels. Obtain botanical review before releasing identification material.
5. Record every new asset in `attribution.json` and `ATTRIBUTION.md`: author or source, URL where applicable, original/adapted status, license, evidence, changes, and unresolved rights. Keep required notices. A download being free does not establish redistribution rights.
6. For historical textiles, identify the actual object, provenance, and supported interpretation. Do not invent regional or universal symbolic meanings. The v0.1 kilim/burdock motif is explicitly new geometry.
7. Keep code dependency-free unless a documented reason warrants a dependency. Do not add required paid tools, subscriptions, font services, analytics, tracking pixels, or proprietary assets. Named artists and platforms are references, never a license to copy their works.
8. Update tokens in both JSON and CSS. Check normal text on both background and surface. Do not use decorative swatches for necessary text or state labels without checking contrast.
9. Run `python tools/validate.py`, inspect the demo at desktop and narrow widths, expand each example, navigate by keyboard, and test reduced-motion preferences. Document what you actually tested.

For a future public contribution, state that you have authority to contribute your changes under the Unlicense for code and CC BY 4.0 for documentation and original art, as mapped in `licenses/README.md`. Disclose AI assistance and borrowed material. Do not assert the AI as a copyright owner. Do not silently relicense previous contributions.

For plugin work, read [plugins/README.md](plugins/README.md). The six files under `plugins/uniflora/` are an exact imported release. Do not silently edit its pinned reference or claim that repository changes update the hosted plugin. Refresh the release and provenance together, preserve all default prompts and license boundaries, and run the export validator. Metadata normalization for a new upload must be identified as a modification and versioned.

Suggested change description:

```text
Branch / subject:
Invariant preserved:
New interpretation or recovered choice:
Files changed:
Asset provenance and license evidence:
Botanical or cultural review:
Validation performed:
Unresolved decisions:
```
