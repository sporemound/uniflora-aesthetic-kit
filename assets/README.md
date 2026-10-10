# Editable vector assets

These six scenes are **new v0.1 interpretations**, created for this template. They are not recovered Uniflora image files, copies of an artist's work, commercial game assets, or authenticated historical textile patterns.

All files use `viewBox="0 0 480 360"`. They contain editable vector paths, named layer groups, local SVG definitions, an accessible title, and a description. They contain no raster images, scripts, bundled fonts, network requests, or external dependencies. No lettering or slogan is required by these compositions.

| File | Branch | Useful editable groups |
| --- | --- | --- |
| `svg/isometric-signal.svg` | Isometric botanical IDM | `mirrored-signal-geometry`, `isometric-ground`, `botanical-forms`, `inverted-echo` |
| `svg/engraved-fold.svg` | Impossible engraved architecture | `romanesque-arches`, `folded-ceiling`, `folded-floor`, `impossible-stair-loop`, `deformed-projection-lines` |
| `svg/crt-forest.svg` | CRT botanical worlds | `monitor-frame`, `screen-content`, `stepped-forest`, `ghost-pipes`, `localized-signal-displacement`, `scanlines` |
| `svg/nocturnal-optics.svg` | Nocturnal botanical optics | `moon`, `mist`, `oval-bokeh`, `optical-refraction`, `moonlit-plants` |
| `svg/kilim-burdock.svg` | Kilim and burdock | `balanced-corner-modules`, `centered-diamond`, `burdock-hook-interpretation`, `side-burr-echoes` |
| `svg/specimen-ghost-pipe.svg` | Botanical specimen art | `main-specimen`, `scale-leaf-detail`, `petal-detail`, `morphology-leaders` |

## Edit and reuse

1. Open a file in any text editor or in a free SVG editor such as Inkscape. Recolor its `fill`, `stroke`, and gradient `stop-color` attributes; change a named group's position with `transform`.
2. Preserve or update `<title>` and `<desc>` when you change the subject. These text alternatives should describe the resulting image, not merely the branch name.
3. To embed the whole scene, use `<img src="assets/svg/isometric-signal.svg" alt="Three pale nodding plants on an isometric signal grid">`. Provide contextual alt text in the HTML; the SVG's internal title alone is not a reliable alternative for an external image. Use `alt=""` only when adjacent text already conveys all the information and the image is decorative.
4. To extract a motif, copy its group **and any local definitions it uses**. For example, the CRT screen needs `crt-screen-clip`, `crt-sky`, `crt-scanlines`, and `crt-vignette`. Update the surrounding viewBox and accessible description.
5. If you inline multiple copies of one SVG in HTML, prefix every `id` and update all `url(#...)` and `aria-labelledby` references to avoid duplicate IDs.

No SVG is animated. In the CRT example, all scene marks and displacement marks are inside `screen-content`, clipped by `crt-screen-clip`. Its screen is `x=30`, `y=34`, `width=420`, `height=260`, `rx=22`; the monitor frame is outside that clip. Animate only groups inside this clipped screen, keep the camera and frame fixed, and preserve scene continuity. Keep any playback optional and respect reduced-motion preferences.

The hook-diamond scene was composed to remain equivalent after a 180-degree rotation. It is a generic new interpretation using rhythm and balanced hooks; it assigns no traditional name, provenance, or symbolic meaning to those shapes.

## Plant limits

The ghost-pipe illustrations intentionally retain ivory achlorophyllous scale-leaved stems without ordinary foliage, and **one open nodding flower per stem**, with separate overlapping obovate petals, rounded lower ends, and a visible lower mouth. Inset reproductive hints suggest visible stamens and a stigma; they do not depict the complete number of stamens. Pixel assets quantize that silhouette. The pale or colored light in the CRT and optical scenes is an artistic treatment; it does not imply that *Monotropa uniflora* bioluminesces. The branching optical-garden marks are lichen-like visual motifs without a species identification.

The specimen plate is an illustrative starting point, not a taxonomic key, verified scientific plate, or life-size drawing. No scale or specimen measurements are asserted. Its detached petal study shows a typical five-petal configuration rather than a universal petal count. The morphology was checked against [Native Plant Trust's Go Botany account](https://gobotany.nativeplanttrust.org/species/monotropa/uniflora/); no reference images were copied. Before using an asset for botanical education, an album's factual caption, or a field guide, check the final depiction against the botanical references in the project documentation. Keep any anatomy edits explicit.

## Provenance and terms

See [SVG provenance](../docs/SVG-PROVENANCE.md), [license status](../LICENSE.md), and the repository's [attribution register](../ATTRIBUTION.md). The original SVGs have **CC BY 4.0 terms**, under the project's asset terms. Retain the creator credit and indicate modifications; do not imply endorsement or a historical/cultural attribution that has not been established. Named artist, game-console, and textile references describe a direction; their artwork and product assets are not included.
