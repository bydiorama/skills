# Chapter 3 -- Document Structure Patterns

> Meta-analysis of 180 brand guideline documents (36 Diorama, 144 external).
> Data extracted programmatically from per-document analysis files, April 2026.

---

## 1. Section Frequency

How often does each of the eight canonical sections appear with substantive content (i.e., not marked "Not covered")?

| Rank | Section | Present | of 180 | % |
|------|---------|--------:|-------:|------:|
| 1 | Color | 176 | 180 | 97.8% |
| 2 | Brand Strategy | 171 | 180 | 95.0% |
| 3 | Logo | 171 | 180 | 95.0% |
| 4 | Applications | 170 | 180 | 94.4% |
| 5 | Typography | 167 | 180 | 92.8% |
| 6 | Graphics | 162 | 180 | 90.0% |
| 7 | Tone of Voice | 143 | 180 | 79.4% |
| 8 | Photography | 139 | 180 | 77.2% |

**Key findings:**

- The top six sections (Color through Graphics) all exceed 90%, forming the structural backbone of brand guidelines regardless of industry, size, or era.
- **Color is the single most universal section** (97.8%), ahead of even Logo. Only four documents in the entire corpus omit color guidance -- all are narrowly scoped supplements (TOV documents or partially sampled guides).
- **Photography is the most commonly omitted** standard section (77.2%). This makes sense: photography requires existing image libraries, shoot direction, or stock curation -- assets that many brands lack at the time of guideline creation.
- **Tone of Voice** sits at 79.4%, meaningfully below the visual identity sections. Many documents -- particularly older ones and those from design-led agencies -- treat brand guidelines as a purely visual exercise. Specialized documents like Ogilvy Typography (E085, a typography-only addendum) naturally omit verbal identity entirely.
- The gap between the top six sections (90-98%) and the bottom two (77-79%) suggests a natural division: visual identity fundamentals vs. extended brand system.

### Tier structure (empirical)

| Tier | Sections | Frequency |
|------|----------|-----------|
| **Core** (near-universal) | Color, Logo, Brand Strategy, Applications | 94-98% |
| **Standard** (expected) | Typography, Graphics | 90-93% |
| **Extended** (common but not assumed) | Tone of Voice, Photography | 77-79% |

---

## 2. Page Count Distribution

Page counts were extractable from 94 of 180 documents (52%). The remaining 86 either did not record total pages in the analysis or were partially sampled.

| Category | Pages | Count | % of known |
|----------|-------|------:|-----:|
| Short | < 20 pp | 19 | 20.2% |
| Medium | 20--59 pp | 45 | 47.9% |
| Long | 60--120 pp | 23 | 24.5% |
| Epic | > 120 pp | 7 | 7.4% |

**Statistical summary (n=94):**

| Metric | Value |
|--------|-------|
| Minimum | 10 pp |
| Q1 (25th percentile) | 22 pp |
| Median | 39 pp |
| Mean | 52.5 pp |
| Q3 (75th percentile) | 72 pp |
| Maximum | 192 pp |

**Key findings:**

- The **median brand guidelines document is 39 pages**. This is the realistic center of gravity -- not the 100+ page epics that dominate design award portfolios.
- Nearly half (47.9%) fall in the 20--59 page range, making "Medium" the dominant category by a wide margin.
- Only 7.4% exceed 120 pages. These are invariably enterprise-scale brands (HSBC at 181pp, Virgin Media at 150pp, Hulu at 138pp) with complex multi-market, multi-product needs.
- Short documents (< 20pp) are not necessarily low quality. They include focused partner guides (Uber at 10pp, scored 3/5), tight visual identity summaries, and multi-state reactive logo specs (SuperHi at 10pp). At the other extreme, The Shed at 120 pages uses a conceptual art framework to justify its length.
- The mean (52.5pp) is pulled upward by the Epic outliers. Median (39pp) is a more honest benchmark.

**Implication for the toolkit:** A default template targeting 30--50 pages would serve the majority use case (matching the median of 39pp). Epic-scale documents are custom projects, not template candidates.

---

## 3. Section Ordering

Among the 163 documents with six or more sections, the ordering is remarkably consistent.

### Dominant sequence

```
Brand Strategy > Logo > Typography > Color > Graphics > Photography > Applications > Tone of Voice
```

This exact eight-section order appears in **93 documents (60.0%)** -- a clear majority. No alternative ordering exceeds 8.4%.

### Top ordering variants

| Count | % | Ordering |
|------:|------:|----------|
| 93 | 60.0% | Strategy > Logo > Type > Color > Graphics > Photo > Applications > TOV |
| 13 | 8.4% | Strategy > Logo > Type > Color > Photo > Applications > TOV *(Graphics omitted)* |
| 12 | 7.7% | Strategy > Logo > Type > Color > Graphics > Applications > TOV *(Photo omitted)* |
| 10 | 6.5% | Strategy > Logo > Type > Color > Graphics > Photo > Applications *(TOV omitted)* |

The top four patterns account for 82.6% of all documents. The remaining 17.4% are distributed across 16 minor variants, none exceeding 2.6%.

### Position consensus

What section appears most often at each position?

| Position | Most common section | Consensus |
|----------|-------------------|-----------|
| 1st | Brand Strategy | 96% |
| 2nd | Logo | 92% |
| 3rd | Typography | 87% |
| 4th | Color | 85% |
| 5th | Graphics | 76% |
| 6th | Photography | 70% |
| 7th | Applications | 78% |
| 8th | Tone of Voice | 100% |

**Key findings:**

- **Brand Strategy always opens.** 96% consensus at position 1. The remaining 4% are logo-only or minimal-scope documents that skip strategy entirely.
- **Logo always follows Strategy.** 92% at position 2. This reflects the natural logic of: "Here's who we are" followed by "Here's our mark."
- **Typography before Color** is the standard (87% vs. 85%), though some guides swap these -- the two are near-interchangeable in position.
- **Tone of Voice invariably closes.** 100% consensus at position 8 when present. It is the verbal capstone to a visual document.
- **Graphics and Photography** show the most positional variance (76% and 70%), suggesting these "supporting visual" sections are the most flexible in placement.

**The canonical order is not arbitrary** -- it follows a logical narrative: strategy (why) > identity mark (what) > typographic system (how text looks) > color system (how it feels) > graphic elements (decoration/enrichment) > photography (real-world imagery) > applications (everything in context) > voice (how it sounds).

---

## 4. Completeness vs. Quality

Does covering more sections lead to a higher quality score?

| Sections covered | Documents | Avg. score | Score range |
|-----------------:|----------:|-----------:|------------:|
| 2 | 3 | 4.33 | 4.0--5.0 |
| 4 | 4 | 3.25 | 3.0--4.0 |
| 5 | 8 | 2.75 | 2.0--3.0 |
| 6 | 15 | 3.07 | 2.0--4.0 |
| 7 | 38 | 3.38 | 2.0--5.0 |
| 8 | 102 | 3.99 | 2.0--5.0 |

**Pearson correlation: r = 0.34** (weak-to-moderate positive)

**Key findings:**

- There is a positive relationship between completeness and quality, but it is not strong. Covering all eight sections does not guarantee a high score, nor does covering fewer sections doom a document.
- The **2-section outlier** (avg. 4.0) reflects TOV supplements -- narrow scope, high execution within that scope (notably IKEA TOV at 4.0/5).
- The real quality cliff is between 5 and 6 sections: documents with only 5 sections average just 2.69/5. This suggests a **minimum threshold around 6 sections** for a document to feel "complete enough" to score well.
- 8-section documents average 3.99/5 -- essentially 4.0. But with a range of 2.0--5.0, covering all sections is necessary but not sufficient. **Execution quality matters more than checkbox completeness.**

### What separates top-rated from low-rated?

Comparing the 32 highest-rated documents (score >= 4.5) against the 16 lowest-rated (score <= 2.5):

| Section | Top-rated (>=4.5) | Low-rated (<=2.5) | Delta |
|---------|------------------:|------------------:|------:|
| Brand Strategy | 100% | 94% | +6% |
| Logo | 100% | 100% | 0% |
| Typography | 100% | 88% | +12% |
| Color | 100% | 100% | 0% |
| Graphics | 100% | 88% | +12% |
| **Photography** | **97%** | **44%** | **+53%** |
| Applications | 97% | 100% | -3% |
| **Tone of Voice** | **94%** | **75%** | **+19%** |

**The biggest differentiator is Photography** (+53% delta). Top-rated documents almost universally include photography direction; low-rated documents omit it more than half the time. This makes intuitive sense: photography guidelines require sophistication and investment, and their presence signals a mature, considered brand system.

**Tone of Voice** is the second-largest differentiator (+19%). Including verbal identity guidance correlates with a more holistic, higher-quality approach.

Logo, Color, and Applications show zero or near-zero delta -- these sections are universal regardless of quality.

---

## 5. Document Types

Based on content analysis, scope, and explicit document type declarations, the 180 documents fall into seven categories:

| Type | Count | % | Avg. sections | Avg. score |
|------|------:|----:|--------------:|-----------:|
| **Full Brand Guidelines** | 125 | 69.4% | 7.5 | 3.76 |
| **Partner / Quick Guide** | 30 | 16.7% | 7.2 | 3.50 |
| **Standards Manual** | 16 | 8.9% | 7.2 | 4.06 |
| **Visual Identity (Minimal)** | 4 | 2.2% | 4.5 | 2.70 |
| **TOV Supplement** | 3 | 1.7% | 2.7 | 3.75 |
| **Typography Supplement** | 1 | 0.6% | 2.0 | 5.00 |
| **Digital Style Guide** | 1 | 0.6% | 7.0 | 3.00 |

### Type definitions

**Full Brand Guidelines** (69.4%) -- The default. Comprehensive documents covering most or all sections with original content. Created for internal teams. Includes both Diorama-produced and externally sourced examples.

**Partner / Quick Guide** (17.1%) -- Simplified versions created for external partners, sponsors, or third-party vendors. Typically shorter, focused on "don't mess up the logo and colors" rather than deep brand immersion. Notable examples: Uber (10pp), Snapchat, TikTok, Apple partner materials.

**Standards Manual** (8.9%) -- Older-format or highly systematic design standards documents. Often more rigid and rule-driven than contemporary brand guidelines. Score highest on average (4.06/5), likely because the format demands precision. Notable examples: NASA, Bell System, US Army Corps, NJ Transit, Network Rail (E084, whose 30-page single-symbol specification with 8 color systems and 24 misuse examples epitomizes the format).

**Visual Identity (Minimal)** (2.4%) -- Bare-bones visual identity documents covering logo, color, and perhaps typography, with little else. Lowest average score (2.7/5). These feel incomplete rather than intentionally focused.

**TOV Supplement** (1.8%) -- Standalone tone of voice documents, designed as companions to a separate visual identity guide. Naturally cover only 2-3 of the eight sections but can be high quality within their scope (IKEA TOV at 4.0/5, Titans TOV).

**Typography Supplement** (0.6%) -- Standalone typography documents designed as companions to a separate main brand guide. Ogilvy Typography (E085, 38pp, 5/5) is the sole example: a COLLINS+MCKL-commissioned custom typeface system with detailed specifications including a "gi" ligature prohibition -- the most granular typographic rule in the corpus.

**Digital Style Guide** (0.6%) -- Web/digital-focused style documents covering UI patterns, grids, and digital-specific considerations. Only one example in corpus (DPD Web Style Rules).

### Diorama vs. External

| Metric | Diorama (n=36) | External (n=144) |
|--------|---------------:|------------------:|
| Avg. sections covered | 7.42 | 7.20 |
| Avg. quality score | 3.82 | 3.68 |
| Avg. page count | 45.4 pp | 53.8 pp |

Diorama documents are slightly more complete and slightly higher rated, while being shorter on average. This suggests efficient, well-structured documents -- more sections in fewer pages.

---

## 6. Minimum Viable Guide

Based on frequency analysis, quality correlations, and the tier structure that emerged from the data, here is the empirical division between essential and optional sections:

### Essential (must-have) -- present in 92-98% of all documents

| Section | Why essential |
|---------|---------------|
| **Color** | Most universal section (97.6%). Enables consistent brand expression across all media. |
| **Brand Strategy** | Sets context for every decision. Present in 95.9% and at position 1 in 96% of documents. |
| **Logo** | The primary brand identifier. 95.3% presence. Without logo rules, everything else is moot. |
| **Applications** | Demonstrates the system in action. 95.3%. Without applications, guidelines remain theoretical. |
| **Typography** | Defines how text looks. 92.4%. Critical for any brand that communicates in writing (i.e., all of them). |
| **Graphics** | Supporting visual language. 90.6%. Includes iconography, patterns, graphic devices -- the connective tissue of a visual identity. |

### Nice-to-have -- present in 78-82% of documents, but strongly correlated with quality

| Section | Why valuable |
|---------|-------------|
| **Tone of Voice** | Present in 82.4%. The +19% delta between top and low-rated documents suggests it signals brand maturity. A full brand system is incomplete without verbal guidance, but many visual-design-led guidelines omit it. |
| **Photography** | Present in 78.8%. The +53% delta between top and low-rated documents makes this the single strongest quality predictor. However, it requires existing photography assets or shoot direction, making it harder to include in early-stage brand work. |

### The minimum viable guide

A **6-section document** (the six essential sections) represents the floor for a credible brand guidelines document. Documents with 5 or fewer sections average only 2.69/5, while 6-section documents jump to 3.04/5.

However, the data strongly suggests that **8 sections is the target** -- documents covering all eight average 3.99/5, and the two "nice-to-have" sections are the strongest quality differentiators.

**Recommended minimum:** All six essential sections, with Photography and TOV added when assets and content are available. Never omit them from the template structure -- instead, include them as placeholder sections that signal to the client what the complete system should eventually contain.

---

## 7. Toolkit Implications -- Recommended Default Template Structure

Based on the empirical evidence from 180 documents, here is the recommended default template:

### Template structure

```
1. Brand Strategy        [ALWAYS -- position 1, 96% consensus]
2. Logo                  [ALWAYS -- position 2, 92% consensus]
3. Typography            [ALWAYS -- position 3, 87% consensus]
4. Color                 [ALWAYS -- position 4, 85% consensus]
5. Graphics              [ALWAYS -- position 5, 76% consensus]
6. Photography           [WHEN AVAILABLE -- position 6, 70% consensus]
7. Applications          [ALWAYS -- position 7, 78% consensus]
8. Tone of Voice         [WHEN AVAILABLE -- position 8, 100% consensus]
```

### Template sizing

| Tier | Target pages | Use case |
|------|-------------|----------|
| **Compact** | 20--30 pp | Startups, sub-brands, quick-turnaround projects |
| **Standard** | 30--50 pp | Most brand guidelines projects (matches the median of 39pp) |
| **Comprehensive** | 60--90 pp | Enterprise brands, multi-market systems |
| **Extended** | 100+ pp | Custom projects -- not template candidates |

### Design decisions supported by data

1. **Always include all eight section slots**, even when Photography or TOV content is not yet available. Use "To be developed" placeholders rather than omitting sections. This signals completeness of intent and raises the perceived quality of the document.

2. **Never reorder the top four.** Brand Strategy > Logo > Typography > Color is fixed in 85%+ of documents. Breaking this order would feel wrong to anyone who has read more than a few brand guidelines.

3. **Graphics and Photography are the most flexible** in positioning. If a brand's identity is heavily photographic, Photography could move up to position 5, pushing Graphics to 6. The data supports this variant (13 documents, 8.4%).

4. **Tone of Voice always closes.** 100% consensus when present. It provides a verbal conclusion to a visual document. Do not place it mid-document.

5. **Target 30--50 pages for the standard template.** This is where 47.9% of real-world guidelines land, and it is sufficient to cover all eight sections with meaningful depth. Going under 20 pages risks feeling thin; going over 60 is rarely necessary unless the brand demands it.

6. **Photography is the quality lever.** The +53% delta between top and low-rated documents makes photography direction the single most impactful "upgrade" to a guidelines document. When budgets allow, invest in photography guidance.

7. **Standalone supplements are a valid format.** Three documents in the corpus exist as standalone TOV guides, and one (Ogilvy Typography, E085) exists as a standalone typography supplement. If verbal identity or typographic work happens separately from visual identity, a standalone supplement (10--40pp) is an established format.

---

## Appendix: Data Coverage Notes

- **Page counts** were extractable from 94 of 180 documents (52.2%). The remaining documents either did not record total pages or were partially sampled during analysis.
- **Quality scores** were available for 168 of 180 documents (93.3%). The 12 unscored documents are all Diorama-produced files that used a sub-score format (Comprehensiveness / Visual execution / Practical usability / Innovation) without a composite; where possible, these were averaged into a single score.
- **Section detection** used pattern matching across multiple header variants (e.g., "Color" / "Colour" / "Color Palette"; "Graphics" / "Iconography" / "Illustration") with "Not covered" / "Not addressed" / "Not included" filtering. Edge cases (sections partially covered or mentioned in passing) may cause minor over- or under-counting, estimated at +/- 2-3%.
- **Document type classification** is inferred from content patterns rather than explicit metadata (only 9 documents had a formal "Document Type" field). The partner/quick guide category is the least precise, as some full guidelines mention "partner" contexts without being partner-specific documents.
