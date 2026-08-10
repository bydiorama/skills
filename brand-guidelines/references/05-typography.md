# Section 3 — Typography

Position 3 (87% consensus). Present in 92.8% of the corpus.

Typography is where amateur guidelines are exposed. "Use Helvetica" is not typography. A type system specifies sizes, weights, leading, tracking, roles, and pairings — and ideally embodies the brand voice through its choice.

## Required subsections

| # | Subsection | Required? |
|---|-----------|-----------|
| 1 | Typeface family / families | Always |
| 2 | Weights and styles in use | Always |
| 3 | Hierarchy / scale (5–7 levels) | Standard+ |
| 4 | Per-level specifications (size, weight, leading, tracking) | Standard+ |
| 5 | Pairing rules (when 2+ families) | When applicable |
| 6 | Web fallbacks / system stack | When digital |
| 7 | Multilingual / multi-script support | When applicable |
| 8 | Special characters, ligatures, glyph rules | Comprehensive |
| 9 | Misuse / don'ts | Always |
| 10 | Licensing / source / file location | Always |

## Typeface choice — three paths

| Path | % of corpus | Example | When to use |
|------|------------:|---------|-------------|
| **Commercial / foundry** | ~55% | Inter, Söhne, GT America, Matter, Haffer | Default for most brands; license fits budget |
| **Bespoke / custom** | ~25% | Cisco Sans, DS Indigo (Docusign), F1 family, Olympic Headline | Enterprise-scale, want true distinction |
| **Open-source / system** | ~20% | Inter, IBM Plex, system stacks | Tight budget, technical brands, high accessibility |

**Diorama-favored foundries** (Central European typography character):
- Displaay (Prague) — appears in 5+ Diorama projects
- Boutique foundries: Sans Plomb 98, Haffer, Matter

When proposing a typeface, justify the choice in one sentence: what voice does it carry? what's it doing better than the obvious default?

## Hierarchy — the 5–7 levels sweet spot

Per the corpus independent study: 6–7 levels is the sweet spot. Fewer than 5 → not enough distinction. More than 8 → impossible to remember.

**Standard 7-level hierarchy:**

| Level | Role | Typical size (web) | Typical weight | Use |
|-------|------|---------------------|----------------|-----|
| H1 / Display | Hero headlines | 56–96 px | Bold / Black | Hero spread, big moments |
| H2 / Headline | Section openers | 36–48 px | Bold / Semibold | Sections |
| H3 / Subhead | Subsections | 24–32 px | Semibold | Subsections |
| H4 / Eyebrow | Labels, kickers | 14–16 px UPPERCASE | Medium / Semibold | Pre-headlines |
| Body | Reading copy | 16–18 px | Regular | Paragraphs |
| Caption | Metadata, footnotes | 12–14 px | Regular / Medium | Small text |
| UI / Microcopy | Buttons, labels, tooltips | 14 px | Medium | Interactive |

For each level, specify all four:

```
H2 / Headline
  Typeface:  Söhne Breit Halbfett
  Size:      40 / 32 / 24 px (desktop / tablet / mobile)
  Weight:    600
  Leading:   1.15 (46 px / 37 / 28)
  Tracking:  −0.01em
  Color:     Ink-900 (#0F1115)
```

## Two scale strategies

### Linear scale (what most use)
List explicit values per level, typically on a multiples-of-8 grid (NOVEBA D033 uses multiples-of-8). Easy to reason about; scales poorly across very different breakpoints.

### Ratio-based scale
Scale via mathematical ratio (1.25 minor third, 1.333 perfect fourth, 1.5 perfect fifth). Kia (E069, 5/5) uses percentage-based scaling: H 100% / 60% / 50% / 20%. Channel 4 uses formula-based leading.

**Recommendation**: linear scale for Compact / Standard, ratio for Comprehensive.

## Pairing rules

When using 2 typefaces (most common: a display + a text), document:

- Which goes where (display only at H1–H2; text from H3 down)
- Never mix at the same level
- Never use both in the same word / line / paragraph
- One family must dominate; the other accents

Avoid 3-typeface systems unless there's a clear reason (e.g. body + display + monospace for code).

## Web fallbacks / system stack

For any digital brand, specify a fallback stack so the site degrades gracefully:

```css
--font-display: "Söhne Breit", "Inter", system-ui, sans-serif;
--font-body:    "Söhne", "Inter", system-ui, sans-serif;
--font-mono:    "Söhne Mono", "JetBrains Mono", ui-monospace, monospace;
```

State `font-display: swap;` for performance. Document FOUT/FOIT behavior.

## Multilingual / multi-script

If the brand operates in non-Latin markets, address:

- Character coverage (does the typeface ship Cyrillic, Greek, Arabic, CJK?)
- Optical adjustments per script (Arabic baseline shift, CJK line-height bump)
- Script-specific weights (Arabic typically reads heavier than Latin at the same weight)
- RTL layout rules

Top examples: IOC (E070, 5/5) — three bespoke typefaces by different designers across Olympic markets, with variable font tech. Kia (E069) — dual Latin/Korean system. HSBC (E082) — multilingual logos with custom small-usage Chinese sizes. Howden (E067) — Arabic, Thai, Hebrew script support.

## Special rules — the precision differentiator

Top documents (5/5) include granular typographic rules. Examples worth modeling:

- **Ogilvy Typography (E085, 5/5)** — wordspacing Min/Desired/Max; characters-per-line guidance; "gi" ligature prohibition (yes, that specific)
- **NJ Transit (E065)** — legibility formula: 1" cap height per 50 feet of viewing distance
- **Channel 4** — formula-based leading
- **Ferrari (E029)** — bilingual hyphenation rules

Borrow patterns:
- Numerals: lining vs old-style; tabular vs proportional
- Quote marks: curly only ("/" vs '/') ; never straight
- Em / en dash usage rules
- Ligatures: which are sanctioned; which prohibited
- All-caps tracking adjustment (typically +5% to +10%)

## Token-based naming (emerging best practice)

For design-system compatibility, name styles as tokens rather than just headings:

```
text-display-xl
text-display-lg
text-headline-md
text-body-md
text-body-sm
text-label-sm
```

Marina Dorcol (D008) uses Family.Weight convention. This bridges the brand-guidelines-to-design-tokens gap (one of the five identified industry gaps).

## Don'ts

- **Stretch or condense** typefaces (use the actual condensed weight if it exists)
- **Outline / drop-shadow** for emphasis (use weight or color)
- **Justify body text** at narrow column widths
- **Underline for emphasis** (use weight or color; underline is for links)
- **Mix more than 2 weights** in a single composition unless intentional
- **Set H1 in regular** weight — defeats hierarchy

## Licensing — make it explicit

State for each typeface:

```
Söhne Breit (foundry: Klim Type Foundry)
License:     Desktop (5 users) + Web (250k pageviews/mo)
Renewal:     2027-03-15
Files:       /Brand/Fonts/Söhne/
Web fonts:   self-hosted via /assets/fonts/sohne-breit-{400,600,700}.woff2
```

Licensing failures are a real cost: Adobe Fonts vs. desktop license vs. web license confusion is rampant. Spell it out.

## Anti-patterns

- **Typeface named, no hierarchy.** "We use Inter." → useless. (BONET SLEEK D015 anti-pattern.)
- **No weight specifications.** Designer guesses; consistency breaks.
- **Different typefaces in print vs web** without explicit mapping.
- **All-caps body text.** Reduces legibility; only for short emphasis.

## Reference examples from the corpus

- **E085 Ogilvy Typography** (5/5) — sole typography-only document in corpus; 38pp, gold standard
- **E069 Kia** — 31° angles + percentage-based ratio system
- **E108 Deutsche Bank** — Univers, International Typographic Style heritage
- **E060 F1** — Bespoke 4-weight family, each weight assigned an emotional personality
- **D033 NOVEBA** — Multiples-of-8 system, 12-column grid with exact margins/gutters
- **E065 NJ Transit** — Cap-height-per-50-feet legibility formula
- **E067 Howden** — 9pt modular type sizing
