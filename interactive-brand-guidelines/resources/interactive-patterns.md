# Interactive patterns — the "elevated" bar

Static screenshots are table stakes. These interactions are what separate this
from a one-pager. All are self-contained (no backend) and must degrade
gracefully.

## 1. Click-to-copy tokens

Every colour tile is a `<button>` that copies its value (hex or `rgba(...)`).
Show a transient "Copied" state without layout shift. Provide a
non-secure-context fallback so it works off `https`:

```ts
async function copy(text: string) {
  try {
    if (navigator.clipboard?.writeText) {
      await navigator.clipboard.writeText(text);
    } else {
      const ta = document.createElement('textarea');
      ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      document.execCommand('copy'); ta.remove();
    }
    // set a self-resetting "copied" flag for UI feedback
  } catch { /* leave value visible so the user can select it manually */ }
}
```

Use the same pattern for prompt cards and any spec value.

## 2. Downloadable assets through the UI

Every logo, mark, logotype, insignia, and font row is a real `download` link or
a client-side `Blob` download. Ship a **single archive** (`press-kit.zip`) wired
to a persistent "Download all assets" action in the nav rail and hero. Rebuild
the archive whenever assets change. **Exclude licensed fonts** from the archive
and say so in its README.

Client-side Blob download:

```ts
function downloadSvg(svg: string, name: string) {
  const url = URL.createObjectURL(new Blob([svg], { type: 'image/svg+xml' }));
  const a = document.createElement('a');
  a.href = url; a.download = name; a.click();
  URL.revokeObjectURL(url);
}
```

## 3. Live generator (when the brand has a generative system)

If the brand has a combinatorial supporting-graphic system (an icon alphabet, a
pattern grammar, a badge builder), build a generator: compose within the
documented rules, preview live, and download the result as a standalone SVG
assembled client-side. **Enforce the brand's own constraints in the UI** (e.g.
"3–5 segments, once per surface"). Offer a second mode where useful (e.g. type a
word → set it in the icon alphabet).

Layout follows the product's panel pattern: flexible full-width surface,
mode/composition controls on the **top edge**, the composition centred, and the
usage rule + download action pinned to the **bottom edge**.

When assembling a multi-piece SVG, **namespace every `id`** (clip paths,
gradients) per piece so repeated elements don't collide in one document.

## 4. Copy as Markdown (llms.txt-style)

Add a **"Copy as Markdown"** button beside the archive download. Serialise the
*same data module the page renders* into a structured Markdown document — every
section, hex, type-scale row, prompt, and asset URL. This makes the guidelines
consumable by LLMs and docs tools, and because it is generated from the data
module it can never drift from the visible page. A now-common, expected
affordance for documentation surfaces.

## 5. Motion, honestly

Animate motion-token demos, but gate every scroll/idle/drag animation on
`prefers-reduced-motion` and render the final state when reduced.
