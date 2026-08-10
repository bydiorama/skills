---
name: b2b-sos-analysis
description: >
  Perform strategic B2B Share of Search (SoS) analysis for client engagements.
  Use this skill whenever the user asks to analyze Share of Search data, interpret
  SoS datasets, run a Category Entry Point (CEP) validation, assess mental/physical
  availability in B2B markets, or produce a strategic SoS interpretation for a client.
  Also trigger when the user mentions "SoS analysis", "share of search", "CEP mapping",
  "demand structure analysis", "category entry points", "mental availability audit",
  or uploads SoS datasets (trend data, query clusters, brand/non-brand queries)
  and asks for strategic interpretation. This skill covers US market analysis
  (other regions follow separately). Do NOT use for SEO audits, PPC plans,
  or performance marketing reports — this is a strategy skill, not a channel skill.
---

# B2B Share of Search — Strategic Analysis Skill

## What this skill does

Guides Claude through a disciplined, 17-step strategic interpretation of Share of Search data for B2B clients. The output is a senior-level strategic document that maps category demand structure, validates Category Entry Points (CEPs), assesses competitive mental availability, and translates findings into actionable strategic implications.

## When to read the reference files

This skill uses a two-part reference for the analytical sequence. **Always read both before starting the analysis:**

1. `references/analytical-steps-part1.md` — Steps 0–8 (foundation: scope, data hygiene, category fit, competition, demand structure, CEP validation, CEP prioritisation, serviceability, value signals)
2. `references/analytical-steps-part2.md` — Steps 9–16 (advanced: decision criteria, brand associations, segment fit, regional granularity, barriers, default choice, NO-GO zones, strategic translation)

Read Part 1 first, execute those steps, then read Part 2 and continue.

---

## Strategic context — non-negotiable framing

Share of Search is **not** a marketing KPI, campaign effectiveness metric, or competitive benchmark. In this skill it serves as:

- A **strategic research tool** for understanding how demand is structured in a category
- A lens on **mental availability** — which brands and solutions buyers think of in specific situations
- A method for **mapping the language and situations** through which buyers enter the category
- An input into **CEP validation and prioritisation**
- A basis for strategic decisions: what to build, what to capture, what to avoid

The broader B2B framework this skill sits within follows this logic:

1. Strategy starts with reality, not communication
2. Work flows from **diagnosis → strategy → actions**
3. Buyers enter purchasing through concrete situations (CEPs)
4. Brands grow when they are mentally and physically/digitally available in those situations
5. The goal is fewer, better decisions — not more activities

## Methodology rules — always enforce

### What SoS can and cannot do

| SoS can reliably... | SoS cannot reliably... |
|---|---|
| Show demand structure and share patterns | Prove mental ownership of a concept |
| Surface recurring language and situation patterns | Replace CRM, pipeline, or qualitative data |
| Identify competitive presence and gaps | Attribute causality to any single factor |
| Validate or challenge internal CEP hypotheses | Serve as a standalone brand tracker |
| Reveal value signals and decision criteria | Produce tactical SEO/PPC recommendations |

### Three confidence tiers — label every important conclusion

1. **Confirmed by data** — clear, repeated, methodologically sound signal
2. **Strong working hypothesis** — directionally consistent signal, but not fully proven
3. **Weak / cautious signal** — suggestive only; needs corroboration

Never blend these tiers. If the data is noisy, incomplete, or ambiguous, say so plainly. Do not use confident language where evidence is thin.

### Guardrails

- A strong keyword cluster is not automatically a CEP
- An open space is not automatically an opportunity
- A one-time spike is not automatically a trend
- Search association ≠ proven mental ownership
- Correlation ≠ causation
- Never produce SEO audits, PPC plans, pricing strategies, or full brand tracking as output
- You may name implications for those areas, but not pretend SoS resolves them

## Required inputs

Expect some or all of these from the user:

- SoS trend dataset (multi-year)
- Brand queries, non-brand queries, hybrid queries
- Query clusters / categorised topics
- Direct competitors list
- Aspirational competitors list
- Substitutes / alternative solutions list
- Internal CEP hypotheses
- Client notes (category, products, segments, prior workshops)
- Supplementary findings from earlier strategic modules

**If inputs are incomplete**, identify what is missing and flag which gaps are critical for interpretation before proceeding.

## Analytical sequence — overview

Execute all 17 steps in order. Do not skip any step. Read the reference files for full instructions on each.

| Step | Name | Core question |
|------|------|---------------|
| 0 | Interpretation frame | What is in scope, what is not, what can SoS answer here? |
| 1 | Data hygiene | Are the data methodologically sound enough to interpret? |
| 2 | Customer-defined category fit | Does search confirm the client's category definition? |
| 3 | Competitive field & mental standard | Who is the default choice and who sets the norm? |
| 4 | Demand structure | How does demand split across brand / non-brand / hybrid? |
| 5 | CEP validation & discovery | Which internal CEPs hold up, which are new? |
| 6 | CEP prioritisation | Which CEPs are strategically worth pursuing? |
| 7 | CEP serviceability | Can the firm actually serve each priority CEP? |
| 8 | Value signals | What type of value do buyers seek in each cluster? |
| 9 | Decision criteria & RTBs | What evidence of credibility do buyers look for? |
| 10 | Brand mental association map | What is each brand linked to in search? |
| 11 | Segment-specific CEP relevance | Are some CEPs tied to specific verticals or use cases? |
| 12 | US regional granularity | Do demand patterns differ within the US? |
| 13 | Barriers & friction | What fears, objections, and friction appear? |
| 14 | Default choice & category standard | Who is the implicit benchmark and what follows from that? |
| 15 | NO-GO zones | Where should the brand deliberately not go? |
| 16 | Strategic translation | What does all this mean for positioning, VP, brand, sales? |

## Required output structure

The final deliverable must follow this skeleton:

### A. Executive summary
7–12 most important findings. For each: what is confirmed, what is hypothesis, what is the strategic consequence.

### B. Methodological limits
What is solid, what is debatable, what needs verification.

### C. Category & demand map
Category boundaries, substitutes, demand structure, default choice.

### D. CEP evidence & priority map
Confirmed CEPs, new CEP candidates, priorities, latent spaces, NO-GO candidates.

### E. Availability & barriers overlay
What is serviceable, what is not, key friction points, key barriers.

### F. Value / criteria / RTB map
What value the market seeks, how it chooses, what credibility evidence it needs.

### G. Brand mental association map
Top competitor associations, client associations, open vs occupied territories.

### H. Strategic implications
Organise into at minimum:
- Category definition and battlefield
- CEPs
- Positioning
- Value proposition
- Brand building vs demand capture
- Sales / web / content implications
- NO-GO decisions

### Closing sections (mandatory)

1. **"Most probable picture of the market according to SoS"** — brief synthesis
2. **"Strongest strategic opportunities"** — max 5 points
3. **"What to avoid"** — max 5 points
4. **"What needs further validation"** — things SoS suggests but does not prove

## Output style rules

- Be analytical, systematic, factual
- Do not flatter the client or the data
- Do not use generic marketing phrases
- For every strong conclusion, state which data supports it
- For every uncertainty, state why it is uncertain
- The output must be usable for strategic discussion with leadership, marketing, and sales
- The goal is to reduce complexity to the right decisions — not to describe everything in the data

## What you must never do

- Confuse correlation with causation
- Draw conclusions that require CRM, pipeline, or qualitative interview data
- Produce a "keyword report" without strategic synthesis
- Ignore substitutes, default choice, or availability reality
- Recommend tactical SEO/PPC tasks as the main output
- Use absolute statements where you only have a weak signal
