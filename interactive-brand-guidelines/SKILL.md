---
name: interactive-brand-guidelines
description: >
  Generate an ELEVATED, INTERACTIVE brand-guidelines page that lives INSIDE a
  product's own design system — not a generic one-pager. Use when a team has a
  real website, token file, and/or Figma brand deck and wants a guidelines
  surface that demonstrates the brand by being built in it: the dark-or-light
  system reused verbatim, click-to-copy colour tokens, downloadable
  logos/marks/fonts, reverse-engineered geometric systems (icon/insignia
  alphabets), live generators, and an llms.txt-style Markdown export. Distinct
  from a plain "brand one-pager": the bar here is a shipped page indistinguishable
  from the product's marketing site, reviewed against references like
  devrev.standard-projects.com, brand.zapier.com, design.cash.app, and
  brandstandards.hermanmiller.com. Brand-agnostic.
---

# Interactive Brand Guidelines

Build a brand-guidelines **page inside an existing product codebase** (or a
standalone app that mirrors one), at the quality bar of the best public brand
sites. The defining difference from a generic generator: **the page is not a
document about the brand, it is an instance of the brand.** Every surface,
token, type ramp, and motion value is the product's own, consumed from the same
source of truth the app uses. If a reviewer cannot tell the guidelines page
apart from the marketing site, the bar is met.

This SKILL.md is the operating procedure. Deep-dive references live in
`resources/` and are loaded on demand:

- `resources/pipeline.md` — the extraction → data-model → build → verify pipeline.
- `resources/interactive-patterns.md` — copy-to-clipboard, downloads, generators, Markdown export.
- `resources/geometry-systems.md` — reverse-engineering an icon/insignia alphabet or pattern grammar.
- `resources/anti-footguns.md` — the specific mistakes that cost review rounds.

---

## When this skill applies (and when it does not)

**Use it when** the inputs include at least one authoritative source of truth:

- A **codebase** with a design-token file (`tokens.css`, `theme.ts`, Tailwind
  config, Figma-exported variables) and a component library. This is the richest
  case — reuse beats extraction.
- A **Figma brand deck** (guidelines slides, a component page, brand variables).
- A **live site** whose CSS encodes the real buttons, cards, and palette.
- Supporting **PDFs / older brand documents** that describe systems the current
  files only partially encode (naming, geometry rules, do/don't).

**Do not use it for**: a from-scratch Markdown brand book with no extractable
sources (write prose instead), a marketing campaign brief, or an SEO style
guide. If there is no product design system to inhabit, this skill has nothing
to inhabit.

**The decisive signal**: the deliverable is a *rendered, interactive page in the
brand's own system*, not a description of it.

---

## Model-tier strategy (Fable / Opus / Sonnet)

Brand-guidelines work spans three very different kinds of labour. Assign each to
the tier it fits; do not run everything on one.

| Phase | Work | Best tier | Why |
|---|---|---|---|
| **Discover & architect** | Audit the token file, component inventory, routing, SEO registry, asset tree, and reference sites; design the data model, section taxonomy, and download/interaction contracts; decide what to reuse vs build | **Fable** | High-context reasoning over a whole codebase; one wrong architectural call (overwriting a shared asset, using the wrong token layer) costs a whole round |
| **Author** | Section markup, the large CSS module, copy in the brand voice, geometry generators | **Opus** | Long, exacting generation once the data model is fixed; benefits from the strongest coding model |
| **Mechanical** | Asset-zip assembly, screenshot harnesses, lint/typecheck loops, SEO/story boilerplate, bulk copy passes | **Sonnet** | Cheap, verifiable, high-volume; over-powered models waste budget here |

Practical rule: **the first pass is the most expensive to get wrong.** Spend the
most capable reasoning on discovery/architecture; everything downstream inherits
its decisions. Copy edits and zip rebuilds are Sonnet-cheap and iterate freely.

---

## Procedure (high level)

1. **Ground truth — never guess a value.** Read the token file (consume the
   *semantic* layer, not primitives), the component inventory (reuse the real
   `Button`/`Text`/`Logo`), the design doc, the asset tree, and the routing/SEO
   registries. Pull Figma tokens from *small leaf nodes*; screenshot brand
   slides. See `resources/pipeline.md`.
2. **Data model first.** Put every string, swatch, asset path, and scale value
   in one declarative data module. The page component is pure composition. This
   same module is what the Markdown export serialises from, so the export can
   never drift from the page.
3. **Build in the brand's system.** Sidebar numbered manual (sticky rail on
   desktop, sticky chip row on mobile), scroll-spy the active section, hairline
   separators, the product's own smooth-scroll and header offset.
4. **Add the interactive layer.** Click-to-copy tokens, per-asset + full-archive
   downloads, a live generator where the brand has a generative system, and a
   "Copy as Markdown" export. See `resources/interactive-patterns.md`.
5. **Verify, then ship.** Typecheck + lint; render in a real browser at
   ~1600/1024/390 px; exercise every interaction; check asset endpoints; rebuild
   the archive; re-review against the named reference sites; commit and open/​
   update the PR. Never claim done without the browser pass.

---

## Section taxonomy

Canonical order, adapted per brand. Add brand-specific sections (a company with a
supporting-graphic system needs a whole section for it).

1. **About / Principles** — the brand's logic as 2–4 named principles in the
   brand voice.
2. **Logo** — wordmark on a stage; clearspace / minimum-size / one-colour /
   on-photography rules; downloadable variants.
3. **Product & Symbol** — the standalone mark: construction + usage; SVG plus a
   high-res raster app-icon.
4. **Sub-brands** — product marks and **logotype lockups** (mark on its tile +
   name in the display face), each downloadable; usage rules.
5. **Typography** — typefaces (specimen per family), the full type scale as a
   live specimen table, the hierarchy/emphasis rule, font access. **Licensed
   fonts are listed but not distributed; open fonts get real download links.**
6. **Color** — grouped swatches (foundation / accent / opacity steps), each a
   **click-to-copy** tile, with contrast notes.
7. **Insignias / supporting graphics** — any geometric secondary system: the
   vocabulary, the construction rule, the downloadable set, and (if generative)
   an **interactive generator**.
8. **Imagery** — art-direction rules and *on-brand-only* example images, plus
   **copyable prompt examples** for generated imagery.
9. **Interactive elements** — live demos of the real buttons, chips, the "live"
   indicator, and motion tokens as animated cards.
10. **Layouts & surfaces** — the container/grid, the spacing rhythm as a labelled
    bar chart, and surface samples.

Close with a full-archive download panel.

---

## Design & voice standards

- **Reuse the site's patterns**; never invent a parallel visual language.
- **Microtypography**: consistent eyebrow/label treatment, tabular figures for
  specs, one separator convention (match the project — it may prefer `/` over
  `·`), correct dashes/quotes.
- **Large headlines, high size-contrast**: type carries hierarchy, not borders.
- **Numbers match labels**: in a numbered nav, index and label share a size
  unless the brand says otherwise.
- Design **both desktop and mobile** of the manual from the start.
- Write copy in the **brand's own voice**, pulled from its principles; terse and
  declarative if that is the brand. Use its two-tone emphasis device if it has
  one, and honour its rules.
- **Restrain em-dashes** — reviewers notice; prefer colons, commas, semicolons.
  Keep quoted source text verbatim.
- Colour is for interactive/status elements; do not decorate.

---

## Reference bar

Study these first; match their conventions, then exceed them with the
interactive layer (click-to-copy, live generator, Markdown export):

- `devrev.standard-projects.com` — numbered sidebar manual, breadcrumb eyebrows,
  persistent asset download.
- `brand.zapier.com/principles` — principle-led voice, typeface strategy.
- `design.cash.app` — restraint, type-driven hierarchy.
- `brandstandards.hermanmiller.com` — editorial rigour, do/don't discipline.
