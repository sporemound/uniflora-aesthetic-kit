# Uniflora aesthetic template — v0.1

A small, editable creative system for artwork, image prompts, websites, and interfaces. Uniflora is a way to organize perception: botanical specificity, hidden relationships, spatial contradictions, rhythmic repetition, and deliberate material treatments. Your chosen subject stays the subject.

**Status:** initial v0.1 release for review. Repository: [sporemound/uniflora-aesthetic-kit](https://github.com/sporemound/uniflora-aesthetic-kit). Exact palettes, token names, motifs, and example wording are new v0.1 proposals. Recovered directions are recorded separately in [HISTORY-AND-INTERPRETATION.md](docs/HISTORY-AND-INTERPRETATION.md).

## Start in five minutes

1. Open [demo/index.html](demo/index.html) in a browser. It works directly from disk, with no install, account, subscription, or network request. Keep its sibling folders in place.
2. Read the short [manifesto](docs/MANIFESTO.md), then choose a branch in the [style guide](docs/STYLE-GUIDE.md).
3. For images, fill the [prompt template](prompts/TEMPLATE.md). Use the [six examples](prompts/examples.md) as examples of different construction methods, not universal subjects or slogans.
4. For an interface, link `presets/tokens.css`, apply `data-uniflora="BRANCH-ID"` to a container, and use the semantic variables below. The preset changes variables; it does not automatically style your components.
5. Open the compact [preset starter](demo/starter.html) to replace the example subject without adding unrelated imagery.
6. Edit an [SVG motif](assets/README.md) in a text editor or a free vector editor such as Inkscape. Preserve the descriptive metadata and record changes.

```html
<link rel="stylesheet" href="presets/tokens.css">
<style>
  .panel { padding: 2rem; background: var(--uf-bg); color: var(--uf-text); }
  .panel h2 { font-family: var(--uf-heading); }
  .panel a { color: var(--uf-accent); }
</style>
<section class="panel" data-uniflora="engraved-architecture">
  <h2>Your own subject</h2>
  <p>Keep its meaning legible.</p>
</section>
```

## Six branches

| Branch ID | Construction principle | Example asset |
| --- | --- | --- |
| `isometric-idm` | Stepped forms, isometric depth, mirrored signals, restrained inversion | `isometric-signal.svg` |
| `engraved-architecture` | Locally readable Romanesque spaces, impossible connections, hatching and folded facets | `engraved-fold.svg` |
| `crt-worlds` | Pixel forest, phosphor color, deliberate display-contained distortion | `crt-forest.svg` |
| `nocturnal-optics` | One focal plane, moonlight, mist and restrained refraction | `nocturnal-optics.svg` |
| `kilim-burdock` | Centered geometric hooks, rhythmic repetition and half-turn reversal | `kilim-burdock.svg` |
| `botanical-specimen` | Credible morphology, paper margins and adaptable annotations | `specimen-ghost-pipe.svg` |

An archive, machine, landscape, or abstract concept can use these branches without adding plants. Where a plant is identifiable, [botanical accuracy](docs/BOTANICAL-ACCURACY.md) remains explicit. Neon ghost pipe and luminous lichen are artistic treatments, not natural-history claims. Abstract telepathy is represented by correspondence and shared rhythm, without claiming a scientific mechanism.

## Tokens and editing

The same six palettes are in [presets/tokens.json](presets/tokens.json) and [presets/tokens.css](presets/tokens.css). Keep them synchronized. Roles `bg`, `surface`, `text`, `muted`, and `accent` are for readable interfaces; `decor` is an artistic swatch and is not guaranteed suitable for text. Generic font stacks resolve locally; zero fonts are bundled or fetched. Different systems may render different typefaces.

The SVG colors are independently editable artwork colors. Changing CSS tokens does not recolor an SVG loaded with `<img>`. Edit the SVG's color declarations separately, or inline it in your application and deliberately map its fills to your own variables.

The demo is HTML and CSS only. Its sole animation is an optional, slow CRT scanline overlay. The scene and display casing remain stationary. Reduced-motion preferences suppress it. Interface text sits outside the effects. This demonstrates an effect boundary, not a complete video/datamosh generator.

## Repository map

```text
uniflora-aesthetic-kit/
  README.md
  CONTRIBUTING.md
  LICENSE
  LICENSE.md
  ATTRIBUTION.md
  attribution.json
  CHANGELOG.md
  docs/
    MANIFESTO.md
    STYLE-GUIDE.md
    HISTORY-AND-INTERPRETATION.md
    BOTANICAL-ACCURACY.md
    RIGHTS-REVIEW.md
    REFERENCE-SOURCES.md
    SVG-PROVENANCE.md
    REVIEW-CHECKLIST.md
    VALIDATION.md
  presets/
    tokens.json
    tokens.css
  prompts/
    TEMPLATE.md
    template.json
    examples.md
    examples.json
  assets/
    README.md
    svg/
      isometric-signal.svg
      engraved-fold.svg
      crt-forest.svg
      nocturnal-optics.svg
      kilim-burdock.svg
      specimen-ghost-pipe.svg
  demo/
    index.html
    demo.css
    starter.html
  licenses/
    README.md
    Unlicense.txt
    CC-BY-4.0.txt
  tools/
    validate.py
```

## Verify a change

Optional validation needs only Python 3.10+; there is no package installation:

```sh
python tools/validate.py
```

It checks JSON consistency, readable token pairs, local links, SVG structure and external-resource exclusions. It cannot certify botanical identification, legal rights, or full accessibility. See [VALIDATION.md](docs/VALIDATION.md) for the performed checks and [REVIEW-CHECKLIST.md](docs/REVIEW-CHECKLIST.md) for the remaining human review. If a browser blocks local file links, you can optionally serve the folder with `python -m http.server 8000 --bind 127.0.0.1` and open `http://127.0.0.1:8000/demo/`.

## Licenses and contributions

License scope: Unlicense for code and tokens, preserving the repository's established software license; CC BY 4.0 for documentation, prompt prose, and original motifs. Complete license texts and the exact scope map are in [licenses/README.md](licenses/README.md). Maintained by [sporemound](https://github.com/sporemound), with original creative material credited to Uniflora contributors. AI-assisted material is not asserted to have guaranteed copyright protection. No historic artwork, third-party images, game sprites, origami instructions, commercial fonts, or paid resources are bundled.

Read [ATTRIBUTION.md](ATTRIBUTION.md) and [RIGHTS-REVIEW.md](docs/RIGHTS-REVIEW.md) before releasing. The code/art licenses do not convey official community status or trademark rights. Follow [CONTRIBUTING.md](CONTRIBUTING.md) when changing branches or importing material. The creator authorized publication to the repository after this package review. Future imports need their own rights review.
