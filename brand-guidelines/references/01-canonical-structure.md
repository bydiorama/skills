# Canonical Structure

The 8-section structure used by 60% of the 180-document corpus, with 96–100% consensus at the bookend positions. This is the default scaffold for every brand guidelines document.

## The eight sections

```
1. Brand Strategy        ← position consensus 96%
2. Logo                  ← 92%
3. Typography            ← 87%
4. Color                 ← 85%
5. Graphics              ← 76%
6. Photography           ← 70%
7. Applications          ← 78%
8. Tone of Voice         ← 100% (always closes)
```

**Section presence in the corpus:**

| Section | Present in | Tier |
|---------|-----------:|------|
| Color | 97.8% | Core |
| Brand Strategy | 95.0% | Core |
| Logo | 95.0% | Core |
| Applications | 94.4% | Core |
| Typography | 92.8% | Core |
| Graphics | 90.0% | Standard |
| Tone of Voice | 79.4% | Extended |
| Photography | 77.2% | Extended |

## Ordering rules

1. **Brand Strategy always opens.** No exceptions for full guidelines. Logo-only / supplement docs may skip, but full guidelines must lead with strategy.
2. **Logo always second.** "Who we are" → "Our mark."
3. **Typography → Color → Graphics → Photography → Applications** is the standard middle.
4. **Tone of Voice always closes** when present (100% consensus).
5. **Allowed swaps**: Typography ↔ Color (only). Graphics ↔ Photography (only) when the brand is photography-led.
6. **Never put Applications before the systems they apply.** Applications is a synthesis section; it requires Logo, Color, Type, and Graphics to exist first.

## Three sizing tiers

| Tier | Pages | Section depth | Use case |
|------|-------|---------------|----------|
| **Compact** | 20–30 | One spread per section, no extended elements | Startup MVP, sub-brand, partner/quick guide |
| **Standard** | 30–50 | 2–4 spreads per section, all 8 sections, basic extended elements | Most projects (corpus median = 39pp) |
| **Comprehensive** | 60–90 | 4–8 spreads per section, full extended elements (motion, architecture, accessibility, governance) | Enterprise, multi-market, public-sector, multi-product |
| Extended | 100+ | Custom | Not a template — bespoke project |

**Page count guardrails:**
- Under 20pp: feels thin unless deliberately a supplement
- 80+ pp: requires real content; padding shows
- 120+ pp: only justified by genuine multi-market / multi-product complexity

## Format

- **Default**: 1920×1080 landscape (63.5% of corpus, near-100% post-2018)
- **Alternative**: A4 portrait (27.6%, for institutional / print-production / archival)
- **Choose A4 portrait when**: heavy regulatory/legal content, designed for print production, public-sector or institutional brand, has dense long-form text

## Default section anatomy

Every section follows this internal structure:

1. **Opening narrative** — 1–2 paragraphs, in the brand's voice, explaining why this element matters and what role it plays
2. **The system** — the actual rules / specifications / framework, expressed as tables, lists, or visual specs
3. **In context** — how it appears in the wild (mockups, examples, applications)
4. **Misuse** — what NOT to do (Do/Don't pairs scoring 3.8/5 vs. Do-only at 3.1/5 and Don't-only at 2.5/5)

## Section slot table — never delete, only mark deferred

If a brand isn't ready for a section (e.g. no photography assets yet), DO NOT remove the section. Replace its content with a single placeholder spread:

> **Photography — to be developed**
> A full photography direction will be added in v2.0 of these guidelines, once the photo library is established. In the interim, defer to brand strategy for tonal direction and use the [color/typography] system to anchor any imagery used.

Documents that ship 8 slots (with placeholders) outperform documents that ship 6 sections cleanly — completeness of intent reads as system maturity.

## Cross-cutting elements

These do NOT get their own canonical section but should be threaded through:

- **Versioning + changelog** — ideally on the cover or back page
- **Contact / governance** — "who to talk to" page (see RAC E015)
- **Asset locations** — link to file repository, CMS, or DAM
- **Update cadence** — when the document is reviewed (annual / per-major-release)

## What this means for the workflow

- Always include the Logo, Color, Typography, Applications quartet — these never get cut
- Brand Strategy goes first even when thin (use `references/03-brand-strategy.md` to elicit content from the user)
- TOV is the most-skipped section in the corpus (79.4% present); push the user to include it — its inclusion correlates with a +19% quality lift
- Photography is the strongest quality differentiator (+53% delta between top and bottom-rated docs); push the user to commit to a photography direction even if the asset library doesn't yet exist
