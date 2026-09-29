# Phase 5: Quality Checklist

Run this checklist before delivering the document. It screens for five critical omissions and verifies that the system is complete, usable, and ready for handoff.

## Five critical omissions

If ANY of these are present in the document as currently drafted, flag and fix before delivery:

### 1. No brand strategy section
Verify Section 1 (Brand Strategy) contains at minimum:
- A statement of purpose / mission
- 3–5 named values OR personality traits
- A 1-line positioning / tagline

If the user has no strategy and won't develop it now, ship a clearly-marked "v0.1 — strategy pending" placeholder, not a missing section.

### 2. No tone of voice
Verify Section 8 (Tone of Voice) contains at minimum:
- Voice description (who we sound like) — 3–5 traits with anti-definitions
- 6+ Do/Don't worked examples
- A short vocabulary list (words used / words avoided)

If the brand has no voice yet, draft a starter framework (see `references/10-tone-of-voice.md` "When the brand has no voice yet").

### 3. Missing color specifications (HEX-only)
Verify every color has the formats required for both print and screen, including at minimum:
- Pantone Coated AND Pantone Uncoated
- CMYK
- RGB
- HEX

For environmental / signage / industrial brands, add RAL. Cross-validate that values agree (no Pantone-vs-HEX mismatches).

### 4. No misuse / don'ts
Verify the document includes paired Do/Don't guidance for:
- Logo (minimum 6 misuse examples)
- Color (at least 1 anti-pattern)
- Typography (at least 1 anti-pattern)
- Photography (when section exists, at least 3 anti-patterns)
- TOV (at least 6 do/don't worked examples)

### 5. No photography direction
Verify Section 6 either:
- Contains substantive direction (philosophy + mood + named categories + don'ts), OR
- Contains a clearly-marked "Photography direction in development for v2.0" placeholder with intent statement

Don't omit the section entirely.

## Quality scorecard

Score each dimension from 1–5 and resolve any item below 4 before delivery.

| Dimension | Completion threshold | Self-score 1–5 |
|-----------|----------------------|--------------:|
| Page count appropriate to scope | Compact 20–30 / Standard 30–50 / Comprehensive 60–90 | __ |
| All 8 sections present (or placeholder) | Yes | __ |
| Strategy section opens (position 1) | Yes | __ |
| TOV section closes (position 8) | Yes | __ |
| Color specs ≥ 4 formats per color | Yes | __ |
| Logo: 3+ variants + clear space + min size | Yes | __ |
| Typography: full hierarchy with size/weight/leading/tracking | Yes | __ |
| Photography: named categories OR documented placeholder | Yes | __ |
| Applications: 5+ real-world examples (Compact), 8–12 (Standard), 15+ (Comp) | Yes | __ |
| TOV: 4-framework choice + 6+ Do/Don't pairs | Yes | __ |
| Don'ts present for logo, color, type, photo, TOV | Yes | __ |
| Voice of document matches brand (or deliberately neutral) | Yes | __ |
| File size under 50 MB | Yes | __ |
| Versioning + changelog included | Yes | __ |
| Asset locations referenced | Yes | __ |

## Extended (Comprehensive tier) scorecard

For Comprehensive tier projects, also verify:

| Extended element | Threshold | Present? |
|-----------------|-----------|----------|
| Accessibility statement + WCAG ratios | Yes | __ |
| Dark mode tokens | If digital | __ |
| Motion / animation specs | If digital | __ |
| Brand architecture | If multi-brand | __ |
| Governance + contact section | Yes | __ |
| Design token export (CSS/JSON/Figma) | If digital | __ |
| AI usage policy | Recommended | __ |
| Sustainability / materials policy | If ESG-relevant | __ |

Include every extended element relevant to the brand's products, markets, and operations.

## Spot-check anti-patterns

Scan the document for these:

- [ ] Any "Lorem ipsum" or unfinished placeholder copy?
- [ ] Any "TBD" / "to be determined" sections that aren't explicitly marked v0.1 placeholders?
- [ ] Any color value that fails its own claimed contrast ratio?
- [ ] Any reference to a typeface without licensing details?
- [ ] Any application mockup without supporting specifications?
- [ ] Any inconsistency in voice across sections (suggesting different authors)?
- [ ] Any generic mission statement that could belong to any brand?
- [ ] Any value/trait without an anti-definition?
- [ ] Any logo variant shown without minimum size?
- [ ] Any "Don'ts" section without paired "Dos"?

## Industry-specific spot-checks

Run the relevant industry check based on the brand's category:

### Real estate / Hospitality
- Property photography direction defined?
- Signage application included?
- Multi-language considered (especially if international)?
- Environmental / wayfinding rules?

### SaaS / Tech
- Dark-mode color tokens?
- App icon system across platforms (iOS, Android, watch, web favicon)?
- UI component direction (buttons, inputs, alerts)?
- Documentation / API guideline?

### Retail / Consumer goods
- Packaging guidelines?
- POS / in-store materials?
- E-commerce tile / product card?
- Hangtag / care label?

### Finance / Insurance
- Compliance / disclaimer typographic treatment?
- Print-grade color specs (Pantone + CMYK)?
- Multi-jurisdictional language considered?
- Statement / policy doc template?

### Healthcare
- Patient-facing accessibility (large type, high contrast, clear hierarchy)?
- Regulatory / FDA / EMA labels considered?
- Multi-language readiness?

### Public sector / Civic
- Multi-language and multi-script readiness?
- Accessibility per public-sector standards (e.g. EN 301 549)?
- Vehicle / uniform / environmental signage?
- Regulatory disclaimers?

### Sports / Fitness
- Kit / jersey rules?
- Broadcast / scoreboard treatment?
- Athlete representation guidance?
- Live event / on-pitch graphics?

### Arts / Culture / Education
- Donor recognition / sponsor lockup rules?
- Exhibition / event treatment?
- Wayfinding / environmental?

## Final delivery checklist

Before delivering to the user:

- [ ] Document name + version + date on cover
- [ ] Table of contents (if 30+ pages)
- [ ] All sections present in canonical order
- [ ] No critical omission unaddressed
- [ ] Industry-specific extras included where relevant
- [ ] Voice of document matches brand (or deliberately neutral)
- [ ] File size under 50 MB
- [ ] Asset references / template links included
- [ ] Contact / governance footer
- [ ] One pass of read-aloud — does it sound like the brand?

## Reporting back to the user

Deliver with a short summary:

```
Brand Guidelines for [brand]
Tier: [Compact/Standard/Comprehensive] — [N] pages
Voice: [brand voice / hybrid / neutral]

Sections covered:
  [✓] Brand Strategy
  [✓] Logo
  [✓] Typography
  [✓] Color (4-format spec)
  [✓] Graphics
  [✓ / placeholder] Photography
  [✓] Applications
  [✓] Tone of Voice

Extended elements:
  [✓ / —] Accessibility
  [✓ / —] Dark mode
  [✓ / —] Design tokens
  [✓ / —] Governance

Open items:
  - [Anything pending — e.g. "photography direction to be added in v2.0 once shoot complete"]
  - [Any user decisions still needed]

Quality assessment: [ready / ready with noted open items / revision required].

Next steps:
  - Review the document with [stakeholder list]
  - [Any layout / production work needed before final deliverable]
```

Always be honest about open items. A document marked "v1.0 — TOV pending shoot" is more credible than a document that ships incomplete sections without acknowledgment.
