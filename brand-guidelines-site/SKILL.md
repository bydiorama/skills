---
name: brand-guidelines-site
description: >
  Build a brand-guidelines WEB PAGE by extracting the real brand system from live
  sources — a website's CSS, a Figma file, or a codebase's design tokens — and rendering
  a page that is styled IN the brand rather than merely describing it. Use when the user
  provides a website URL, a Figma link, or a product repo and asks to "generate brand
  guidelines", "build a brand guidelines site/page", "extract our brand", "make a brand
  one-pager", "document our colours and type from our site/Figma", "turn our Figma into a
  brand guide", or "add a brand page to our app". The defining signals are EXTRACTION FROM
  A SOURCE plus a RENDERED web output. Two output modes: a standalone one-page site, or an
  interactive guidelines route inside an existing product codebase. Do NOT use for writing
  a Markdown brand book with no extractable sources (use `brand-guidelines`), campaign
  briefs, or SEO style guides. Brand-agnostic.
---

# Brand Guidelines Site

Build a brand-guidelines page from the brand's **actual** system: the colours with their
real token names, the type scale, the logo and its variants, the button and card styles
that already ship. The page is set in the brand so it *demonstrates* the system rather
than describing it.

This is the extraction-and-rendering counterpart to `brand-guidelines`, which produces the
Markdown brand book. Reuse that skill for the canonical section order and content rules;
this one adds the source pipeline and the built page.

## Core rule

**Never guess a value.** Every hex, token name, radius, weight and spacing step comes out
of a source file — site CSS, Figma `get_design_context`, or the project's token module. If
a value cannot be extracted, say so and ask; do not approximate and move on.

## Pick the output mode first

| | **Mode A — Standalone one-pager** | **Mode B — In-product guidelines route** |
|---|---|---|
| Inputs | A live URL and/or a Figma file | A codebase with a token file and component library |
| Output | `index.html` + `styles.css` + `script.js`, no build step | A route/page inside the app, using its own components |
| Bar | Essentials, clean, self-contained | Indistinguishable from the product's marketing site |
| Sections | At-a-glance → Logo → Typography → Colour → Tone of voice | The full taxonomy below |

Mode B is only available when there is a real design system to inhabit. If the repo has no
token file or component library, it is a Mode A job — say so rather than inventing a
parallel visual language inside someone's app.

Confirm the mode, the document language, and the depth with one batched `AskUserQuestion`.

## Model-tier strategy

This work spans three kinds of labour. Assign each to the tier it fits.

| Phase | Work | Tier | Why |
|---|---|---|---|
| **Discover & architect** | Audit tokens, components, routing, asset tree; design the data model and section taxonomy; decide reuse vs build | Highest available | One wrong architectural call costs a whole round |
| **Author** | Section markup, the CSS module, copy in the brand voice, geometry generators | Strong coding model | Long, exacting generation once the data model is fixed |
| **Mechanical** | Asset zips, screenshot harnesses, lint/typecheck loops, bulk copy passes | Cheapest capable | High-volume and verifiable |

The first pass is the most expensive to get wrong. Everything downstream inherits the
discovery decisions; copy edits and rebuilds iterate cheaply.

## Procedure

### 1 — Gather sources

Collect what exists: live URL, Figma file URL **with a `node-id`**, font kit link, brand
name, and (Mode B) the repo path. If a Figma URL has no `node-id`, ask for a node-specific
link. Ask only for genuinely missing inputs.

### 2 — Extract ground truth

**From a live site** — fetch the page for positioning and tone, then `curl` it, grep for
stylesheet `<link>`s, and `curl` the main stylesheet. From that CSS pull the button rules
(radius, padding, colours, hover, shadow), card styles, the named colour scale, and
`font-family` declarations. Site CSS is authoritative for anything interactive.

**From Figma** — `get_metadata` for structure only, then `get_design_context` on **small
leaf nodes** (a heading, a stat, a button). Leaf nodes return real CSS *and* colours
carrying their Figma variable names (`var(--fawn,#F7B267)`); metadata returns no styles at
all. `get_screenshot` for visual reference.

**From a codebase** (Mode B) — read the token file and consume the **semantic** layer, not
the primitives. Inventory the components and reuse the real `Button`/`Text`/`Logo` rather
than restyling copies. Read the routing and asset registries before adding anything.

Reconcile the sources against each other and report any discrepancy rather than silently
picking one.

See `resources/pipeline.md` and `resources/extraction-playbook.md` for exact commands.

### 3 — Prepare logo assets

Download Figma assets **during the build** — the URLs expire in about a week. Files
labelled `.png` are often SVG; verify with `file` and rename.

Make recolourable copies by replacing `fill="var(--x,#hex)"` with `fill="currentColor"`,
then inline the paths as an SVG `<symbol>` sprite. **Inline `<symbol>` paths must carry a
fill** — with none they render black and ignore the CSS `color`, a silent and very common
bug.

Generate the lockup variants as self-contained SVGs: primary, reversed, mono, symbol-only.
**Logo colour rule:** the symbol keeps the accent colour in every variant; only the
wordmark text swaps for light and dark backgrounds. Build a favicon from the symbol and
tighten its padding until the mark reads at 16px.

### 4 — Model the data before building

Put every string, swatch, asset path and scale value in **one declarative data module**.
The page becomes pure composition over it, and the Markdown export serialises from the
same module — so the export can never drift from the page.

### 5 — Build

Take the section order from `brand-guidelines`. Mode A keeps to the essentials; Mode B uses
the full taxonomy:

1. **About / Principles** — the brand's logic as 2–4 named principles, in its voice
2. **Logo** — wordmark on a stage; clearspace, minimum size, one-colour, on-photography; downloadable variants
3. **Product & symbol** — the standalone mark: construction, usage, SVG + high-res raster
4. **Sub-brands** — product marks and logotype lockups, each downloadable, with usage rules
5. **Typography** — specimen per family, the full scale as a live specimen table, the hierarchy rule, font access
6. **Colour** — grouped swatches (foundation / accent / opacity steps), each click-to-copy, with contrast notes
7. **Supporting graphics** — any secondary geometric system: vocabulary, construction rule, downloadable set, and a live generator if it is generative
8. **Imagery** — art direction and on-brand-only examples, plus copyable prompt examples for generated imagery
9. **Interactive elements** — live demos of the real buttons, chips, indicators, and motion tokens as animated cards
10. **Layouts & surfaces** — the container/grid, spacing rhythm as a labelled bar chart, surface samples

Close with a full-archive download panel.

Define the palette and type scale as `:root` custom properties **mirroring the source token
names**. Reuse the real button and card styles. Add the interactive layer: click-to-copy
tokens with a visible affordance and a toast, per-asset and full-archive downloads,
scroll-spy on a numbered sidebar (sticky rail on desktop, chip row on mobile), and a "Copy
as Markdown" export.

See `resources/build-patterns.md`, `resources/interactive-patterns.md` and
`resources/geometry-systems.md`.

**Fonts, honestly.** Fetch the font-kit CSS to confirm the exact family slugs and the
weights actually available. If the kit lacks a design weight, render with what exists and
document intent versus availability. Always ship fallback stacks. **Licensed fonts are
listed, never distributed**; open-licensed fonts get real download links.

### 6 — Verify in a browser

Never claim done without this pass. Confirm: fonts load from the kit; every token shows the
correct hex and copy-to-clipboard works (including the non-secure-context fallback); logos
are crisp on light **and** dark; the favicon reads at 16px; the layout reflows at ~390px
with no horizontal overflow; contrast is sane. Mode B additionally: typecheck and lint pass,
asset endpoints resolve, and the archive rebuilds.

`resources/anti-footguns.md` lists the specific mistakes that cost review rounds.

## Design & voice standards

- **Reuse the source's patterns.** Never invent a parallel visual language.
- **Type carries hierarchy, not borders** — large headlines, high size contrast.
- **Microtypography**: consistent eyebrow/label treatment, tabular figures for specs, one
  separator convention (match the project), correct dashes and quotes.
- Design desktop **and** mobile from the start, not mobile as an afterthought.
- Write copy in the brand's own voice, drawn from its principles.
- Colour is for interactive and status elements; do not decorate with it.
- Flag gaps rather than hiding them — a missing weight or a low-contrast accent is
  information the brand owner needs.

## Reference bar

Study these before building, then exceed them with the interactive layer:
`devrev.standard-projects.com` (numbered sidebar manual, persistent asset download),
`brand.zapier.com/principles` (principle-led voice), `design.cash.app` (restraint,
type-driven hierarchy), `brandstandards.hermanmiller.com` (editorial rigour, do/don't
discipline).

## Output

**Mode A** — in the working directory:

```
index.html · styles.css · script.js · README.md
favicon.svg · favicon.ico
assets/   logo exports, colour-variant SVGs, favicon PNGs
```

**Mode B** — a route in the app, its data module, its styles, and the generated asset
archive, following the repo's existing conventions for each.

## Definition of done

Every value extracted, not guessed · buttons and cards match the source · logo colour logic
correct on both backgrounds · font weights confirmed and documented · inline SVGs recolour
correctly · copy-to-clipboard works · responsive with no overflow · no leftover `[brackets]`
or placeholder copy · verified in a real browser.

## Related skills

- `brand-guidelines` — the canonical section order and content rules this skill builds on
- `brand-strategy` — the strategy the About / Principles section should express
- `anti-skill` — review the built page before handover
