# Pipeline — extraction → data model → build → verify

## Phase A — Ground truth (never guess a value)

Read, in priority order:

1. **The token file.** Learn the two layers most systems have — *primitives*
   (`--gs-900`, `--blue-500`) and *semantic roles* (`--color-text-secondary`,
   `--text-h2-size`). Consume the **semantic** layer everywhere; the page must
   obey the same rule the codebase imposes on its own components. Record: exact
   hexes, the opacity ramp (many dark systems use one white at many opacities
   instead of a grey scale), the type ramp with matched size/leading/tracking,
   spacing scale, radii, elevation recipes, motion durations + easings, and
   breakpoints (CSS media queries can't read custom properties, so note the
   literal px stops the project uses).
2. **The component inventory.** Find the real `Button`, `Text`, `Logo`, chip,
   card, header, footer. **Reuse them.** A page that imports the product's own
   `<Button>` cannot drift from the product.
3. **The design doc / CLAUDE.md.** Codebases that ship a design system usually
   ship its rules (when to add a token, breakpoint stops, typography
   distinctions, gotchas). Free correctness.
4. **The asset tree.** Enumerate `public/` (or equivalent): logos, marks, icons,
   insignias, fonts, imagery. Note viewBoxes, fills, and which files are
   **shared with the live site** (see anti-footguns).
5. **The routing + SEO registries.** A new page usually needs a route, a
   prerender/sitemap entry, and per-route metadata. Find the single sources of
   truth so the page doesn't 404 on direct load or drift from the sitemap.
6. **Figma (if present).** Metadata for *structure only* (node ids, names,
   geometry); design-context on *small leaf nodes* to harvest real tokens and
   CSS with variable names; screenshot brand slides for reference. Figma asset
   URLs **expire (~7 days)** and may be **blocked by network policy** — download
   immediately, and have a fallback (regenerate the asset from the mark + the
   real font outlines) when the URL 403s.

## Phase B — Data model first

Put **every string, swatch, asset path, and scale value** in one declarative
data module. The page component stays pure composition — no inline copy, no
hardcoded paths. This is what lets copy iterate a dozen times without touching
JSX, and it is the single source the Markdown export serialises from (so the
export can never drift from the rendered page).

## Phase C — Build the page in the brand's system

- **Sidebar manual layout**: sticky numbered section nav on desktop; sticky
  horizontal chip row on mobile. Scroll-spy the active section with an
  `IntersectionObserver` (rootMargin biased to the upper third of the viewport).
- Sections stacked with hairline separators (never a colour change if the system
  says so).
- Reuse the product's smooth-scroll/anchor behaviour and header offset
  (`scroll-margin-top` equal to the header height on every anchor target).
- Add the interactive affordances (see interactive-patterns.md).

## Phase D — Verify, then ship

1. **Typecheck + lint** clean.
2. **Render in a real browser** (headless is fine) at ~1600/1024/390 px. Read the
   screenshots; check reflow, no horizontal scroll, legibility.
3. **Exercise every interaction**: copy returns the right clipboard value; each
   download serves the right bytes; the generator downloads valid SVG; the
   Markdown export is well-formed and complete.
4. **Verify asset endpoints** (200 + expected size), including the archive.
5. **Confirm you did not disturb shared assets.**
6. **Re-review against the reference sites** named in the brief; note where you
   deliberately exceed them.

State explicitly what you *couldn't* verify (e.g. a reference site blocked by
network policy) rather than implying full coverage.
