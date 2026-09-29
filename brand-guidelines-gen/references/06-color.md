# Section 4 — Color

Place color after typography and specify every approved color in the formats required by the brand's production contexts.

## Required subsections

| # | Subsection | Required? |
|---|-----------|-----------|
| 1 | Primary palette | Always |
| 2 | Secondary / extended palette | Standard+ |
| 3 | Multi-format specifications per color | Always — 4 minimum |
| 4 | Tints and shades scale | Standard+ |
| 5 | Functional / semantic colors (success, warning, error) | When digital product |
| 6 | Color pairings / adjacency rules | Standard+ |
| 7 | Accessibility / contrast ratios | Always |
| 8 | Naming convention | Standard+ |
| 9 | Backgrounds / dark mode | Comprehensive or digital product |
| 10 | Don'ts | Always |

## Multi-format specifications

Provide the formats required for screen, print, production, and implementation. For most brands, include at least Pantone, CMYK, RGB, and HEX.

**Always provide at minimum:** Pantone (Coated AND Uncoated), CMYK, RGB, HEX.

Add when relevant:
- **RAL** — environmental, architectural, signage, automotive
- **Industry systems** — Cotton TCX (textile), DuPont/3M/PPG (paint), vinyl film codes, BS 4800 (UK gov)
- **HSL** — for design-system flexibility
- **NCS** — Nordic / public sector

For an infrastructure brand, consider RAL, NCS, Pantone, CMYK, RGB, HEX, HSL, and vinyl-film specifications.

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

## Palette size

Use four to six colors as a practical starting point, then adjust to the brand's actual needs.

| Palette size | Typical use |
|-------------:|-------------|
| 1–3 | Minimalist brands and high-discipline institutional systems |
| **4–6** | Primary + secondary + 2–3 accents |
| 7–10 | Rich systems with categorical use (e.g. an 8-colour set where each colour codes a category) |
| 27+ | Rare; usually flat-palette brands, and only workable with an accessibility pairing matrix |

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
2. **Adjacency system** — restrict combinations to specific named pairs, so no writer can invent a bad one

Rule of thumb: if a brand has 6+ colors, NOT all combinations are approved. Document only the sanctioned pairs.

## Accessibility

Document for every text/background combination:

- WCAG 2.2 contrast ratio (AA: 4.5:1 normal text, 3:1 large; AAA: 7:1 normal, 4.5:1 large)
- Whether it meets AA / AAA / fails
- Recommended use (body text / large text only / decorative only / not for text)

Tools: webaim.org/resources/contrastchecker, Stark Contrast Checker, Colour Contrast Analyser.

Apply these practices:
- Thread accessibility through every colour page rather than isolating it in one section
- Document the contrast ratio for every approved pairing, not just the primary
- For large palettes, ship a full pairing matrix marking which combinations pass
- State the standard you are claiming (WCAG AA / AAA) and at which text sizes

## Naming — beyond HEX strings

Give colors memorable names tied to the brand strategy when that helps teams discuss and apply them:

| Brand | Naming approach | Examples |
|-------|----------------|----------|
| Residential development | Food and drink | Cola, Avocado, Blueberry, Honey |
| Mixed-use property | Bird species | Raven, Owl, Pigeon, Finch, Flamingo |
| Home energy | Energy particles | Photon, Electron, Joule, Watt, Kelvin |
| Mountain resort | Local flora | Named after plants that grow on the site |
| Sportswear | Cultural references | Drawn from the brand's country of origin |

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

Distinguish RAG data colors (red/amber/green for status) from brand colors.

## Dark mode

Add dark-mode guidance for any digital brand that supports or expects dark interfaces.

Approach:
1. Define dark-mode equivalents for each light-mode token
2. Document inversion rules (some colors swap, some are theme-stable)
3. Specify token relationships, not duplicate hard values:
   - `surface.background` ≠ pure black; use a near-black like `#0A0B0D`
   - `surface.foreground` ≠ pure white; use `#F5F5F7`
4. Test contrast ratios in BOTH modes

A 4-level background system (base, raised, overlay, accent) is the pattern worth copying.

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

- **"Use our blue."** — vague and not production-ready.
- **Color value errors.** Many documents have specification mismatches (Pantone says one thing, HEX says another). Cross-validate.
- **No tints/shades.** Designers will improvise; results are inconsistent.
- **Colors that fail their own contrast claims.** Validate before publishing.
