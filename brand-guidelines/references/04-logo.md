# Section 2 — Logo

Place the logo section after Brand Strategy and specify it in enough detail for reliable production use.

The logo section is where most designers feel comfortable, which means the bar is high. Specifications must be production-ready, not aspirational.

## Required subsections

| # | Subsection | Required? |
|---|-----------|-----------|
| 1 | Primary logo | Always |
| 2 | Logo variants (3–5 typical, 6+ for comprehensive) | Always |
| 3 | Construction / anatomy | Standard+ |
| 4 | Clear space (exclusion zone) | Always |
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
| Standard | 4–5 (primary, secondary, monochrome, reversed, icon-only) | Full everyday set |
| Comprehensive | 6+ (above + horizontal/vertical, language variants, partner lockups, app icon) | Global banks, sporting bodies |

Use optical sizing when the logo must remain legible across a wide size range. Create custom-drawn Large, Regular, and Small variants with appropriate stroke and spacing adjustments. Default to a single mark with mathematical scaling unless the brand has the budget and need for separate artwork.

## Clear space — use a brand-native unit

Best practice: define clear space in terms of a measurable element of the logo itself, not in mm or px. This survives scaling.

- Clear space = the height of the lowercase 'a' in the wordmark — memorable because it is named
- Clear space = the height of a distinctive mark within the logo (a slash, a dot, a crossbar)
- Clear space = the width of a specific letter in the wordmark — the same trick, measured horizontally

Default rule if no obvious unit: **clear space = height of the cap-x of the wordmark**, on all four sides.

## Minimum size

State both **digital (px)** and **print (mm)** minimum sizes, and validate them with actual logo artwork.

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

Document **contrast ratio thresholds** where applicable and state how to validate logo legibility against backgrounds.

## Misuse gallery — the standard six

Create at least these six misuse examples for every logo:

1. **Stretch / distort** — non-uniform scaling
2. **Rotate** — at angles other than 0/90/180/270
3. **Recolor** — using non-brand colors
4. **Low-contrast background** — illegible placement
5. **Busy background** — over patterns or photography without scrim
6. **Reconfigure** — rearranging mark + wordmark, or changing spacing

Show each with a red ✗ overlay or "DO NOT" label. Pair it with a corresponding "DO" example wherever possible.

For Comprehensive tier, add: 7. add effects (drop shadow, bevel), 8. tilt 3D, 9. embed in shape, 10. use unauthorized lockup with another brand.

## Construction / anatomy

For brands with proprietary marks (not just typeset wordmarks), document:

- **Geometric construction** — grid system, ratios, angles
- **Mathematical proportions** — a fixed construction angle, a modular point grid, golden-ratio parametric curves, or a published construction grid in the International Typographic tradition
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

Naming convention example (a multi-entity financial group):

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

A thorough app-icon system covers six contexts: core, sub-brand, product, internal, watch and social.

## In context — the proof

Show the logo in 3–5 real placements:
- Business card (corner detail)
- Website header
- Social profile photo
- Document watermark
- Signage / environmental application

Prioritize real placements over abstract isolated marks so users can see the logo in context.

## Anti-patterns to avoid

- **Logo without minimum size** — incomplete production guidance
- **Clear space in mm only** — breaks at scale; use brand-native unit
- **Misuse gallery without paired do** — show the correct treatment beside the incorrect one
- **Single variant** — even Compact tier needs 3 variants
- **No background matrix** — every logo lives on backgrounds; document it
- **"Use the .ai file"** without specifying which derivatives are sanctioned
