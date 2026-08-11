# [Brand Name] Brand Guidelines

> **Version**: 1.0 · **Published**: [YYYY-MM-DD] · **Owner**: [name + email]
> **Format**: 1920×1080 landscape PDF · **Target**: 30–50 pages

---

## Contents

1. Brand Strategy
2. Logo
3. Typography
4. Color
5. Graphics
6. Photography
7. Applications
8. Tone of Voice
9. Governance & Asset Locations

---

## Foreword

[1–2 paragraphs in the brand's voice. Set tone for the rest of the document. See `references/12-writing-the-guidelines.md` for templates.]

---

# 1. Brand Strategy

## 1.1 Purpose
[One short sentence — the philosophical "why."]

[1–2 sentences unpacking what this means for this brand specifically.]

## 1.2 Vision
[The aspirational future state.]

## 1.3 Mission
[What the brand does today to get there.]

## 1.4 Values
[3–5 named values, each with 1-line unpack and an anti-definition where possible.]

| Value | What it means | What it isn't |
|-------|--------------|---------------|
| [Value 1] | ... | ... |
| [Value 2] | ... | ... |
| [Value 3] | ... | ... |

## 1.5 Personality
[4–6 traits, ideally as "X but not Y" pairs.]

- [Trait] but not [opposite]
- [Trait] but not [opposite]
- [Trait] but not [opposite]
- [Trait] but not [opposite]

## 1.6 Positioning
> [One short, distinctive sentence — the brand promise.]

## 1.7 Audience
[Primary audience description — demographic + psychographic + behavioral.]

[Secondary audiences if relevant.]

---

# 2. Logo

## 2.1 The Logo
[Image of primary logo + one paragraph describing its rationale.]

## 2.2 Variants
[Image grid of 3–5 variants with labels: Primary, Secondary, Monochrome, Reversed, Icon-only.]

## 2.3 Construction
[Construction grid showing geometry / proportions / clear-space units.]

## 2.4 Clear Space
**Clear space = [brand-native unit, e.g. height of cap-x of wordmark]** on all four sides.

## 2.5 Minimum Size

```
Full wordmark
  Digital:    [N] px width
  Print:      [N] mm width
  Embroidery: [N] mm width

Icon only
  Digital:    [N] px width  (Favicon: 16 × 16)
  Print:      [N] mm width
```

## 2.6 Color Variants
[Image grid: positive on white, reversed on black, on brand color, on photo with scrim.]

## 2.7 Background Usage Matrix

|  | White | Black | Brand color | Photo (light) | Photo (dark) | Pattern |
|---|---|---|---|---|---|---|
| Primary | ✓ | ✗ | — | — | — | — |
| Reversed | ✗ | ✓ | ✓ | — | ✓ | — |
| Mono black | ✓ | ✗ | ok if ≥4.5:1 | ✓ | — | ok if ≥4.5:1 |
| Mono white | ✗ | ✓ | ok if ≥4.5:1 | — | ✓ | ok if ≥4.5:1 |

## 2.8 Misuse — Standard Six Don'ts
[Image grid with 6 misuse examples, each with red ✗ overlay.]
1. Stretch / distort
2. Rotate
3. Recolor
4. Low-contrast background
5. Busy background without scrim
6. Reconfigure / rearrange

## 2.9 File Formats
[Vector master, print PDF, web SVG, app PNG, favicon. With naming convention.]

---

# 3. Typography

## 3.1 Type Family / Families
**[Typeface name]** — [foundry] — [one-line on why this typeface for this brand]
**[Optional second family]** — [foundry] — [one-line]

## 3.2 Hierarchy

| Level | Typeface · Weight | Size (px) | Leading | Tracking | Use |
|-------|-------------------|-----------|---------|----------|-----|
| Display | [Family] · [Weight] | [N] | [N] | [N]em | Hero |
| H1 | [Family] · [Weight] | [N] | [N] | [N]em | Section opener |
| H2 | [Family] · [Weight] | [N] | [N] | [N]em | Subsection |
| H3 | [Family] · [Weight] | [N] | [N] | [N]em | Group |
| Body | [Family] · [Weight] | 16–18 | 1.5 | 0 | Reading copy |
| Caption | [Family] · [Weight] | 12–14 | 1.4 | 0 | Metadata |
| UI / Label | [Family] · [Weight] | 14 | 1.4 | 0.02em | Buttons, labels |

## 3.3 Pairing Rules
[One paragraph: which family appears at which level; never mix at same level.]

## 3.4 Web Stack

```css
--font-display: "[Name]", system-ui, sans-serif;
--font-body:    "[Name]", system-ui, sans-serif;
```

## 3.5 Special Rules
- Numerals: [lining / old-style; tabular / proportional]
- Quote marks: curly only (" / ')
- Em / en dash: [usage rule]
- All-caps tracking: +5–10%

## 3.6 Don'ts
- Stretch / condense (use the actual condensed weight)
- Underline for emphasis (use weight or color)
- Mix more than 2 weights in a composition
- Set H1 in regular weight

## 3.7 Licensing
[Per-typeface license type, user count, renewal date, file location.]

---

# 4. Color

## 4.1 Primary Palette

### [Color name 1]

```
Pantone Coated:    [code]
Pantone Uncoated:  [code]
CMYK:              C[N] / M[N] / Y[N] / K[N]
RGB:               R[N] / G[N] / B[N]
HEX:               #[XXXXXX]
RAL:               [if relevant]

Token:             color.brand.primary
WCAG vs white:     [N]:1 — AA / AAA / Fail
WCAG vs black:     [N]:1 — AA / AAA / Fail
```

### [Color name 2]
[Same spec block.]

### [Color name 3]
[Same spec block.]

## 4.2 Secondary / Extended Palette
[3–5 secondary colors, full spec each.]

## 4.3 Tints and Shades
[5-step scale per primary color: 100, 300, 500, 700, 900.]

## 4.4 Functional / Semantic
- Success — [HEX]
- Warning — [HEX]
- Error — [HEX]
- Info — [HEX]
- Neutral scale — [5–9 stops]

## 4.5 Pairing Matrix
[N×N matrix of approved combinations.]

## 4.6 Accessibility
[Statement of WCAG 2.2 AA target. Pairing matrix with AA/AAA pass/fail per combination.]

## 4.7 Don'ts
- Brand color for body text at small sizes (often fails contrast)
- Mixing warm + cool from the secondary palette
- Gradients outside the sanctioned set
- Functional colors used as brand colors

---

# 5. Graphics

## 5.1 The System
[Open with the philosophy. Pick one: named device, generative system, pattern/texture, or illustration.]

## 5.2 [Named Device, if applicable]
[Image + 1-paragraph rationale + construction rules + 5–10 example uses.]

## 5.3 Iconography
- Style: [line / filled / duotone]
- Stroke: [N]pt at 24px
- Grid: 24 × 24 with 2px padding
- Library: [N] icons available
- Source / file location: [...]

## 5.4 Patterns / Textures
[If used — tile size, repeat, color treatment, scale.]

## 5.5 Don'ts
- Recolor outside palette
- Resize disproportionately
- Apply effects (drop-shadow, glow, bevel)
- Mix illustration with photography in same composition

---

# 6. Photography

## 6.1 Philosophy
[3–6 sentences in the brand's voice on what photography is for and what it must do.]

## 6.2 Categories
[3–6 named categories with role + 2–3 reference images each.]

| Category | Role | Notes |
|----------|------|-------|
| [Name 1] | [Hero / atmospheric] | [direction] |
| [Name 2] | [Story / human] | [direction] |
| [Name 3] | [Product / object] | [direction] |

## 6.3 Mood Board
[6–12 image grid showing approved direction.]

## 6.4 Composition Rules
- Framing: [...]
- Negative space: ample
- Subject placement: [...]
- Crop: [...]

## 6.5 Color Treatment
- Profile: [sRGB / Adobe RGB]
- White balance: [...]
- LUT: [filename + version]

## 6.6 Don'ts
[3–6 anti-examples with ✗ overlay: staged corporate stock; heavy filters; inconsistent grading; bad cropping; over-airbrushing.]

## 6.7 Commissioning Process
[Workflow: brief → approval → shoot → grade → DAM upload.]

---

# 7. Applications

## 7.1 Stationery

### Business Card
[Mockup + specs: format, stock, print, layout, files.]

### Letterhead
[Mockup + specs.]

### Envelope
[Mockup + specs.]

## 7.2 Digital

### Website Hero
[Mockup + specs: dimensions, type sizes, logo placement, color rule.]

### Social Media
[1080×1080 + 1920×1080 mockups + specs per platform.]

### Email Signature
[HTML + plain-text version + specs.]

## 7.3 Presentation
[Cover + content + section divider templates + specs.]

## 7.4 Print
[Brochure / report / poster — mockup + specs.]

## 7.5 [Industry-specific application]
[E.g. signage, packaging, vehicle livery — based on brand category.]

## 7.6 Templates
[Links to InDesign / Figma / PowerPoint / Canva templates.]

## 7.7 Don'ts
- Generic stock-mockup overlays
- Lorem ipsum in delivered work
- Single mockup per application type without variants
- Application without specifications

---

# 8. Tone of Voice

## 8.1 Voice
[Personality framework: 3–5 traits with anti-definitions. Or tension-pair format.]

| We are... | We are not... |
|-----------|--------------|
| [Trait] | [Opposite] |
| [Trait] | [Opposite] |
| [Trait] | [Opposite] |

## 8.2 Tone (How Voice Flexes)
[Channel matrix: how the voice shifts across website / email / social / support / legal / crisis.]

## 8.3 Vocabulary

### Words we use
[List of 10–20 brand-specific or preferred terms.]

### Words we avoid
[List of 10–20 — industry jargon, hedged corporate filler, brand-specific avoidances.]

## 8.4 Linguistic Rules
- Contractions: [preferred / avoid]
- Capitalization: [sentence case / title case]
- Punctuation: one ! per piece; curly quotes only
- Oxford comma: [yes / no]
- Numbers: spell out under 10
- Dates: [format]

## 8.5 Worked Examples — Do/Don't

| Situation | DO | DON'T |
|-----------|-----|-------|
| Product launch | [brand-voice example] | [generic example] |
| Error message | [brand-voice example] | [generic example] |
| Customer apology | [brand-voice example] | [generic example] |
| Social caption | [brand-voice example] | [generic example] |
| Subject line | [brand-voice example] | [generic example] |
| Help / support | [brand-voice example] | [generic example] |

---

# 9. Governance & Asset Locations

## 9.1 Brand Owner
[Role + name + email + Slack/Teams channel]

## 9.2 Asset Locations
- Logos: [DAM URL / shared drive path]
- Templates: [...]
- Fonts: [...]
- Photo library: [...]

## 9.3 Approval Workflow
[For new applications, partnerships, exceptions — who signs off and SLA.]

## 9.4 Update Cadence
[When this document is reviewed; how to suggest changes.]

## 9.5 Version History
| Version | Date | Changes |
|---------|------|---------|
| 1.0 | [YYYY-MM-DD] | Initial release |
