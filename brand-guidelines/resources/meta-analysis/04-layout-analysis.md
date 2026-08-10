# Chapter 4 -- Document Layout Analysis

> Meta-analysis of 180 brand guideline documents (36 Diorama, 144 external).
> Data extracted from per-document analysis files, April 2026.

---

## 1. Page Format

### Landscape vs. portrait

The corpus splits into two dominant page orientations with a clear leader:

| Orientation | Count | % | Typical use |
|-------------|------:|------:|-------------|
| Landscape (16:9 / widescreen) | ~108 | 63.5% | Presentation-style decks, screen-first delivery |
| Portrait (A4 / US Letter) | ~47 | 27.6% | Print-first manuals, stationery-era documents |
| Square or mixed | ~15 | 8.8% | Web-native guides, hybrid formats |

**Landscape dominance is overwhelming in post-2018 documents.** Among Diorama's own 36 documents, landscape 1920x1080 is effectively the house standard -- appearing in at least 30 of 36 files. The few portrait exceptions (D003 FONA at A4, D004 Generali Balans at A4 landscape) are older deliverables or sub-brand supplements inheriting parent format conventions.

### Common dimensions

| Dimension | Format name | Frequency | Context |
|-----------|-------------|-----------|---------|
| 1920 x 1080 pts | HD / 16:9 | Dominant | Diorama standard; common across modern agencies |
| 1920 x 1008 pts | Near-HD variant | Occasional | Minor variation (e.g., D010 TECHBOX) |
| 841.89 x 595.28 pts | A4 landscape | Moderate | Traditional print manuals (D009 REMPO, older externals) |
| 595.28 x 841.89 pts | A4 portrait | Moderate | Print-production manuals, stationery-focused guides |
| 1224 x 792 pts | Custom landscape | Rare | Spotify (E100), some enterprise guides |
| US Letter (612 x 792) | 8.5 x 11" | Rare | American institutional guides (NASA, US Army Corps) |

**Key finding:** The 1920x1080 pixel dimension has become the de facto standard for brand guideline documents. It maps directly to HD screen resolution, making it native for presentation software (Keynote, Google Slides, PowerPoint) and comfortable for screen reading. However, this format creates practical friction for print reference use -- A4/Letter output requires cropping or scaling.

### Historical shift

The format evolution tracks closely with delivery medium:

- **Pre-2015:** Predominantly A4 portrait (print-production PDFs from InDesign). Examples: NASA 1976 manual, Expo 67 manual, DPD 2013, Bell System 1969.
- **2015--2019:** Mixed -- A4 portrait still common for enterprise brands (HSBC, Deutsche Bank), but presentation format emerging (D001 GameJam 2016 already at 1920x1080).
- **2020--2026:** Landscape 16:9 is the default. Portrait documents in this era are exceptions, typically either sub-brand supplements inheriting parent formats or deliberately print-first production manuals.

**Implication for the toolkit:** Generate documents at 1920x1080 as the primary format. Offer A4 portrait as an alternative for clients requiring print-first deliverables.

---

## 2. Grid and Layout Systems

Explicit grid documentation is relatively rare. Only about 25-30% of documents define a grid system for the guideline document itself or for branded layouts. When grids are documented, they fall into clear patterns.

### Column systems

| Column count | Frequency | Typical context |
|-------------|-----------|-----------------|
| 12-column | Most common | Web-native / design-systems-influenced brands (D033 NOVEBA: 12-col with 72px margin, 16px gutter; D002 SHARK: 12-col for lookbook) |
| 6-column | Common | Editorial layouts, real estate branding (D008 Marina Dorcol: 6-col equal grid; D018 Nordika: 6x10 vertical, 10x8 horizontal) |
| 3-column | Occasional | Asymmetric editorial layouts (D008 Marina Dorcol: 3-col asymmetric variant) |
| No explicit grid | Majority (~70%) | Grid is implied through consistent layouts but never documented |

### Grid documentation depth

Three tiers emerge:

1. **Full specification** (~10% of documents): Explicit column count, margin values, gutter widths, and worked examples across multiple formats. Examples: D033 NOVEBA (12-col, margin 72, gutter 16), D018 Nordika (6x10 and 10x8 grids with layout demonstrations), D008 Marina Dorcol (three grid variants with application examples).

2. **Layout demonstrations** (~20% of documents): Grid is shown through application examples (presentation slides, poster layouts, brochure spreads) without formal grid specifications. The grid is visible in the work but not codified. Examples: D002 SHARK lookbook spreads, D007 DSTRCT.BERLIN color-block compositions, Barbican (E022) with format-specific lock-up placements.

3. **No grid guidance** (~70% of documents): Layout is communicated entirely through visual examples and mockups. The implementor must reverse-engineer spacing and alignment from the applications section.

### Grid as visible brand element

A distinctive pattern in the Diorama corpus: grid lines used as decorative/brand elements rather than hidden construction.

- **D018 Nordika:** Grid lines are the primary graphic device -- visible thin rules dividing compositions appear on posters, t-shirts, notebooks, and signage, referencing the building's facade grid.
- **D032 KBT:** Crosshair grid lines overlaid on the cover and section pages, giving the document an architectural/technical drawing quality.
- **D023 PROSIGHT:** Diagonal layout principle -- logo and LightGuide placed at maximum distance, diagonally, creating a distinctive compositional rule.

This approach is rare in the external corpus. Most external brand guidelines treat grids as invisible infrastructure.

### Layout system patterns

| Pattern | Description | Examples |
|---------|-------------|----------|
| **Modular color-block** | Full-bleed color rectangles divided into halves/quadrants | D007 DSTRCT.BERLIN, D011 DSTRCT 2023, D036 Workin |
| **Diagonal split** | Angled line separating photo from color/text | D016 CORWIN chevron cut, D023 PROSIGHT diagonal placement |
| **Surface division ratios** | Explicit rules for splitting formats | D009 REMPO (1:1, 2:1, 3:2 ratios for two-color splits) |
| **Type-as-layout** | Oversized typography creates the compositional structure | D007 DSTRCT.BERLIN "Work. Eat. Meet." at extreme scale |
| **Format-specific grids** | Different grid for portrait vs. landscape | D018 Nordika (6x10 vertical, 10x8 horizontal) |

**Implication for the toolkit:** The majority of documents do not specify grids, yet the best-scoring ones do. A generated guideline should include at least a basic grid system (6 or 12 columns with margin/gutter values) as a default, with worked layout examples across 2-3 common formats (A4, 16:9 slide, social square).

---

## 3. Whitespace Philosophy

The corpus reveals two distinct whitespace philosophies, with a strong correlation to document quality and purpose.

### The spectrum

| Style | Characteristics | % of corpus | Avg quality score |
|-------|----------------|-------------|-------------------|
| **Airy / Inspirational** | Generous margins, one concept per page, section dividers on full-bleed color, imagery breathing room | ~60% | 3.8 / 5 |
| **Dense / Reference** | Compact layouts, multiple specifications per page, tables and diagrams, minimal blank space | ~25% | 3.2 / 5 |
| **Hybrid** | Airy section openers + dense specification pages | ~15% | 4.1 / 5 |

### Airy documents

The majority of modern brand guidelines (especially post-2018) adopt generous whitespace:

- **Section dividers** consume entire pages -- a solid color background with only a section title and number. This is standard in the Diorama corpus (visible in D020 ANYWHALE, D028 Eterno Cloud, D031 IN-KANAL, D032 KBT, D033 NOVEBA) and common in premium external guides (Spotify E100, Oyster E066, Bumble E061).
- **One concept per spread:** Logo construction gets its own page. Clear space gets its own page. Minimum size gets its own page. This drives higher page counts but improves scanability.
- **Large-scale visual examples** occupy 60-80% of page area, with specifications tucked into margins or footnotes.

### Dense documents

Older and institutional documents pack more information per page:

- NASA 1976 (E034): Multiple logo variations, reproduction art, and usage rules on a single spread. Efficient but requires careful reading.
- Bell System 1969 (E103): Technical specification manual with dense diagram layouts.
- DPD 2013 (E001): Web style guide with annotated wireframes, module specifications, and pixel dimensions compressed into compact pages.
- US Army Corps (E046): Reference-heavy approach typical of government/institutional guides.

### The hybrid advantage

The highest-scoring documents combine both approaches:

- **D017 Vratna** (5/5): Airy section openers and large photography, but compact specification tables for the 40 pictograms and detailed menu layouts.
- **D016 CORWIN** (4/5): Bold color-block section dividers with dense logo construction grids and mathematical spacing ratios.
- **D033 NOVEBA** (4.5/5): Full-page section dividers but then precise 12-column grid specifications and multiples-of-8 typography on detail pages.

**Correlation with quality:** Airy documents score higher on average (3.8 vs 3.2 for dense), but the highest individual scores come from hybrid approaches. Pure airiness can mask thin content; pure density sacrifices usability.

**Implication for the toolkit:** Default to the hybrid approach -- airy section openers (full-color page with section title) transitioning into specification-dense content pages. This matches both the aesthetic expectations of modern branding and the practical needs of implementors.

---

## 4. Typography Hierarchy Specifications

How documents define their type systems is one of the most revealing indicators of production quality. Three specification methods dominate.

### Specification methods

| Method | Description | % of docs with type hierarchy | Examples |
|--------|-------------|-------------------------------|----------|
| **Absolute sizes (pt/px)** | Fixed values for each level | ~45% | D008 Marina Dorcol (72/80 to 13/16), D013 Rajska (80pt to 16pt), D033 NOVEBA (136pt to 16pt), D029 Gerulata (135/120 to 14/21) |
| **Relative/percentage scale** | Base size at 100%, others as percentages | ~35% | D002 SHARK (80% to 900%), D014 Queens 2023 (80% to 300%), D016 CORWIN (80% to 300%), D025 Corvus (50% to 600%), D034 Queens 2015 (100% to 900%) |
| **Named levels only** | Weight and role specified, no sizing | ~20% | D004 Generali Balans (five weights, no sizes), D006 DEUS (weights only), many minimal external guides |

### Number of hierarchy levels

| Levels | Count | % | Assessment |
|--------|------:|------:|------------|
| 2--3 | ~25 | ~22% | Minimal; adequate for simple identities |
| 4--5 | ~40 | ~35% | Standard; covers headline through caption |
| 6--8 | ~35 | ~31% | Comprehensive; includes display, overline, footnote |
| 9--11 | ~14 | ~12% | Exhaustive; design-system level |

**The sweet spot is 5--7 levels.** This covers Display/Sequencer, Headline, Subheadline, Body, Small/Caption, and Overline -- sufficient for most applications without overwhelming implementors.

### Most common level names

Across the corpus, these names recur with high frequency:

| Level | Alternate names | Typical position |
|-------|----------------|------------------|
| **Display / Sequencer / Pre-Title** | Hero, Display 1 | Largest; 200-900% of base or 72-144pt |
| **Headline / Heading 1** | Title, Page Title | Primary heading; 150-500% or 48-80pt |
| **Subheadline / Heading 2** | Section Title, Subtitle | Secondary heading; 120-200% or 32-48pt |
| **Body / Copy** | Paragraph, Text M, Copy Medium | Base size (100%); 14-20pt |
| **Small / Caption** | Text S, Body Small, Copy Small | Below base; 60-80% or 12-14pt |
| **Overline / Label** | Tag, Caption Heading | Utility text; 60-80%, often ALL CAPS |

### Line-height conventions

| Context | Common range | Most frequent value |
|---------|-------------|---------------------|
| Display / Headlines | 0.9--1.1 | 1.0 (100%) |
| Subheadlines | 1.0--1.25 | 1.1 |
| Body text | 1.2--1.5 | 1.5 |
| Captions | 1.2--1.5 | 1.5 |

Tight line-heights (0.9--1.0) for display text and generous line-heights (1.5) for body copy is the dominant pattern. This is consistent across both Diorama and external documents.

### The percentage vs. absolute debate

**Percentage-based scales** (Diorama's preferred approach) offer format-agnostic flexibility -- the same hierarchy works on a business card, a billboard, and a website by changing only the base size. Documents using this method: D002 SHARK, D003 FONA, D014 Queens 2023, D016 CORWIN, D017 Vratna, D025 Corvus Atrium, D034 Queens 2015.

**Absolute sizes** provide immediate implementation clarity -- a designer can type "72pt, 80pt leading" directly. Documents using this method: D005 LUCRON, D008 Marina Dorcol, D012 WEM Private Fund, D013 Rajska, D018 Nordika, D021 Kolinska Distrikt, D029 Gerulata, D033 NOVEBA, D035 WEM.

**Some documents provide both** (e.g., D009 REMPO gives size/leading ratios "designed for the format at hand"), which is the most robust approach.

### Notable innovations

- **Multiples-of-8 system** (D033 NOVEBA): All type sizes designed in multiples of 8 for mathematical vertical rhythm alignment. This is a design-systems approach that ensures consistent spacing.
- **Headline multiples of 36** (D018 Nordika): Heading sizes (144, 108, 72, 36pt) follow a strict mathematical progression where each level is a multiple of 36.
- **Consistent leading multiplier** (D035 WEM): Headings at 1.25x leading, body at 1.5x -- a simple rule that governs the entire system.
- **Tracking specification** (D013 Rajska, D018 Nordika, D021 Kolinska): Some documents specify letter-spacing alongside size and leading -- -3% to -4% for headings, 0% for body, +20 for small text. This level of detail is rare but valuable.
- **Wordspacing specification** (Ogilvy E085): Min/Desired/Max wordspacing values alongside character-per-line guidance -- the most detailed typography layout rules in the corpus. Also prohibits the "gi" ligature, an exceptionally granular typographic control.
- **Proportional type sizing** (Havas E086): x/x2/x4 ratio system for type sizing, creating a mathematically clean doubling progression across scale levels.

**Implication for the toolkit:** Generate type hierarchies using the relative percentage method as the primary specification (for format flexibility), supplemented by a worked example in absolute pt values at a reference size. Include 5--7 levels as the default. Always specify line-height. Optionally include tracking for the two most extreme levels (display and small text).

---

## 5. Color Specification Depth

Color is the most universal section (97.6% of documents), but the depth of specification varies dramatically.

### Formats provided

| Format | Presence in corpus | Context |
|--------|-------------------|---------|
| **HEX** | ~95% | Near-universal; the minimum digital specification |
| **RGB** | ~85% | Standard digital; often alongside HEX |
| **CMYK** | ~75% | Print production; expected for any print-ready guide |
| **Pantone** | ~65% | Spot color matching; standard for professional brands |
| **RAL** | ~20% | Industrial/architectural; signage, vehicle livery, environmental |
| **NCS** | ~1% | Natural Color System; architectural/industrial (Network Rail E084) |
| **HSL** | ~1% | Hue-Saturation-Lightness; web-native alternative to RGB (Network Rail E084) |
| **Vinyl film codes** | ~2% | Vinyl wrapping; extremely niche (D003 FONA with Oracal 641, Network Rail E084 with film references) |

### Specification depth tiers

| Tier | Formats included | % of corpus | Quality correlation |
|------|-----------------|-------------|---------------------|
| **Minimal** | HEX only | ~15% | Avg score 2.5 |
| **Digital-ready** | HEX + RGB | ~20% | Avg score 3.0 |
| **Print-ready** | HEX + RGB + CMYK | ~25% | Avg score 3.4 |
| **Professional** | HEX + RGB + CMYK + Pantone | ~25% | Avg score 3.8 |
| **Comprehensive** | HEX + RGB + CMYK + Pantone + RAL | ~15% | Avg score 4.2 |
| **Exhaustive** | 8+ systems (RAL, NCS, Pantone, CMYK, RGB, HEX, HSL, vinyl film) | ~1% | Network Rail (E084) -- the most comprehensive color specification in the corpus |

### The Pantone/RAL threshold

Documents that include Pantone references score significantly higher on average (3.8 vs 3.0 for those without). This is not because Pantone inherently improves quality -- it signals that the creators thought about physical production, not just screen display. Similarly, RAL inclusion (found in D003 FONA, D005 LUCRON, D012 WEM Private Fund, D013 Rajska, D015 BONET-SLEEK, D016 CORWIN, D017 Vratna, D025 Corvus Atrium, D029 Gerulata, D033 NOVEBA, D036 Workin, and a handful of external enterprise guides) correlates with brands that anticipate signage, architectural, or environmental applications.

### Tint/shade systems

How documents extend their base palette:

| Approach | Description | Examples |
|----------|-------------|----------|
| **Percentage tints** | Fixed opacity steps (100%, 75%, 50%, 25%) | D002 SHARK (100/75/50/25/15/5%), D003 FONA (90/75/50/25/10%), D006 DEUS (100/75/50/25%) |
| **Named shade scales** | 3-5 named tonal steps per color family | D014 Queens 2023 (Light/Mid/Dark x 5 families), D024 WEM Wingman (100-900 scale), D012 WEM Private Fund (5-step light-to-dark ramp) |
| **Token-based naming** | Programmatic Family.Weight convention | D008 Marina Dorcol (Blue.Medium, Blue.Light, Blue.ExtraLight), D023 PROSIGHT (Grey.700 through Grey.300) |
| **No extension** | Only base colors, no tints | ~30% of corpus |

**Token-based naming** is the most forward-thinking approach and appears almost exclusively in post-2020 documents. It maps directly to CSS custom properties and design token systems.

### Color usage ratios

Explicitly defined usage ratios are rare but highly valued when present:

- D002 SHARK: Turquoise and Deep Ocean are not to be combined directly.
- D009 REMPO: 50% primary blue, 29% dark blue, 21% secondary colors (with further 10/7/3/1 breakdown).
- D016 CORWIN: Explicit approved/forbidden logo-on-background combination grid.
- D021 Kolinska Distrikt: Max 2-3 colors per layout; 2 must come from a tint pair.
- D033 NOVEBA: 70:20:10 ratio (dominant/neutral/accent).
- D035 WEM: 50% primary, 20% secondary, remaining split across accents.
- Havas (E086): 60/30/10 usage rule across 49 colors (7 families x 7 tints).

### Color naming conventions

| Convention | Examples | Frequency |
|-----------|----------|-----------|
| **Descriptive** (most common) | "Deep Ocean," "Forest Green Dark," "Marina Blue" | ~50% |
| **Industry/material** | "Safety Orange," "Industrial Gray," "Steel Blue" (D031 IN-KANAL) | ~10% |
| **Narrative/thematic** | "Cola," "Avocado," "Bubblegum" (D021 Kolinska), "Raven," "Owl," "Flamingo" (D025 Corvus) | ~5% |
| **Generic** | "Primary Blue," "Secondary 1," "Accent" | ~25% |
| **Technical** | "Grey 40%," "Neutrals.05" | ~10% |

Thematic naming (food names, bird names) is rare but creates memorable, brand-reinforcing palette identities. This is a distinctive Diorama innovation that appears in multiple recent projects.

### Minimum acceptable specification

Based on correlation with quality scores and practical usability:

- **Absolute minimum:** HEX + RGB (digital-only brands).
- **Recommended minimum:** HEX + RGB + CMYK + Pantone (any brand with print touchpoints).
- **Best practice:** HEX + RGB + CMYK + Pantone + RAL (brands with environmental/architectural applications).
- **Benchmark:** Network Rail (E084) provides 8 color specification systems (RAL, NCS, Pantone, CMYK, RGB, HEX, HSL, vinyl film) -- the most comprehensive in the corpus, surpassing even FONA's Oracal and NJ Transit's industrial systems.

**Implication for the toolkit:** Generate all five primary formats (HEX, RGB, CMYK, Pantone, RAL) by default. Include at least a 3-step tint system per color. Use token-based naming (Family.Weight) as the naming convention for the extended palette. Provide a usage ratio recommendation.

---

## 6. Visual Examples vs. Written Rules

The balance between showing and telling varies considerably and tracks with both era and quality.

### The spectrum

| Approach | Characteristics | % of corpus |
|----------|----------------|-------------|
| **Show-heavy** | Extensive mockups and visual examples, minimal written specifications | ~35% |
| **Tell-heavy** | Dense written rules, construction grids, mathematical specifications | ~15% |
| **Balanced** | Visual examples with corresponding written specifications | ~50% |

### Do/don't examples

| Element | "Don'ts" present | % |
|---------|-----------------|---:|
| Logo misuse | ~112 of 180 | 62% |
| Color misuse | ~52 of 180 | 29% |
| Typography misuse | ~26 of 180 | 14% |
| Photography misuse | ~32 of 180 | 18% |

**Logo misuse** is the most commonly included don't section. Typical prohibited behaviors (appearing in 90%+ of logo don't sections):
1. Non-proportional scaling (stretch/squash)
2. Rotation
3. Unauthorized color changes
4. Low-contrast background placement
5. Placement on busy photography without overlay
6. Enclosure in unauthorized shapes

Fewer documents include don'ts for color, typography, or photography. When they do, it correlates with higher quality scores.

### Photography do/don't depth

Documents that include explicit photography avoidance rules stand out:

- **D016 CORWIN:** Avoid bright/saturated colors, stock-feel imagery, staged portraits, food photography, vivid sunsets.
- **D018 Nordika:** No low-quality photos, no high-contrast/overexposed images, no meaningless stock, no overly complicated compositions.
- **D033 NOVEBA:** Forbidden: generic stock with artificial feel, staged handshake-into-camera poses, cold/sterile lighting. Required: warm tones, correct verticals, depth of field.
- **D025 Corvus Atrium:** Avoid cool color schemes, overly emotive expressions, poor composition.
- **Havas (E086):** Photography principles with explicit prohibitions -- a structured approach to image direction within a broader 60/30/10 usage framework.

These specific, actionable don'ts are far more useful than vague "use high-quality photography" guidance.

### Visual example categories in application sections

| Application type | Frequency across corpus |
|-----------------|------------------------|
| Business cards | ~80% |
| Letterhead / stationery | ~70% |
| Social media posts | ~65% |
| Presentation slides | ~55% |
| Billboard / OOH | ~50% |
| Email signature | ~50% |
| Roll-up / banner | ~45% |
| Website mockup | ~40% |
| Merchandise (apparel) | ~40% |
| Vehicle livery | ~25% |
| Wayfinding / signage | ~20% |
| Menu / on-site materials | ~10% |
| Packaging | ~15% |

Business cards remain the most universally included application example, followed by letterhead and social media. Newer documents increasingly include social media templates and display ad formats, while older documents emphasize stationery.

**Implication for the toolkit:** Include both visual mockups and written specifications for every rule. Logo misuse examples (6 standard don'ts) should be generated by default. Include at minimum: business card, social post, and one large-format application (billboard or presentation slide) as worked examples.

---

## 7. Toolkit Implications -- Layout Recommendations for Generated Guidelines

Based on the patterns observed across 180 documents, these are the recommended defaults for auto-generated brand guideline documents.

### Document format

| Parameter | Recommended default | Rationale |
|-----------|-------------------|-----------|
| **Page dimensions** | 1920 x 1080 px (landscape 16:9) | 63.5% of corpus; native to screen presentation; Diorama standard |
| **Alternative format** | A4 portrait (210 x 297 mm) | For print-first clients; 27.6% of corpus |
| **Export format** | PDF, RGB color space | Universal compatibility |

### Grid system

| Parameter | Recommended default | Rationale |
|-----------|-------------------|-----------|
| **Column count** | 12-column | Most flexible; divisible by 2, 3, 4, 6; matches web conventions |
| **Margins** | 72 px (at 1920 width) = 3.75% | Matches D033 NOVEBA; provides generous breathing room |
| **Gutters** | 16 px | Matches D033 NOVEBA; tight enough for efficient layouts |
| **Layout demonstrations** | 3 format examples (16:9, A4, square) | Covers presentation, print, and social media |

### Whitespace and page structure

| Parameter | Recommended default | Rationale |
|-----------|-------------------|-----------|
| **Section dividers** | Full-bleed color page with section number + title | Hybrid approach (airy openers + dense content) scores highest |
| **Content density** | One primary concept per page; specifications in sidebar/footer | Matches the dominant airy style while preserving information density |
| **Page count target** | 40--60 pages | Median is 41pp; 40-60 covers the standard use case |

### Typography hierarchy

| Parameter | Recommended default | Rationale |
|-----------|-------------------|-----------|
| **Specification method** | Relative percentages (primary) + worked pt example (secondary) | Percentage method enables format flexibility; absolute example aids implementation |
| **Number of levels** | 6 | Display, Headline, Subheadline, Body, Small, Overline -- covers 95% of use cases |
| **Line-height rules** | Display: 1.0, Headings: 1.1, Body: 1.5 | Matches the dominant pattern across corpus |
| **Include tracking** | Yes, for Display (-2 to -4%) and Small (+1 to +2%) | Found in highest-quality documents; adds production value |

### Color specification

| Parameter | Recommended default | Rationale |
|-----------|-------------------|-----------|
| **Formats** | HEX, RGB, CMYK, Pantone (4 minimum) | "Professional" tier; correlates with 3.8+ quality scores |
| **Add RAL** | Yes, for brands with physical/environmental touchpoints | 20% of corpus includes RAL; high quality correlation |
| **Tint system** | 3-step (Light / Base / Dark) per color family | Balances flexibility with simplicity |
| **Naming** | Token-based (Family.Weight) | Forward-compatible with design systems / CSS variables |
| **Usage ratio** | Include a recommended ratio (e.g., 60:30:10) | Found in highest-quality documents; aids consistent application |

### Visual examples and rules

| Parameter | Recommended default | Rationale |
|-----------|-------------------|-----------|
| **Logo don'ts** | 6 standard misuse examples | 65% of corpus includes logo don'ts; 6 is the modal count |
| **Application mockups** | Minimum 5: business card, social post, presentation slide, email signature, one large-format | Covers the top-5 most frequent application categories |
| **Photography don'ts** | Include if photography section exists | Specific avoidance rules score higher than vague "quality" guidance |
| **Color combinations** | Approved/forbidden grid | Found in best-practice documents (CORWIN, NOVEBA, Corvus Atrium) |

### Production considerations

| Parameter | Recommended default | Rationale |
|-----------|-------------------|-----------|
| **File size target** | < 30 MB for 40-60 pages | Multiple documents in corpus suffer from bloat (D028 Eterno Cloud at 315 MB, D012 WEM Private Fund at 333 MB); optimize raster assets. The Shed (E149) demonstrates extreme text-to-size efficiency: 120 pages at only 2.0 MB. |
| **Authoring tool** | Adobe InDesign (export to PDF) | Dominant tool across both corpora; PDF/X-4 for print-ready |
| **Internal navigation** | Table of contents with page numbers; numbered section dividers | Standard across well-structured documents; improves usability |
| **Breadcrumb/header** | Section name in running header | Found in best-practice documents (D030 IMS, enterprise guides) |

---

## Summary of Key Findings

1. **Landscape 16:9 (1920x1080) is the modern default** (across 180 documents) for brand guideline documents, with A4 portrait as a legacy/print alternative. The toolkit should generate landscape-first.

2. **Most documents do not formally specify grids**, but the highest-scoring ones do. A 12-column grid with explicit margin/gutter values should be included by default.

3. **The hybrid whitespace approach scores highest:** airy section openers (full-color divider pages) combined with specification-dense content pages. Pure airiness inflates page counts without adding value; pure density reduces usability.

4. **Typography hierarchies work best with 5--7 levels** specified in relative percentages. The percentage method is Diorama's standard and enables format-agnostic scaling. Always include line-height; tracking specification for extreme sizes adds production value.

5. **Four color formats (HEX, RGB, CMYK, Pantone) represent the professional minimum.** RAL should be added for brands with environmental/architectural applications. Token-based naming and 3-step tint scales are best practice.

6. **Logo misuse examples are the most common "don't" section** (65% of corpus). Photography and color don'ts are rarer but correlate with higher quality. The toolkit should generate 6 standard logo misuse examples by default.

7. **The best documents combine visual mockups with written specifications** for every rule. Neither pure visual demonstration nor pure textual specification is optimal alone.
