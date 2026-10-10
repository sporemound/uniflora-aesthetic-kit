# Uniflora bundled reference snapshot
Source: https://github.com/sporemound/uniflora-aesthetic-kit
Commit: 92acf469da1a832c0bad510472dd2a31a832acd8
Each section below reproduces a bundled source file. Preserve the separate license terms described in the source files.

===== BEGIN FILE SKILL.md =====
---
name: uniflora
description: Create Uniflora artwork briefs, image prompts, websites, and interfaces using its six botanical and visual branches. Use when the user requests the Uniflora aesthetic or asks to adapt its kit; do not apply it to unrelated design work.
---

# Uniflora

Apply a selected Uniflora branch to the user's actual subject. The bundled `snapshot/` is a complete local reference copy of [sporemound/uniflora-aesthetic-kit](https://github.com/sporemound/uniflora-aesthetic-kit) at commit `92acf469da1a832c0bad510472dd2a31a832acd8`. Ordinary use needs no GitHub fetch. See `SOURCE-SNAPSHOT.md` when checking provenance or redistributing material.

## Choose and preserve

Start with the user's subject, intended meaning, required content, medium, and constraints. Keep the subject recognizable and the intended message intact. Choose one primary branch for its construction principle; a secondary branch may supply a bounded effect if useful. Do not insert ghost pipe or other plants into a subject that does not call for them.

| Branch ID | Use for | Read |
| --- | --- | --- |
| `isometric-idm` | Isometric depth, stepped forms, mirrored signal rhythm, restrained inversion | `snapshot/docs/STYLE-GUIDE.md` §1 |
| `engraved-architecture` | Romanesque mass, locally legible spatial contradiction, hatching, folded planes, surface-responsive projection | Style guide §2 |
| `crt-worlds` | Coherent pixel forest, fixed display, contained analog treatment or animation | Style guide §3 |
| `nocturnal-optics` | Moonlit moisture, one focal plane, mist, material-motivated refraction | Style guide §4 |
| `kilim-burdock` | Repeated hooks and diamonds, balanced offsets, reversible ornament | Style guide §5 |
| `botanical-specimen` | Morphology-led plant study, detail views, measured margins, checked labels | Style guide §6 |

Read only the selected section and the shared rules of `snapshot/docs/STYLE-GUIDE.md`. Use `snapshot/docs/MANIFESTO.md` for the conceptual language when the user asks what Uniflora means. Read `snapshot/docs/HISTORY-AND-INTERPRETATION.md` when drawing on prior choices: distinguish reconfirmed directions from newly proposed palettes, motifs, lettering, and compositions. An exclusion from one earlier brief is not a global rule. CRT distortion remains valid in `crt-worlds` when it serves the scene.

## Route by task

- **Artwork brief or image-generation prompt:** Fill the fields in `snapshot/prompts/TEMPLATE.md` with concrete subject invariants, branch, medium, composition, palette, optics, abstraction, exact text, brief-specific exclusions, biology, and motion. `snapshot/prompts/template.json` is an editable data shape; `snapshot/prompts/examples.md` offers branch-specific examples, not defaults to copy wholesale. Deliver a complete, usable prompt or brief, not a list of aesthetic adjectives. Treat example colors, lettering, and layouts as editable choices.
- **Website or interface:** Read `snapshot/presets/tokens.json` and `tokens.css`, the relevant style-guide section, and the accessibility section of the guide. `snapshot/demo/starter.html` and `snapshot/demo/index.html` are editable local examples. Build the requested functioning page or interface with semantic structure, responsive layout, visible focus, checked text and control contrast, descriptive alternatives for meaningful art, and reduced-motion behavior where needed. Keep essential text and controls separate from distorted artwork. Tokens are proposals; adapt them while retaining readable roles. CSS tokens do not automatically recolor external SVG files.
- **Botanical subject:** Read `snapshot/docs/BOTANICAL-ACCURACY.md` and `snapshot/assets/README.md`. Name an identifiable plant and life stage; verify its morphology against an institutional flora or equivalent source before making educational or identification claims. For flowering *Monotropa uniflora*, preserve pale scale-leaved stems and one nodding terminal flower per stem; do not depict it as a mushroom. Separate flowering from upright fruiting stages. Mark invented glow, color, organ changes, or ecology as artistic interpretation. A schematic asset is not a field-identification plate.
- **Vector motif or asset adaptation:** Inspect `snapshot/assets/README.md`, `snapshot/docs/SVG-PROVENANCE.md`, and the selected original SVG in `snapshot/assets/svg/`. Preserve editable paths and groups. Update title, description, and contextual alt text when changing the subject. Carry over local SVG definitions used by extracted groups and avoid duplicate IDs when inlining copies.
- **Provenance or reuse:** Read `snapshot/ATTRIBUTION.md`, `snapshot/licenses/README.md`, and `snapshot/docs/RIGHTS-REVIEW.md`. Preserve the separate terms: software, demo code, and tokens under Unlicense; documentation, prompt prose, and original SVGs under CC BY 4.0. Credit **Uniflora contributors**, link the source and CC BY 4.0, and indicate changes when reusing its CC BY material. Do not claim these motifs are historical originals, certified botanical plates, third-party artwork, or official endorsements.

## Complete the result

Keep exact requested copy editable as HTML text, a vector text layer, or a separate text overlay; generated lettering requires character-by-character review. For motion, specify scene continuity, effect boundary, a static view, and pause/reduced-motion behavior. In CRT work, the camera and display border stay fixed while selected changes occur within the screen; controlled distortion is allowed there. Check the delivered artifact against the user's invariants, botanical accuracy, legibility, and license obligations. When a choice is newly interpreted rather than recovered, label it as a proposal for this brief.

===== END FILE SKILL.md =====

===== BEGIN FILE SOURCE-SNAPSHOT.md =====
# Bundled source snapshot

- Repository: https://github.com/sporemound/uniflora-aesthetic-kit
- Source commit: `92acf469da1a832c0bad510472dd2a31a832acd8` (`main`, 2026-10-10 UTC)
- Bundled path: `snapshot/`
- Scope: all 36 tracked files from that commit, preserving paths and content; Git history is excluded.
- Purpose: local reference and editable starting material for ordinary skill use. The bundled copy is not evidence that the examples are approved global brand rules.

The snapshot contains the repository's documentation, prompt templates and examples, JSON and CSS tokens, six original SVGs, demo, validation tool, attribution records, and complete separate license texts. `snapshot/licenses/README.md` maps software and tokens to Unlicense and documentation, prompt prose, and original SVGs to CC BY 4.0. Credit the original art and documentation to **Uniflora contributors**, link the source and license, and indicate modifications when reusing those CC BY materials. `snapshot/ATTRIBUTION.md` and `snapshot/docs/RIGHTS-REVIEW.md` describe the provenance limits.

`SHA256SUMS.txt` lists the bytewise hashes of every bundled source file. To refresh the snapshot, review upstream changes and rights, then update the commit, copied files, hashes, and any skill guidance affected by changed source material. Do not silently replace the pinned reference during routine use.

===== END FILE SOURCE-SNAPSHOT.md =====

===== BEGIN FILE snapshot/assets/README.md =====
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

===== END FILE snapshot/assets/README.md =====

===== BEGIN FILE snapshot/assets/svg/crt-forest.svg =====
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 360" role="img" aria-labelledby="crt-forest-title crt-forest-desc">
  <title id="crt-forest-title">Fixed-screen botanical CRT world</title>
  <desc id="crt-forest-desc">An original static CRT monitor encloses a stepped forest with a crescent moon, pale scaled ghost-pipe stems, cyan and magenta accents, scanlines, and small displaced signal bands. All marks are clipped inside the screen; its frame stays intact. Distortion is intentional in this branch. This is a stylized scene, not a botanical field plate.</desc>
  <metadata>Uniflora aesthetic template v0.1. Original newly proposed vector interpretation; no historical asset, artist artwork, game asset, photograph, or traditional textile pattern reproduced. Asset terms: CC BY 4.0; creator-authorized repository publication; see LICENSE.md, ATTRIBUTION.md and docs/SVG-PROVENANCE.md.</metadata>
  <defs>
    <clipPath id="crt-screen-clip"><rect x="30" y="34" width="420" height="260" rx="22"/></clipPath>
    <linearGradient id="crt-sky" x2="0" y2="1"><stop stop-color="#101b36"/><stop offset="1" stop-color="#0b4142"/></linearGradient>
    <pattern id="crt-scanlines" width="4" height="4" patternUnits="userSpaceOnUse"><path d="M0 1H4" stroke="#031714" stroke-width="1"/></pattern>
    <radialGradient id="crt-vignette"><stop offset=".56" stop-color="#071521" stop-opacity="0"/><stop offset="1" stop-color="#071521" stop-opacity=".67"/></radialGradient>
</defs>

  <rect id="background" width="480" height="360" fill="#100f22"/>
  <g id="monitor-frame"><rect x="12" y="14" width="456" height="324" rx="21" fill="#2b2a36" stroke="#605967" stroke-width="2"/><rect x="25" y="28" width="430" height="275" rx="27" fill="#080e18" stroke="#807585" stroke-width="2"/><path d="M33 307H447V324H33Z" fill="#1b1d27"/><path d="M190 338V350H290V338" fill="#24242f"/><rect x="38" y="314" width="24" height="3" fill="#77717e"/><circle cx="430" cy="316" r="3" fill="#70d4bf"/></g>
  <g id="screen-content" clip-path="url(#crt-screen-clip)">
    <rect x="30" y="34" width="420" height="260" fill="url(#crt-sky)"/>
    <g id="moon-and-stars"><path d="M313 54A28 28 0 1 0 343 92A24 24 0 0 1 313 54Z" fill="#92dce0"/><rect x="68" y="226" width="10" height="3" fill="#cf53b6"/><rect x="93" y="236" width="7" height="4" fill="#67e9d3"/><rect x="134" y="253" width="9" height="3" fill="#cf53b6"/><rect x="150" y="215" width="4" height="4" fill="#68dccc"/><rect x="352" y="231" width="14" height="2" fill="#7af0dc"/><rect x="384" y="246" width="9" height="4" fill="#d354b8"/><rect x="75" y="178" width="3" height="3" fill="#79dbc6"/><rect x="323" y="194" width="3" height="3" fill="#dc79c2"/><rect x="360" y="150" width="4" height="4" fill="#70c8d4"/><rect x="211" y="69" width="2" height="2" fill="#93d4df"/><rect x="339" y="75" width="2" height="2" fill="#93d4df"/></g>
    <g id="stepped-forest"><path d="M40 280V84H59V280Z" fill="#082d31"/><path d="M40 116H27V109H17V103H11 M59 136H71V127H79" fill="none" stroke="#0d6660" stroke-width="5"/><path d="M44 279V92" stroke="#08716a" stroke-width="2"/><path d="M71 280V64H84V280Z" fill="#073e3c"/><path d="M71 96H58V89H48V83H42 M84 116H96V107H104" fill="none" stroke="#0d6660" stroke-width="5"/><path d="M75 279V72" stroke="#08716a" stroke-width="2"/><path d="M107 280V115H130V280Z" fill="#0a5450"/><path d="M107 147H94V140H84V134H78 M130 167H142V158H150" fill="none" stroke="#0d6660" stroke-width="5"/><path d="M111 279V123" stroke="#08716a" stroke-width="2"/><path d="M155 280V73H169V280Z" fill="#082d31"/><path d="M155 105H142V98H132V92H126 M169 125H181V116H189" fill="none" stroke="#0d6660" stroke-width="5"/><path d="M159 279V81" stroke="#08716a" stroke-width="2"/><path d="M197 280V113H218V280Z" fill="#073e3c"/><path d="M197 145H184V138H174V132H168 M218 165H230V156H238" fill="none" stroke="#0d6660" stroke-width="5"/><path d="M201 279V121" stroke="#08716a" stroke-width="2"/><path d="M268 280V59H281V280Z" fill="#0a5450"/><path d="M268 91H255V84H245V78H239 M281 111H293V102H301" fill="none" stroke="#0d6660" stroke-width="5"/><path d="M272 279V67" stroke="#08716a" stroke-width="2"/><path d="M304 280V92H326V280Z" fill="#082d31"/><path d="M304 124H291V117H281V111H275 M326 144H338V135H346" fill="none" stroke="#0d6660" stroke-width="5"/><path d="M308 279V100" stroke="#08716a" stroke-width="2"/><path d="M354 280V67H369V280Z" fill="#073e3c"/><path d="M354 99H341V92H331V86H325 M369 119H381V110H389" fill="none" stroke="#0d6660" stroke-width="5"/><path d="M358 279V75" stroke="#08716a" stroke-width="2"/><path d="M398 280V103H421V280Z" fill="#0a5450"/><path d="M398 135H385V128H375V122H369 M421 155H433V146H441" fill="none" stroke="#0d6660" stroke-width="5"/><path d="M402 279V111" stroke="#08716a" stroke-width="2"/><path d="M435 280V43H447V280Z" fill="#082d31"/><path d="M435 75H422V68H412V62H406 M447 95H459V86H467" fill="none" stroke="#0d6660" stroke-width="5"/><path d="M439 279V51" stroke="#08716a" stroke-width="2"/></g>
    <g id="forest-floor"><path d="M30 258H74V252H118V261H165V249H216V259H260V251H298V264H343V250H389V261H450V294H30Z" fill="#09514a"/><path d="M30 276H110V269H186V278H252V269H320V279H387V273H450V294H30Z" fill="#07332e"/></g>
    <g id="bioluminescent-accents" fill="none" stroke-width="2"><path d="M84 253H114M129 269H148M307 263H326M351 280H397" stroke="#71e5d5"/><path d="M48 268H73M161 257H194M263 279H289M400 264H421" stroke="#bf57ae"/></g>
    <g id="ghost-pipes"><g id="crt-left" transform="translate(196 267) scale(0.84)" stroke-linejoin="miter">
      <path fill="#e4e8ed" d="M0 0H8V-27H5V-54H9V-89H13V-116H19V-127H30V-124H36V-114H42V-116H47V-132H40V-138H18V-133H10V-121H5V-100H1V-74H-3V-35H0Z"/>
      <path fill="#ed8ed5" d="M0-23H-6V-34H-10V-42H-4V-36H2Z M6-57H14V-67H18V-74H12V-68H6Z M2-85H-4V-92H-6V-100H0V-96H5Z M10-109H18V-115H20V-122H14V-116H9Z"/>
      <g id="crt-left-five-petals" stroke="#559185" stroke-width="1" fill="#e4e8ed">
        <path d="M36-115L32-111L30-101V-92H32V-89H36V-91H40V-104Z"/>
        <path d="M43-115L47-111L49-101V-92H47V-89H43V-91H39V-104Z"/>
        <path d="M35-112L32-106L29-96V-88H31V-85H37V-88H41V-102Z"/>
        <path d="M43-112L47-106L50-96V-88H48V-85H42V-88H38V-102Z"/>
        <path d="M39-113L35-105L34-95V-87H36V-84H43V-87H45V-95L43-105Z"/>
        <g id="crt-left-flower-opening" stroke="none"><path d="M32-93H48V-91H50V-87H48V-85H33V-87H30V-91H32Z" fill="#559185"/><path d="M34-90H36V-88H34Z M43-90H45V-88H43Z M38-89H41V-87H38Z" fill="#e4e8ed"/><path d="M31-87H34V-85H47V-87H49V-84H32Z" fill="#e4e8ed"/></g>
      </g>
    </g><g id="crt-center" transform="translate(240 272) scale(1.15)" stroke-linejoin="miter">
      <path fill="#ddf3ef" d="M0 0H8V-27H5V-54H9V-89H13V-116H19V-127H30V-124H36V-114H42V-116H47V-132H40V-138H18V-133H10V-121H5V-100H1V-74H-3V-35H0Z"/>
      <path fill="#b16fc1" d="M0-23H-6V-34H-10V-42H-4V-36H2Z M6-57H14V-67H18V-74H12V-68H6Z M2-85H-4V-92H-6V-100H0V-96H5Z M10-109H18V-115H20V-122H14V-116H9Z"/>
      <g id="crt-center-five-petals" stroke="#559185" stroke-width="1" fill="#ddf3ef">
        <path d="M36-115L32-111L30-101V-92H32V-89H36V-91H40V-104Z"/>
        <path d="M43-115L47-111L49-101V-92H47V-89H43V-91H39V-104Z"/>
        <path d="M35-112L32-106L29-96V-88H31V-85H37V-88H41V-102Z"/>
        <path d="M43-112L47-106L50-96V-88H48V-85H42V-88H38V-102Z"/>
        <path d="M39-113L35-105L34-95V-87H36V-84H43V-87H45V-95L43-105Z"/>
        <g id="crt-center-flower-opening" stroke="none"><path d="M32-93H48V-91H50V-87H48V-85H33V-87H30V-91H32Z" fill="#559185"/><path d="M34-90H36V-88H34Z M43-90H45V-88H43Z M38-89H41V-87H38Z" fill="#ddf3ef"/><path d="M31-87H34V-85H47V-87H49V-84H32Z" fill="#ddf3ef"/></g>
      </g>
    </g><g id="crt-right" transform="translate(291 273) scale(0.62)" stroke-linejoin="miter">
      <path fill="#d8e9df" d="M0 0H8V-27H5V-54H9V-89H13V-116H19V-127H30V-124H36V-114H42V-116H47V-132H40V-138H18V-133H10V-121H5V-100H1V-74H-3V-35H0Z"/>
      <path fill="#cf6abd" d="M0-23H-6V-34H-10V-42H-4V-36H2Z M6-57H14V-67H18V-74H12V-68H6Z M2-85H-4V-92H-6V-100H0V-96H5Z M10-109H18V-115H20V-122H14V-116H9Z"/>
      <g id="crt-right-five-petals" stroke="#559185" stroke-width="1" fill="#d8e9df">
        <path d="M36-115L32-111L30-101V-92H32V-89H36V-91H40V-104Z"/>
        <path d="M43-115L47-111L49-101V-92H47V-89H43V-91H39V-104Z"/>
        <path d="M35-112L32-106L29-96V-88H31V-85H37V-88H41V-102Z"/>
        <path d="M43-112L47-106L50-96V-88H48V-85H42V-88H38V-102Z"/>
        <path d="M39-113L35-105L34-95V-87H36V-84H43V-87H45V-95L43-105Z"/>
        <g id="crt-right-flower-opening" stroke="none"><path d="M32-93H48V-91H50V-87H48V-85H33V-87H30V-91H32Z" fill="#559185"/><path d="M34-90H36V-88H34Z M43-90H45V-88H43Z M38-89H41V-87H38Z" fill="#d8e9df"/><path d="M31-87H34V-85H47V-87H49V-84H32Z" fill="#d8e9df"/></g>
      </g>
    </g></g>
    <g id="localized-signal-displacement" fill="none"><path d="M31 139H117M124 139H205M221 139H449" stroke="#42cfbf" stroke-width="2" opacity=".33"/><path d="M31 141H104M138 141H195M230 141H449" stroke="#db56b8" opacity=".34"/><path d="M44 228H92M321 228H416" stroke="#a4ebdf" stroke-width="2" opacity=".33"/><path d="M48 230H97M316 230H411" stroke="#da6ab9" opacity=".42"/></g>
    <rect id="scanlines" x="30" y="34" width="420" height="260" fill="url(#crt-scanlines)" opacity=".3"/>
    <rect id="screen-edge-shade" x="30" y="34" width="420" height="260" fill="url(#crt-vignette)"/>
  </g>
  <path id="glass-reflection" d="M51 42Q40 43 37 72V184" fill="none" stroke="#9fa4b0" stroke-width="2" opacity=".27"/>

</svg>

===== END FILE snapshot/assets/svg/crt-forest.svg =====

===== BEGIN FILE snapshot/assets/svg/engraved-fold.svg =====
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 360" role="img" aria-labelledby="engraved-fold-title engraved-fold-desc">
  <title id="engraved-fold-title">Engraved impossible folded interior</title>
  <desc id="engraved-fold-desc">An original black-and-ivory Romanesque interior. Round arches, dense cross-hatching, an impossible elevated stair loop, and sharp folded rhombi share one room. Thin projection-like curves change direction over the folded ceiling and stair surfaces. No existing engraving or origami crease pattern is reproduced.</desc>
  <metadata>Uniflora aesthetic template v0.1. Original newly proposed vector interpretation; no historical asset, artist artwork, game asset, photograph, or traditional textile pattern reproduced. Asset terms: CC BY 4.0; creator-authorized repository publication; see LICENSE.md, ATTRIBUTION.md and docs/SVG-PROVENANCE.md.</metadata>
  <defs>
    <pattern id="engraved-hatch" width="6" height="6" patternUnits="userSpaceOnUse"><rect width="6" height="6" fill="#ded9cd"/><path d="M-1 1L5 7M2-2L8 4" stroke="#36382e" stroke-width=".7"/></pattern>
    <pattern id="engraved-crosshatch" width="7" height="7" patternUnits="userSpaceOnUse"><rect width="7" height="7" fill="#c8c4b8"/><path d="M-1 1L6 8M1-1L8 6M-1 6L6-1M1 8L8 1" stroke="#292b24" stroke-width=".7"/></pattern>
</defs>

  <rect id="background" width="480" height="360" fill="#eee9dd"/>
  <g id="crosshatched-room" stroke="#262721" stroke-width="1">
    <path d="M20 337V26H460V337Z" fill="url(#engraved-hatch)"/>
    <path d="M44 277V71L240 28L437 71V277L240 337Z" fill="#eee9dd"/>
    <path d="M44 71L240 119L437 71M240 119V337M44 277L240 337L437 277" fill="none"/>
    <path d="M44 71V277L72 284V78Z M409 78V284L437 277V71Z" fill="url(#engraved-hatch)"/>
  </g>
  <g id="romanesque-arches"><path d="M61 277V164A35.0 35.0 0 0 1 131 164V277Z" fill="#171816" stroke="#171816" stroke-width="7"/><path d="M54 278V164A42.0 42.0 0 0 1 138 164V278" fill="none" stroke="#171816" stroke-width="3"/><path d="M67 270V165A29.0 29.0 0 0 1 125 165V270" fill="none" stroke="#e9e4d8" stroke-width="1"/><path d="M146 277V125A38.0 38.0 0 0 1 222 125V277Z" fill="#171816" stroke="#171816" stroke-width="7"/><path d="M139 278V125A45.0 45.0 0 0 1 229 125V278" fill="none" stroke="#171816" stroke-width="3"/><path d="M152 270V126A32.0 32.0 0 0 1 216 126V270" fill="none" stroke="#e9e4d8" stroke-width="1"/><path d="M251 277V125A38.0 38.0 0 0 1 327 125V277Z" fill="#171816" stroke="#171816" stroke-width="7"/><path d="M244 278V125A45.0 45.0 0 0 1 334 125V278" fill="none" stroke="#171816" stroke-width="3"/><path d="M257 270V126A32.0 32.0 0 0 1 321 126V270" fill="none" stroke="#e9e4d8" stroke-width="1"/><path d="M349 277V164A35.0 35.0 0 0 1 419 164V277Z" fill="#171816" stroke="#171816" stroke-width="7"/><path d="M342 278V164A42.0 42.0 0 0 1 426 164V278" fill="none" stroke="#171816" stroke-width="3"/><path d="M355 270V165A29.0 29.0 0 0 1 413 165V270" fill="none" stroke="#e9e4d8" stroke-width="1"/></g>
  <g id="folded-ceiling" stroke="#272823" stroke-width="1">
    <path d="M44 71L140 48L240 119Z" fill="#c6c2b6"/>
    <path d="M140 48L240 28L240 119Z" fill="url(#engraved-hatch)"/>
    <path d="M240 28L340 48L240 119Z" fill="#ded9cd"/>
    <path d="M340 48L437 71L240 119Z" fill="url(#engraved-crosshatch)"/>
    <path d="M44 71L142 88L140 48 M142 88L240 119 M437 71L337 88L340 48 M337 88L240 119" fill="none"/>
  </g>
  <g id="folded-floor"><path d="M74 284L101 270L128 284L101 298Z" fill="#ded8cc" stroke="#292a25" stroke-width=".8"/><path d="M74 284L101 286L101 270M101 286L128 284" fill="none" stroke="#292a25" stroke-width=".7"/><path d="M128 284L155 270L182 284L155 298Z" fill="#262721" stroke="#292a25" stroke-width=".8"/><path d="M128 284L155 286L155 270M155 286L182 284" fill="none" stroke="#292a25" stroke-width=".7"/><path d="M182 284L209 270L236 284L209 298Z" fill="#aca89b" stroke="#292a25" stroke-width=".8"/><path d="M182 284L209 286L209 270M209 286L236 284" fill="none" stroke="#292a25" stroke-width=".7"/><path d="M236 284L263 270L290 284L263 298Z" fill="#ded8cc" stroke="#292a25" stroke-width=".8"/><path d="M236 284L263 286L263 270M263 286L290 284" fill="none" stroke="#292a25" stroke-width=".7"/><path d="M290 284L317 270L344 284L317 298Z" fill="#262721" stroke="#292a25" stroke-width=".8"/><path d="M290 284L317 286L317 270M317 286L344 284" fill="none" stroke="#292a25" stroke-width=".7"/><path d="M344 284L371 270L398 284L371 298Z" fill="#aca89b" stroke="#292a25" stroke-width=".8"/><path d="M344 284L371 286L371 270M371 286L398 284" fill="none" stroke="#292a25" stroke-width=".7"/><path d="M101 305L128 291L155 305L128 319Z" fill="#262721" stroke="#292a25" stroke-width=".8"/><path d="M101 305L128 307L128 291M128 307L155 305" fill="none" stroke="#292a25" stroke-width=".7"/><path d="M155 305L182 291L209 305L182 319Z" fill="#aca89b" stroke="#292a25" stroke-width=".8"/><path d="M155 305L182 307L182 291M182 307L209 305" fill="none" stroke="#292a25" stroke-width=".7"/><path d="M209 305L236 291L263 305L236 319Z" fill="#ded8cc" stroke="#292a25" stroke-width=".8"/><path d="M209 305L236 307L236 291M236 307L263 305" fill="none" stroke="#292a25" stroke-width=".7"/><path d="M263 305L290 291L317 305L290 319Z" fill="#262721" stroke="#292a25" stroke-width=".8"/><path d="M263 305L290 307L290 291M290 307L317 305" fill="none" stroke="#292a25" stroke-width=".7"/><path d="M317 305L344 291L371 305L344 319Z" fill="#aca89b" stroke="#292a25" stroke-width=".8"/><path d="M317 305L344 307L344 291M344 307L371 305" fill="none" stroke="#292a25" stroke-width=".7"/><path d="M371 305L398 291L425 305L398 319Z" fill="#ded8cc" stroke="#292a25" stroke-width=".8"/><path d="M371 305L398 307L398 291M398 307L425 305" fill="none" stroke="#292a25" stroke-width=".7"/><path d="M74 326L101 312L128 326L101 340Z" fill="#aca89b" stroke="#292a25" stroke-width=".8"/><path d="M74 326L101 328L101 312M101 328L128 326" fill="none" stroke="#292a25" stroke-width=".7"/><path d="M128 326L155 312L182 326L155 340Z" fill="#ded8cc" stroke="#292a25" stroke-width=".8"/><path d="M128 326L155 328L155 312M155 328L182 326" fill="none" stroke="#292a25" stroke-width=".7"/><path d="M182 326L209 312L236 326L209 340Z" fill="#262721" stroke="#292a25" stroke-width=".8"/><path d="M182 326L209 328L209 312M209 328L236 326" fill="none" stroke="#292a25" stroke-width=".7"/><path d="M236 326L263 312L290 326L263 340Z" fill="#aca89b" stroke="#292a25" stroke-width=".8"/><path d="M236 326L263 328L263 312M263 328L290 326" fill="none" stroke="#292a25" stroke-width=".7"/><path d="M290 326L317 312L344 326L317 340Z" fill="#ded8cc" stroke="#292a25" stroke-width=".8"/><path d="M290 326L317 328L317 312M317 328L344 326" fill="none" stroke="#292a25" stroke-width=".7"/><path d="M344 326L371 312L398 326L371 340Z" fill="#262721" stroke="#292a25" stroke-width=".8"/><path d="M344 326L371 328L371 312M371 328L398 326" fill="none" stroke="#292a25" stroke-width=".7"/></g>
  <g id="impossible-stair-loop" stroke="#23251f" stroke-width="1.4" stroke-linejoin="round">
    <path d="M119 248L239 188L360 246L239 307Z" fill="#eee9dd"/>
    <path d="M119 248V231L239 170L360 230V246L239 188Z" fill="url(#engraved-hatch)"/>
    <path d="M157 246L239 205L322 245L239 286Z" fill="#171816"/>
    <path d="M119 231L157 212L181 224L143 243Z M143 243L181 224V231L143 250Z M143 250L182 231L205 243L168 262Z M168 262L205 243V250L168 269Z M168 269L205 250L230 262L192 281Z M192 281L230 262V269L192 288Z" fill="#e8e3d6"/>
    <path d="M239 170L263 183L225 201L201 189Z M263 183V190L225 208V201Z M263 190L287 202L248 222L225 208Z M287 202V209L248 229V222Z M287 209L311 221L272 242L248 229Z M311 221V228L272 249V242Z M311 228L335 240L296 260L272 249Z" fill="#e8e3d6"/>
    <path d="M119 231V312L141 323V243Z M337 241V305L360 294V230Z" fill="url(#engraved-crosshatch)"/>
    <path d="M201 189V136L222 126V200Z" fill="url(#engraved-hatch)"/>
    <path d="M222 126L239 134L239 170L225 201Z" fill="#eee9dd"/>
  </g>
  <g id="deformed-projection-lines" fill="none" stroke="#eee9dd" stroke-width="1.1">
    <path d="M71 70L134 55L166 94L240 108L312 94L346 55L409 70"/>
    <path d="M81 66L132 61L171 96L240 100L307 96L348 61L398 66"/>
    <path d="M91 63L130 68L176 98L240 92L302 98L350 68L389 63"/>
  </g>
  <g id="surface-contours" fill="none" stroke="#6a6b61" stroke-width=".7"><path d="M129 245L241 182L349 238M132 250L241 191L345 244M183 273L218 256M188 276L222 260M195 280L229 264"/></g>

</svg>

===== END FILE snapshot/assets/svg/engraved-fold.svg =====

===== BEGIN FILE snapshot/assets/svg/isometric-signal.svg =====
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 360" role="img" aria-labelledby="isometric-signal-title isometric-signal-desc">
  <title id="isometric-signal-title">Isometric botanical signal garden</title>
  <desc id="isometric-signal-desc">A new isometric interpretation: three pale scaled ghost-pipe stems with individual nodding open flowers, separate blunt petals, and visible lower openings sit on a turquoise rhomboid grid. Stepped geometry and mirrored signal diamonds suggest transmission and inversion. The plants are deliberately quantized, not a diagnostic illustration.</desc>
  <metadata>Uniflora aesthetic template v0.1. Original newly proposed vector interpretation; no historical asset, artist artwork, game asset, photograph, or traditional textile pattern reproduced. Asset terms: CC BY 4.0; creator-authorized repository publication; see LICENSE.md, ATTRIBUTION.md and docs/SVG-PROVENANCE.md.</metadata>
  

  <rect id="background" width="480" height="360" fill="#0b211d"/>
  <g id="pixel-grain" fill="#54a18c" opacity=".42"><rect x="24" y="32" width="2" height="2"/><rect x="42" y="72" width="2" height="2"/><rect x="448" y="42" width="2" height="2"/><rect x="430" y="90" width="2" height="2"/><rect x="60" y="154" width="2" height="2"/><rect x="390" y="35" width="2" height="2"/><rect x="35" y="276" width="2" height="2"/><rect x="441" y="286" width="2" height="2"/><rect x="76" y="326" width="2" height="2"/><rect x="382" y="317" width="2" height="2"/><rect x="310" y="31" width="2" height="2"/><rect x="155" y="30" width="2" height="2"/></g>
  <g id="mirrored-signal-geometry" fill="none" stroke="#5bd9cb" stroke-width="1.5"><path d="M216 129L240 90L264 129L240 168Z" opacity="0.515"/><path d="M192 140L240 78L288 140L240 202Z" opacity="0.450"/><path d="M168 151L240 66L312 151L240 236Z" opacity="0.385"/><path d="M144 162L240 54L336 162L240 270Z" opacity="0.320"/><path d="M120 173L240 42L360 173L240 304Z" opacity="0.255"/>
    <path d="M78 98H131L169 76H202 M402 98H349L311 76H278"/>
    <path d="M78 105H137L171 85H197 M402 105H343L309 85H283" opacity=".5"/>
  </g>
  <g id="isometric-ground">
    <path d="M54 236L240 138L426 236L240 334Z" fill="#143d31" stroke="#40977c" stroke-width="2"/>
    <path d="M54 236V248L240 346V334Z" fill="#082c27"/>
    <path d="M426 236V248L240 346V334Z" fill="#115245"/>
    <g fill="none" stroke="#31866c" stroke-width="1"><path d="M85.0 252.3L271.0 154.3"/><path d="M85.0 219.7L271.0 317.7"/><path d="M116.0 268.7L302.0 170.7"/><path d="M116.0 203.3L302.0 301.3"/><path d="M147.0 285.0L333.0 187.0"/><path d="M147.0 187.0L333.0 285.0"/><path d="M178.0 301.3L364.0 203.3"/><path d="M178.0 170.7L364.0 268.7"/><path d="M209.0 317.7L395.0 219.7"/><path d="M209.0 154.3L395.0 252.3"/></g>
    <path d="M111 236L240 168L369 236L240 304Z" fill="none" stroke="#83d7bb" stroke-width="1.5"/>
  </g>
  <g id="plant-shadows" fill="#071713" opacity=".65"><path d="M151 241L221 272L244 262L172 229Z"/><path d="M225 230L286 261L315 246L246 218Z"/><path d="M290 256L329 276L347 266L310 246Z"/></g>
  <g id="botanical-forms">
    <g id="isometric-left" transform="translate(156 241) scale(0.89)" stroke-linejoin="miter">
      <path fill="#e4edcf" d="M0 0H8V-27H5V-54H9V-89H13V-116H19V-127H30V-124H36V-114H42V-116H47V-132H40V-138H18V-133H10V-121H5V-100H1V-74H-3V-35H0Z"/>
      <path fill="#54c7b6" d="M0-23H-6V-34H-10V-42H-4V-36H2Z M6-57H14V-67H18V-74H12V-68H6Z M2-85H-4V-92H-6V-100H0V-96H5Z M10-109H18V-115H20V-122H14V-116H9Z"/>
      <g id="isometric-left-five-petals" stroke="#559185" stroke-width="1" fill="#e4edcf">
        <path d="M36-115L32-111L30-101V-92H32V-89H36V-91H40V-104Z"/>
        <path d="M43-115L47-111L49-101V-92H47V-89H43V-91H39V-104Z"/>
        <path d="M35-112L32-106L29-96V-88H31V-85H37V-88H41V-102Z"/>
        <path d="M43-112L47-106L50-96V-88H48V-85H42V-88H38V-102Z"/>
        <path d="M39-113L35-105L34-95V-87H36V-84H43V-87H45V-95L43-105Z"/>
        <g id="isometric-left-flower-opening" stroke="none"><path d="M32-93H48V-91H50V-87H48V-85H33V-87H30V-91H32Z" fill="#559185"/><path d="M34-90H36V-88H34Z M43-90H45V-88H43Z M38-89H41V-87H38Z" fill="#e4edcf"/><path d="M31-87H34V-85H47V-87H49V-84H32Z" fill="#e4edcf"/></g>
      </g>
    </g>
    <g id="isometric-center" transform="translate(231 234) scale(1.14)" stroke-linejoin="miter">
      <path fill="#e4edcf" d="M0 0H8V-27H5V-54H9V-89H13V-116H19V-127H30V-124H36V-114H42V-116H47V-132H40V-138H18V-133H10V-121H5V-100H1V-74H-3V-35H0Z"/>
      <path fill="#54c7b6" d="M0-23H-6V-34H-10V-42H-4V-36H2Z M6-57H14V-67H18V-74H12V-68H6Z M2-85H-4V-92H-6V-100H0V-96H5Z M10-109H18V-115H20V-122H14V-116H9Z"/>
      <g id="isometric-center-five-petals" stroke="#559185" stroke-width="1" fill="#e4edcf">
        <path d="M36-115L32-111L30-101V-92H32V-89H36V-91H40V-104Z"/>
        <path d="M43-115L47-111L49-101V-92H47V-89H43V-91H39V-104Z"/>
        <path d="M35-112L32-106L29-96V-88H31V-85H37V-88H41V-102Z"/>
        <path d="M43-112L47-106L50-96V-88H48V-85H42V-88H38V-102Z"/>
        <path d="M39-113L35-105L34-95V-87H36V-84H43V-87H45V-95L43-105Z"/>
        <g id="isometric-center-flower-opening" stroke="none"><path d="M32-93H48V-91H50V-87H48V-85H33V-87H30V-91H32Z" fill="#559185"/><path d="M34-90H36V-88H34Z M43-90H45V-88H43Z M38-89H41V-87H38Z" fill="#e4edcf"/><path d="M31-87H34V-85H47V-87H49V-84H32Z" fill="#e4edcf"/></g>
      </g>
    </g>
    <g id="isometric-right" transform="translate(297 257) scale(0.7)" stroke-linejoin="miter">
      <path fill="#e4edcf" d="M0 0H8V-27H5V-54H9V-89H13V-116H19V-127H30V-124H36V-114H42V-116H47V-132H40V-138H18V-133H10V-121H5V-100H1V-74H-3V-35H0Z"/>
      <path fill="#54c7b6" d="M0-23H-6V-34H-10V-42H-4V-36H2Z M6-57H14V-67H18V-74H12V-68H6Z M2-85H-4V-92H-6V-100H0V-96H5Z M10-109H18V-115H20V-122H14V-116H9Z"/>
      <g id="isometric-right-five-petals" stroke="#559185" stroke-width="1" fill="#e4edcf">
        <path d="M36-115L32-111L30-101V-92H32V-89H36V-91H40V-104Z"/>
        <path d="M43-115L47-111L49-101V-92H47V-89H43V-91H39V-104Z"/>
        <path d="M35-112L32-106L29-96V-88H31V-85H37V-88H41V-102Z"/>
        <path d="M43-112L47-106L50-96V-88H48V-85H42V-88H38V-102Z"/>
        <path d="M39-113L35-105L34-95V-87H36V-84H43V-87H45V-95L43-105Z"/>
        <g id="isometric-right-flower-opening" stroke="none"><path d="M32-93H48V-91H50V-87H48V-85H33V-87H30V-91H32Z" fill="#559185"/><path d="M34-90H36V-88H34Z M43-90H45V-88H43Z M38-89H41V-87H38Z" fill="#e4edcf"/><path d="M31-87H34V-85H47V-87H49V-84H32Z" fill="#e4edcf"/></g>
      </g>
    </g>
  </g>
  <g id="inverted-echo" fill="none" stroke="#3cad99" opacity=".5" stroke-width="1.5"><path d="M187 276L213 289L214 316L221 320L227 316V290L252 277"/><path d="M203 278L223 269L242 278L223 288Z"/></g>
  <g id="rhythm-markers" fill="#8dd8c6"><path d="M50 188H62V190H50Z M418 188H430V190H418Z"/><rect x="43" y="184" width="3" height="3"/><rect x="434" y="184" width="3" height="3"/></g>

</svg>

===== END FILE snapshot/assets/svg/isometric-signal.svg =====

===== BEGIN FILE snapshot/assets/svg/kilim-burdock.svg =====
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 360" role="img" aria-labelledby="kilim-burdock-title kilim-burdock-desc">
  <title id="kilim-burdock-title">Reversible hook-diamond and burdock study</title>
  <desc id="kilim-burdock-desc">An original reversible card composition using centered diamonds, balanced angular hooks, repeated borders, and small burr-like hooked rosettes. It is a newly proposed generic geometric textile interpretation, not a recovered Uniflora artifact or an authenticated motif from a named weaving tradition. No traditional meaning is asserted.</desc>
  <metadata>Uniflora aesthetic template v0.1. Original newly proposed vector interpretation; no historical asset, artist artwork, game asset, photograph, or traditional textile pattern reproduced. Asset terms: CC BY 4.0; creator-authorized repository publication; see LICENSE.md, ATTRIBUTION.md and docs/SVG-PROVENANCE.md.</metadata>
  <defs><pattern id="woven-lines" width="4" height="4" patternUnits="userSpaceOnUse"><path d="M0 0V4M0 2H4" stroke="#736b58" stroke-width=".35"/></pattern></defs>

  <rect id="background" width="480" height="360" fill="#eee1c6"/>
  <g id="woven-grain" fill="none" stroke="#6b6555" stroke-width=".4" opacity=".14"><path d="M0 6H480M0 354H480"/><rect x="33" y="51" width="414" height="258" fill="url(#woven-lines)"/></g>
  <g id="repeating-border" fill="#283f41"><path d="M42 25L52 35L42 45L32 35Z M42 315L52 325L42 335L32 325Z"/><path d="M78 25L88 35L78 45L68 35Z M78 315L88 325L78 335L68 325Z"/><path d="M114 25L124 35L114 45L104 35Z M114 315L124 325L114 335L104 325Z"/><path d="M150 25L160 35L150 45L140 35Z M150 315L160 325L150 335L140 325Z"/><path d="M186 25L196 35L186 45L176 35Z M186 315L196 325L186 335L176 325Z"/><path d="M222 25L232 35L222 45L212 35Z M222 315L232 325L222 335L212 325Z"/><path d="M258 25L268 35L258 45L248 35Z M258 315L268 325L258 335L248 325Z"/><path d="M294 25L304 35L294 45L284 35Z M294 315L304 325L294 335L284 325Z"/><path d="M330 25L340 35L330 45L320 35Z M330 315L340 325L330 335L320 325Z"/><path d="M366 25L376 35L366 45L356 35Z M366 315L376 325L366 335L356 325Z"/><path d="M402 25L412 35L402 45L392 35Z M402 315L412 325L402 335L392 325Z"/><path d="M438 25L448 35L438 45L428 35Z M438 315L448 325L438 335L428 325Z"/><path d="M18 62L28 72L18 82L8 72Z M462 62L472 72L462 82L452 72Z"/><path d="M18 98L28 108L18 118L8 108Z M462 98L472 108L462 118L452 108Z"/><path d="M18 134L28 144L18 154L8 144Z M462 134L472 144L462 154L452 144Z"/><path d="M18 170L28 180L18 190L8 180Z M462 170L472 180L462 190L452 180Z"/><path d="M18 206L28 216L18 226L8 216Z M462 206L472 216L462 226L452 216Z"/><path d="M18 242L28 252L18 262L8 252Z M462 242L472 252L462 262L452 252Z"/><path d="M18 278L28 288L18 298L8 288Z M462 278L472 288L462 298L452 288Z"/></g>
  <g id="balanced-corner-modules">
      <path d="M160 72L199 111L160 150L121 111Z" fill="#94614b"/>
      <path d="M160 82L189 111L160 140L131 111Z" fill="#eee1c6"/>
      <path d="M160 92L179 111L160 130L141 111Z" fill="#64796d"/>
      <path d="M160 72V58H144V67H153 M121 111H107V95H116V104 M199 111H213V95H204V104 M160 150V164H144V155H153" fill="none" stroke="#94614b" stroke-width="5"/>
      <path d="M77 79L96 98L77 117L58 98Z" fill="#64796d"/>
      <path d="M77 87L88 98L77 109L66 98Z" fill="#eee1c6"/>
      <path d="M112 55H118V62H112Z M201 73H207V80H201Z" fill="#ad8c4a"/>
<g transform="translate(480 0) scale(-1 1)">
      <path d="M160 72L199 111L160 150L121 111Z" fill="#94614b"/>
      <path d="M160 82L189 111L160 140L131 111Z" fill="#eee1c6"/>
      <path d="M160 92L179 111L160 130L141 111Z" fill="#64796d"/>
      <path d="M160 72V58H144V67H153 M121 111H107V95H116V104 M199 111H213V95H204V104 M160 150V164H144V155H153" fill="none" stroke="#94614b" stroke-width="5"/>
      <path d="M77 79L96 98L77 117L58 98Z" fill="#64796d"/>
      <path d="M77 87L88 98L77 109L66 98Z" fill="#eee1c6"/>
      <path d="M112 55H118V62H112Z M201 73H207V80H201Z" fill="#ad8c4a"/>
</g><g transform="translate(0 360) scale(1 -1)">
      <path d="M160 72L199 111L160 150L121 111Z" fill="#94614b"/>
      <path d="M160 82L189 111L160 140L131 111Z" fill="#eee1c6"/>
      <path d="M160 92L179 111L160 130L141 111Z" fill="#64796d"/>
      <path d="M160 72V58H144V67H153 M121 111H107V95H116V104 M199 111H213V95H204V104 M160 150V164H144V155H153" fill="none" stroke="#94614b" stroke-width="5"/>
      <path d="M77 79L96 98L77 117L58 98Z" fill="#64796d"/>
      <path d="M77 87L88 98L77 109L66 98Z" fill="#eee1c6"/>
      <path d="M112 55H118V62H112Z M201 73H207V80H201Z" fill="#ad8c4a"/>
</g><g transform="translate(480 360) scale(-1 -1)">
      <path d="M160 72L199 111L160 150L121 111Z" fill="#94614b"/>
      <path d="M160 82L189 111L160 140L131 111Z" fill="#eee1c6"/>
      <path d="M160 92L179 111L160 130L141 111Z" fill="#64796d"/>
      <path d="M160 72V58H144V67H153 M121 111H107V95H116V104 M199 111H213V95H204V104 M160 150V164H144V155H153" fill="none" stroke="#94614b" stroke-width="5"/>
      <path d="M77 79L96 98L77 117L58 98Z" fill="#64796d"/>
      <path d="M77 87L88 98L77 109L66 98Z" fill="#eee1c6"/>
      <path d="M112 55H118V62H112Z M201 73H207V80H201Z" fill="#ad8c4a"/>
</g></g>
  <g id="centered-diamond" stroke-linejoin="miter">
    <path d="M240 75L345 180L240 285L135 180Z" fill="#283f41"/>
    <path d="M240 87L333 180L240 273L147 180Z" fill="#ad8c4a"/>
    <path d="M240 97L323 180L240 263L157 180Z" fill="#eee1c6"/>
    <path d="M240 114L306 180L240 246L174 180Z" fill="#94614b"/>
    <path d="M240 130L290 180L240 230L190 180Z" fill="#eee1c6"/>
    <path d="M240 143L277 180L240 217L203 180Z" fill="#64796d"/>
    <g fill="none" stroke="#283f41" stroke-width="5"><path d="M240 75V59H224V69H232 M345 180H362V163H352V172 M240 285V301H256V291H248 M135 180H118V197H128V188"/><path d="M240 75V59H256V69H248 M345 180H362V197H352V188 M240 285V301H224V291H232 M135 180H118V163H128V172"/></g>
  </g>
  <g id="burdock-hook-interpretation" fill="none" stroke="#eee1c6" stroke-width="2.1" stroke-linecap="round" transform="translate(240 180)"><circle r="12"/><path transform="rotate(0)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(30)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(60)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(90)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(120)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(150)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(180)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(210)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(240)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(270)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(300)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(330)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/></g>
  <g id="side-burr-echoes" fill="none" stroke="#94614b" stroke-width="2" stroke-linecap="round"><g transform="translate(74 180) scale(.73)"><circle r="12"/><path transform="rotate(0)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(30)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(60)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(90)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(120)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(150)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(180)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(210)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(240)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(270)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(300)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(330)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/></g><g transform="translate(406 180) rotate(180) scale(.73)"><circle r="12"/><path transform="rotate(0)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(30)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(60)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(90)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(120)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(150)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(180)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(210)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(240)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(270)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(300)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/><path transform="rotate(330)" d="M0-10V-20Q0-27 6-24Q9-23 7-19"/></g></g>

</svg>

===== END FILE snapshot/assets/svg/kilim-burdock.svg =====

===== BEGIN FILE snapshot/assets/svg/nocturnal-optics.svg =====
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 360" role="img" aria-labelledby="nocturnal-optics-title nocturnal-optics-desc">
  <title id="nocturnal-optics-title">Nocturnal botanical optical garden</title>
  <desc id="nocturnal-optics-desc">An original vector interpretation of a moonlit garden: ivory ghost pipes with reduced scale leaves and one open nodding flower each, overlapping rounded obovate petals, lower flower openings and inset reproductive hints, fine branching lichen-like marks, mist layers, oval bokeh, silver-lavender moonlight, and restrained refracted teal, pink, and gold arcs. Glow is an artistic treatment, not a claim that ghost pipe is bioluminescent.</desc>
  <metadata>Uniflora aesthetic template v0.1. Original newly proposed vector interpretation; no historical asset, artist artwork, game asset, photograph, or traditional textile pattern reproduced. Asset terms: CC BY 4.0; creator-authorized repository publication; see LICENSE.md, ATTRIBUTION.md and docs/SVG-PROVENANCE.md.</metadata>
  <defs>
    <linearGradient id="night-sky" x2="0" y2="1"><stop stop-color="#101825"/><stop offset=".68" stop-color="#23383e"/><stop offset="1" stop-color="#172e30"/></linearGradient>
    <radialGradient id="moon-glow"><stop stop-color="#c5c3dd" stop-opacity=".5"/><stop offset="1" stop-color="#a4abc5" stop-opacity="0"/></radialGradient>
</defs>

  <rect id="background" width="480" height="360" fill="url(#night-sky)"/>
  <g id="moon"><circle cx="302" cy="71" r="33" fill="url(#moon-glow)"/><circle cx="302" cy="71" r="22" fill="#c8c9d6"/><path d="M309 53Q324 66 314 85Q305 93 294 89Q322 95 324 74Q325 60 309 53Z" fill="#aeaabb"/></g>
  <g id="distant-garden" fill="#123a3c"><path d="M0 289C35 232 46 270 71 243S109 275 137 247S183 278 206 251S251 275 277 246S320 276 347 238S393 271 425 234S464 246 480 223V360H0Z"/><path d="M28 302C43 217 47 189 40 158C53 184 58 238 44 313M400 312C418 235 437 221 450 207C428 245 419 276 417 321"/></g>
  <g id="mist" fill="none" stroke="#a5b4c7" stroke-linecap="round"><path d="M-10 212C91 170 131 247 248 208S382 210 498 175" stroke-width="22" opacity=".07"/><path d="M-10 262C75 237 169 289 276 244S388 274 491 237" stroke-width="32" opacity=".1"/><path d="M-15 305C80 293 129 316 228 300S375 315 499 289" stroke-width="16" opacity=".13"/></g>
  <g id="oval-bokeh" fill="none" stroke="#c0bdc9" opacity=".24"><ellipse cx="73" cy="82" rx="28" ry="17"/><ellipse cx="398" cy="120" rx="18" ry="11"/><ellipse cx="139" cy="129" rx="12" ry="7"/><ellipse cx="356" cy="181" rx="30" ry="18"/><ellipse cx="51" cy="196" rx="17" ry="10"/></g>
  <g id="optical-refraction" fill="none"><path d="M71 328C50 244 90 153 160 113C201 90 247 83 307 87" stroke="#73bbb2" stroke-width="1.4" opacity=".56"/><path d="M78 330C56 245 96 157 166 117C207 94 256 89 313 91" stroke="#b5a6cd" stroke-width="1" opacity=".43"/><path d="M341 347C427 272 425 189 377 140" stroke="#dcafbb" stroke-width="1" opacity=".36"/><path d="M347 351C433 276 431 193 383 144" stroke="#bdab7d" stroke-width="1" opacity=".37"/></g>
  <g id="anamorphic-streak" stroke="#97bbc6" stroke-width="1" opacity=".26"><path d="M39 73H228M330 73H453"/><path d="M98 76H275M341 76H414" stroke-width=".6"/></g>
  <path id="garden-ground" d="M0 323Q71 291 125 319T230 308T334 319T480 312V360H0Z" fill="#132a2c"/>
  <g id="lichen-like-branching"><g transform="translate(56 291) scale(1)" stroke="#69b3a4" stroke-width="1.6" fill="none"><path d="M0 0V-17L-7-23L-9-34M-7-23L-18-21L-24-28M0-12L10-20L12-31M10-20L22-19L26-26M0-7L-12-10L-19-6M0-17L2-32L-3-40M2-32L9-37"/></g><g transform="translate(85 301) scale(0.8)" stroke="#bdb4ce" stroke-width="1.6" fill="none"><path d="M0 0V-17L-7-23L-9-34M-7-23L-18-21L-24-28M0-12L10-20L12-31M10-20L22-19L26-26M0-7L-12-10L-19-6M0-17L2-32L-3-40M2-32L9-37"/></g><g transform="translate(339 296) scale(1.1)" stroke="#a6b59d" stroke-width="1.6" fill="none"><path d="M0 0V-17L-7-23L-9-34M-7-23L-18-21L-24-28M0-12L10-20L12-31M10-20L22-19L26-26M0-7L-12-10L-19-6M0-17L2-32L-3-40M2-32L9-37"/></g><g transform="translate(391 311) scale(1.2)" stroke="#69b3a4" stroke-width="1.6" fill="none"><path d="M0 0V-17L-7-23L-9-34M-7-23L-18-21L-24-28M0-12L10-20L12-31M10-20L22-19L26-26M0-7L-12-10L-19-6M0-17L2-32L-3-40M2-32L9-37"/></g><g transform="translate(418 285) scale(0.7)" stroke="#bdb4ce" stroke-width="1.6" fill="none"><path d="M0 0V-17L-7-23L-9-34M-7-23L-18-21L-24-28M0-12L10-20L12-31M10-20L22-19L26-26M0-7L-12-10L-19-6M0-17L2-32L-3-40M2-32L9-37"/></g><g transform="translate(122 324) scale(0.75)" stroke="#a6b59d" stroke-width="1.6" fill="none"><path d="M0 0V-17L-7-23L-9-34M-7-23L-18-21L-24-28M0-12L10-20L12-31M10-20L22-19L26-26M0-7L-12-10L-19-6M0-17L2-32L-3-40M2-32L9-37"/></g></g>
  <g id="moonlit-plants"><g id="night-left" transform="translate(184 326) scale(1.04)" stroke="#8b8f94" stroke-width="1.3" stroke-linejoin="round">
      <path id="night-left-stem" fill="#e6e3db" d="M-5 0 C-8-34-9-71-5-106 C-3-140 3-166 18-174 C35-183 52-170 51-153 L44-152 C43-166 34-174 23-168 C10-162 5-137 3-105 C0-70-1-34 3 0Z"/>
      <g id="night-left-scales" fill="#c7bbc3">
        <path d="M-6-26 Q-17-41-10-49 Q-3-41 0-29Z"/>
        <path d="M1-52 Q12-66 8-73 Q-2-67-3-57Z"/>
        <path d="M-5-81 Q-15-93-9-100 Q-3-94 0-83Z"/>
        <path d="M1-109 Q12-120 8-128 Q2-126-2-111Z"/>
        <path d="M4-139 Q-2-152 3-158 Q9-150 10-145Z"/>
      </g>
      <g id="night-left-flower" fill="#e6e3db">
        <path id="night-left-sepal-left" fill="#c7bbc3" d="M42-158 Q34-159 32-151 L41-148Z"/>
        <path id="night-left-sepal-right" fill="#c7bbc3" d="M49-158 Q60-157 61-149 L53-146Z"/>
        <path id="night-left-petal-back-left" d="M43-154 C37-150 35-142 33-134 C31-128 34-123 38-123 C43-123 47-128 48-135 C49-144 47-151 43-154Z"/>
        <path id="night-left-petal-back-right" d="M51-154 C57-150 59-142 61-134 C63-128 60-123 56-123 C51-123 47-128 46-135 C45-144 47-151 51-154Z"/>
        <path id="night-left-petal-left" d="M43-153 C38-148 37-139 34-131 C32-125 33-120 38-120 C44-120 49-125 50-132 C51-141 47-149 43-153Z"/>
        <path id="night-left-petal-right" d="M51-153 C56-148 57-139 60-131 C62-125 61-120 56-120 C50-120 45-125 44-132 C43-141 47-149 51-153Z"/>
        <path id="night-left-petal-front" d="M46-153 C42-146 40-138 40-129 C40-122 42-119 47-119 C52-119 54-122 54-129 C54-138 52-146 49-153Z"/>
        <g id="night-left-flower-opening">
          <ellipse cx="47" cy="-123.5" rx="13.5" ry="4.1" fill="#8b8f94" stroke="#e6e3db" stroke-width="1.7"/>
          <g id="night-left-included-reproductive-parts" fill="#c7bbc3" stroke="#c7bbc3" stroke-width=".8">
            <path d="M40-126V-123M43-126V-122.7M51-126V-122.7M54-126V-123"/>
            <circle cx="40" cy="-123" r=".8"/><circle cx="43" cy="-122.7" r=".8"/><circle cx="51" cy="-122.7" r=".8"/><circle cx="54" cy="-123" r=".8"/>
            <path d="M47-127V-123.2" stroke-width="1.1"/><ellipse cx="47" cy="-123.2" rx="1.7" ry=".9"/>
          </g>
          <path d="M34-123.1Q47-117.5 60-123.1" fill="none" stroke="#e6e3db" stroke-width="1.8"/>
        </g>
      </g>
    </g><g id="night-right" transform="translate(267 328) scale(0.76)" stroke="#7c9593" stroke-width="1.3" stroke-linejoin="round">
      <path id="night-right-stem" fill="#d7ded6" d="M-5 0 C-8-34-9-71-5-106 C-3-140 3-166 18-174 C35-183 52-170 51-153 L44-152 C43-166 34-174 23-168 C10-162 5-137 3-105 C0-70-1-34 3 0Z"/>
      <g id="night-right-scales" fill="#c2b2c5">
        <path d="M-6-26 Q-17-41-10-49 Q-3-41 0-29Z"/>
        <path d="M1-52 Q12-66 8-73 Q-2-67-3-57Z"/>
        <path d="M-5-81 Q-15-93-9-100 Q-3-94 0-83Z"/>
        <path d="M1-109 Q12-120 8-128 Q2-126-2-111Z"/>
        <path d="M4-139 Q-2-152 3-158 Q9-150 10-145Z"/>
      </g>
      <g id="night-right-flower" fill="#d7ded6">
        <path id="night-right-sepal-left" fill="#c2b2c5" d="M42-158 Q34-159 32-151 L41-148Z"/>
        <path id="night-right-sepal-right" fill="#c2b2c5" d="M49-158 Q60-157 61-149 L53-146Z"/>
        <path id="night-right-petal-back-left" d="M43-154 C37-150 35-142 33-134 C31-128 34-123 38-123 C43-123 47-128 48-135 C49-144 47-151 43-154Z"/>
        <path id="night-right-petal-back-right" d="M51-154 C57-150 59-142 61-134 C63-128 60-123 56-123 C51-123 47-128 46-135 C45-144 47-151 51-154Z"/>
        <path id="night-right-petal-left" d="M43-153 C38-148 37-139 34-131 C32-125 33-120 38-120 C44-120 49-125 50-132 C51-141 47-149 43-153Z"/>
        <path id="night-right-petal-right" d="M51-153 C56-148 57-139 60-131 C62-125 61-120 56-120 C50-120 45-125 44-132 C43-141 47-149 51-153Z"/>
        <path id="night-right-petal-front" d="M46-153 C42-146 40-138 40-129 C40-122 42-119 47-119 C52-119 54-122 54-129 C54-138 52-146 49-153Z"/>
        <g id="night-right-flower-opening">
          <ellipse cx="47" cy="-123.5" rx="13.5" ry="4.1" fill="#7c9593" stroke="#d7ded6" stroke-width="1.7"/>
          <g id="night-right-included-reproductive-parts" fill="#c2b2c5" stroke="#c2b2c5" stroke-width=".8">
            <path d="M40-126V-123M43-126V-122.7M51-126V-122.7M54-126V-123"/>
            <circle cx="40" cy="-123" r=".8"/><circle cx="43" cy="-122.7" r=".8"/><circle cx="51" cy="-122.7" r=".8"/><circle cx="54" cy="-123" r=".8"/>
            <path d="M47-127V-123.2" stroke-width="1.1"/><ellipse cx="47" cy="-123.2" rx="1.7" ry=".9"/>
          </g>
          <path d="M34-123.1Q47-117.5 60-123.1" fill="none" stroke="#d7ded6" stroke-width="1.8"/>
        </g>
      </g>
    </g><g id="night-center" transform="translate(232 329) scale(1.22)" stroke="#9a9696" stroke-width="1.3" stroke-linejoin="round">
      <path id="night-center-stem" fill="#ece8dc" d="M-5 0 C-8-34-9-71-5-106 C-3-140 3-166 18-174 C35-183 52-170 51-153 L44-152 C43-166 34-174 23-168 C10-162 5-137 3-105 C0-70-1-34 3 0Z"/>
      <g id="night-center-scales" fill="#cebbcb">
        <path d="M-6-26 Q-17-41-10-49 Q-3-41 0-29Z"/>
        <path d="M1-52 Q12-66 8-73 Q-2-67-3-57Z"/>
        <path d="M-5-81 Q-15-93-9-100 Q-3-94 0-83Z"/>
        <path d="M1-109 Q12-120 8-128 Q2-126-2-111Z"/>
        <path d="M4-139 Q-2-152 3-158 Q9-150 10-145Z"/>
      </g>
      <g id="night-center-flower" fill="#ece8dc">
        <path id="night-center-sepal-left" fill="#cebbcb" d="M42-158 Q34-159 32-151 L41-148Z"/>
        <path id="night-center-sepal-right" fill="#cebbcb" d="M49-158 Q60-157 61-149 L53-146Z"/>
        <path id="night-center-petal-back-left" d="M43-154 C37-150 35-142 33-134 C31-128 34-123 38-123 C43-123 47-128 48-135 C49-144 47-151 43-154Z"/>
        <path id="night-center-petal-back-right" d="M51-154 C57-150 59-142 61-134 C63-128 60-123 56-123 C51-123 47-128 46-135 C45-144 47-151 51-154Z"/>
        <path id="night-center-petal-left" d="M43-153 C38-148 37-139 34-131 C32-125 33-120 38-120 C44-120 49-125 50-132 C51-141 47-149 43-153Z"/>
        <path id="night-center-petal-right" d="M51-153 C56-148 57-139 60-131 C62-125 61-120 56-120 C50-120 45-125 44-132 C43-141 47-149 51-153Z"/>
        <path id="night-center-petal-front" d="M46-153 C42-146 40-138 40-129 C40-122 42-119 47-119 C52-119 54-122 54-129 C54-138 52-146 49-153Z"/>
        <g id="night-center-flower-opening">
          <ellipse cx="47" cy="-123.5" rx="13.5" ry="4.1" fill="#9a9696" stroke="#ece8dc" stroke-width="1.7"/>
          <g id="night-center-included-reproductive-parts" fill="#cebbcb" stroke="#cebbcb" stroke-width=".8">
            <path d="M40-126V-123M43-126V-122.7M51-126V-122.7M54-126V-123"/>
            <circle cx="40" cy="-123" r=".8"/><circle cx="43" cy="-122.7" r=".8"/><circle cx="51" cy="-122.7" r=".8"/><circle cx="54" cy="-123" r=".8"/>
            <path d="M47-127V-123.2" stroke-width="1.1"/><ellipse cx="47" cy="-123.2" rx="1.7" ry=".9"/>
          </g>
          <path d="M34-123.1Q47-117.5 60-123.1" fill="none" stroke="#ece8dc" stroke-width="1.8"/>
        </g>
      </g>
    </g></g>
  <g id="foreground-softness" fill="#5a8d7f" opacity=".16"><ellipse cx="30" cy="340" rx="56" ry="23"/><ellipse cx="437" cy="354" rx="72" ry="32"/></g>

</svg>

===== END FILE snapshot/assets/svg/nocturnal-optics.svg =====

===== BEGIN FILE snapshot/assets/svg/specimen-ghost-pipe.svg =====
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 360" role="img" aria-labelledby="specimen-ghost-pipe-title specimen-ghost-pipe-desc">
  <title id="specimen-ghost-pipe-title">Ghost pipe specimen composition</title>
  <desc id="specimen-ghost-pipe-desc">An original illustrative field-plate study of Monotropa uniflora, ghost pipe. Three ivory achlorophyllous stems carry reduced scale leaves and one open downward nodding flower each, with separate overlapping obovate rounded petals, a visible lower opening and included reproductive hints. Separate details show one scale leaf and five obovate petals; fine leaders and plain layout rules support an adaptable specimen composition. This unverified vector study is not a taxonomic key or a life-size scientific plate.</desc>
  <metadata>Uniflora aesthetic template v0.1. Original newly proposed vector interpretation; no historical asset, artist artwork, game asset, photograph, or traditional textile pattern reproduced. Asset terms: CC BY 4.0; creator-authorized repository publication; see LICENSE.md, ATTRIBUTION.md and docs/SVG-PROVENANCE.md.</metadata>
  

  <rect id="paper" width="480" height="360" fill="#f2eddf"/>
  <path id="plate-border" d="M21 24H459V337H21Z" fill="none" stroke="#b8b1a2" stroke-width=".8"/>
  <g id="paper-grain" fill="none" stroke="#bcb3a1" stroke-width=".6" opacity=".5"><path d="M28 32h2"/><path d="M94 50h2"/><path d="M390 46h2"/><path d="M437 85h2"/><path d="M45 120h2"/><path d="M415 137h2"/><path d="M30 255h2"/><path d="M68 315h2"/><path d="M410 310h2"/><path d="M381 335h2"/><path d="M127 343h2"/><path d="M456 230h2"/><path d="M183 28h2"/></g>
  <g id="specimen-shadows" fill="#8b7c6d" opacity=".09"><ellipse cx="248" cy="305" rx="77" ry="8"/></g>
  <g id="main-specimen"><g id="specimen-left" transform="translate(207 304) scale(1.16)" stroke="#8d8880" stroke-width="1.3" stroke-linejoin="round">
      <path id="specimen-left-stem" fill="#f2efe5" d="M-5 0 C-8-34-9-71-5-106 C-3-140 3-166 18-174 C35-183 52-170 51-153 L44-152 C43-166 34-174 23-168 C10-162 5-137 3-105 C0-70-1-34 3 0Z"/>
      <g id="specimen-left-scales" fill="#ddd0c5">
        <path d="M-6-26 Q-17-41-10-49 Q-3-41 0-29Z"/>
        <path d="M1-52 Q12-66 8-73 Q-2-67-3-57Z"/>
        <path d="M-5-81 Q-15-93-9-100 Q-3-94 0-83Z"/>
        <path d="M1-109 Q12-120 8-128 Q2-126-2-111Z"/>
        <path d="M4-139 Q-2-152 3-158 Q9-150 10-145Z"/>
      </g>
      <g id="specimen-left-flower" fill="#f2efe5">
        <path id="specimen-left-sepal-left" fill="#ddd0c5" d="M42-158 Q34-159 32-151 L41-148Z"/>
        <path id="specimen-left-sepal-right" fill="#ddd0c5" d="M49-158 Q60-157 61-149 L53-146Z"/>
        <path id="specimen-left-petal-back-left" d="M43-154 C37-150 35-142 33-134 C31-128 34-123 38-123 C43-123 47-128 48-135 C49-144 47-151 43-154Z"/>
        <path id="specimen-left-petal-back-right" d="M51-154 C57-150 59-142 61-134 C63-128 60-123 56-123 C51-123 47-128 46-135 C45-144 47-151 51-154Z"/>
        <path id="specimen-left-petal-left" d="M43-153 C38-148 37-139 34-131 C32-125 33-120 38-120 C44-120 49-125 50-132 C51-141 47-149 43-153Z"/>
        <path id="specimen-left-petal-right" d="M51-153 C56-148 57-139 60-131 C62-125 61-120 56-120 C50-120 45-125 44-132 C43-141 47-149 51-153Z"/>
        <path id="specimen-left-petal-front" d="M46-153 C42-146 40-138 40-129 C40-122 42-119 47-119 C52-119 54-122 54-129 C54-138 52-146 49-153Z"/>
        <g id="specimen-left-flower-opening">
          <ellipse cx="47" cy="-123.5" rx="13.5" ry="4.1" fill="#8d8880" stroke="#f2efe5" stroke-width="1.7"/>
          <g id="specimen-left-included-reproductive-parts" fill="#ddd0c5" stroke="#ddd0c5" stroke-width=".8">
            <path d="M40-126V-123M43-126V-122.7M51-126V-122.7M54-126V-123"/>
            <circle cx="40" cy="-123" r=".8"/><circle cx="43" cy="-122.7" r=".8"/><circle cx="51" cy="-122.7" r=".8"/><circle cx="54" cy="-123" r=".8"/>
            <path d="M47-127V-123.2" stroke-width="1.1"/><ellipse cx="47" cy="-123.2" rx="1.7" ry=".9"/>
          </g>
          <path d="M34-123.1Q47-117.5 60-123.1" fill="none" stroke="#f2efe5" stroke-width="1.8"/>
        </g>
      </g>
    </g><g id="specimen-right" transform="translate(283 305) scale(0.89)" stroke="#8d8880" stroke-width="1.3" stroke-linejoin="round">
      <path id="specimen-right-stem" fill="#eae7dd" d="M-5 0 C-8-34-9-71-5-106 C-3-140 3-166 18-174 C35-183 52-170 51-153 L44-152 C43-166 34-174 23-168 C10-162 5-137 3-105 C0-70-1-34 3 0Z"/>
      <g id="specimen-right-scales" fill="#d7c8bf">
        <path d="M-6-26 Q-17-41-10-49 Q-3-41 0-29Z"/>
        <path d="M1-52 Q12-66 8-73 Q-2-67-3-57Z"/>
        <path d="M-5-81 Q-15-93-9-100 Q-3-94 0-83Z"/>
        <path d="M1-109 Q12-120 8-128 Q2-126-2-111Z"/>
        <path d="M4-139 Q-2-152 3-158 Q9-150 10-145Z"/>
      </g>
      <g id="specimen-right-flower" fill="#eae7dd">
        <path id="specimen-right-sepal-left" fill="#d7c8bf" d="M42-158 Q34-159 32-151 L41-148Z"/>
        <path id="specimen-right-sepal-right" fill="#d7c8bf" d="M49-158 Q60-157 61-149 L53-146Z"/>
        <path id="specimen-right-petal-back-left" d="M43-154 C37-150 35-142 33-134 C31-128 34-123 38-123 C43-123 47-128 48-135 C49-144 47-151 43-154Z"/>
        <path id="specimen-right-petal-back-right" d="M51-154 C57-150 59-142 61-134 C63-128 60-123 56-123 C51-123 47-128 46-135 C45-144 47-151 51-154Z"/>
        <path id="specimen-right-petal-left" d="M43-153 C38-148 37-139 34-131 C32-125 33-120 38-120 C44-120 49-125 50-132 C51-141 47-149 43-153Z"/>
        <path id="specimen-right-petal-right" d="M51-153 C56-148 57-139 60-131 C62-125 61-120 56-120 C50-120 45-125 44-132 C43-141 47-149 51-153Z"/>
        <path id="specimen-right-petal-front" d="M46-153 C42-146 40-138 40-129 C40-122 42-119 47-119 C52-119 54-122 54-129 C54-138 52-146 49-153Z"/>
        <g id="specimen-right-flower-opening">
          <ellipse cx="47" cy="-123.5" rx="13.5" ry="4.1" fill="#8d8880" stroke="#eae7dd" stroke-width="1.7"/>
          <g id="specimen-right-included-reproductive-parts" fill="#d7c8bf" stroke="#d7c8bf" stroke-width=".8">
            <path d="M40-126V-123M43-126V-122.7M51-126V-122.7M54-126V-123"/>
            <circle cx="40" cy="-123" r=".8"/><circle cx="43" cy="-122.7" r=".8"/><circle cx="51" cy="-122.7" r=".8"/><circle cx="54" cy="-123" r=".8"/>
            <path d="M47-127V-123.2" stroke-width="1.1"/><ellipse cx="47" cy="-123.2" rx="1.7" ry=".9"/>
          </g>
          <path d="M34-123.1Q47-117.5 60-123.1" fill="none" stroke="#eae7dd" stroke-width="1.8"/>
        </g>
      </g>
    </g><g id="specimen-center" transform="translate(250 306) scale(1.34)" stroke="#8d8880" stroke-width="1.3" stroke-linejoin="round">
      <path id="specimen-center-stem" fill="#f6f3e9" d="M-5 0 C-8-34-9-71-5-106 C-3-140 3-166 18-174 C35-183 52-170 51-153 L44-152 C43-166 34-174 23-168 C10-162 5-137 3-105 C0-70-1-34 3 0Z"/>
      <g id="specimen-center-scales" fill="#dfcfc7">
        <path d="M-6-26 Q-17-41-10-49 Q-3-41 0-29Z"/>
        <path d="M1-52 Q12-66 8-73 Q-2-67-3-57Z"/>
        <path d="M-5-81 Q-15-93-9-100 Q-3-94 0-83Z"/>
        <path d="M1-109 Q12-120 8-128 Q2-126-2-111Z"/>
        <path d="M4-139 Q-2-152 3-158 Q9-150 10-145Z"/>
      </g>
      <g id="specimen-center-flower" fill="#f6f3e9">
        <path id="specimen-center-sepal-left" fill="#dfcfc7" d="M42-158 Q34-159 32-151 L41-148Z"/>
        <path id="specimen-center-sepal-right" fill="#dfcfc7" d="M49-158 Q60-157 61-149 L53-146Z"/>
        <path id="specimen-center-petal-back-left" d="M43-154 C37-150 35-142 33-134 C31-128 34-123 38-123 C43-123 47-128 48-135 C49-144 47-151 43-154Z"/>
        <path id="specimen-center-petal-back-right" d="M51-154 C57-150 59-142 61-134 C63-128 60-123 56-123 C51-123 47-128 46-135 C45-144 47-151 51-154Z"/>
        <path id="specimen-center-petal-left" d="M43-153 C38-148 37-139 34-131 C32-125 33-120 38-120 C44-120 49-125 50-132 C51-141 47-149 43-153Z"/>
        <path id="specimen-center-petal-right" d="M51-153 C56-148 57-139 60-131 C62-125 61-120 56-120 C50-120 45-125 44-132 C43-141 47-149 51-153Z"/>
        <path id="specimen-center-petal-front" d="M46-153 C42-146 40-138 40-129 C40-122 42-119 47-119 C52-119 54-122 54-129 C54-138 52-146 49-153Z"/>
        <g id="specimen-center-flower-opening">
          <ellipse cx="47" cy="-123.5" rx="13.5" ry="4.1" fill="#8d8880" stroke="#f6f3e9" stroke-width="1.7"/>
          <g id="specimen-center-included-reproductive-parts" fill="#dfcfc7" stroke="#dfcfc7" stroke-width=".8">
            <path d="M40-126V-123M43-126V-122.7M51-126V-122.7M54-126V-123"/>
            <circle cx="40" cy="-123" r=".8"/><circle cx="43" cy="-122.7" r=".8"/><circle cx="51" cy="-122.7" r=".8"/><circle cx="54" cy="-123" r=".8"/>
            <path d="M47-127V-123.2" stroke-width="1.1"/><ellipse cx="47" cy="-123.2" rx="1.7" ry=".9"/>
          </g>
          <path d="M34-123.1Q47-117.5 60-123.1" fill="none" stroke="#f6f3e9" stroke-width="1.8"/>
        </g>
      </g>
    </g></g>
  <g id="scale-leaf-detail" stroke="#9a9286" stroke-width="1" fill="none"><circle cx="81" cy="115" r="40"/><path d="M73 145C71 118 76 95 82 83L89 85C82 107 80 125 81 145Z" fill="#ece7dc"/><path d="M76 128C55 109 56 95 62 91C75 103 79 115 80 125Z" fill="#dfd0c6"/><path d="M68 104L76 124"/><path d="M121 120H154L200 207" stroke-dasharray="3 3"/></g>
  <g id="petal-detail"><path d="M90 273C88 279 81 287 83 297Q84 305 90 305Q96 305 97 297C99 288 92 279 90 273Z" fill="#eeeadf" stroke="#928d83" stroke-width="1"/><path d="M107 273C105 279 98 287 100 297Q101 305 107 305Q113 305 114 297C116 288 109 279 107 273Z" fill="#eeeadf" stroke="#928d83" stroke-width="1"/><path d="M124 273C122 279 115 287 117 297Q118 305 124 305Q130 305 131 297C133 288 126 279 124 273Z" fill="#eeeadf" stroke="#928d83" stroke-width="1"/><path d="M141 273C139 279 132 287 134 297Q135 305 141 305Q147 305 148 297C150 288 143 279 141 273Z" fill="#eeeadf" stroke="#928d83" stroke-width="1"/><path d="M158 273C156 279 149 287 151 297Q152 305 158 305Q164 305 165 297C167 288 160 279 158 273Z" fill="#eeeadf" stroke="#928d83" stroke-width="1"/><path d="M85 312H164M85 309V315M164 309V315" fill="none" stroke="#9a9286" stroke-width=".9"/></g>
  <g id="morphology-leaders" fill="none" stroke="#9e9689" stroke-width=".8"><path d="M314 116L358 84H420"/><circle cx="314" cy="116" r="2" fill="#9e9689"/><path d="M254 224L365 232H420"/><circle cx="254" cy="224" r="2" fill="#9e9689"/><path d="M208 270L154 237H58"/><circle cx="208" cy="270" r="2" fill="#9e9689"/></g>
  <g id="layout-separator" stroke="#b9b0a1" stroke-width=".8"><path d="M346 312H417"/></g>
  <g id="unlabelled-layout-rule" fill="none" stroke="#b9b0a1" stroke-width=".8"><path d="M40 42H146M335 42H440M40 325H111"/></g>

</svg>

===== END FILE snapshot/assets/svg/specimen-ghost-pipe.svg =====

===== BEGIN FILE snapshot/attribution.json =====
{
  "version": "0.1.0",
  "status": "initial-v0.1-release-for-review",
  "dateUTC": "2026-10-10",
  "datePacific": "2026-10-09",
  "aiAssistance": "Code, documentation, prompt examples and vector paths authored with ChatGPT/Codex assistance for the creator brief; selection/review disclosed. AI is not identified as rights holder.",
  "licenseScope": {
    "software": [
      "demo/*.html",
      "demo/*.css",
      "presets/*.json",
      "presets/*.css",
      "tools/*.py"
    ],
    "softwareLicense": "Unlicense",
    "documentation": [
      "*.md",
      "docs/*.md",
      "assets/README.md",
      "prompts/*.md",
      "prompts/*.json",
      "attribution.json"
    ],
    "documentationLicense": "CC-BY-4.0",
    "artwork": [
      "assets/svg/*.svg"
    ],
    "artworkLicense": "CC-BY-4.0"
  },
  "fonts": {
    "bundled": [],
    "networkRequests": false,
    "families": [
      "system-ui, sans-serif",
      "ui-serif, serif",
      "ui-monospace, monospace"
    ],
    "redistribution": "No font binaries distributed; installed fonts resolved locally."
  },
  "includedThirdPartyVisualAssets": [],
  "assets": [
    {
      "path": "assets/svg/isometric-signal.svg",
      "origin": "new-v0.1-original-ai-assisted",
      "authorCredit": "Uniflora contributors",
      "sourceURL": null,
      "license": "CC-BY-4.0",
      "redistributionBasis": "Original project paths; no imported third-party visual resource",
      "changes": "New in v0.1; botanical flower silhouettes refined during review where relevant.",
      "notes": "Original stepped isometric signal geometry; schematic ghost pipe.",
      "unresolved": "No imported third-party material; copyright protection for AI-assisted expression not assured; expert review required for botanical identification use."
    },
    {
      "path": "assets/svg/engraved-fold.svg",
      "origin": "new-v0.1-original-ai-assisted",
      "authorCredit": "Uniflora contributors",
      "sourceURL": null,
      "license": "CC-BY-4.0",
      "redistributionBasis": "Original project paths; no imported third-party visual resource",
      "changes": "New in v0.1; botanical flower silhouettes refined during review where relevant.",
      "notes": "Original arches, conflicting levels, hatching and facets; no artist image or folding diagram copied.",
      "unresolved": "No imported third-party material; copyright protection for AI-assisted expression not assured; expert review required for botanical identification use."
    },
    {
      "path": "assets/svg/crt-forest.svg",
      "origin": "new-v0.1-original-ai-assisted",
      "authorCredit": "Uniflora contributors",
      "sourceURL": null,
      "license": "CC-BY-4.0",
      "redistributionBasis": "Original project paths; no imported third-party visual resource",
      "changes": "New in v0.1; botanical flower silhouettes refined during review where relevant.",
      "notes": "Original pixel forest and fixed screen; no commercial sprites; invented lighting.",
      "unresolved": "No imported third-party material; copyright protection for AI-assisted expression not assured; expert review required for botanical identification use."
    },
    {
      "path": "assets/svg/nocturnal-optics.svg",
      "origin": "new-v0.1-original-ai-assisted",
      "authorCredit": "Uniflora contributors",
      "sourceURL": null,
      "license": "CC-BY-4.0",
      "redistributionBasis": "Original project paths; no imported third-party visual resource",
      "changes": "New in v0.1; botanical flower silhouettes refined during review where relevant.",
      "notes": "Original garden optics and light geometry; glow is artistic interpretation.",
      "unresolved": "No imported third-party material; copyright protection for AI-assisted expression not assured; expert review required for botanical identification use."
    },
    {
      "path": "assets/svg/kilim-burdock.svg",
      "origin": "new-v0.1-original-ai-assisted",
      "authorCredit": "Uniflora contributors",
      "sourceURL": null,
      "license": "CC-BY-4.0",
      "redistributionBasis": "Original project paths; no imported third-party visual resource",
      "changes": "New in v0.1; botanical flower silhouettes refined during review where relevant.",
      "notes": "Original centered hook/diamond/radial geometry; new interpretation, no traditional meaning asserted.",
      "unresolved": "No imported third-party material; copyright protection for AI-assisted expression not assured; expert review required for botanical identification use."
    },
    {
      "path": "assets/svg/specimen-ghost-pipe.svg",
      "origin": "new-v0.1-original-ai-assisted",
      "authorCredit": "Uniflora contributors",
      "sourceURL": null,
      "license": "CC-BY-4.0",
      "redistributionBasis": "Original project paths; no imported third-party visual resource",
      "changes": "New in v0.1; nodding flower silhouettes refined during review; uncalibrated specimen scale markings removed.",
      "notes": "Original morphology-led schematic; not traced or an identification plate.",
      "unresolved": "No imported third-party material; copyright protection for AI-assisted expression not assured; expert review required for botanical identification use."
    }
  ],
  "references": [
    {
      "id": "B1",
      "url": "https://gobotany.nativeplanttrust.org/species/monotropa/uniflora/",
      "consultedUTC": "2026-10-10",
      "use": "Factual morphology/ecology; photos and full source text excluded",
      "bundledResource": false
    },
    {
      "id": "B2",
      "url": "https://powo.science.kew.org/taxon/281016-2",
      "consultedUTC": "2026-10-10",
      "use": "Accepted scientific name and family; no imagery/dataset copied",
      "bundledResource": false
    },
    {
      "id": "R1",
      "url": "https://unlicense.org/",
      "consultedUTC": "2026-10-10",
      "use": "Existing repository Unlicense retained",
      "bundledResource": true,
      "includedPath": "licenses/Unlicense.txt",
      "verificationURL": "https://opensource.org/license/unlicense"
    },
    {
      "id": "R2",
      "url": "https://creativecommons.org/licenses/by/4.0/legalcode.en",
      "consultedUTC": "2026-10-10",
      "use": "Complete legal code included separately; legal text CC0",
      "bundledResource": true,
      "includedPath": "licenses/CC-BY-4.0.txt"
    },
    {
      "id": "R3",
      "url": "https://creativecommons.org/faq/#can-i-apply-a-creative-commons-license-to-software",
      "consultedUTC": "2026-10-10",
      "use": "Software/art/documentation license distinction",
      "bundledResource": false
    },
    {
      "id": "A1",
      "url": "https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html",
      "consultedUTC": "2026-10-10",
      "use": "Contrast target paraphrase",
      "bundledResource": false
    },
    {
      "id": "A2",
      "url": "https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html",
      "consultedUTC": "2026-10-10",
      "use": "Essential UI contrast guidance",
      "bundledResource": false
    },
    {
      "id": "A3",
      "url": "https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html",
      "consultedUTC": "2026-10-10",
      "use": "Nonessential interaction animation guidance; no AAA compliance claim",
      "bundledResource": false
    },
    {
      "id": "A4",
      "url": "https://www.w3.org/WAI/WCAG22/Techniques/css/C39.html",
      "consultedUTC": "2026-10-10",
      "use": "Reduced-motion CSS technique",
      "bundledResource": false
    }
  ],
  "historicalAssets": {
    "included": false,
    "rightsVerified": false,
    "note": "Recovered directions and scoped choices are documented; previous images/logos/lettering not bundled."
  },
  "culturalContext": {
    "kilimBurdock": "New generic interpretation; no regional or universal symbolic meaning established."
  },
  "unresolvedBeforePublication": [
    "No third-party included assets awaiting clearance. Historical referenced images excluded and not audited.",
    "No jurisdiction-independent copyrightability assurance for AI-assisted expression.",
    "Reference names do not confer trademark rights or endorsement; future imported resources require review."
  ],
  "maintainer": "sporemound",
  "repository": "https://github.com/sporemound/uniflora-aesthetic-kit",
  "publicationAuthorization": "Creator explicitly instructed publication to this existing repository after completion on 2026-10-09 Pacific.",
  "attribution": "Uniflora contributors"
}

===== END FILE snapshot/attribution.json =====

===== BEGIN FILE snapshot/ATTRIBUTION.md =====
# Attribution register

Version 0.1.0, prepared 2026-10-10 UTC / 2026-10-09 Pacific. Creative material credit: **Uniflora contributors**. Maintainer: [sporemound](https://github.com/sporemound). The creator authorized repository publication; the AI is not identified as a rights holder. The machine-readable register is [attribution.json](attribution.json).

## Included files

| Material | Origin | License | Evidence / boundary |
| --- | --- | --- | --- |
| `demo/index.html`, `demo/starter.html`, `demo/demo.css` | Newly authored with ChatGPT/Codex assistance for this brief | Unlicense | Original markup and CSS; no copied website, template, runtime library or remote dependency |
| `presets/tokens.json`, `presets/tokens.css` | New v0.1 implementation proposals | Unlicense | Exact values and names are proposals, not recovered historical assets |
| `tools/validate.py` | Newly authored Python standard-library script | Unlicense | No vendored package; Python itself is not distributed |
| README, contribution guide, guides and prompt records | Newly authored with AI assistance; informed by the creator's brief | CC BY 4.0 | No full botanical source text copied; private historical images not included |
| `assets/svg/isometric-signal.svg` | Original paths, isometric and stepped signal study | CC BY 4.0 | New artwork; not console/game sprites; ghost-pipe structure is schematic |
| `assets/svg/engraved-fold.svg` | Original paths, arches, stairs, hatching and folded facets | CC BY 4.0 | Not a copied Escher work or Tomoko Fuse diagram; no validated origami folding claim |
| `assets/svg/crt-forest.svg` | Original paths, pixel forest and fixed-screen study | CC BY 4.0 | Not Sega graphics; invented lighting and original analog texture |
| `assets/svg/nocturnal-optics.svg` | Original paths, garden and refractive light study | CC BY 4.0 | Stylized optics; luminous treatment is artistic, not a claim of natural emission |
| `assets/svg/kilim-burdock.svg` | Original hook, diamond and radial geometry | CC BY 4.0 | New interpretation; no authenticated traditional pattern or symbolism claim |
| `assets/svg/specimen-ghost-pipe.svg` | Original paths, morphology-led schematic | CC BY 4.0 | Not traced from a photograph or herbarium sheet; not an identification plate |
| `LICENSE` and `licenses/Unlicense.txt` | Standard Unlicense preserved from the existing repository | Unlicense | Existing license retained without changing its terms |
| `licenses/CC-BY-4.0.txt` | Complete official English legal code from Creative Commons | CC0 for license text itself | The footer identifies the legal-code text's CC0 dedication; project art/docs would use CC BY 4.0 |

There are **no included third-party visual assets or font files**. Generic browser font stacks use locally installed fonts without redistribution. No paid tools, font services, accounts, subscriptions, model weights, music samples, logos, ROMs, or proprietary textures are required.

## References only — not bundled resources

| Reference | Use | Redistribution status |
| --- | --- | --- |
| Creator's six-branch brief and scoped historical choices | Defines the aesthetic directions and subject-preservation rules | Prior screenshots, lettering, logos and generated images omitted; rights not audited |
| M. C. Escher | Broad spatial-contradiction reference in the brief | No named artwork reproduced or adapted; no endorsement |
| Tomoko Fuse | Broad modular-fold/form reference in the brief | No crease pattern, diagram, recipe, page or named unit reproduced or adapted |
| Sega Genesis | Limited-ramp pixel-world reference in the brief | No game asset, sprite, logo or commercial interface reproduced |
| Kilim / burdock motifs | Broad geometric textile direction | No specific object, regional attribution or traditional meaning claimed |
| Native Plant Trust and Kew | Botanical facts and name/family checks | Links and factual paraphrases only; images/datasets not included |
| W3C | Contrast and reduced-motion guidance | Links and brief paraphrases only; no conformance claim |
| OSI / Creative Commons | License scope and complete license forms | Complete public forms supplied with their issuer notices |

Exact reference URLs and consulted dates are in [docs/REFERENCE-SOURCES.md](docs/REFERENCE-SOURCES.md). The six SVGs' construction notes are in [docs/SVG-PROVENANCE.md](docs/SVG-PROVENANCE.md).

## Reuse credit

Use this credit for the original art and documentation:

```text
Uniflora Aesthetic Template v0.1 — Uniflora contributors.
Original motifs and documentation: CC BY 4.0.
https://creativecommons.org/licenses/by/4.0/
Code: Unlicense; no attribution condition is imposed on software.
Source: https://github.com/sporemound/uniflora-aesthetic-kit
Changes: [your modifications, or unmodified]
```

Record new imports before distribution: exact file, source URL, author, license version, permission evidence, attribution, modifications, and unresolved claims. Do not extend this register's original-work status to later imports. Grants cover only rights that exist and the contributor can grant. See [RIGHTS-REVIEW.md](docs/RIGHTS-REVIEW.md) for AI-assisted copyright scope and excluded reference rights.

===== END FILE snapshot/ATTRIBUTION.md =====

===== BEGIN FILE snapshot/CHANGELOG.md =====
# Changelog

## 0.1.0 — 2026-10-10 UTC / 2026-10-09 Pacific

Initial v0.1 release for review: six distinct branch presets, proposed semantic palettes, offline HTML/CSS gallery, six original editable SVG studies, platform-neutral prompt template and examples, history/interpretation separation, botanical guidance, licensing and provenance registers, contribution guide, and a dependency-free validator. Published to the creator-specified existing repository after package review; no hosted website deployment.

===== END FILE snapshot/CHANGELOG.md =====

===== BEGIN FILE snapshot/CONTRIBUTING.md =====
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

===== END FILE snapshot/CONTRIBUTING.md =====

===== BEGIN FILE snapshot/demo/demo.css =====
/* SPDX-License-Identifier: Unlicense */
* { box-sizing: border-box; }
body { margin: 0; background: #F7F2E8; color: #282E29; font: 1rem/1.6 var(--uf-font-body); }
a { color: inherit; text-underline-offset: .2em; }
a:hover { text-decoration-thickness: .15em; }
:focus-visible { outline: 3px solid currentColor; outline-offset: 5px; }
.skip { position: absolute; top: .5rem; left: .5rem; transform: translateY(-180%); background: #FFFCF5; padding: .5rem; z-index: 4; }
.skip:focus { transform: none; }
header, main, footer { max-width: 78rem; margin: auto; padding: 2rem; }
header { padding-top: 3rem; border-bottom: 1px solid #606B5C; }
.eyebrow, .index { font: .8rem/1.5 var(--uf-font-mono); letter-spacing: .08em; text-transform: uppercase; }
h1 { margin: .5rem 0 1rem; font: clamp(2.5rem, 8vw, 6rem)/1.05 var(--uf-font-display); letter-spacing: -.03em; }
.intro { max-width: 48rem; font-size: 1.125rem; }
nav { display: flex; flex-wrap: wrap; gap: 1rem; margin: 1.5rem 0; }
nav a { padding: .25rem 0; }
.gallery { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1.5rem; }
.preset { min-width: 0; padding: 1.5rem; background: var(--uf-bg); color: var(--uf-text); border: 1px solid var(--uf-accent); }
.preset h2 { font: 1.7rem/1.2 var(--uf-heading); margin: .4rem 0 1rem; }
.index, .note { color: var(--uf-muted); }
.note { font-size: .9rem; }
.art { position: relative; margin: 0; aspect-ratio: 4/3; overflow: hidden; background: var(--uf-surface); border: 1px solid var(--uf-accent); }
.art img { display: block; width: 100%; height: 100%; object-fit: contain; }
.swatches { display: flex; gap: .5rem; margin: 1rem 0; align-items: center; }
.swatch { width: 1.4rem; height: 1.4rem; border: 1px solid var(--uf-text); border-radius: 50%; }
.swatch:nth-child(1) { background: var(--uf-bg); }
.swatch:nth-child(2) { background: var(--uf-accent); }
.swatch:nth-child(3) { background: var(--uf-decor); }
.swatch:nth-child(4) { background: var(--uf-text); }
.swatches span:last-child { font: .75rem var(--uf-font-mono); }
details { border-top: 1px solid var(--uf-accent); padding-top: .7rem; margin-top: 1rem; }
summary { cursor: pointer; padding: .3rem 0; font-weight: 600; }
pre { overflow-x: auto; padding: .75rem; font: .8rem/1.5 var(--uf-font-mono); background: var(--uf-surface); color: var(--uf-text); }
.motion { display: flex; align-items: center; gap: .7rem; margin: 1rem 0 .5rem; }
input[type=checkbox] { width: 1.3rem; height: 1.3rem; accent-color: var(--uf-accent); }
.crt-screen { position: absolute; inset: 9.4444% 6.25% 18.3333%; border-radius: 5.238% / 8.462%; overflow: hidden; pointer-events: none; }
.crt-screen::after { content: ''; position: absolute; inset: -40% 0; opacity: .12; background: repeating-linear-gradient(transparent 0 3px, #071C1A 3px 4px); }
/* Only the scanline overlay moves; scene, camera, and bezel stay fixed. */
.crt-toggle:checked ~ .art .crt-screen::after { animation: scan-drift 12s linear infinite; }
@keyframes scan-drift { to { transform: translateY(24px); } }
.rule { padding: 1rem 0; border-top: 1px solid #606B5C; }
footer { font-size: .9rem; padding-top: 0; }
@media (max-width: 48rem) { .gallery { grid-template-columns: 1fr; } header, main, footer { padding: 1.25rem; } }
@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation: none !important; scroll-behavior: auto !important; } }
@media (forced-colors: active) { .preset, .art { border-color: CanvasText; } .crt-screen { display: none; } }

===== END FILE snapshot/demo/demo.css =====

===== BEGIN FILE snapshot/demo/index.html =====
<!doctype html>
<!-- SPDX-License-Identifier: Unlicense -->
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Six editable Uniflora aesthetic presets. A free, offline creative system, version 0.1.">
  <title>Uniflora / Creative system 0.1</title>
  <link rel="stylesheet" href="../presets/tokens.css">
  <link rel="stylesheet" href="demo.css">
</head>
<body>
<a class="skip" href="#presets">Skip to presets</a>
<header>
  <p class="eyebrow">Uniflora / Creative system / 0.1 initial release</p>
  <h1>A language for<br>unseen relationships.</h1>
  <p class="intro">Choose a subject. Keep its meaning intact. Use one of six visual branches to shape depth, rhythm, material, and perception. This headline and these palettes are editable examples, not required Uniflora branding.</p>
  <nav aria-label="Project resources"><a href="../README.md">Start here</a><a href="../docs/STYLE-GUIDE.md">Style guide</a><a href="../prompts/TEMPLATE.md">Prompt template</a><a href="../docs/RIGHTS-REVIEW.md">Rights review</a></nav>
</header>
<main id="presets" tabindex="-1">
  <p class="note">Six new vector studies demonstrate the recovered directions. Identifiable ghost pipe is drawn with scale leaves and one nodding flower per stem. These stylized studies are not botanical identification plates.</p>
  <div class="gallery">
    <article class="preset" data-uniflora="isometric-idm">
      <p class="index">01 / rhythm · inversion · depth</p><h2>Isometric botanical IDM</h2>
      <figure class="art"><img src="../assets/svg/isometric-signal.svg" width="480" height="360" alt="Ivory ghost-pipe stems on mirrored isometric platforms with turquoise stepped signal paths."></figure>
      <div class="swatches" aria-hidden="true"><span class="swatch"></span><span class="swatch"></span><span class="swatch"></span><span class="swatch"></span><span>turquoise / forest / ivory</span></div>
      <p>16-bit forms occupy a consistent isometric lattice. Paired paths imply communication through shared rhythm and alignment.</p>
      <details><summary>Use this preset</summary><pre>&lt;section data-uniflora="isometric-idm"&gt;
  &lt;h2&gt;Your subject stays central&lt;/h2&gt;
&lt;/section&gt;</pre><p>Use the semantic color variables from tokens.css on your own components. See prompt example 01.</p></details>
    </article>
    <article class="preset" data-uniflora="engraved-architecture">
      <p class="index">02 / contradictions · pressure · fold</p><h2>Impossible engraved architecture</h2>
      <figure class="art"><img src="../assets/svg/engraved-fold.svg" width="480" height="360" alt="Romanesque arches, conflicting stair levels, cross-hatched masonry, and an original faceted folded surface."></figure>
      <div class="swatches" aria-hidden="true"><span class="swatch"></span><span class="swatch"></span><span class="swatch"></span><span class="swatch"></span><span>black / ivory / print</span></div>
      <p>Readable local spaces form an impossible whole. Projection lines bend across the facets of an original tessellation.</p>
      <details><summary>Use this preset</summary><pre>&lt;section data-uniflora="engraved-architecture"&gt;
  &lt;h2&gt;Your subject stays central&lt;/h2&gt;
&lt;/section&gt;</pre><p>Keep dense hatching behind the artwork, with clear paper around interface text. See prompt example 02.</p></details>
    </article>
    <article class="preset" data-uniflora="crt-worlds">
      <p class="index">03 / continuity · signal · phosphor</p><h2>CRT botanical worlds</h2>
      <input class="crt-toggle" id="crt-motion" type="checkbox"><label for="crt-motion">Enable slow screen scanline drift</label>
      <figure class="art"><img src="../assets/svg/crt-forest.svg" width="480" height="360" alt="A fixed CRT display contains a pixel forest, crescent moon, and cyan and magenta accents around ivory ghost pipe."><div class="crt-screen" aria-hidden="true"></div></figure>
      <div class="swatches" aria-hidden="true"><span class="swatch"></span><span class="swatch"></span><span class="swatch"></span><span class="swatch"></span><span>cyan / magenta / forest</span></div>
      <p>The bezel stays still. Optional distortion stays within the screen, preserving the forest and its landmarks.</p>
      <p class="note">Static by default. Reduced-motion preferences disable movement even when this control is checked. The ghost pipe is not naturally bioluminescent.</p>
      <details><summary>Use this preset</summary><pre>&lt;section data-uniflora="crt-worlds"&gt;
  &lt;h2&gt;Your subject stays central&lt;/h2&gt;
&lt;/section&gt;</pre><p>For animation, lock the camera and clip every effect to the display interior. See prompt example 03.</p></details>
    </article>
    <article class="preset" data-uniflora="nocturnal-optics">
      <p class="index">04 / mist · refraction · distance</p><h2>Nocturnal botanical optics</h2>
      <figure class="art"><img src="../assets/svg/nocturnal-optics.svg" width="480" height="360" alt="Moonlight, layered mist, luminous lichen marks, and soft refractive arcs surround an ivory flowering stem."></figure>
      <div class="swatches" aria-hidden="true"><span class="swatch"></span><span class="swatch"></span><span class="swatch"></span><span class="swatch"></span><span>silver / lavender / teal</span></div>
      <p>One focal plane anchors a quiet garden. Light separation and refraction create distance without obscuring the subject.</p>
      <p class="note">Optical glow and luminous lichen here are artistic interpretations, not biological claims.</p>
      <details><summary>Use this preset</summary><pre>&lt;section data-uniflora="nocturnal-optics"&gt;
  &lt;h2&gt;Your subject stays central&lt;/h2&gt;
&lt;/section&gt;</pre><p>Keep bloom away from reading surfaces. Use optical effects sparingly. See prompt example 04.</p></details>
    </article>
    <article class="preset" data-uniflora="kilim-burdock">
      <p class="index">05 / repetition · hook · reversal</p><h2>Kilim and burdock</h2>
      <figure class="art"><img src="../assets/svg/kilim-burdock.svg" width="480" height="360" alt="Centered diamond and hook forms repeat in a balanced textile-like card with half-turn symmetry."></figure>
      <div class="swatches" aria-hidden="true"><span class="swatch"></span><span class="swatch"></span><span class="swatch"></span><span class="swatch"></span><span>rust / teal / woven earth</span></div>
      <p>Balanced repetition and 180-degree reversal give a card two equivalent orientations. Neighboring hooks establish rhythm.</p>
      <p class="note">A new geometric interpretation. No historical textile, regional provenance, or traditional meaning is claimed.</p>
      <details><summary>Use this preset</summary><pre>&lt;section data-uniflora="kilim-burdock"&gt;
  &lt;h2&gt;Your subject stays central&lt;/h2&gt;
&lt;/section&gt;</pre><p>Reversal belongs to the art; keep reading order and interface labels upright. See prompt example 05.</p></details>
    </article>
    <article class="preset" data-uniflora="botanical-specimen">
      <p class="index">06 / morphology · annotation · paper</p><h2>Botanical specimen art</h2>
      <figure class="art"><img src="../assets/svg/specimen-ghost-pipe.svg" width="480" height="360" alt="An original schematic ghost-pipe study on ivory paper, showing scale leaves and separate overlapping petals on nodding flowers."></figure>
      <div class="swatches" aria-hidden="true"><span class="swatch"></span><span class="swatch"></span><span class="swatch"></span><span class="swatch"></span><span>paper / graphite / green</span></div>
      <p>Morphology controls the silhouette. Margins and leader lines adapt the study to a field-guide page, album cover, or poster.</p>
      <p class="note"><i>Monotropa uniflora</i> is a flowering plant that obtains carbon through fungi. Check botanical references before publishing identification material.</p>
      <details><summary>Use this preset</summary><pre>&lt;section data-uniflora="botanical-specimen"&gt;
  &lt;h2&gt;Your subject stays central&lt;/h2&gt;
&lt;/section&gt;</pre><p>Use documented specimens for fine diagnostic details. Never invent measurements. See prompt example 06.</p></details>
    </article>
  </div>
</main>
<footer><p class="rule">Built without JavaScript, network assets, bundled fonts, or subscriptions. Code: Unlicense. Original SVGs and documentation: CC BY 4.0. Maintained by sporemound; creative material credited to Uniflora contributors. See <a href="../ATTRIBUTION.md">attribution</a> and the <a href="../docs/REVIEW-CHECKLIST.md">release checklist</a>.</p></footer>
</body>
</html>

===== END FILE snapshot/demo/index.html =====

===== BEGIN FILE snapshot/demo/starter.html =====
<!doctype html>
<!-- SPDX-License-Identifier: Unlicense -->
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Uniflora preset starter</title>
<link rel="stylesheet" href="../presets/tokens.css">
<style>
  * { box-sizing: border-box; }
  body { margin: 0; font: 1rem/1.6 system-ui, sans-serif; }
  .panel { min-height: 100vh; padding: clamp(1.5rem, 6vw, 5rem);
    color: var(--uf-text); background: var(--uf-bg); }
  h1 { max-width: 24ch; font-family: var(--uf-heading); line-height: 1.2; }
  p { max-width: 60ch; }
  a { color: var(--uf-accent); text-underline-offset: .2em; }
  a:focus-visible { outline: 3px solid currentColor; outline-offset: 5px; }
  .note { color: var(--uf-muted); }
</style>
<!-- Change the branch: isometric-idm, engraved-architecture, crt-worlds,
     nocturnal-optics, kilim-burdock, or botanical-specimen. -->
<main class="panel" data-uniflora="isometric-idm">
  <h1>Community audio archive</h1>
  <p>Recordings, listening notes, and conversations remain the subject.
     Replace this example with your own content and composition.</p>
  <p class="note">This preset applies color and type roles. Add only the
     geometry and texture that serve your subject.</p>
  <a href="index.html">Explore all six presets</a>
</main>
</html>

===== END FILE snapshot/demo/starter.html =====

===== BEGIN FILE snapshot/docs/BOTANICAL-ACCURACY.md =====
# Botanical accuracy

Accuracy follows the depicted species, in every branch. A pixel plant, engraved plant, or optically distorted plant still needs a credible underlying structure when identified by name. If no plant is relevant to the subject, do not add one merely to make the image look like Uniflora.

## Ghost pipe checklist

*Monotropa uniflora* L. is an accepted flowering plant in Ericaceae, not a mushroom. Kew's Plants of the World Online supplies the accepted name and family [B2]. Native Plant Trust supplies these field checks [B1]:

- A stem normally bears one downward-facing flower during flowering; several stems may occur together.
- The flower has separate petals. Their number varies; five is a useful starting depiction, not an invariant diagnostic rule.
- Reduced, small, stalkless, alternate scale-like leaves replace broad green foliage.
- The plant lacks green pigment and is mycoheterotrophic: it obtains resources through fungi. Avoid drawings that label it a decomposer or show a direct feeding pipe into a tree.
- Pale coloration may include pink or red. Dry plants darken. Do not present neon emission as observed natural coloration.
- Show the selected life stage consistently: flowering heads nod; mature capsules can face upward.

Use the specific ecological term “mycoheterotrophic” rather than an unexplained general parasite label. The linked sources have different regional and taxonomic scopes; check a local flora before labeling an unusual regional form.

## Review workflow

1. Name every identifiable plant and select its life stage. For burdock, specify a species such as *Arctium lappa* before making specimen claims.
2. Consult an institutional flora, herbarium, or botanical organization's species treatment. Record the page, access date, and relevant observation in the attribution register.
3. Compare silhouette, branching, attachment, flower or fruit orientation, and organ detail. Correct the artwork before adding texture or optical effects.
4. Label invented colors, lights, impossible duplication, or organ alterations as artistic interpretation. Keep a less distorted reference view when identification matters.
5. Have a botanical reviewer check educational or specimen releases. Never describe a simplified motif as an identification key or verified scientific plate.

The bundled ghost-pipe motif is an original simplified silhouette for design use. It is not a traced photograph, herbarium specimen, or field identification aid. The burdock textile motif is an abstract hooked rhythm, not a specimen drawing.

## Sources

- **B1:** Native Plant Trust, [Go Botany: *Monotropa uniflora*](https://gobotany.nativeplanttrust.org/species/monotropa/uniflora/). Consulted 2026-10-10 UTC. Facts were paraphrased; no images or page text are bundled.
- **B2:** Royal Botanic Gardens, Kew, [Plants of the World Online: *Monotropa uniflora* L.](https://powo.science.kew.org/taxon/281016-2). Consulted 2026-10-10 UTC. Used for name and family only; no images or datasets are bundled.

See [REFERENCE-SOURCES.md](REFERENCE-SOURCES.md) for reference scope and [RIGHTS-REVIEW.md](RIGHTS-REVIEW.md) for reuse limits.

===== END FILE snapshot/docs/BOTANICAL-ACCURACY.md =====

===== BEGIN FILE snapshot/docs/HISTORY-AND-INTERPRETATION.md =====
# Historical choices and new interpretations

This record separates what the current brief reconfirms from what v0.1 adds. It is not a claim that a complete visual archive has been recovered. Earlier image outputs and commercial reference works are not included in this repository.

## Reconfirmed directions

The user's v0.1 brief is the controlling source for these six branches:

| Branch ID | Reconfirmed direction |
| --- | --- |
| `isometric-idm` | 16-bit botanical forms; *Monotropa uniflora* anatomy; isometric depth; inversion; telepathy as an artistic theme; mirrored signal geometry; restrained kaleidoscopic structures; turquoise and forest green. |
| `engraved-architecture` | Romanesque interiors; spatial contradictions associated with M. C. Escher; black-and-ivory woodcut surfaces; dense cross-hatching; sharp modular-origami tessellations associated with Tomoko Fuse; projected lines deformed by implied surfaces. |
| `crt-worlds` | Sega Genesis-like forest imagery; cyan-magenta bioluminescence; ghost pipe; crescent moons; intentional VHS/NTSC or datamosh treatments; fixed-display animation with scene continuity. |
| `nocturnal-optics` | Moonlit gardens, mist, luminous lichen, shallow depth of field, anamorphic optics, refraction, and restrained silver/lavender/teal/pink/gold/ivory relationships. |
| `kilim-burdock` | Geometric textile motifs, rhythmic repetition, balanced offsets, and reversible card compositions; incomplete historical references must be identified. |
| `botanical-specimen` | Anatomically credible ghost pipe, careful plant morphology, field-guide detail, and adaptable album-cover or poster arrangements. |

These reference names describe directions. They do not supply redistributable artworks, game graphics, fonts, origami diagrams, or a right to imply endorsement. v0.1 constructs new geometry and text rather than bundling those works.

## Context that remains scoped

- Simulated glitch was rejected for a particular logo brief. That exclusion remains local to that brief. Intentional distortion is expressly supported in `crt-worlds`.
- An earlier burdock/kilim treatment did not read correctly in its Discord/logo context, and a horizontal offset was disliked there. This is not proof that all textile offsets are forbidden. v0.1 uses a centered reversible structure and proposes balanced repeats for other compositions.
- A compact woven signal or maker-mark treatment was an assistant proposal, not a confirmed universal Uniflora mark.
- Earlier lettering, slogans, channel names, generated images, and exact compositions are examples of individual work. They are not required brand elements.

The current brief takes precedence if a past experiment conflicts with these requested branches. Before describing a previous result as an approved master asset, retrieve that result and confirm its scope and rights.

## New v0.1 proposals

The following are newly authored implementation choices, available for review and revision:

- All exact hex values, semantic token roles, generic font stacks, spacing, border treatments, and CSS selectors in [the presets](../presets/tokens.json).
- The six-panel demonstration, its text, and every example prompt. They show different subjects and media; they are not canonical compositions.
- The original SVG motifs. They are editable design studies, not copied historical artifacts, scientific plates, or foldable origami instructions.
- A centered, 180-degree rotational burdock/textile motif using a hook-and-diamond vocabulary. It has no assigned historical, regional, protective, or spiritual meaning. “Burdock” names the design cue; it is not a claim to reproduce a specific traditional kilim motif.
- The one-primary-branch workflow and the practical limits on decorative density and motion. These make a small reusable kit coherent; they do not close off future branches.

## Recording future decisions

For a future preset or asset, record: its author, date, affected brief, source links, license, whether it is recovered or newly proposed, and its approval status. A useful status vocabulary is `reconfirmed`, `recovered-unverified`, `new-proposal`, and `approved-for-this-brief`.

Never turn `approved-for-this-brief` into a global requirement without an explicit design decision. Preserve both the reason for a local exclusion and the place where it applies.

===== END FILE snapshot/docs/HISTORY-AND-INTERPRETATION.md =====

===== BEGIN FILE snapshot/docs/MANIFESTO.md =====
# Uniflora aesthetic manifesto · v0.1

Uniflora is a way of giving an existing subject a visual language: botanical specificity, experimental rhythm, uncertain perception, and carefully constructed space. It can dress a field guide, an album cover, a public library, a seed exchange, or a useful interface. The subject keeps its identity and meaning.

Begin with what the work is about. Decide what must remain recognizable. Choose one of six visual branches, then translate the subject into that branch's materials, proportions, and spatial rules. A branch changes how the subject is expressed; it does not replace the subject with the same imaginary forest.

Let strangeness have a structure. An unseen connection can become matching intervals in two distant forms. Inversion can become a reflected plane or an exchanged foreground and background. Rhythm can become a repeating module with one deliberate interruption. Impossible architecture can contain a legible spatial contradiction. These are artistic devices, not evidence of telepathy or other extraordinary phenomena.

Treat identifiable plants as organisms. Ghost pipe, *Monotropa uniflora*, is a mycoheterotrophic flowering plant. Its pale stem, scale leaves, and single nodding flower must survive stylization when it is depicted as that species. Label a schematic as a schematic. Keep imaginative light and geometry distinct from botanical claims.

Use texture with a purpose: a carved shadow, a woven repeat, a phosphor edge, a refracted highlight. Give the eye somewhere to rest. Readable text, accessible controls, and a calm alternative to motion belong to the work.

This version preserves six requested directions, not one mandatory look. Its hex colors, token names, layouts, prompt examples, and original motifs are editable v0.1 proposals. No slogan, sample lettering, particular image result, or font is compulsory. Distortion belongs to the CRT branch when chosen; a restriction from one logo brief does not prohibit it elsewhere.

Make the system open by keeping its parts understandable, editable, and attributable. Share original work under the appropriate license, record its sources, and carry unresolved reference rights into review instead of treating them as permission.

Continue with [the practical style guide](STYLE-GUIDE.md), [historical status](HISTORY-AND-INTERPRETATION.md), or [the image-prompt template](../prompts/TEMPLATE.md).

===== END FILE snapshot/docs/MANIFESTO.md =====

===== BEGIN FILE snapshot/docs/REFERENCE-SOURCES.md =====
# Reference sources and boundaries

This is a reference register, not a list of bundled third-party assets. The main attribution register records individual project files. Access dates use UTC.

| ID | Source | Checked | Used for | Included source material / rights boundary |
| --- | --- | --- | --- | --- |
| B1 | Native Plant Trust, [Go Botany: *Monotropa uniflora*](https://gobotany.nativeplanttrust.org/species/monotropa/uniflora/) | 2026-10-10 | Single nodding flower, reduced leaves, pale coloration, fungal dependence, and life-stage review | Facts paraphrased; no images or copied descriptions. Page images/text remain under their stated copyright. |
| B2 | Royal Botanic Gardens, Kew, [Plants of the World Online](https://powo.science.kew.org/taxon/281016-2) | 2026-10-10 | Accepted scientific name and Ericaceae family | No images or dataset copied. Item-specific licenses apply to any later use. |
| R1 | [Unlicense steward](https://unlicense.org/) and Open Source Initiative, [The Unlicense](https://opensource.org/license/unlicense) | 2026-10-10 | Standard public-domain software dedication; OSI approval and SPDX identifier `Unlicense` | Established root `LICENSE` preserved; matching text in `licenses/Unlicense.txt`. Code uses these selected terms. |
| R2 | Creative Commons, [CC BY 4.0 legal code](https://creativecommons.org/licenses/by/4.0/legalcode.en) and [plain text](https://creativecommons.org/licenses/by/4.0/legalcode.txt) | 2026-10-10 | Full documentation/asset license and grant limits | Complete legal-code text in `licenses/CC-BY-4.0.txt`; official public-license text is CC0. No CC logo bundled. |
| R3 | Creative Commons, [FAQ: software licensing](https://creativecommons.org/faq/#can-i-apply-a-creative-commons-license-to-software) | 2026-10-10 | Separating software from documentation and artwork licenses | Guidance paraphrased; no FAQ text bundled. |
| A1 | W3C WAI, [Understanding SC 1.4.3: Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) | 2026-10-10 | WCAG 2.2 AA: normal text at least 4.5:1; large text at least 3:1 | No source text or images bundled. See the [normative criterion](https://www.w3.org/TR/WCAG22/#contrast-minimum). |
| A2 | W3C WAI, [Understanding SC 1.4.11: Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) | 2026-10-10 | WCAG 2.2 AA: necessary control and graphical information generally needs 3:1 against adjacent colors | No source text or images bundled. See the [normative criterion](https://www.w3.org/TR/WCAG22/#non-text-contrast) and its exceptions. |
| A3 | W3C WAI, [Understanding SC 2.3.3: Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html) | 2026-10-10 | WCAG 2.2 AAA: nonessential interaction-triggered motion can be disabled; informs reduced-motion handling | No source text or images bundled. See the [normative criterion](https://www.w3.org/TR/WCAG22/#animation-from-interactions). |

These three criteria inform the template's minimum design checks; meeting them alone is not a full WCAG conformance claim. Large text means at least 18pt regular or 14pt bold, or equivalent. Palette contrast checks apply to the actual foreground/background pairs; gradients, opacity, and textured backgrounds require their own evaluation. Autoplay animation, flashing, keyboard access, focus visibility, and content semantics require additional review.

## References recovered from the brief

| Reference | Status in v0.1 | Boundary |
| --- | --- | --- |
| Escher-inspired spatial contradictions | User-specified visual reference, translated into new spatial construction | No artwork traced, copied, embedded, or asserted to be freely redistributable. |
| Tomoko Fuse-inspired modular origami | User-specified structural reference, translated into new abstract faceted geometry | No published diagram, unit design, instruction, or book image bundled. Demonstration geometry is not a folding recipe or mechanically validated unit. |
| Sega Genesis-like imagery | User-specified era/medium reference, translated into a limited-palette pixel treatment | No commercial sprites, game screens, logos, ROMs, or console fonts bundled. |
| Kilim and burdock | Historical branch designation from the brief; motif construction is newly proposed | Cultural origin, object history, and symbolic readings are unresolved. Do not present the new hooked pattern as an authenticated traditional symbol. |
| Commercial typefaces or named lettering in earlier artwork | Contextual references only | No paid font or proprietary font resource required or redistributed. |

## Adding a source

For each imported asset, add its exact file path, creator, source URL, version or retrieval date, license identifier and URL, modification note, required credit, and a copy of any required notices. Verify the actual object, not just the hosting website. If rights are unknown, keep it outside the distributable package and mark the unresolved decision clearly.

- **A4:** W3C, [CSS technique C39](https://www.w3.org/WAI/WCAG22/Techniques/css/C39.html). Consulted 2026-10-10 UTC. Used for the reduced-motion CSS approach; no page content or illustrations copied.

===== END FILE snapshot/docs/REFERENCE-SOURCES.md =====

===== BEGIN FILE snapshot/docs/REVIEW-CHECKLIST.md =====
# Review before publication

The creator authorized publishing this v0.1 package to the existing repository after review. The checklist records completed checks and limits to carry into future revisions.

| Review | Current position | Required release decision |
| --- | --- | --- |
| Six branch separation | Six presets, artworks and prompt examples provided | Check that each reads distinctly and suits its subject |
| Historical evidence | Brief and recovered context separated from new proposals | Correct any uncertain attribution; don't promote examples to requirements |
| Botanical detail | Source-grounded morphology guidance; simplified SVG studies | Botanical reviewer checks any educational/specimen use |
| Kilim/burdock context | New generic geometry; no traditional meaning asserted | Keep label or research a specific historical object before claiming authenticity |
| Assets and fonts | Original path artwork; zero bundled fonts or third-party visual assets | Inspect for recognizable copying and register any later imports |
| License scope | Existing Unlicense preserved; CC BY 4.0 for docs/art, explicit scope | Maintainer sporemound; creator authorized repository publication; grants limited to rights held |
| Interface and motion | Contrast roles, keyboard controls, static default, reduced motion | Check chosen browser/device and assistive technology before claiming compliance |
| Source completeness | Exact filenames, complete editable text source | Verify package against the delivered source copy |
| Repository publication | Authorized: `sporemound/uniflora-aesthetic-kit` | Publish the reviewed v0.1; no hosted website deployment requested |

No historic Uniflora images have been cleared for inclusion. Their absence is deliberate. AI assistance is disclosed; the project does not claim jurisdiction-independent copyright protection for AI-generated expression. These limits do not block the authorized v0.1 publication; verify later imports separately.

===== END FILE snapshot/docs/REVIEW-CHECKLIST.md =====

===== BEGIN FILE snapshot/docs/RIGHTS-REVIEW.md =====
# Rights review for v0.1

Maintainer **sporemound** has authorized publication of this kit at [sporemound/uniflora-aesthetic-kit](https://github.com/sporemound/uniflora-aesthetic-kit). The code keeps the repository's established **Unlicense**; documentation, prompt prose, and original artwork use **CC BY 4.0**. Attribution is **Uniflora contributors**. This document records the selected terms and known boundaries. A dedication or license applies only to rights that exist and can be granted.

## Selected separation

| Material | Terms | Reason and reuse obligation |
| --- | --- | --- |
| HTML, CSS, JavaScript, scripts, design-token JSON | Unlicense | Public-domain dedication and unrestricted software permission, including modification, redistribution, and commercial reuse. Code attribution is not a condition. |
| README, guides, prompt prose, and other documentation | CC BY 4.0 | Permits sharing and adaptation, including commercially, with credit, a license reference, and indication of modifications. |
| Original SVG motifs and original preview compositions | CC BY 4.0 | Keeps artwork attribution distinct from software notices. Same credit and change-marking requirements as documentation. |
| Official legal text itself | Original issuer's terms | CC public-license text is dedicated under CC0; retain its complete text. The Unlicense is the standard public-domain software dedication already selected by this repository. |

The complete texts are in [../licenses/](../licenses/), and the existing root [LICENSE](../LICENSE) remains unchanged. The scope map is in [../licenses/README.md](../licenses/README.md). CC recommends software-specific terms for software, while allowing CC licenses for separate documentation and artistic elements [R3]. No NonCommercial or NoDerivatives restriction applies.

## Included material audit

- **Fonts:** zero font files, web-font imports, font-service requests, or font packages. Generic CSS families use fonts installed by the viewer. No font is redistributed, so there is no included font license to verify. If a later release bundles a font, verify the exact font version, redistribution terms, required notices, and any reserved names first.
- **Images and textures:** no third-party photographs, scans, game sprites, artwork, or downloaded textures. SVG paths and CSS textures are newly constructed for this project. AI assistance is disclosed in the attribution register; new imports still require their own rights review.
- **Historical Uniflora work:** earlier generated images, unpublished logos, captions, and screenshots are not included. Their rights have not been audited. Recovering an aesthetic preference does not authorize redistributing an earlier asset.
- **References:** M. C. Escher, Tomoko Fuse, and Sega Genesis are descriptive references from the brief. No named artwork, crease diagram, instruction page, logo, ROM, commercial sprite, or commercial font is bundled or adapted. No endorsement is claimed.
- **Kilim and burdock:** the geometric hooked design is a new interpretation. No attribution to a specific community, weaver, period, or universal symbolic meaning is established. An authentic historical reconstruction needs a separately sourced object and contextual research.
- **Botanical sources:** sources support factual morphology checks only. Their photographs and full descriptive text are not redistributed. Native Plant Trust marks its images and text as copyrighted; Kew's image and dataset terms vary by item. Linking is not permission to copy an asset.

## Known limits and future imports

1. “Uniflora contributors” is a collective credit selected for the release. The AI is not identified as a copyright owner. The public maintainer is sporemound.
2. This kit makes no assurance that AI-assisted expression has copyright protection in every jurisdiction. Record later human editing and selection honestly. Terms apply only to interests that exist and can be dedicated or licensed.
3. Historical Uniflora images and other creators' reference artwork remain excluded because their redistribution rights have not been audited. Verify and separately register any future import before including it.
4. Neither the code dedication nor CC BY 4.0 grants trademark rights, artist endorsement, or official community status. “Uniflora” is used here as the project identifier.
5. The specimen drawings are schematic and have not received expert botanical certification. Browser and assistive-technology review remains incomplete; the kit makes no full accessibility-conformance claim. These are documented limitations of v0.1.

There are no bundled external visual assets or fonts awaiting clearance. Publication is authorized; future imported assets need separate provenance and redistribution evidence.

## Primary sources

- **R1:** Unlicense steward, [Unlicense](https://unlicense.org/), and Open Source Initiative, [The Unlicense](https://opensource.org/license/unlicense), consulted 2026-10-10 UTC. OSI identifies it as an approved license with SPDX identifier `Unlicense`.
- **R2:** Creative Commons, [CC BY 4.0 legal code](https://creativecommons.org/licenses/by/4.0/legalcode.en), especially sections 2–3 and its CC0 notice, consulted 2026-10-10 UTC.
- **R3:** Creative Commons, [FAQ: software licensing](https://creativecommons.org/faq/#can-i-apply-a-creative-commons-license-to-software), consulted 2026-10-10 UTC.

These release terms do not clear unrelated reference works or any particular future imported resource.

===== END FILE snapshot/docs/RIGHTS-REVIEW.md =====

===== BEGIN FILE snapshot/docs/STYLE-GUIDE.md =====
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

===== END FILE snapshot/docs/STYLE-GUIDE.md =====

===== BEGIN FILE snapshot/docs/SVG-PROVENANCE.md =====
# SVG provenance register

All six files below were created anew on 2026-10-10 for Uniflora aesthetic template v0.1 using original programmatic SVG paths, rectangles, circles, ellipses, gradients, clipping paths, and hatch patterns. No image tracing, screenshot extraction, raster incorporation, traditional textile copying, artist-image sampling, or third-party asset download was used. These are **new proposals**, not evidence of past Uniflora artwork choices.

The user supplied the six branch directions and the named cultural/artistic reference points. Those references do not establish ownership of, permission to reproduce, or direct descent from another creator's individual designs. These files aim to interpret general visual relationships with original geometry.

| Exact asset path | New geometry and treatment | Third-party material included | Accuracy and attribution limits |
| --- | --- | --- | --- |
| `assets/svg/isometric-signal.svg` | Rhomboid ground grid, nested mirrored signal diamonds, stepped ghost-pipe silhouettes, an inverted echo | None | Pixel forms are illustrative; do not use as a diagnostic botanical image. |
| `assets/svg/engraved-fold.svg` | Four round arches, hatch patterns, contradictory stair/support relationships, folded rhombi, curves changing direction on geometric facets | None | No Escher engraving or Tomoko Fuse unit/crease pattern is copied. The facets are visual geometry, not a tested folding recipe. |
| `assets/svg/crt-forest.svg` | Original monitor frame, stepped trunks, crescent, ghost-pipe forms, clipped displacement bands, scanlines | None | No Sega game sprites or hardware logo. Cyan/magenta lighting and scanlines are stylistic simulation. Screen content is static and clipped inside an intact frame. |
| `assets/svg/nocturnal-optics.svg` | Layered garden silhouettes, moon, mist curves, oval bokeh, refraction arcs, nodding plants, branching lichen-like marks | None | Optical effects are vector interpretations; pale plants are not asserted to glow naturally. Lichen-like marks are not an identified species. |
| `assets/svg/kilim-burdock.svg` | Centered diamond outlines, angular hooks, repeated balanced border, curved hooked burr rosettes, a composition reversible at 180 degrees | None | New generic textile interpretation; no named community, specific weaving tradition, traditional motif meaning, or authenticated historical reference is claimed. The burr rosettes are abstract, not a burdock identification drawing. |
| `assets/svg/specimen-ghost-pipe.svg` | Three scale-leaved stems without ordinary foliage, one open nodding flower per stem, separate rounded obovate petals, lower opening, partial inset reproductive hints, detached petal study, scale-leaf inset, leader lines, plain layout rules | None | Intended morphology: *Monotropa uniflora*. This has not been certified by a botanist; five petals are illustrative, visible stamens are partial rather than a complete count, and no calibrated scale or specimen measurements are asserted. |

## Botanical reference used for the revision

[Native Plant Trust, Go Botany: *Monotropa uniflora*](https://gobotany.nativeplanttrust.org/species/monotropa/uniflora/) was consulted for anatomical characteristics on 2026-10-10 UTC. Its account supports individual downward flowers, a bell-like perianth formed by separate petals, obovate rounded petal ends, and a stigma remaining inside the mouth. The four botanical assets were revised accordingly to show flowering rather than closed capsule-like silhouettes. This is a schematic interpretation, not botanical certification. No reference image or source text is redistributed.

## Authorship and license declaration

Credit: **Uniflora contributors, “Uniflora v0.1 original SVG studies,” 2026, CC BY 4.0. Created with AI-assisted code generation; modified by [your name] where applicable.**

CC BY 4.0 applies to these original SVGs under the creator-authorized publication scope. The repository's license status, asset terms, and attribution register control any final grant and explain the limits of AI-assisted authorship. A license can offer only rights the contributors actually hold; it does not establish exclusive copyright, protect a trademark, authenticate a traditional motif, or license unrelated reference artwork. Future contributors must add provenance for every replacement or imported component. Do not merge an externally sourced asset merely because it is visible online or described as a reference.

## Implementation inspection

- Each SVG is a standalone valid XML document with a title, description, and layer IDs.
- Each SVG has the same 480 by 360 coordinate space.
- Every `url(#...)` reference points to a local SVG definition. No external image, font, stylesheet, or network resource is required.
- No SVG contains script, an event handler, or animation. Distortion in the CRT asset is static.
- The CRT screen clip is `rect x="30" y="34" width="420" height="260" rx="22"`; scene elements stay within that clipped group.
- Asset palettes are individual editable proposals, not universal Uniflora requirements.

These implementation checks do not replace a botanical or cultural subject review.

===== END FILE snapshot/docs/SVG-PROVENANCE.md =====

===== BEGIN FILE snapshot/docs/VALIDATION.md =====
# Validation record

Portable validator: **PASS**, 3000 checks, 0 failures.

Executed 2026-10-10 UTC. Uses Python standard library; no paid dependencies.

## Readable token pairs

Minimum across text, muted, and accent against both bg and surface. Threshold checked without rounding: 4.5:1.

| Branch | Minimum ratio |
| --- | --- |
| `isometric-idm` | 6.39:1 |
| `engraved-architecture` | 5.53:1 |
| `crt-worlds` | 6.27:1 |
| `nocturnal-optics` | 7.53:1 |
| `kilim-burdock` | 5.46:1 |
| `botanical-specimen` | 5.01:1 |

## Scope

Checks JSON/CSS synchronization, all six demo/prompt/SVG branches, internal links, SVG parse and references, absence of font files and external demo resources, and declared opt-in/reduced-motion CSS.

Six SVGs were rendered and visually inspected separately. No complete browser interaction, assistive-technology, or botanical expert certification is claimed. A local browser runtime download failed in this environment; inspect the HTML in your target browser before publication. Static CSS checks do not prove animation confinement at runtime. No hosted website deployment has occurred. The creator authorized publishing the reviewed v0.1 to the existing GitHub repository.

Decorative swatches are not approved text colors. This record is not a full WCAG conformance or legal clearance report.

===== END FILE snapshot/docs/VALIDATION.md =====

===== BEGIN FILE snapshot/LICENSE =====
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>

===== END FILE snapshot/LICENSE =====

===== BEGIN FILE snapshot/LICENSE.md =====
# License map — v0.1

**Unlicense** applies to software and design tokens, preserving the existing repository [LICENSE](LICENSE). **CC BY 4.0** applies to documentation, prompt prose, and original artwork. Complete texts and exact scope are in [licenses/README.md](licenses/README.md).

Maintained by [sporemound](https://github.com/sporemound); original creative contributions are credited to **Uniflora contributors**. The creator authorized publication of this kit to the repository. AI assistance is disclosed; no assurance is made that AI-assisted expression has copyright protection in every jurisdiction. Grants cover only rights that exist and can be granted; they do not cover external references, trademarks, or official affiliation. See [docs/RIGHTS-REVIEW.md](docs/RIGHTS-REVIEW.md).

===== END FILE snapshot/LICENSE.md =====

===== BEGIN FILE snapshot/licenses/CC-BY-4.0.txt =====
Attribution 4.0 International

=======================================================================
Creative Commons Corporation ("Creative Commons") is not a law firm and
does not provide legal services or legal advice. Distribution of
Creative Commons public licenses does not create a lawyer-client or
other relationship. Creative Commons makes its licenses and related
information available on an "as-is" basis. Creative Commons gives no
warranties regarding its licenses, any material licensed under their
terms and conditions, or any related information. Creative Commons
disclaims all liability for damages resulting from their use to the
fullest extent possible.
Using Creative Commons Public Licenses

Creative Commons public licenses provide a standard set of terms and
conditions that creators and other rights holders may use to share
original works of authorship and other material subject to copyright
and certain other rights specified in the public license below. The
following considerations are for informational purposes only, are not
exhaustive, and do not form part of our licenses.
     Considerations for licensors: Our public licenses are
     intended for use by those authorized to give the public
     permission to use material in ways otherwise restricted by
     copyright and certain other rights. Our licenses are
     irrevocable. Licensors should read and understand the terms
     and conditions of the license they choose before applying it.
     Licensors should also secure all rights necessary before
     applying our licenses so that the public can reuse the
     material as expected. Licensors should clearly mark any
     material not subject to the license. This includes other CC-
     licensed material, or material used under an exception or
     limitation to copyright. More considerations for licensors:
    wiki.creativecommons.org/Considerations_for_licensors
     Considerations for the public: By using one of our public
     licenses, a licensor grants the public permission to use the
     licensed material under specified terms and conditions. If
     the licensor's permission is not necessary for any reason--for
     example, because of any applicable exception or limitation to
     copyright--then that use is not regulated by the license. Our
     licenses grant only permissions under copyright and certain
     other rights that a licensor has authority to grant. Use of
     the licensed material may still be restricted for other
     reasons, including because others have copyright or other
     rights in the material. A licensor may make special requests,
     such as asking that all changes be marked or described.
     Although not required by our licenses, you are encouraged to
     respect those requests where reasonable. More considerations
     for the public:
    wiki.creativecommons.org/Considerations_for_licensees
=======================================================================

Creative Commons Attribution 4.0 International Public License
By exercising the Licensed Rights (defined below), You accept and agree
to be bound by the terms and conditions of this Creative Commons
Attribution 4.0 International Public License ("Public License"). To the
extent this Public License may be interpreted as a contract, You are
granted the Licensed Rights in consideration of Your acceptance of
these terms and conditions, and the Licensor grants You such rights in
consideration of benefits the Licensor receives from making the
Licensed Material available under these terms and conditions.

Section 1 -- Definitions.
  a. Adapted Material means material subject to Copyright and Similar
     Rights that is derived from or based upon the Licensed Material
     and in which the Licensed Material is translated, altered,
     arranged, transformed, or otherwise modified in a manner requiring
     permission under the Copyright and Similar Rights held by the
     Licensor. For purposes of this Public License, where the Licensed
     Material is a musical work, performance, or sound recording,
     Adapted Material is always produced where the Licensed Material is
     synched in timed relation with a moving image.
  b. Adapter's License means the license You apply to Your Copyright
     and Similar Rights in Your contributions to Adapted Material in
     accordance with the terms and conditions of this Public License.
  c. Copyright and Similar Rights means copyright and/or similar rights
     closely related to copyright including, without limitation,
     performance, broadcast, sound recording, and Sui Generis Database
     Rights, without regard to how the rights are labeled or
     categorized. For purposes of this Public License, the rights
     specified in Section 2(b)(1)-(2) are not Copyright and Similar
     Rights.
  d. Effective Technological Measures means those measures that, in the
     absence of proper authority, may not be circumvented under laws
     fulfilling obligations under Article 11 of the WIPO Copyright
     Treaty adopted on December 20, 1996, and/or similar international
     agreements.

  e. Exceptions and Limitations means fair use, fair dealing, and/or
     any other exception or limitation to Copyright and Similar Rights
     that applies to Your use of the Licensed Material.
  f. Licensed Material means the artistic or literary work, database,
     or other material to which the Licensor applied this Public
     License.

  g. Licensed Rights means the rights granted to You subject to the
     terms and conditions of this Public License, which are limited to
     all Copyright and Similar Rights that apply to Your use of the
     Licensed Material and that the Licensor has authority to license.
  h. Licensor means the individual(s) or entity(ies) granting rights
     under this Public License.
  i. Share means to provide material to the public by any means or
     process that requires permission under the Licensed Rights, such
     as reproduction, public display, public performance, distribution,
     dissemination, communication, or importation, and to make material
     available to the public including in ways that members of the
     public may access the material from a place and at a time
     individually chosen by them.
  j. Sui Generis Database Rights means rights other than copyright
     resulting from Directive 96/9/EC of the European Parliament and of
     the Council of 11 March 1996 on the legal protection of databases,
     as amended and/or succeeded, as well as other essentially
     equivalent rights anywhere in the world.

  k. You means the individual or entity exercising the Licensed Rights
     under this Public License. Your has a corresponding meaning.


Section 2 -- Scope.

  a. License grant.
       1. Subject to the terms and conditions of this Public License,
          the Licensor hereby grants You a worldwide, royalty-free,
          non-sublicensable, non-exclusive, irrevocable license to
          exercise the Licensed Rights in the Licensed Material to:

            a. reproduce and Share the Licensed Material, in whole or
               in part; and

            b. produce, reproduce, and Share Adapted Material.
       2. Exceptions and Limitations. For the avoidance of doubt, where
          Exceptions and Limitations apply to Your use, this Public
          License does not apply, and You do not need to comply with
          its terms and conditions.

       3. Term. The term of this Public License is specified in Section
          6(a).
       4. Media and formats; technical modifications allowed. The
          Licensor authorizes You to exercise the Licensed Rights in
          all media and formats whether now known or hereafter created,
          and to make technical modifications necessary to do so. The
          Licensor waives and/or agrees not to assert any right or
          authority to forbid You from making technical modifications
          necessary to exercise the Licensed Rights, including
          technical modifications necessary to circumvent Effective
          Technological Measures. For purposes of this Public License,
          simply making modifications authorized by this Section 2(a)
          (4) never produces Adapted Material.
       5. Downstream recipients.

            a. Offer from the Licensor -- Licensed Material. Every
               recipient of the Licensed Material automatically
               receives an offer from the Licensor to exercise the
               Licensed Rights under the terms and conditions of this
               Public License.
            b. No downstream restrictions. You may not offer or impose
               any additional or different terms or conditions on, or
               apply any Effective Technological Measures to, the
               Licensed Material if doing so restricts exercise of the
               Licensed Rights by any recipient of the Licensed
               Material.
       6. No endorsement. Nothing in this Public License constitutes or
          may be construed as permission to assert or imply that You
          are, or that Your use of the Licensed Material is, connected
          with, or sponsored, endorsed, or granted official status by,
          the Licensor or others designated to receive attribution as
          provided in Section 3(a)(1)(A)(i).

  b. Other rights.
       1. Moral rights, such as the right of integrity, are not
          licensed under this Public License, nor are publicity,
          privacy, and/or other similar personality rights; however, to
          the extent possible, the Licensor waives and/or agrees not to
          assert any such rights held by the Licensor to the limited
          extent necessary to allow You to exercise the Licensed
          Rights, but not otherwise.
       2. Patent and trademark rights are not licensed under this
          Public License.

       3. To the extent possible, the Licensor waives any right to
          collect royalties from You for the exercise of the Licensed
          Rights, whether directly or through a collecting society
          under any voluntary or waivable statutory or compulsory
          licensing scheme. In all other cases the Licensor expressly
          reserves any right to collect such royalties.

Section 3 -- License Conditions.

Your exercise of the Licensed Rights is expressly made subject to the
following conditions.

  a. Attribution.

       1. If You Share the Licensed Material (including in modified
          form), You must:

            a. retain the following if it is supplied by the Licensor
               with the Licensed Material:
                 i. identification of the creator(s) of the Licensed
                    Material and any others designated to receive
                    attribution, in any reasonable manner requested by
                    the Licensor (including by pseudonym if
                    designated);

                ii. a copyright notice;

               iii. a notice that refers to this Public License;

                iv. a notice that refers to the disclaimer of
                    warranties;
                 v. a URI or hyperlink to the Licensed Material to the
                    extent reasonably practicable;

            b. indicate if You modified the Licensed Material and
               retain an indication of any previous modifications; and

            c. indicate the Licensed Material is licensed under this
               Public License, and include the text of, or the URI or
               hyperlink to, this Public License.
       2. You may satisfy the conditions in Section 3(a)(1) in any
          reasonable manner based on the medium, means, and context in
          which You Share the Licensed Material. For example, it may be
          reasonable to satisfy the conditions by providing a URI or
          hyperlink to a resource that includes the required
          information.
       3. If requested by the Licensor, You must remove any of the
          information required by Section 3(a)(1)(A) to the extent
          reasonably practicable.

       4. If You Share Adapted Material You produce, the Adapter's
          License You apply must not prevent recipients of the Adapted
          Material from complying with this Public License.


Section 4 -- Sui Generis Database Rights.
Where the Licensed Rights include Sui Generis Database Rights that
apply to Your use of the Licensed Material:

  a. for the avoidance of doubt, Section 2(a)(1) grants You the right
     to extract, reuse, reproduce, and Share all or a substantial
     portion of the contents of the database;
  b. if You include all or a substantial portion of the database
     contents in a database in which You have Sui Generis Database
     Rights, then the database in which You have Sui Generis Database
     Rights (but not its individual contents) is Adapted Material; and

  c. You must comply with the conditions in Section 3(a) if You Share
     all or a substantial portion of the contents of the database.
For the avoidance of doubt, this Section 4 supplements and does not
replace Your obligations under this Public License where the Licensed
Rights include other Copyright and Similar Rights.


Section 5 -- Disclaimer of Warranties and Limitation of Liability.
  a. UNLESS OTHERWISE SEPARATELY UNDERTAKEN BY THE LICENSOR, TO THE
     EXTENT POSSIBLE, THE LICENSOR OFFERS THE LICENSED MATERIAL AS-IS
     AND AS-AVAILABLE, AND MAKES NO REPRESENTATIONS OR WARRANTIES OF
     ANY KIND CONCERNING THE LICENSED MATERIAL, WHETHER EXPRESS,
     IMPLIED, STATUTORY, OR OTHER. THIS INCLUDES, WITHOUT LIMITATION,
     WARRANTIES OF TITLE, MERCHANTABILITY, FITNESS FOR A PARTICULAR
     PURPOSE, NON-INFRINGEMENT, ABSENCE OF LATENT OR OTHER DEFECTS,
     ACCURACY, OR THE PRESENCE OR ABSENCE OF ERRORS, WHETHER OR NOT
     KNOWN OR DISCOVERABLE. WHERE DISCLAIMERS OF WARRANTIES ARE NOT
     ALLOWED IN FULL OR IN PART, THIS DISCLAIMER MAY NOT APPLY TO YOU.
  b. TO THE EXTENT POSSIBLE, IN NO EVENT WILL THE LICENSOR BE LIABLE
     TO YOU ON ANY LEGAL THEORY (INCLUDING, WITHOUT LIMITATION,
     NEGLIGENCE) OR OTHERWISE FOR ANY DIRECT, SPECIAL, INDIRECT,
     INCIDENTAL, CONSEQUENTIAL, PUNITIVE, EXEMPLARY, OR OTHER LOSSES,
     COSTS, EXPENSES, OR DAMAGES ARISING OUT OF THIS PUBLIC LICENSE OR
     USE OF THE LICENSED MATERIAL, EVEN IF THE LICENSOR HAS BEEN
     ADVISED OF THE POSSIBILITY OF SUCH LOSSES, COSTS, EXPENSES, OR
     DAMAGES. WHERE A LIMITATION OF LIABILITY IS NOT ALLOWED IN FULL OR
     IN PART, THIS LIMITATION MAY NOT APPLY TO YOU.
  c. The disclaimer of warranties and limitation of liability provided
     above shall be interpreted in a manner that, to the extent
     possible, most closely approximates an absolute disclaimer and
     waiver of all liability.


Section 6 -- Term and Termination.

  a. This Public License applies for the term of the Copyright and
     Similar Rights licensed here. However, if You fail to comply with
     this Public License, then Your rights under this Public License
     terminate automatically.
  b. Where Your right to use the Licensed Material has terminated under
     Section 6(a), it reinstates:

       1. automatically as of the date the violation is cured, provided
          it is cured within 30 days of Your discovery of the
          violation; or

       2. upon express reinstatement by the Licensor.

     For the avoidance of doubt, this Section 6(b) does not affect any
     right the Licensor may have to seek remedies for Your violations
     of this Public License.
  c. For the avoidance of doubt, the Licensor may also offer the
     Licensed Material under separate terms or conditions or stop
     distributing the Licensed Material at any time; however, doing so
     will not terminate this Public License.

  d. Sections 1, 5, 6, 7, and 8 survive termination of this Public
     License.


Section 7 -- Other Terms and Conditions.

  a. The Licensor shall not be bound by any additional or different
     terms or conditions communicated by You unless expressly agreed.
  b. Any arrangements, understandings, or agreements regarding the
     Licensed Material not stated herein are separate from and
     independent of the terms and conditions of this Public License.


Section 8 -- Interpretation.

  a. For the avoidance of doubt, this Public License does not, and
     shall not be interpreted to, reduce, limit, restrict, or impose
     conditions on any use of the Licensed Material that could lawfully
     be made without permission under this Public License.
  b. To the extent possible, if any provision of this Public License is
     deemed unenforceable, it shall be automatically reformed to the
     minimum extent necessary to make it enforceable. If the provision
     cannot be reformed, it shall be severed from this Public License
     without affecting the enforceability of the remaining terms and
     conditions.
  c. No term or condition of this Public License will be waived and no
     failure to comply consented to unless expressly agreed to by the
     Licensor.

  d. Nothing in this Public License constitutes or may be interpreted
     as a limitation upon, or waiver of, any privileges and immunities
     that apply to the Licensor or You, including from the legal
     processes of any jurisdiction or authority.


=======================================================================
Creative Commons is not a party to its public
licenses. Notwithstanding, Creative Commons may elect to apply one of
its public licenses to material it publishes and in those instances
will be considered the “Licensor.” The text of the Creative Commons
public licenses is dedicated to the public domain under the CC0 Public
Domain Dedication. Except for the limited purpose of indicating that
material is shared under a Creative Commons public license or as
otherwise permitted by the Creative Commons policies published at
creativecommons.org/policies, Creative Commons does not authorize the
use of the trademark "Creative Commons" or any other trademark or logo
of Creative Commons without its prior written consent including,
without limitation, in connection with any unauthorized modifications
to any of its public licenses or any other arrangements,
understandings, or agreements concerning use of licensed material. For
the avoidance of doubt, this paragraph does not form part of the
public licenses.
Creative Commons may be contacted at creativecommons.org.

===== END FILE snapshot/licenses/CC-BY-4.0.txt =====

===== BEGIN FILE snapshot/licenses/README.md =====
# License scope

The public maintainer **sporemound** has authorized this release with **Unlicense** for software and design tokens, preserving the repository's existing root [LICENSE](../LICENSE). Documentation, prompt prose, and original artwork use **CC BY 4.0**, credited to **Uniflora contributors**. These terms do not claim rights over historical references, botanical facts, names, trademarks, or external linked resources. Known boundaries are recorded in [../docs/RIGHTS-REVIEW.md](../docs/RIGHTS-REVIEW.md).

| Paths or material | SPDX identifier | Full text |
| --- | --- | --- |
| `demo/*.html`, `demo/*.css`, `demo/*.js`, `presets/*.json`, `presets/*.css`, `tools/*.py` and other executable source | `Unlicense` | [Unlicense.txt](Unlicense.txt) |
| `README.md`, `CONTRIBUTING.md`, `docs/*.md`, `prompts/*.md`, `prompts/*.json` (prompt prose), and explanatory prose elsewhere | `CC-BY-4.0` | [CC-BY-4.0.txt](CC-BY-4.0.txt) |
| `assets/**/*.svg`, original screenshots, and original illustration compositions | `CC-BY-4.0` | [CC-BY-4.0.txt](CC-BY-4.0.txt) |
| Attribution metadata and provenance records | `CC-BY-4.0` for authored prose; factual fields unrestricted where no rights subsist | [CC-BY-4.0.txt](CC-BY-4.0.txt) |

In an HTML file, executable markup and styling are under Unlicense; separately identified illustrations and substantial guide text retain their stated CC BY 4.0 terms. Prefer linked SVG files so this boundary stays clear. The root software dedication does not override this explicit CC BY designation for the guides, prompt prose, and artwork.

## Copyable credit

For documentation and artwork reuse, use:

```text
Uniflora Aesthetic Template v0.1, Uniflora contributors.
Code: Unlicense. Documentation and original motifs: CC BY 4.0.
License: https://creativecommons.org/licenses/by/4.0/
Source: https://github.com/sporemound/uniflora-aesthetic-kit
Changes: [describe your changes, or state "unmodified"]
```

Code attribution is optional under Unlicense. Keeping its dedication with redistributed source communicates the terms, but is not an attribution condition. For CC BY material, retain the supplied credit and license reference and indicate changes. Do not claim endorsement by Uniflora or a referenced artist.

`CC-BY-4.0.txt` contains the complete English plain-text legal code retrieved from Creative Commons on 2026-10-10 UTC. The legal-code text itself carries Creative Commons' CC0 dedication in its footer. `Unlicense.txt` matches the existing root dedication. AI assistance is disclosed in the attribution register; these terms do not assert copyright protection for AI-assisted expression in every jurisdiction.

===== END FILE snapshot/licenses/README.md =====

===== BEGIN FILE snapshot/licenses/Unlicense.txt =====
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>

===== END FILE snapshot/licenses/Unlicense.txt =====

===== BEGIN FILE snapshot/presets/tokens.css =====
/* SPDX-License-Identifier: Unlicense
   New v0.1 proposal. No fonts are bundled or fetched. */
:root {
  --uf-font-body: system-ui, sans-serif;
  --uf-font-display: ui-serif, serif;
  --uf-font-mono: ui-monospace, monospace;
  --uf-space-sm: .5rem;
  --uf-space-md: 1rem;
  --uf-space-lg: 2rem;
  --uf-bg: #F7F2E8;
  --uf-surface: #FFFCF5;
  --uf-text: #282E29;
  --uf-muted: #606B5C;
  --uf-accent: #385B45;
  --uf-decor: #A4AE95;
  --uf-heading: var(--uf-font-display);
}
[data-uniflora="isometric-idm"] {
  --uf-bg: #092E2C;
  --uf-surface: #123D35;
  --uf-text: #F4F1DC;
  --uf-muted: #A4C4B6;
  --uf-accent: #63DDC8;
  --uf-decor: #1F5F46;
  --uf-heading: ui-monospace, monospace;
}
[data-uniflora="engraved-architecture"] {
  --uf-bg: #F3ECD9;
  --uf-surface: #FBF7ED;
  --uf-text: #201E1A;
  --uf-muted: #635D53;
  --uf-accent: #7A5523;
  --uf-decor: #201E1A;
  --uf-heading: ui-serif, serif;
}
[data-uniflora="crt-worlds"] {
  --uf-bg: #071C1A;
  --uf-surface: #123D35;
  --uf-text: #EDF9E8;
  --uf-muted: #9BC4B2;
  --uf-accent: #65F1E8;
  --uf-decor: #F99CE6;
  --uf-heading: ui-monospace, monospace;
}
[data-uniflora="nocturnal-optics"] {
  --uf-bg: #101C2B;
  --uf-surface: #1D2B3C;
  --uf-text: #EEF0F6;
  --uf-muted: #B5BCCB;
  --uf-accent: #8AD9CE;
  --uf-decor: #C5B8DE;
  --uf-heading: ui-serif, serif;
}
[data-uniflora="kilim-burdock"] {
  --uf-bg: #F1E5CF;
  --uf-surface: #FAF3E6;
  --uf-text: #402A28;
  --uf-muted: #715450;
  --uf-accent: #28635D;
  --uf-decor: #8E392C;
  --uf-heading: system-ui, sans-serif;
}
[data-uniflora="botanical-specimen"] {
  --uf-bg: #F7F2E8;
  --uf-surface: #FFFCF5;
  --uf-text: #282E29;
  --uf-muted: #606B5C;
  --uf-accent: #385B45;
  --uf-decor: #A4AE95;
  --uf-heading: ui-serif, serif;
}


===== END FILE snapshot/presets/tokens.css =====

===== BEGIN FILE snapshot/presets/tokens.json =====
{
  "version": "0.1.0",
  "status": "review draft",
  "provenance": "New v0.1 proposals; exact values are not historical requirements.",
  "fonts": {
    "body": "system-ui, sans-serif",
    "display": "ui-serif, serif",
    "mono": "ui-monospace, monospace"
  },
  "bundledFonts": [],
  "spacing": {
    "small": "0.5rem",
    "medium": "1rem",
    "large": "2rem"
  },
  "branches": {
    "isometric-idm": {
      "roles": {
        "bg": "#092E2C",
        "surface": "#123D35",
        "text": "#F4F1DC",
        "muted": "#A4C4B6",
        "accent": "#63DDC8",
        "decor": "#1F5F46"
      },
      "palette": {
        "forest": "#1F5F46",
        "turquoise": "#63DDC8",
        "ivory": "#F4F1DC"
      },
      "displayFont": "ui-monospace, monospace"
    },
    "engraved-architecture": {
      "roles": {
        "bg": "#F3ECD9",
        "surface": "#FBF7ED",
        "text": "#201E1A",
        "muted": "#635D53",
        "accent": "#7A5523",
        "decor": "#201E1A"
      },
      "palette": {
        "ink": "#201E1A",
        "ivory": "#F3ECD9",
        "gold": "#7A5523"
      },
      "displayFont": "ui-serif, serif"
    },
    "crt-worlds": {
      "roles": {
        "bg": "#071C1A",
        "surface": "#123D35",
        "text": "#EDF9E8",
        "muted": "#9BC4B2",
        "accent": "#65F1E8",
        "decor": "#F99CE6"
      },
      "palette": {
        "cyan": "#65F1E8",
        "magenta": "#F99CE6",
        "forest": "#123D35"
      },
      "displayFont": "ui-monospace, monospace"
    },
    "nocturnal-optics": {
      "roles": {
        "bg": "#101C2B",
        "surface": "#1D2B3C",
        "text": "#EEF0F6",
        "muted": "#B5BCCB",
        "accent": "#8AD9CE",
        "decor": "#C5B8DE"
      },
      "palette": {
        "silver": "#EEF0F6",
        "lavender": "#C5B8DE",
        "teal": "#8AD9CE",
        "pink": "#E6B6CD",
        "gold": "#D8C08E",
        "ivory": "#F4F1DC"
      },
      "displayFont": "ui-serif, serif"
    },
    "kilim-burdock": {
      "roles": {
        "bg": "#F1E5CF",
        "surface": "#FAF3E6",
        "text": "#402A28",
        "muted": "#715450",
        "accent": "#28635D",
        "decor": "#8E392C"
      },
      "palette": {
        "rust": "#8E392C",
        "teal": "#28635D",
        "gold": "#86682A"
      },
      "displayFont": "system-ui, sans-serif"
    },
    "botanical-specimen": {
      "roles": {
        "bg": "#F7F2E8",
        "surface": "#FFFCF5",
        "text": "#282E29",
        "muted": "#606B5C",
        "accent": "#385B45",
        "decor": "#A4AE95"
      },
      "palette": {
        "paper": "#F7F2E8",
        "green": "#385B45",
        "ivory": "#FFFCF5"
      },
      "displayFont": "ui-serif, serif"
    }
  }
}

===== END FILE snapshot/presets/tokens.json =====

===== BEGIN FILE snapshot/prompts/examples.json =====
{
  "version": "0.1.0",
  "record_type": "prompt-examples",
  "status": "new-proposal",
  "instructions": [
    "All subjects, palettes, lettering, and compositions are editable proposals, not universal requirements.",
    "Use the prompt field values as a provider-neutral drawing or image-generation brief; metadata is not visible text.",
    "Subject preservation and documented botanical accuracy take precedence over added visual effects."
  ],
  "examples": [
    {
      "id": "remote-listening",
      "title": "Remote listening",
      "status": "new-proposal",
      "subject": {
        "description": "Two remote listening stations exchanging a short rhythmic sequence.",
        "meaning_to_preserve": "Reciprocal attention across distance, with telepathy represented as a visual metaphor.",
        "invariant_features": [
          "Two equally important remote stations",
          "Small speaker and four-step indicator at each station",
          "Matching rhythmic sequence"
        ]
      },
      "branch": "isometric-idm",
      "medium": "16-bit-inspired pixel illustration for a square album-cover study.",
      "composition": "Two raised isometric forest-floor platforms occupy opposite corners, separated by a broad dark diagonal gap. Equal four-step sequences mirror across that gap; a single inverted plane appears below the right platform. Keep one bounded fourfold geometric structure behind the stations.",
      "palette": "Dominant deep green-teal #092E2C; supporting forest #1F5F46; turquoise #63DDC8 for sequence marks; ivory #F4F1DC for pale plant forms.",
      "optics": "None; use crisp pixel edges and an orthographic isometric projection.",
      "abstraction": "Telepathy is a visual metaphor of matching timing and mirrored intervals, without a literal beam, brain icon, or factual paranormal claim.",
      "text": {
        "mode": "none",
        "literal": "",
        "placement": "None; leave the upper-left margin quiet for optional later lettering.",
        "instructions": "No text is baked into this study. Any exact lettering is optional and should be added in a separate editable layer."
      },
      "exclusions": [
        "No generic occult symbols, noisy full-image kaleidoscope, cyberpunk city, mushrooms substituted for plants, or invented text."
      ],
      "biology": {
        "species": [
          "Monotropa uniflora"
        ],
        "life_stage": "Flowering",
        "traits_to_preserve": [
          "At each platform edge, a small flowering Monotropa uniflora group has pale stems, small scale leaves, and one nodding terminal flower per stem. This is an artistic pixel schematic, not a field-identification plate."
        ],
        "reference": "See docs/BOTANICAL-ACCURACY.md and its primary sources; check the produced image before making identification claims.",
        "status": "artistic-study-unverified",
        "instructions": "At each platform edge, a small flowering Monotropa uniflora group has pale stems, small scale leaves, and one nodding terminal flower per stem. This is an artistic pixel schematic, not a field-identification plate."
      },
      "motion": {
        "mode": "static",
        "duration_seconds": null,
        "allowed_changes": [],
        "locked_elements": [],
        "continuity": "Static; the repeat pattern itself supplies the sense of rhythm.",
        "accessibility": "Use a static default and reduced-motion version; any animation is opt-in and pausable, with no flashes or rapid hue oscillation."
      }
    },
    {
      "id": "impossible-library",
      "title": "Library with an impossible upper room",
      "status": "new-proposal",
      "subject": {
        "description": "A public library with books, reading desks, and three reading levels.",
        "meaning_to_preserve": "Welcoming civic access to reading spaces and one deliberate contradiction in access to knowledge.",
        "invariant_features": [
          "Books and reading desks",
          "Three reading levels",
          "A welcoming public library"
        ]
      },
      "branch": "engraved-architecture",
      "medium": "Black-and-ivory woodcut-style print for a portrait poster.",
      "composition": "A central Romanesque nave has rounded arches and heavy piers. One side stair reaches two incompatible upper rooms while the ground-floor desks remain spatially coherent. A narrow folded triangular surface crosses the upper-right vault. Project parallel lines across it: spacing compresses with foreshortening, direction changes at folds, and piers occlude the lines.",
      "palette": "Paper #F3ECD9 and ink #201E1A; a small ochre #7A5523 registration-like accent is optional and carries no archival or authenticity claim.",
      "optics": "None; use carved lines rather than photographic blur or lens effects.",
      "abstraction": "A single architectural contradiction conveys uncertain access to knowledge; repeated sharp modules suggest folded structure without claiming a foldable origami model.",
      "text": {
        "mode": "none",
        "literal": "",
        "placement": "None; retain a clean lower margin for an editable caption.",
        "instructions": "No text is baked into this study. Any exact lettering is optional and should be added in a separate editable layer."
      },
      "exclusions": [
        "No copied prints or origami diagrams, occult emblems, arbitrary noise, illegible pseudo-books, or global kaleidoscopic duplication."
      ],
      "biology": {
        "species": [],
        "life_stage": "Not specified",
        "traits_to_preserve": [
          "No identifiable plants requested; add no species claims."
        ],
        "reference": "No botanical specimen requested.",
        "status": "not-applicable",
        "instructions": "No identifiable plants requested; add no species claims."
      },
      "motion": {
        "mode": "static",
        "duration_seconds": null,
        "allowed_changes": [],
        "locked_elements": [],
        "continuity": "Static. Dense directional cross-hatching describes shadow and planes; leave the caption margin unhatched.",
        "accessibility": "Use a static default and reduced-motion version; any animation is opt-in and pausable, with no flashes or rapid hue oscillation."
      }
    },
    {
      "id": "fixed-crt-spring",
      "title": "Spring inside a fixed CRT display",
      "status": "new-proposal",
      "subject": {
        "description": "A small forest spring flowing past fallen wood under a crescent moon.",
        "meaning_to_preserve": "Continuity of a quiet forest spring within a fixed display.",
        "invariant_features": [
          "Same spring, banks, logs, moon, and plants",
          "Fixed camera and display border",
          "Continuous terrain and object identity"
        ]
      },
      "branch": "crt-worlds",
      "medium": "Sega Genesis-like pixel scene displayed within a plain fixed CRT border; an optional eight-second continuous loop with a static first frame.",
      "composition": "A low woodland viewpoint layers the near bank, spring, and distant trunks. The border and camera never move. Water shifts inside the spring and a small patch of mist drifts inside the display; existing objects do not change location and the loop endpoint matches its beginning.",
      "palette": "Dark forest #071C1A and green shadows #123D35; cyan #65F1E8 water highlights, magenta #F99CE6 in one restrained luminous patch, ivory #EDF9E8.",
      "optics": "Stable low-opacity scanlines and slight static chroma displacement, confined to the image inside the display; the border remains clean.",
      "abstraction": "Bioluminescent color is speculative lighting, not a biological claim. Keep the forest recognizable beneath the display treatment.",
      "text": {
        "mode": "none",
        "literal": "",
        "placement": "None. Any later player controls remain sharp outside the image.",
        "instructions": "No text is baked into this study. Any exact lettering is optional and should be added in a separate editable layer."
      },
      "exclusions": [
        "No copied game sprites or logos, camera drift, cuts, zooms, new objects, border warping, flashes, rapid hue oscillation, or scene replacement."
      ],
      "biology": {
        "species": [
          "Monotropa uniflora"
        ],
        "life_stage": "Flowering",
        "traits_to_preserve": [
          "Flowering Monotropa uniflora grows on the wooded humus bank, away from open water, with pale scale-leaved stems and one nodding flower each."
        ],
        "reference": "See docs/BOTANICAL-ACCURACY.md and its primary sources; check the produced image before making identification claims.",
        "status": "artistic-study-unverified",
        "instructions": "Flowering Monotropa uniflora grows on the wooded humus bank, away from open water, with pale scale-leaved stems and one nodding flower each."
      },
      "motion": {
        "mode": "optional-continuous-loop",
        "duration_seconds": 8,
        "allowed_changes": [
          "Restrained water movement inside the spring",
          "A small drifting patch of mist inside the display"
        ],
        "locked_elements": [
          "Camera",
          "Display border",
          "Terrain",
          "Existing logs and plants",
          "Moon position",
          "Scene identity"
        ],
        "continuity": "Optional, restrained, and pausable. Provide the static image as the default and for reduced-motion viewing. All changes stay inside the display.",
        "accessibility": "Use a static default and reduced-motion version; any animation is opt-in and pausable, with no flashes or rapid hue oscillation."
      }
    },
    {
      "id": "garden-crossing",
      "title": "A quiet garden crossing",
      "status": "new-proposal",
      "subject": {
        "description": "A narrow moonlit garden path crossing a shallow stone-lined stream.",
        "meaning_to_preserve": "A calm garden encounter with a path continuing beyond the visible focal plane.",
        "invariant_features": [
          "A walkable garden path",
          "A shallow stone-lined stream crossing",
          "A quiet encounter"
        ]
      },
      "branch": "nocturnal-optics",
      "medium": "Photographic-style landscape image for a website's introductory panel.",
      "composition": "The wet foreground stepping stone is crisp, while the garden behind it recedes into mist. Leave a darker quiet region on the left for separate live website text. Show a small patch of lichen on the stone edge.",
      "palette": "Midnight #101C2B, silver-ivory #EEF0F6, restrained teal #8AD9CE; one lavender #C5B8DE reflection, with pink and gold omitted in this brief.",
      "optics": "Shallow depth of field centered on the stone; a modest horizontal anamorphic highlight from reflected moonlight; refraction only in visible water droplets and along the shallow water surface.",
      "abstraction": "An unseen garden is conveyed by partially occluded distances and a path continuing beyond the focal plane, without symbolic decorations.",
      "text": {
        "mode": "none",
        "literal": "",
        "placement": "None in the image; add accessible editable HTML text separately.",
        "instructions": "No text is baked into this study. Any exact lettering is optional and should be added in a separate editable layer."
      },
      "exclusions": [
        "No obligatory ghost pipe or mushrooms, bright neon signage, full-frame lens flare, pseudo-script, or random glass overlays."
      ],
      "biology": {
        "species": [],
        "life_stage": "Not specified",
        "traits_to_preserve": [
          "The lichen is illuminated by reflected moonlight, not claimed to emit light. Garden foliage remains morphologically coherent; if a species is made identifiable during production, record and verify it before release."
        ],
        "reference": "See docs/BOTANICAL-ACCURACY.md and its primary sources; check the produced image before making identification claims.",
        "status": "artistic-study-unverified",
        "instructions": "The lichen is illuminated by reflected moonlight, not claimed to emit light. Garden foliage remains morphologically coherent; if a species is made identifiable during production, record and verify it before release."
      },
      "motion": {
        "mode": "static",
        "duration_seconds": null,
        "allowed_changes": [],
        "locked_elements": [],
        "continuity": "Static. Do not make text legibility depend on moving mist or bokeh.",
        "accessibility": "Use a static default and reduced-motion version; any animation is opt-in and pausable, with no flashes or rapid hue oscillation."
      }
    },
    {
      "id": "reversible-seed-card",
      "title": "Reversible seed-exchange card",
      "status": "new-proposal",
      "subject": {
        "description": "A printable invitation card for a community seed exchange.",
        "meaning_to_preserve": "A practical community seed-exchange invitation with reversible ornamental geometry.",
        "invariant_features": [
          "Invitation purpose for a community seed exchange",
          "Plain readable text area",
          "Reversible ornament with two usable orientations"
        ]
      },
      "branch": "kilim-burdock",
      "medium": "Flat textile-inspired graphic intended to be redrawn as editable vector geometry; this generated study itself does not guarantee vector source.",
      "composition": "A centered diamond-and-hook ornament has 180-degree rotational balance. Stepped border repeats use equal opposing offsets. Keep the middle reading field plain. The ornament is reversible; text belongs on a separate card face or in two clearly separated opposite-facing text zones.",
      "palette": "Warm ivory #F1E5CF, brown-black #402A28, rust #8E392C, and dark teal #28635D; omit the optional gold for a simple three-ink print treatment.",
      "optics": "None; maintain flat geometry and crisp, scalable edges.",
      "abstraction": "Burdock's hooked forms become new hooked turns in a repeated geometric vocabulary. This is a new interpretation, with no assigned traditional, regional, spiritual, or protective meaning.",
      "text": {
        "mode": "none",
        "literal": "",
        "placement": "None in the study. Optional separate literal: \"SEED EXCHANGE\". Do not invent dates, venues, instructions, or additional slogans.",
        "instructions": "No text is baked into this study. Any exact lettering is optional and should be added in a separate editable layer.",
        "optional_literal": "SEED EXCHANGE"
      },
      "exclusions": [
        "No copied historical textile, unverified cultural attribution, crowded text on patterned ground, or off-center central emblem."
      ],
      "biology": {
        "species": [],
        "life_stage": "Not specified",
        "traits_to_preserve": [
          "No botanical specimen is depicted. Geometric hooks are decorative cues and do not claim to be a diagnostic drawing of Arctium lappa."
        ],
        "reference": "No botanical specimen requested.",
        "status": "not-applicable",
        "instructions": "No botanical specimen is depicted. Geometric hooks are decorative cues and do not claim to be a diagnostic drawing of Arctium lappa."
      },
      "motion": {
        "mode": "static",
        "duration_seconds": null,
        "allowed_changes": [],
        "locked_elements": [],
        "continuity": "Static; review at both 0 and 180 degrees and at the final print size.",
        "accessibility": "Use a static default and reduced-motion version; any animation is opt-in and pausable, with no flashes or rapid hue oscillation."
      }
    },
    {
      "id": "ghost-pipe-observation",
      "title": "Ghost-pipe observation plate",
      "status": "new-proposal",
      "subject": {
        "description": "An observation plate of Monotropa uniflora, showing a flowering whole-plant study and a separate fruiting detail.",
        "meaning_to_preserve": "Careful botanical observation without invented specimen data or unverified identification claims.",
        "invariant_features": [
          "Recognizable Monotropa uniflora",
          "Separated flowering and fruiting stages",
          "Space for verified annotations"
        ]
      },
      "branch": "botanical-specimen",
      "medium": "Restrained pen-and-watercolor botanical illustration for a portrait poster, with a crop suitable for an album cover.",
      "composition": "A small flowering cluster occupies the left two-thirds. One isolated fruiting detail sits at upper right with generous separation. Reserve an untextured lower margin for editable labels added after review.",
      "palette": "Warm paper #F7F2E8, ink #282E29, quiet gray-green #606B5C, and deep green #385B45 only for later labels or layout; keep the plant itself pale.",
      "optics": "None; maintain crisp observable edges without photographic bokeh.",
      "abstraction": "Minimal; simplify paper texture, not diagnostic plant anatomy.",
      "text": {
        "mode": "none",
        "literal": "",
        "placement": "None. Add the checked scientific name and labels later as editable text.",
        "instructions": "No text is baked into this study. Any exact lettering is optional and should be added in a separate editable layer."
      },
      "exclusions": [
        "No invented collection number, locality, scale, root-network diagram, mushroom cap, green foliage, ornamental glow, or occult decoration."
      ],
      "biology": {
        "species": [
          "Monotropa uniflora"
        ],
        "life_stage": "Flowering and separate fruiting detail",
        "traits_to_preserve": [
          "This is a mycoheterotrophic flowering plant with pale fleshy stems, small scale leaves, and one nodding terminal flower per flowering stem. The separate fruiting detail becomes upright. Consult botanical references before adding diagnostic claims. Treat the initial image as an artistic study until its anatomy has been checked; it is not an identification tool."
        ],
        "reference": "See docs/BOTANICAL-ACCURACY.md and its primary sources; check the produced image before making identification claims.",
        "status": "artistic-study-unverified",
        "instructions": "This is a mycoheterotrophic flowering plant with pale fleshy stems, small scale leaves, and one nodding terminal flower per flowering stem. The separate fruiting detail becomes upright. Consult botanical references before adding diagnostic claims. Treat the initial image as an artistic study until its anatomy has been checked; it is not an identification tool."
      },
      "motion": {
        "mode": "static",
        "duration_seconds": null,
        "allowed_changes": [],
        "locked_elements": [],
        "continuity": "Static; specimen detail should remain visible when enlarged.",
        "accessibility": "Use a static default and reduced-motion version; any animation is opt-in and pausable, with no flashes or rapid hue oscillation."
      }
    }
  ]
}

===== END FILE snapshot/prompts/examples.json =====

===== BEGIN FILE snapshot/prompts/examples.md =====
# Six different example briefs

All six are new v0.1 proposals. They vary the subject, medium, perspective, composition, and texture; they are not a progression toward one canonical image. The palette choices and any text apply only to the individual example. Copy a brief, change its subject and invariants first, then adjust its treatment.

## 1. Remote listening · `isometric-idm`

```text
SUBJECT: Two remote listening stations exchanging a short rhythmic sequence.
Preserve the idea of reciprocal attention across distance and two equally
important stations, each with a small speaker and a four-step indicator.
BRANCH: isometric-idm.
MEDIUM: 16-bit-inspired pixel illustration for a square album-cover study.
COMPOSITION: Two raised isometric forest-floor platforms occupy opposite
corners, separated by a broad dark diagonal gap. Equal four-step sequences
mirror across that gap; a single inverted plane appears below the right
platform. Keep one bounded fourfold geometric structure behind the stations.
PALETTE: Dominant deep green-teal #092E2C; supporting forest #1F5F46;
turquoise #63DDC8 for sequence marks; ivory #F4F1DC for pale plant forms.
OPTICS: None; use crisp pixel edges and an orthographic isometric projection.
ABSTRACTION: Telepathy is a visual metaphor of matching timing and mirrored
intervals, without a literal beam, brain icon, or factual paranormal claim.
TEXT: None; leave the upper-left margin quiet for optional later lettering.
EXCLUSIONS: No generic occult symbols, noisy full-image kaleidoscope,
cyberpunk city, mushrooms substituted for plants, or invented text.
BIOLOGY: At each platform edge, a small flowering Monotropa uniflora group
has pale stems, small scale leaves, and one nodding terminal flower per stem.
This is an artistic pixel schematic, not a field-identification plate.
MOTION: Static; the repeat pattern itself supplies the sense of rhythm.
```

## 2. Library with an impossible upper room · `engraved-architecture`

```text
SUBJECT: A public library with books, reading desks, and three reading levels.
Preserve its welcoming civic use and a legible sequence of reading spaces.
BRANCH: engraved-architecture.
MEDIUM: Black-and-ivory woodcut-style print for a portrait poster.
COMPOSITION: A central Romanesque nave has rounded arches and heavy piers.
One side stair reaches two incompatible upper rooms while the ground-floor
desks remain spatially coherent. A narrow folded triangular surface crosses
the upper-right vault. Project parallel lines across it: spacing compresses
with foreshortening, direction changes at folds, and piers occlude the lines.
PALETTE: Paper #F3ECD9 and ink #201E1A; a small ochre #7A5523 registration-like
accent is optional and carries no archival or authenticity claim.
OPTICS: None; use carved lines rather than photographic blur or lens effects.
ABSTRACTION: A single architectural contradiction conveys uncertain access
to knowledge; repeated sharp modules suggest folded structure without
claiming a foldable origami model.
TEXT: None; retain a clean lower margin for an editable caption.
EXCLUSIONS: No copied prints or origami diagrams, occult emblems, arbitrary
noise, illegible pseudo-books, or global kaleidoscopic duplication.
BIOLOGY: No identifiable plants requested; add no species claims.
MOTION: Static. Dense directional cross-hatching describes shadow and planes;
leave the caption margin unhatched.
```

## 3. Spring inside a fixed CRT display · `crt-worlds`

```text
SUBJECT: A small forest spring flowing past fallen wood under a crescent moon.
Preserve the same spring, banks, logs, moon, and plants throughout the scene.
BRANCH: crt-worlds.
MEDIUM: Sega Genesis-like pixel scene displayed within a plain fixed CRT
border; an optional eight-second continuous loop with a static first frame.
COMPOSITION: A low woodland viewpoint layers the near bank, spring, and
distant trunks. The border and camera never move. Water shifts inside the
spring and a small patch of mist drifts inside the display; existing objects
do not change location and the loop endpoint matches its beginning.
PALETTE: Dark forest #071C1A and green shadows #123D35; cyan #65F1E8 water
highlights, magenta #F99CE6 in one restrained luminous patch, ivory #EDF9E8.
OPTICS: Stable low-opacity scanlines and slight static chroma displacement,
confined to the image inside the display; the border remains clean.
ABSTRACTION: Bioluminescent color is speculative lighting, not a biological
claim. Keep the forest recognizable beneath the display treatment.
TEXT: None. Any later player controls remain sharp outside the image.
EXCLUSIONS: No copied game sprites or logos, camera drift, cuts, zooms, new
objects, border warping, flashes, rapid hue oscillation, or scene replacement.
BIOLOGY: Flowering Monotropa uniflora grows on the wooded humus bank, away
from open water, with pale scale-leaved stems and one nodding flower each.
MOTION: Optional, restrained, and pausable. Provide the static image as the
default and for reduced-motion viewing. All changes stay inside the display.
```

## 4. A quiet garden crossing · `nocturnal-optics`

```text
SUBJECT: A narrow moonlit garden path crossing a shallow stone-lined stream.
Preserve the walkable path, the crossing, and the sense of a quiet encounter.
BRANCH: nocturnal-optics.
MEDIUM: Photographic-style landscape image for a website's introductory panel.
COMPOSITION: The wet foreground stepping stone is crisp, while the garden
behind it recedes into mist. Leave a darker quiet region on the left for
separate live website text. Show a small patch of lichen on the stone edge.
PALETTE: Midnight #101C2B, silver-ivory #EEF0F6, restrained teal #8AD9CE;
one lavender #C5B8DE reflection, with pink and gold omitted in this brief.
OPTICS: Shallow depth of field centered on the stone; a modest horizontal
anamorphic highlight from reflected moonlight; refraction only in visible
water droplets and along the shallow water surface.
ABSTRACTION: An unseen garden is conveyed by partially occluded distances
and a path continuing beyond the focal plane, without symbolic decorations.
TEXT: None in the image; add accessible editable HTML text separately.
EXCLUSIONS: No obligatory ghost pipe or mushrooms, bright neon signage,
full-frame lens flare, pseudo-script, or random glass overlays.
BIOLOGY: The lichen is illuminated by reflected moonlight, not claimed to
emit light. Garden foliage remains morphologically coherent; if a species
is made identifiable during production, record and verify it before release.
MOTION: Static. Do not make text legibility depend on moving mist or bokeh.
```

## 5. Reversible seed-exchange card · `kilim-burdock`

```text
SUBJECT: A printable invitation card for a community seed exchange.
Preserve its practical purpose, a clear text area, and two usable orientations.
BRANCH: kilim-burdock.
MEDIUM: Flat textile-inspired graphic intended to be redrawn as editable
vector geometry; this generated study itself does not guarantee vector source.
COMPOSITION: A centered diamond-and-hook ornament has 180-degree rotational
balance. Stepped border repeats use equal opposing offsets. Keep the middle
reading field plain. The ornament is reversible; text belongs on a separate
card face or in two clearly separated opposite-facing text zones.
PALETTE: Warm ivory #F1E5CF, brown-black #402A28, rust #8E392C, and dark teal
#28635D; omit the optional gold for a simple three-ink print treatment.
OPTICS: None; maintain flat geometry and crisp, scalable edges.
ABSTRACTION: Burdock's hooked forms become new hooked turns in a repeated
geometric vocabulary. This is a new interpretation, with no assigned
traditional, regional, spiritual, or protective meaning.
TEXT: None in the study. Optional separate literal: "SEED EXCHANGE".
Do not invent dates, venues, instructions, or additional slogans.
EXCLUSIONS: No copied historical textile, unverified cultural attribution,
crowded text on patterned ground, or off-center central emblem.
BIOLOGY: No botanical specimen is depicted. Geometric hooks are decorative
cues and do not claim to be a diagnostic drawing of Arctium lappa.
MOTION: Static; review at both 0 and 180 degrees and at the final print size.
```

## 6. Ghost-pipe observation plate · `botanical-specimen`

```text
SUBJECT: An observation plate of Monotropa uniflora, showing a flowering
whole-plant study and a separate fruiting detail. Preserve the recognizable
plant, the separation of life stages, and space for verified annotations.
BRANCH: botanical-specimen.
MEDIUM: Restrained pen-and-watercolor botanical illustration for a portrait
poster, with a crop suitable for an album cover.
COMPOSITION: A small flowering cluster occupies the left two-thirds. One
isolated fruiting detail sits at upper right with generous separation.
Reserve an untextured lower margin for editable labels added after review.
PALETTE: Warm paper #F7F2E8, ink #282E29, quiet gray-green #606B5C, and deep
green #385B45 only for later labels or layout; keep the plant itself pale.
OPTICS: None; maintain crisp observable edges without photographic bokeh.
ABSTRACTION: Minimal; simplify paper texture, not diagnostic plant anatomy.
TEXT: None. Add the checked scientific name and labels later as editable text.
EXCLUSIONS: No invented collection number, locality, scale, root-network
diagram, mushroom cap, green foliage, ornamental glow, or occult decoration.
BIOLOGY: This is a mycoheterotrophic flowering plant with pale fleshy stems,
small scale leaves, and one nodding terminal flower per flowering stem.
The separate fruiting detail becomes upright. Consult botanical references
before adding diagnostic claims. Treat the initial image as an artistic
study until its anatomy has been checked; it is not an identification tool.
MOTION: Static; specimen detail should remain visible when enlarged.
```

The JSON versions retain the same instructions as editable records in [examples.json](examples.json). Record any changes to the subject, botanical reference, text, or motion boundary alongside a result so that later variations preserve the intended meaning.

===== END FILE snapshot/prompts/examples.md =====

===== BEGIN FILE snapshot/prompts/template.json =====
{
  "version": "0.1.0",
  "record_type": "prompt-template",
  "status": "new-proposal",
  "instructions": [
    "Replace placeholders with the chosen subject and its invariants before changing style.",
    "Use the prompt fields as a drawing brief or provider-neutral image prompt. Metadata is not visible image text.",
    "Choose one primary branch; a secondary material must not replace the subject or primary structure.",
    "The palette and lettering are choices for this brief, not universal Uniflora requirements.",
    "Verify plant anatomy and exact text after production. Generated raster output is not automatically editable vector source.",
    "Scope every exclusion to its brief. A logo's rejection of simulated glitch does not prohibit CRT distortion."
  ],
  "allowed_branches": [
    "isometric-idm",
    "engraved-architecture",
    "crt-worlds",
    "nocturnal-optics",
    "kilim-burdock",
    "botanical-specimen"
  ],
  "prompt": {
    "subject": {
      "description": "[specific subject, setting, and action]",
      "meaning_to_preserve": "[what the subject communicates]",
      "invariant_features": [
        "[recognizable feature 1]",
        "[recognizable feature 2]"
      ]
    },
    "branch": "isometric-idm",
    "medium": "[medium, aspect ratio, intended size, and use]",
    "composition": "[focal point, projection, spatial layers or flat hierarchy, negative space, symmetry or inversion, and crop]",
    "palette": "[dominant, supporting, and accent colors; note where accents are confined]",
    "optics": "[none, or a specific optical treatment tied to a visible material and focal relationship]",
    "abstraction": "[abstract concept translated into repeat interval, mirrored relationship, offset, layer reveal, or local spatial contradiction; distinguish literal from schematic]",
    "text": {
      "mode": "none",
      "literal": "",
      "placement": "[optional reserved area for later editable text]",
      "instructions": "Use mode none or literal. When literal, fill the exact string and verify every character; a separate editable text layer is preferred."
    },
    "exclusions": [
      "Do not replace the subject with generic occult marks, cyberpunk decoration, unmotivated noise, or a default glowing-mushroom scene.",
      "[additional exclusion and its local reason]"
    ],
    "biology": {
      "species": [],
      "life_stage": "[if relevant]",
      "traits_to_preserve": [],
      "reference": "[verified source and date, or no identifiable plants requested]",
      "status": "artistic-study-unverified",
      "instructions": "Identifiable plants require reference-checked morphology. Label simplified work schematic; do not use an unchecked illustration for field identification."
    },
    "motion": {
      "mode": "static",
      "duration_seconds": null,
      "allowed_changes": [],
      "locked_elements": [],
      "continuity": "[for animation: preserve existing objects and scene identity; matching loop endpoint if required]",
      "accessibility": "Provide a static alternative and pause control when animated; respect reduced motion; no flashes or rapid hue oscillation."
    }
  }
}

===== END FILE snapshot/prompts/template.json =====

===== BEGIN FILE snapshot/prompts/TEMPLATE.md =====
# Platform-neutral image-prompt template

Use this as a drawing brief or as plain text in an image-generation system. It contains no provider-specific commands and requires no subscription. Generation is optional: the same brief can guide a hand-drawn, pixel, vector, photographic, or mixed-media work. An image result is not automatically an editable vector or a scientifically checked illustration.

The subject is the invariant. Uniflora supplies form, materials, rhythm, and spatial relationships around it. Choose one primary branch; do not silently replace the chosen subject with a standard ghost-pipe scene.

## Copyable scaffold

```text
SUBJECT
Depict: [specific subject, setting, and action].
Meaning to preserve: [what this subject communicates].
Invariant features: [two or three features that must survive stylization].

BRANCH
[isometric-idm | engraved-architecture | crt-worlds | nocturnal-optics |
 kilim-burdock | botanical-specimen].
Apply the selected branch to the subject. [Optional: one secondary material
from another branch, without changing the subject or primary structure.]

MEDIUM
[pixel illustration | engraved print | textile-inspired vector graphic |
 photographic image | botanical pen/watercolor plate | other].
[Aspect ratio, intended viewing size, and output use.]

COMPOSITION
[Focal point, foreground/middle/background or flat hierarchy, projection,
 negative space, axis of symmetry or inversion, and crop.]
[State how any projected lines respond to folds, curvature, and occlusion.]

PALETTE
[Named colors or editable hex values, with dominant/secondary/accent roles.]
[Describe where strong accents are confined. These are choices for this brief.]

OPTICS
[None, or a specific depth-of-field/refraction/anamorphic treatment.]
[Explain which material or focal relationship motivates the optical effect.]

ABSTRACTION
[Concept] becomes [a visible relationship: repeat interval, mirrored pair,
 offset, layer reveal, local spatial contradiction, or changed scale].
[Specify what stays literal and what is schematic or speculative.]

TEXT
[None, or the exact literal string in quotation marks.]
[Position and size if used. For precise wording, reserve space and add a
 separate editable text layer after generation; do not invent filler text.]

EXCLUSIONS
[List exclusions for this specific brief, including why they apply.]
Do not replace the subject with generic occult marks, cyberpunk decoration,
 unmotivated noise, or a default glowing-mushroom scene.

BIOLOGY
[If a plant is identifiable: species, life stage, reference source, traits
 to preserve, and whether this is an artistic schematic or checked plate.]
[If absent: no identifiable plants requested; do not add species claims.]

MOTION
[Static, or describe bounded motions, timing, continuity, and a static alternative.]
[For a fixed display: camera and display border locked; all movement inside
 the display; existing terrain, objects, and scene identity remain continuous;
 no cuts, zooms, new objects, border movement, flashes, or rapid hue oscillation.]
```

## Field guidance

| Field | A useful answer | Avoid |
| --- | --- | --- |
| Subject | “A public library with three reading levels; preserve its civic use and books.” | “Uniflora vibes” with no actual subject. |
| Branch | One of the six IDs, plus any clearly bounded secondary material. | Merging all six branches into one overloaded image. |
| Medium | An engraved print, flat vector card, pixel scene, optical photograph, or specimen plate. | Asking a raster generator to prove it produced editable source. |
| Composition | A specific arrangement, projection, crop, or repeat interval. | A pile of aesthetic adjectives with no spatial plan. |
| Palette | Dominant, supporting, and restrained accent colors. | Treating the v0.1 hex values as universal requirements. |
| Optics | None, or an effect tied to a real material and focal plane. | Adding lens flare or blur to every branch. |
| Abstraction | “Two distant modules share a four-step rhythm across an empty gap.” | Claiming that the image demonstrates real telepathy. |
| Text | None, or an exact optional literal. | Automatic slogans, pseudo-script, or invented scientific labels. |
| Exclusions | A local constraint such as “no distortion because this commission is a small logo.” | Making that logo restriction prohibit distortion in the CRT branch. |
| Biology | Named taxon, life stage, anatomy, and verified reference. | Turning ghost pipe into a fungus or inventing morphology. |
| Motion | Static, or a bounded continuous loop with a static alternative. | Moving the display border or replacing the scene between frames. |

## Botanical minimum for ghost pipe

If requesting *Monotropa uniflora*, specify a mycoheterotrophic flowering plant, a pale fleshy stem with small scale leaves, and one terminal flower per flowering stem with a nodding posture. Keep flowering and upright fruiting stages separate. Do not make it a mushroom, add ordinary green foliage, or invent a direct tree-root feeding attachment. Consult [the botanical accuracy notes](../docs/BOTANICAL-ACCURACY.md) and their primary references before presenting a result as identification material.

Color effects can be artistic. “Cyan-magenta glow” does not mean real ghost pipe or lichen produces that light; record invented illumination as speculative. If the anatomy is too simplified to verify, label the result schematic.

## After generation or drawing

Check the invariants first. Then check anatomy, meaningful geometry, exact text, and any motion boundary. Regenerate or redraw the failing part instead of adding more effects. If the subject disappeared, simplify the treatment. Add exact text in an editable layer where possible, and preserve the brief and provenance with the finished asset.

Read [six contrasting examples](examples.md). [template.json](template.json) provides the same field structure for storage; [examples.json](examples.json) contains editable example records. Metadata in these JSON files is explanatory and should not be passed as visible image text.

===== END FILE snapshot/prompts/TEMPLATE.md =====

===== BEGIN FILE snapshot/README.md =====
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

===== END FILE snapshot/README.md =====

===== BEGIN FILE snapshot/tools/validate.py =====
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

===== END FILE snapshot/tools/validate.py =====
