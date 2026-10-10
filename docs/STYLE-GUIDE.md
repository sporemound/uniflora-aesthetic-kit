# Practical style guide · v0.1

Uniflora is a visual language applied to a chosen subject. You do not need prior knowledge of the community to use it. Start with the subject, select a branch, and make the composition legible before adding texture.

## A five-step workflow

1. Write one sentence describing the subject and one describing its meaning. List two or three features the result must preserve.
2. Select one primary branch from the table below. A secondary branch may contribute one material or optical effect; it must not erase the primary branch's structure.
3. Choose a medium and a composition. Decide where the subject, reading area, negative space, and focal point sit.
4. Add only the palette, texture, optical treatment, and abstract geometry that serve that composition. Use [the prompt template](../prompts/TEMPLATE.md) or edit [the HTML demonstration](../demo/index.html).
5. Check subject preservation, plant morphology, legibility, motion, and provenance. Record new interpretations before sharing the result.

| Branch | Start here when the subject needs |
| --- | --- |
| `isometric-idm` | Discrete rhythm, modular depth, reciprocal signals, or mirrored relationships. |
| `engraved-architecture` | Carved material, spatial contradiction, folded planes, or architectural narrative. |
| `crt-worlds` | A continuous forest scene expressed through pixel and analog-display language. |
| `nocturnal-optics` | A quiet encounter with light, moisture, distance, glass, or moonlit surfaces. |
| `kilim-burdock` | Repeat, offset, border, reversible cards, or a woven geometric cadence. |
| `botanical-specimen` | Observation, identification, comparison, or a credible plant-focused composition. |

## Shared rules

**Keep the subject intact.** A library remains a library; an invitation still communicates its event; a plant still has its recognizable structure. Avoid replacing every subject with glowing mushrooms, generic occult marks, cyberpunk decoration, or unmotivated visual noise.

**Translate abstractions into relationships.** For “telepathy,” try two distant clusters repeating the same interval pattern across a quiet gap. For “inversion,” choose one axis and reverse depth or tonal roles across it. For “hidden ecology,” reveal a layer or make an occluded relationship visible. These are compositional metaphors, not factual claims. One clear transformation is stronger than several unrelated symbols.

**Name the biology.** If a plant is identifiable, record its species and life stage, use an appropriate reference, and verify morphology. *Monotropa uniflora* is a pale mycoheterotrophic flowering plant with scale leaves and one terminal flower per stem; the flower nods in flowering stages and becomes more upright in fruit. It is not a mushroom. Do not draw a direct tree-root attachment to explain its nutrition. A geometric abstraction can simplify form, but it should be labeled schematic and should not be presented as an identification plate.

**Keep text editable.** Use live HTML text or a separate vector text layer for exact wording. Image-generator lettering is a draft until checked character by character. “None” is a valid text choice. A sample title or slogan has no global authority.

**Use roles, not random swatches.** The six palettes below are new v0.1 proposals. `bg`, `surface`, `text`, `muted`, and `accent` have interface roles; `decor` is decorative. A color's presence in a palette does not certify it for small text against every other color. The source of truth is [tokens.json](../presets/tokens.json); [tokens.css](../presets/tokens.css) exposes the presets for reuse.

**Use fonts already available to the viewer.** This kit bundles and fetches no fonts. Body text uses `system-ui, sans-serif`, numeric or signal labels can use `ui-monospace, monospace`, and a serif display option uses `ui-serif, serif`. Appearance varies by operating system. Pixel, engraved, and woven character should come primarily from composition and assets rather than unreadable body lettering.

## 1. Isometric botanical IDM

| Role | Proposed color |
| --- | --- |
| Background | Deep green-teal `#092E2C` |
| Decorative forest tone | Forest green `#1F5F46` |
| Accent | Turquoise `#63DDC8` |
| Primary text / botanical light | Ivory `#F4F1DC` |

**Form and composition:** Establish an isometric grid, a small set of elevations, and one readable foreground object. Use stepped pixels, modular clusters, and repeat intervals that suggest musical sequencing. Represent inversion on a chosen plane. Mirrored signals can meet across a gap without becoming a conventional occult emblem. Restrained kaleidoscopic structures should occupy a bounded region; the entire image need not be kaleidoscopic. Keep pale ghost-pipe stems, scale leaves, and nodding terminal flowers intelligible wherever depicted.

**Texture and typography:** Use discrete color ramps, sparse dithering, and hard pixel edges. “16-bit” is a visual reference, not a claim that a modern SVG is a literal console asset. Use monospace for short sequence labels and system sans-serif for explanations.

**Accessibility:** Reserve a quiet opaque area for text. Do not encode steps, selected states, or signal direction through green/turquoise alone; add labels or shape differences. Allow diagrams to enlarge without losing the subject's silhouette. Static pixels can convey rhythm without blinking.

## 2. Impossible engraved architecture

| Role | Proposed color |
| --- | --- |
| Paper / background | Ivory `#F3ECD9` |
| Ink / primary text | Near-black `#201E1A` |
| Secondary text | Warm gray `#635D53` |
| Accent | Dark ochre `#7A5523` |

**Form and composition:** Begin with credible Romanesque mass: rounded arches, piers, vaults, and deep recesses. Introduce one spatial contradiction, such as a stair reaching incompatible levels, and leave enough local consistency for the contradiction to read. Sharp triangular modules may tessellate into folded surfaces. They evoke modular origami without copying a particular diagram or claiming a physically validated assembly.

Projection-like lines must respond to surfaces: change spacing with foreshortening, bend across a curved vault, break at occlusion, and change direction across a fold. A flat overlay that ignores depth misses this branch's key relationship.

**Texture and typography:** Use carved edges, directional hatching, and two or three hatch densities to explain planes and shadow. Keep architectural outlines stronger than interior hatching. Serif display text and clean sans-serif explanations can coexist. Do not hatch behind body copy.

**Accessibility:** Provide a plain-language description of the intended contradiction. Keep navigation and buttons geometrically ordinary even when the illustration is impossible. Preserve ink/paper contrast and avoid hairline lettering on a dense texture.

## 3. CRT botanical worlds

| Role | Proposed color |
| --- | --- |
| Background | Dark forest `#071C1A` |
| Surface | Green display shadow `#123D35` |
| Primary text | Pale ivory `#EDF9E8` |
| Accent | Cyan `#65F1E8` |
| Decorative light | Magenta `#F99CE6` |

**Form and composition:** Build a coherent pixel forest with near, middle, and far layers. Crescent moons, ghost pipe, and cyan-magenta light belong here when they serve the chosen scene. Express Sega Genesis-like spatial economy through limited ramps and tile-like shapes; include no copied sprites, interface marks, or game logos. Speculative plant glow must be identified as artistic lighting rather than a real biological trait.

**Texture and typography:** Choose one intentional analog treatment: low-opacity scanlines, restrained chroma displacement, a stable VHS tracking band, or a controlled datamosh passage. Combine effects only with a reason. Distortion is permitted in this branch; it is not required for every CRT work. Keep interface text live and sharp outside the treated artwork.

**Fixed-screen animation:** Lock the camera and display border. Move water, mist, light, or foliage inside that boundary. Keep object positions, terrain, moon, and scene identity continuous; avoid camera drift, zooms, cuts, new objects, and border warping. Prefer small cyclical motions and a matching loop endpoint. Temporal effects are opt-in; use no flashes or rapid luminance or hue oscillation.

**Accessibility:** Provide a static first frame and a pause control for animation. Respect `prefers-reduced-motion`. Keep essential text free of scanlines, blur, chromatic offsets, and temporal damage. This version's web demonstration combines static SVG texture with an optional slow scanline overlay that is off by default; motion is never necessary to inspect the branch.

## 4. Nocturnal botanical optics

| Role | Proposed color |
| --- | --- |
| Background | Midnight blue `#101C2B` |
| Primary text / silver light | Cool ivory `#EEF0F6` |
| Secondary text | Cool gray `#B5BCCB` |
| Accent | Teal `#8AD9CE` |
| Decorative options | Lavender `#C5B8DE`, pink `#E6B6CD`, gold `#D8C08E` |

**Form and composition:** Place one crisp focal surface in a quieter garden: wet stone, a leaf edge, glass, a basin, or a path. Mist separates distances; moonlight gives the scene a directional source. Use a restrained subset of the palette rather than all hues at full strength. Luminous lichen can mean moonlit or reflected lichen; if self-emitting light is invented, label it speculative.

**Texture and optics:** Use shallow depth of field, soft moisture haze, modest anamorphic highlights, and localized refraction. Refraction should follow a visible wet or transparent material. Optics are optional tools for directing attention, not a blanket blur or flare overlay.

**Typography:** Use generous line spacing and clear sans-serif body copy. A serif display heading is optional. Keep lettering away from bright bokeh and narrow highlights.

**Accessibility:** Supply an opaque text surface so that contrast does not depend on a moving or blurred background. Avoid using blur alone to distinguish content states. Provide a written description if optical effects obscure the subject.

## 5. Kilim and burdock

| Role | Proposed color |
| --- | --- |
| Ground / paper | Warm ivory `#F1E5CF` |
| Primary text | Brown-black `#402A28` |
| Accent | Dark teal `#28635D` |
| Decorative options | Rust `#8E392C`, muted gold `#86682A` |

**Form and composition:** Use diamonds, stepped edges, hooked turns, and a deliberate repeat interval. Equal opposing offsets can create rhythm without making the central mark look misplaced. The v0.1 card motif centers a new hook-and-diamond interpretation with 180-degree rotational balance. A reversible composition means the ornament works in either orientation; ordinary text needs a separate readable arrangement or a second card face.

**Texture and typography:** Suggest a flatwoven material through simple interrupted lines or small stepped shapes. Let geometry carry the textile character. Use legible sans-serif text and generous margins. Do not force woven distortion into body letters.

**Historical status:** No regional attribution or symbolic meaning is established for the v0.1 motif. It is a new interpretation, not an authenticated traditional pattern. For a future historically specific design, document the textile, community, date, provenance, and permission before reproducing it. If depicting real burdock, verify its anatomy separately; hooked fruit-head bracts are not a substitute for the whole plant.

**Accessibility:** Keep repeats outside the reading field. Use orientation marks when a card's text is directional. Check pattern density at small sizes and avoid vibrating adjacent stripes. Color must not be the only cue differentiating card faces or actions.

## 6. Botanical specimen art

| Role | Proposed color |
| --- | --- |
| Paper / background | Warm paper `#F7F2E8` |
| Primary text | Botanical ink `#282E29` |
| Secondary text | Gray-green `#606B5C` |
| Accent | Deep green `#385B45` |

**Form and composition:** Choose a life stage and show it consistently. For ghost pipe, preserve the pale stem, small scale leaves, and single nodding flower per flowering stem. Fruiting plants may become upright; do not mix a flowering and fruiting structure into one invented specimen. Separate detail studies from the main plant and label them. Do not invent field locality, collection numbers, scale, or diagnostic anatomy. Consult [the botanical accuracy notes](BOTANICAL-ACCURACY.md) and their primary sources before making identification claims.

Use measured margins and a clear hierarchy: whole plant, useful detail, annotation. An album cover may omit labels while preserving anatomy. A field-guide plate needs verified identification and checked diagnostic detail; this kit's schematic SVGs alone are insufficient for field identification.

**Texture and typography:** Use restrained pen, pencil, or watercolor marks. Paper texture should not hide the plant edge. Serif titles, italic scientific names, and plain sans-serif labels are options, not required lettering. Keep scientific names editable and check their spelling.

**Accessibility:** Include a useful description of observable morphology rather than color alone. Ensure fine details remain visible in an enlarged version. State whether the image is schematic, artistic, or reference-checked; a decorative illustration should not silently become an identification tool.

## Accessibility and review targets

For interfaces, target at least 4.5:1 contrast for ordinary text, 3:1 for large text as defined by WCAG, and 3:1 for essential UI boundaries or graphical information against adjacent colors. Test actual foreground/background pairs after opacity, image backgrounds, and overlays are applied. Decorative colors have no automatic permission to become body text. These targets do not constitute a conformance claim for a later website.

Use semantic HTML, visible keyboard focus, descriptive link text, useful alt text, and layouts that survive zoom and narrow viewports. Decorative SVGs can be hidden from assistive technology; meaningful diagrams need a short explanation of the relationship they show. Never bake essential instructions into a background image. Supply a static route through animated material and retain manual pause/stop controls where animation is used.

Before review, confirm:

- The subject and intended meaning are still recognizable.
- The primary branch reads through form and composition, not just a color filter.
- Any identifiable species, life stage, and anatomical claim are documented and checked.
- Exact text is correct, readable, and editable; decorative lettering is optional.
- Motion stays within its stated boundary and has a calm alternative.
- Each included asset has an author, provenance record, and redistribution basis.
- New choices are labeled as proposals rather than recovered requirements.

Primary accessibility references: [W3C text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [W3C non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html), and [W3C reduced-motion technique C39](https://www.w3.org/WAI/WCAG22/Techniques/css/C39.html).
