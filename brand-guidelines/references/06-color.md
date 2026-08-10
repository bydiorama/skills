# Section 4 — Color

Position 4 (85% consensus). The MOST UNIVERSAL section in the corpus — present in 97.8% of documents, ahead of even logo (95%). Only four documents in the entire corpus omit color, and all are narrowly scoped supplements.

Color is also Diorama's **strongest measurable differentiator**: 4.1 specification formats per color vs. 2.8 industry average.

## Required subsections

| # | Subsection | Required? |
|---|-----------|-----------|
| 1 | Primary palette | Always |
| 2 | Secondary / extended palette | Standard+ |
| 3 | Multi-format specifications per color | Always — 4 minimum |
| 4 | Tints and shades scale | Standard+ |
| 5 | Functional / semantic colors (success, warning, error) | When digital product |
| 6 | Color pairings / adjacency rules | Standard+ |
| 7 | Accessibility / contrast ratios | Always (industry gap — competitive edge) |
| 8 | Naming convention | Standard+ |
| 9 | Backgrounds / dark mode | Comprehensive (industry gap) |
| 10 | Don'ts | Always |

## Multi-format specifications — the four-minimum

The corpus shows a sharp quality cliff at the 4-format threshold:

| Formats provided | Avg. quality score |
|------------------|-------------------:|
| HEX only | 2.5 / 5 |
| HEX + RGB | 3.0 / 5 |
| HEX + RGB + CMYK | 3.5 / 5 |
| **HEX + RGB + CMYK + Pantone** | **3.8 / 5** |
| + RAL / industry-specific | 4.2 / 5 |

**Always provide at minimum:** Pantone (Coated AND Uncoated), CMYK, RGB, HEX.

Add when relevant:
- **RAL** — environmental, architectural, signage, automotive
- **Industry systems** — Cotton TCX (textile), DuPont/3M/PPG (paint), vinyl film codes, BS 4800 (UK gov)
- **HSL** — for design-system flexibility
- **NCS** — Nordic / public sector

**Network Rail (E084)** sets the corpus benchmark with 8 systems: RAL, NCS, Pantone, CMYK, RGB, HEX, HSL, vinyl film.

### Format example

```
Brand Primary — "Voltage"

  Pantone Coated:    P 2727 C
  Pantone Uncoated:  P 2727 U
  CMYK:              C75 / M40 / Y0 / K0
  RGB:               R47 / G115 / B219
  HEX:               #2F73DB
  RAL:               5017 (Traffic Blue)
  HSL:               217° / 70% / 53%

  Token:             color.brand.primary
  WCAG vs white:     5.1 : 1 (AA Large, AAA Body when ≥18px Bold)
  WCAG vs black:     4.1 : 1 (AA Large only)
```

## Palette size — the 4–6 sweet spot

Independent study finding: 4–6 colors is optimal.

| Palette size | Typical use |
|-------------:|-------------|
| 1–3 | Minimalist brands (NeXT, NASA), high-discipline systems |
| **4–6** | **Sweet spot** — primary + secondary + 2–3 accents |
| 7–10 | Rich systems with categorical use (Discord, Hometree's energy-particle 8-color set) |
| 27+ | Rare; usually flat-palette brands (Tupperware E125, with ADA-compliant pairing matrix) |

If the user proposes 12+ colors, push back: divide into Primary / Secondary / Tertiary tiers and only document the primary tier as "the brand palette."

## Tints and shades

Provide a 5-step scale per primary color, minimum:

| Token | Use |
|-------|-----|
| color-primary-100 | Lightest tint, backgrounds |
| color-primary-300 | Light surfaces, hover |
| color-primary-500 | Base / brand value |
| color-primary-700 | Dark surfaces, pressed |
| color-primary-900 | Text on light, deepest tone |

Generate tints/shades by mixing toward white / black, NOT by lightness shift in HSL — HSL shifts produce muddy mid-tones.

## Color pairings — the adjacency system

Document which colors play well together. Two formats:

1. **Pairing matrix** — N×N grid showing approved combinations
2. **Adjacency system** — Howden (E067, 5/5) pioneer; restrict combinations to specific named pairs

Rule of thumb: if a brand has 6+ colors, NOT all combinations are approved. Document only the sanctioned pairs.

## Accessibility — the competitive edge

92% of the corpus does not address accessibility. Including it puts you ahead of nearly all competition.

Document for every text/background combination:

- WCAG 2.2 contrast ratio (AA: 4.5:1 normal text, 3:1 large; AAA: 7:1 normal, 4.5:1 large)
- Whether it meets AA / AAA / fails
- Recommended use (body text / large text only / decorative only / not for text)

Tools: webaim.org/resources/contrastchecker, Stark Contrast Checker, Colour Contrast Analyser.

Top corpus examples:
- **E074 Docusign** — accessibility throughout
- **E090 Strava** (5/5) — contrast ratios documented
- **E125 Tupperware** (4.5/5) — full ADA-compliant pairing matrix for 27 colors
- **E141 Research Ireland** — accessibility section
- **E159 NMAAHC** — concrete accessibility guidelines

## Naming — beyond HEX strings

Top-scoring documents give colors memorable names tied to the brand strategy:

| Brand | Naming approach | Examples |
|-------|----------------|----------|
| **D021 Kolinska Distrikt** (5/5) | Food / drink coding | Cola, Avocado, Blueberry, Honey |
| **D025 Corvus Atrium** (4.5/5) | Bird species | Raven, Owl, Pigeon, Finch, Flamingo |
| **E122 Hometree** | Energy particles | Photon, Electron, Joule, Watt, Kelvin |
| **D017 Vratna** (5/5) | Local flora | named after specific plants |
| **E147 ASICS** | Cultural / Japanese references | (TBD-flagged) |

Memorable naming is not decoration — it makes the colors easier to discuss in design reviews and client calls.

For tokens, use a structured convention:

```
color.brand.primary
color.brand.primary.tint-100
color.brand.primary.shade-700
color.semantic.success
color.semantic.warning
color.semantic.error
color.surface.foreground
color.surface.background
color.surface.subdued
```

## Functional / semantic colors — when digital

If the brand has any digital product:

- **Success** — green family
- **Warning** — amber / yellow family
- **Error** — red family
- **Info** — blue family
- **Neutral / Surface** — gray scale (5–9 stops)

Distinguish RAG data colors (red/amber/green for status) from brand colors (Howden E067 separates these explicitly — copy the pattern).

## Dark mode — the second industry gap

~90% of the corpus does not address dark mode. Add it as a default for any digital brand.

Approach:
1. Define dark-mode equivalents for each light-mode token
2. Document inversion rules (some colors swap, some are theme-stable)
3. Specify token relationships, not duplicate hard values:
   - `surface.background` ≠ pure black; use a near-black like `#0A0B0D`
   - `surface.foreground` ≠ pure white; use `#F5F5F7`
4. Test contrast ratios in BOTH modes

Twitch (E044) has a 4-level background system — copy that pattern.

## In context

Show the palette applied in 3–5 real settings:

- Primary palette on a poster / hero image
- Secondary palette on a UI screen
- Tints and shades in an infographic
- Failure case (low-contrast pairing) clearly marked

## Don'ts

- **Use brand color for body text** at small sizes (often fails contrast)
- **Combine warm + cool from the secondary palette** without intentional reason
- **Apply gradient combinations** outside the sanctioned set
- **Use functional colors as brand colors** (success-green should not appear in a hero)
- **Specify HEX only** — fails print, fails Pantone-spec partners
- **Skip accessibility** — known, fixable, increasingly mandatory

## Anti-patterns

- **"Use our blue."** — Vague; appears in 2/5 docs.
- **Color value errors.** Multiple corpus documents have specification mismatches (Pantone says one thing, HEX says another). Cross-validate.
- **No tints/shades.** Designers will improvise; results are inconsistent.
- **Colors that fail their own contrast claims.** Validate before publishing.

## Reference examples from the corpus

- **E084 Network Rail** (5/5) — 8 color specification systems
- **E070 IOC** (5/5) — Cotton TCX + Madeira thread alongside Pantone
- **E065 NJ Transit** (5/5) — DuPont, 3M, PPG, Wornow industrial systems
- **D003 FONA Dental** — Oracal 641 vinyl codes
- **E125 Tupperware** (4.5/5) — 27-color palette with ADA pairing matrix
- **E067 Howden** — Color grouping/adjacency system; RAG separated from brand
- **E044 Twitch** — 4-level background system
- **D021 Kolinska Distrikt** — Food-coded naming
- **E028 Discord** — Extensive multi-mode color system
