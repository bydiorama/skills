# Section 2 — Logo

Position 2 (92% consensus). Present in 95% of the corpus. Almost always the most-detailed visual section.

The logo section is where most designers feel comfortable, which means the bar is high. Specifications must be production-ready, not aspirational.

## Required subsections

| # | Subsection | Required? |
|---|-----------|-----------|
| 1 | Primary logo | Always |
| 2 | Logo variants (3–5 typical, 6+ for comprehensive) | Always |
| 3 | Construction / anatomy | Standard+ |
| 4 | Clear space (exclusion zone) | 59% of corpus; should be 100% |
| 5 | Minimum size (mm + px) | Always |
| 6 | Color variants (positive, reversed, monochrome) | Always |
| 7 | Background usage matrix | Standard+ |
| 8 | Co-branding / lockups (if applicable) | When applicable |
| 9 | Misuse gallery (6–8 don'ts) | Always — non-negotiable |
| 10 | File format / asset naming | Standard+ |

## Logo variants — how many?

| Tier | Variants | Example |
|------|----------|---------|
| Compact | 3 (primary + monochrome + icon) | Minimum viable |
| Standard | 4–5 (primary, secondary, monochrome, reversed, icon-only) | Median |
| Comprehensive | 6+ (above + horizontal/vertical, language variants, partner lockups, app icon) | HSBC, IOC |

**Optical sizing variants are a differentiator.** Pentagram's MICA system (E002, 5/5) uses three custom-drawn optical sizes (Large / Regular / Small) with different stroke weights at each size. F1 (E060, 5/5) uses three logo size variants with different artwork (not just scaled). Default to a single mark with mathematical scaling unless the brand has the budget for optical sizing.

## Clear space — use a brand-native unit

Best practice: define clear space in terms of a measurable element of the logo itself, not in mm or px. This survives scaling.

- **RAC (E015, 5/5)** — "the 'a' rule" — clear space = height of the lowercase 'a'
- **MICA** — clear space = height of the slash mark
- **Apple (E144, 5/5)** — clear space = width of the 'a' in "apple"

Default rule if no obvious unit: **clear space = height of the cap-x of the wordmark**, on all four sides.

## Minimum size

State both **digital (px)** and **print (mm)**. The corpus shows minimum size errors are common.

- Digital minimum: typically 24–32px wide for icon-only; 80–120px wide for full wordmark
- Print minimum: typically 8–10mm height for icon; 25–40mm width for full wordmark
- Embroidery / etched / debossed: state separately when relevant (50% larger than print)

Format example:

```
Minimum size — full wordmark
  Digital:    120 px width
  Print:      30 mm width
  Embroidery: 45 mm width

Minimum size — icon only
  Digital:    24 px width
  Print:      8 mm width
  Favicon:    16 × 16 px
```

## Background usage matrix

A grid showing which logo variant goes on which background:

|  | White | Black | Brand color | Photo (light) | Photo (dark) | Pattern |
|---|---|---|---|---|---|---|
| Primary | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Reversed | ✗ | ✓ | ✓ | ✗ | ✓ | ✗ |
| Monochrome black | ✓ | ✗ | when contrast OK | ✓ | ✗ | when contrast OK |
| Monochrome white | ✗ | ✓ | when contrast OK | ✗ | ✓ | when contrast OK |
| With overlay scrim | — | — | — | always for photo | always for photo | — |

Document **contrast ratio thresholds** (e.g., logo must achieve ≥4.5:1 against background per WCAG AA) — almost no corpus document does this; it's a competitive edge.

## Misuse gallery — the standard six

Auto-generate at least these six misuse examples for every logo (this is the corpus-default minimum):

1. **Stretch / distort** — non-uniform scaling
2. **Rotate** — at angles other than 0/90/180/270
3. **Recolor** — using non-brand colors
4. **Low-contrast background** — illegible placement
5. **Busy background** — over patterns or photography without scrim
6. **Reconfigure** — rearranging mark + wordmark, or changing spacing

Each shown with a red ✗ overlay or "DO NOT" label. Pair with a corresponding "DO" example wherever possible — Do/Don't pairs score 3.8/5 vs Don't-only at 2.5/5.

For Comprehensive tier, add: 7. add effects (drop shadow, bevel), 8. tilt 3D, 9. embed in shape, 10. use unauthorized lockup with another brand.

## Construction / anatomy

For brands with proprietary marks (not just typeset wordmarks), document:

- **Geometric construction** — grid system, ratios, angles
- **Mathematical proportions** — Kia's 31° diagonal strokes; Howden's 9pt modular grid; FONA's golden-ratio parametric curves; Deutsche Bank's grid construction (Stankowski 1974, exemplifies the form)
- **Optical adjustments** — where the construction deviates for visual reasons
- **Component anatomy** — name the parts (counter, stem, terminal, etc.) so people can refer to them

This signals seriousness and prevents amateur reconstruction.

## File format and asset naming

Specify exact file deliverables:

```
Vector master:    .ai (CC2024+) or .svg
Print:            .pdf (CMYK, vector)
Web:              .svg (preferred), .png @1x/2x/3x
Office:           .png with transparent background
Favicon:          .ico (16/32/48), .png 192/512
Social profile:   1024 × 1024 .png
```

Naming convention example (HSBC, E082):

```
[brand]_logo_[variant]_[colorway]_[format].[ext]
e.g. acme_logo_primary_full-color_print.pdf
     acme_logo_icon_white_web.svg
```

## Co-branding and lockups

Only if the brand operates with partners / sub-brands. Define:

- **Lockup hierarchy** — primary brand always larger / leftmost / first
- **Separator** — vertical rule, "×", or blank space; specify exact dimensions
- **Approval process** — who signs off on a partner lockup before use

Reference: HSBC (E082) covers app-icon system across core, sub-brand, product, internal, watch, social.

## In context — the proof

Show the logo in 3–5 real placements:
- Business card (corner detail)
- Website header
- Social profile photo
- Document watermark
- Signage / environmental application

Real placements > abstract isolated marks. Top-scoring documents always show the logo in use.

## Anti-patterns to avoid

- **Logo without minimum size** — lazy specification, frequent in 2/5 docs
- **Clear space in mm only** — breaks at scale; use brand-native unit
- **Misuse gallery without paired do** — Don't-only scores 2.5/5
- **Single variant** — even Compact tier needs 3 variants
- **No background matrix** — every logo lives on backgrounds; document it
- **"Use the .ai file"** without specifying which derivatives are sanctioned

## Reference examples from the corpus

- **E015 RAC** — The Chevron device with 8 sub-sections; "'a' rule" clear space
- **E002 MICA / Pentagram** — Three custom-drawn optical sizes
- **E060 F1** — Three logo size variants with different artwork
- **E082 HSBC** — App icon system across 6 contexts
- **E069 Kia** — 31° construction angles, ratio-based geometry
- **E067 Howden** — Logo functions as both wordmark and symbol
- **E029 Ferrari** — Bilingual EN/IT logo construction with full grid
- **E134 NeXT (Paul Rand)** — Gold-standard rationale: each design choice argued
