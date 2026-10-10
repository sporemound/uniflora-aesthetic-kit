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
