---
name: brand-guidelines-generator
description: >
  Generate an essential, practical brand-guideline ONE-PAGER WEBSITE (HTML/CSS/JS) by
  EXTRACTING real brand assets from a live website and/or a Figma file. Use when the user
  provides a website URL or a Figma design link and asks to "generate brand guidelines",
  "generate a brand guideline website/page", "build brand guidelines from our site/Figma",
  "extract our brand", "make a brand one-pager", "document colours/typography/logo from our
  site/Figma", "create a style reference from this website", or "turn our Figma into a brand
  guide page". The defining signal is EXTRACTION FROM SOURCES (a URL and/or Figma link) plus
  a self-contained web-page output. Covers the essentials — logo, colour, typography/fonts,
  and a short tone of voice — grounded in values pulled from the sources (not invented), and
  styled IN the brand. It composes the `brand-guidelines` skill for content structure and the
  canonical section order. Do NOT use for: writing a full Markdown brand book from scratch
  with no extractable sources (use `brand-guidelines`), marketing campaign briefs, or SEO
  style guides. Brand-agnostic — works for any brand.
---

# Brand Guidelines Generator

Build a single, easy-to-read, practical brand-guideline **website** (plain HTML, CSS and a
little vanilla JS — no build step) by **extracting** the real brand system from a live
website and a Figma file: exact colours with their token names, the type scale and fonts,
the logo and its colour variants, and the button/card styles. The page is styled *in* the
brand so it demonstrates the system, not just describes it.

This skill is the **extraction + web-output** counterpart to `brand-guidelines` (which
produces the Markdown brand book). Reuse `brand-guidelines` for the canonical section order
and content rules; this skill adds the source-extraction pipeline and the one-page website.

## Usage

```
@brand-guidelines-generator
@brand-guidelines-generator <website-url> <figma-url-with-node-id>
```

Provide whatever you have; the skill asks only for genuinely missing inputs.

## What This Skill Does

### Phase 1: Gather sources and set scope

- Collect inputs: **live website URL**, **Figma file URL with a `node-id`**, optional
  **font kit** (e.g. an Adobe Typekit `<link>`), and the **brand name**.
- Confirm scope with `AskUserQuestion` — default is the **essentials** (logo, colour,
  typography/fonts) plus a short **tone of voice**; output is a **one-page website**.
  Batch the real decisions in one prompt: document language, depth (essentials only vs
  + logo/voice vs mini brand book), and whether to extract the real logo.
- If a Figma URL has no `node-id`, ask for a node-specific link.

### Phase 2: Extract from the live website (ground truth for UI)

- `WebFetch` the site for the brand overview: what they do, tagline, services, tone.
- Find the real CSS: `curl` the page, `grep` for `<link ... stylesheet>`, then `curl` the
  main theme/app stylesheet.
- From that CSS, pull **ground-truth values**: the `.button` rules (radius, padding,
  bg/text colour, hover, shadow), card styles (radius, dividers, shadow), the **named
  colour scale** (token → rgb/hex), and `font-family` declarations.
- The site CSS is authoritative for buttons, cards and colours — prefer it over guesses.

### Phase 3: Extract from Figma (MCP)

- `get_metadata` on the page/node for **structure only** (node IDs, names, geometry — no
  colours or text). If the output is huge, offload it to a subagent or slice with `jq`.
- `get_design_context` on **small leaf content nodes** (a heading, a stat, a button) →
  returns real CSS with font family/size/line-height/letter-spacing **and** colour values
  carrying their **Figma variable names** (e.g. `var(--fawn,#F7B267)`). This is the
  reliable way to harvest design tokens — metadata will not give them.
- `get_screenshot` for visual reference. `get_variable_defs` needs a live selection in the
  desktop app and often errors — rely on the inline `var(--name,#hex)` names instead.
- Reconcile Figma tokens against the website CSS; they should match. Note any discrepancy.

### Phase 4: Extract and prepare logo assets

- `get_design_context` on the **symbol** and **wordmark** nodes → asset URLs; `curl` them.
  Figma asset URLs **expire (~7 days)** — download during the build. Files labelled `.png`
  may actually be **SVG** — verify with `file` and rename.
- Make recolourable copies: replace `fill="var(--x,#hex)"` with `fill="currentColor"`, and
  inline the paths as an SVG `<symbol>` sprite.
- **CRITICAL:** inline `<symbol>` paths must carry `fill="currentColor"` (or a CSS `fill`).
  With no fill they render **black** and ignore the CSS `color` — a silent, common bug.
- Generate **lockup colour variants** as self-contained SVGs: primary (accent symbol +
  dark text, for light backgrounds), reversed (accent symbol + light text, for dark),
  mono, and symbol-only. **Logo colour rule:** the symbol keeps the accent colour in every
  variant; only the wordmark text swaps for light vs dark backgrounds.
- Build a **favicon**: compose the symbol on a brand tile, render a 256px master with
  `qlmanage -t -s 256`, then build a multi-size `favicon.ico` with Pillow plus an
  apple-touch PNG and the `favicon.svg`. Tighten padding so the mark reads at 16px.

See `resources/extraction-playbook.md` for exact commands and gotchas.

### Phase 5: Build the one-pager (styled in the brand)

- Use `brand-guidelines` for the **canonical section order** — at-a-glance → Logo →
  Typography → Colour → Tone of voice — kept to the essentials.
- **HTML**: semantic sections, sticky in-page nav, the inline SVG sprite. Hero uses the
  **primary** lockup on a light surface; footer uses the **reversed** lockup on a dark one.
- **CSS**: define the palette and type scale as `:root` custom properties **mirroring the
  Figma variable names**; embed the font kit; reuse the site's real **button & card**
  styles (radius, padding, hover, shadow, dotted dividers). Fully responsive.
- **JS** (vanilla, no deps): click-a-swatch-to-copy-HEX with a **visible affordance** and a
  toast; nav scroll-spy; footer year.
- **Honesty on fonts**: `WebFetch`/`curl` the font kit CSS to confirm exact family slugs
  and **available weights**. If the kit lacks design weights (e.g. Thin/Medium), render
  with the available weights and document intent vs availability. Always give fallback
  stacks.

See `resources/build-patterns.md` for reusable HTML/CSS/JS snippets.

### Phase 6: Verify

- Open in a browser. Confirm: fonts load from the kit; every colour token shows the correct
  hex and copy-to-clipboard works; logos are crisp on light **and** dark; favicon is legible
  at 16px; layout reflows at ~375px without overflow; body/accent contrast is sane.

## Output Location

A project repo (the current working directory unless told otherwise):

```
index.html · styles.css · script.js · README.md
favicon.svg · favicon.ico
assets/  (logo source exports + colour-variant SVGs + favicon PNGs)
```

## Quality Assurance

- **Values are extracted, not guessed** — every hex + token name comes from the site CSS or
  Figma `get_design_context`.
- Buttons and cards **match the live site** (radius, padding, hover, shadow).
- Logo colour logic is correct per background (primary on light, reversed on dark; symbol
  always the accent colour).
- Font-kit weights are **confirmed and documented** (intent vs available), with fallbacks.
- Inline logo SVGs use `fill="currentColor"` and recolour correctly everywhere.
- Copy-to-clipboard works (with a non-secure-context fallback) and the favicon reads at 16px.
- Responsive; no leftover `[brackets]` or placeholder copy.

## Tips for Best Results

- Treat the **site CSS as ground truth** for anything interactive; treat **Figma
  `get_design_context`** as ground truth for tokens and the logo.
- Harvest tokens from **small** Figma nodes — large nodes overflow context and metadata
  carries no styles.
- Download Figma assets **immediately** (URLs expire) and `file`-check the real format.
- The page should **demonstrate** the brand — set it in the brand's own colours and type.
- Flag, don't hide, gaps (missing font weights, low-contrast accent on white, etc.).
- Keep it a true one-pager: scannable over decorative.

## Continuous Improvement

After completing this workflow, invoke `@skill-reflect brand-guidelines-generator` to update
this skill with validated learnings from the execution.

## User-Invocable

Yes - users can invoke this skill directly with `@brand-guidelines-generator`
