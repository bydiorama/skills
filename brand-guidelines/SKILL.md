---
name: brand-guidelines
description: >-
  Create comprehensive brand guidelines documents (also called brand books, brand manuals, design manuals, visual identity guides, corporate identity standards, or brand style guides). Use this skill whenever the user asks to build, write, draft, structure, or update brand guidelines — whether starting from a brand brief, an existing visual identity, a strategy session output, or from scratch. Trigger on phrases like "brand guidelines", "brand book", "brand manual", "design manual", "style guide", "visual identity guide", "brand standards", "corporate identity manual", "create guidelines for [brand]", "document our brand system", "write the rules for our brand", or when the user uploads logo files, color palettes, type specs, or strategy decks and asks to formalize them. Also use for partner/quick-guide subset versions and for adding a missing section (e.g. "add a tone of voice section to our guidelines"). Do NOT use for marketing campaign briefs, ad creative concepts, SEO style guides, technical writing style guides, or copywriting briefs.
---

# Brand Guidelines

Build a complete, production-ready brand guidelines document by working section-by-section through the canonical 8-section structure.

## Core principle

**Understand the brand before writing the document.** Brand guidelines must reflect the brand's actual strategy, identity, audiences, assets, and operating context. Phase 1 (context discovery) is mandatory and non-skippable.

## Workflow

Run these phases in order.

### Phase 1 — Discover the brand context [MANDATORY, do not skip]

Before writing any guideline content, build a working understanding of the brand. Open `references/02-brand-context-discovery.md` and run the discovery interview.

You need answers across six dimensions:
1. **Identity basics** — name, industry, what they do, who they serve
2. **Strategic foundation** — purpose, mission, vision, values, personality
3. **Audience and positioning** — target customers, competitors, distinctive promise
4. **Existing assets** — logo, type, color, photography, voice samples
5. **Document scope** — internal vs partner-facing, print vs screen, page tier
6. **Tone of the document itself** — should it sound like the brand, or be neutral?

If the user has provided source materials (brief, strategy doc, asset files), READ those first and only ask about real gaps. Use `AskUserQuestion` to batch related questions — never interrogate one question at a time.

Stop and confirm a written brand summary back to the user before proceeding to Phase 2.

### Phase 2 — Set scope and tier

Confirm with the user which tier fits, defaulting to **Standard** unless context says otherwise:

| Tier | Pages | Template | Use case |
|------|-------|----------|----------|
| **Compact** | 20–30 | `templates/compact-template.md` | Startup, sub-brand, partner/quick guide, supplement |
| **Standard** | 30–50 | `templates/standard-template.md` | Most established single-brand projects |
| **Comprehensive** | 60–90 | `templates/comprehensive-template.md` | Enterprise, multi-market, multi-product |

Load the matching template as the scaffold for the document. Replace bracketed placeholders with discovered content; do not deliver the document with `[brackets]` still in place.

### Phase 3 — Draft sections in canonical order

Use this eight-section order so the document moves from strategic foundations through identity rules and real-world applications to verbal expression:

| # | Section | Reference | Always? |
|---|---------|-----------|---------|
| 1 | Brand Strategy | `references/03-brand-strategy.md` | Yes (or placeholder) |
| 2 | Logo | `references/04-logo.md` | Yes |
| 3 | Typography | `references/05-typography.md` | Yes |
| 4 | Color | `references/06-color.md` | Yes |
| 5 | Graphics | `references/07-graphics.md` | Standard+ |
| 6 | Photography | `references/08-photography.md` | When assets exist; placeholder otherwise |
| 7 | Applications | `references/09-applications.md` | Yes |
| 8 | Tone of Voice | `references/10-tone-of-voice.md` | Standard+ |

**Rules:**
- Always include all 8 section slots, even if Photography or TOV are placeholder. Omitting them signals an incomplete system.
- Keep Strategy → Logo → Typography → Color in that order.
- Place Tone of Voice last so it closes the system with guidance for written expression.
- For each section: load its reference, work through the structured prompts, produce specs, then write copy in the brand's voice.

For modern extensions (motion, brand architecture, accessibility, design tokens, governance, AI policy), use `references/11-extended-elements.md`. Include for Comprehensive tier or when the brand has a digital product.

### Phase 4 — Style the document itself

The guidelines document should usually speak in the brand's voice rather than in a neutral consultant register. Use `references/12-writing-the-guidelines.md` to calibrate. The default register is **hybrid**: narrative context + precise specification, alternating between "why" and "how."

### Phase 5 — Quality check

Before delivering, validate with `references/13-quality-checklist.md`. The check explicitly screens for five critical omissions:

1. No brand strategy section
2. No tone of voice
3. Missing color specifications (HEX-only is not enough)
4. No misuse / don'ts examples
5. No photography direction

If any are present and unaddressed, flag them to the user with remediation options before delivering.

## Output format

**Default**: a single Markdown document with clear section headers, ready for conversion to .docx or for handoff to layout (Figma, InDesign).

**Per-section structure**: opening narrative (1–2 paragraphs in the brand's voice) → specifications (tables / exact values) → applications / examples → don'ts.

If the user wants a Figma-ready or InDesign-ready output, produce the Markdown content first, then ask whether to also generate Figma artboards (use `figma:figma-generate-design` skill) or handoff specs.

## Key triggers and behaviors

- **User shares a logo + asks for guidelines** → Phase 1 discovery first, do not start writing logo rules
- **User shares an existing guidelines PDF and asks to extend** → Read the existing first, then identify gaps against the five critical omissions and the quality checklist
- **User wants only one section** → Load that section's reference and produce just that section, but flag the broader gaps
- **User says "make it look like [Brand X]"** → Do not reproduce Brand X's system. Ask what they admire about it — rigor? minimalism? authority? warmth? — and apply that quality to their own brand
- **User asks for a tier different from the default** → Confirm and load the matching template

## Related skills

- `brand-strategy` — produce the strategic foundation Phase 1 depends on
- `brand-guidelines-site` — render the system as a web page instead of a document
- `anti-skill` — run the finished document through an adversarial review
