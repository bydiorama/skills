# Section 3 — Typography

Place typography after the logo section and define it as a complete system rather than a list of font names.

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

| Path | Example | When to use |
|------|---------|-------------|
| **Commercial / foundry** | Inter, Söhne, GT America, Matter, Haffer | The license fits the budget and usage needs |
| **Bespoke / custom** | A commissioned family, often named after the brand | Enterprise-scale system seeking distinctive ownership |
| **Open-source / system** | Inter, IBM Plex, system stacks | Tight budget, technical products, or broad accessibility needs |

**Look past the obvious foundries.** Independent and regional foundries carry character that the default choices do not, usually at a friendlier licence. Build a shortlist you actually know rather than reaching for the same three families on every project.

When proposing a typeface, justify the choice in one sentence: what voice does it carry? what's it doing better than the obvious default?

## Hierarchy — 5–7 levels

Use enough levels to distinguish content roles without making the system difficult to remember. Five to seven levels suit many projects.

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
List explicit values per level, typically on a multiples-of-8 grid. Easy to reason about; scales poorly across very different breakpoints.

### Ratio-based scale
Scale via mathematical ratio (1.25 minor third, 1.333 perfect fourth, 1.5 perfect fifth). Some automotive systems use percentage-based scaling: H 100% / 60% / 50% / 20%. Others derive leading from size by formula rather than setting it per level.

**Recommendation**: linear scale for Compact / Standard, ratio for Comprehensive.

## Pairing rules

When using two typefaces, such as a display face and a text face, document:

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

For complex global systems, consider script-specific typefaces, multilingual logos with small-use variants, variable-font support, and explicit vertical metrics for each script.

## Special rules

Add granular typographic rules when the brand's contexts require them. Examples:

- **Typography-only manuals** — wordspacing Min/Desired/Max; characters-per-line guidance; named ligature prohibition (yes, that specific)
- **Transit and wayfinding** — a legibility formula: 1" cap height per 50 feet of viewing distance
- **Formula-based leading** — line-height derived from size by rule, not set per level
- **Bilingual brands** — hyphenation and line-breaking rules per language

Borrow patterns:
- Numerals: lining vs old-style; tabular vs proportional
- Quote marks: curly only ("/" vs '/') ; never straight
- Em / en dash usage rules
- Ligatures: which are sanctioned; which prohibited
- All-caps tracking adjustment (typically +5% to +10%)

## Token-based naming

For design-system compatibility, name styles as tokens rather than just headings:

```
text-display-xl
text-display-lg
text-headline-md
text-body-md
text-body-sm
text-label-sm
```

A `Family.Weight` convention creates a clear bridge from brand guidelines to design tokens.

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

- **Typeface named, no hierarchy.** "We use Inter." → useless. Naming a font is not a type system.
- **No weight specifications.** Designer guesses; consistency breaks.
- **Different typefaces in print vs web** without explicit mapping.
- **All-caps body text.** Reduces legibility; only for short emphasis.
