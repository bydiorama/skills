---
name: b2b-icp
description: >
  Build domain-agnostic B2B Ideal Customer Profiles (ICPs) and Buyer Personas
  from four input lenses: competitor data, company (internal) data, market data,
  and search/intent data. Use this skill whenever the user asks to build, define,
  refine, validate, sharpen, or document an ICP, a Buyer Persona, a target
  account profile, a target audience definition, or a "who is our ideal customer"
  strategy deliverable. Also trigger on: "ICP", "ideal customer profile",
  "buyer persona", "target account", "customer profile framework",
  "negative ICP", "ICP scoring", "firmographics + technographics synthesis",
  "jobs-to-be-done for B2B", "buying triggers", or when the user uploads
  CRM exports, closed-won/lost lists, competitor analyses, market research,
  SoS/keyword datasets, or survey data and asks for an ICP. This skill is
  category-agnostic — it works for SaaS, services, industrial, fintech, and
  other B2B categories. Do NOT use for: B2C consumer personas, media audience
  planning, SEO keyword prioritisation, campaign briefs, or creative concepts.
  This is a strategy skill, not a channel or creative skill.
---

# B2B Ideal Customer Profile — Strategic Definition Skill

## What this skill does

Guides Claude through a disciplined, 9-phase construction of a B2B Ideal Customer Profile (ICP) and its companion Buyer Persona. The output is a senior-level strategic deliverable that defines **which companies to pursue** (ICP), **who to talk to inside them** (Persona), **what job they are hiring a solution for** (Jobs-to-be-Done), **what pains and triggers open the buying window**, and **what language actually reaches them**.

The skill is **domain-agnostic**: it makes no category assumptions. It adapts to SaaS, professional services, industrial B2B, fintech, healthtech, and other categories by changing which inputs dominate — not by changing the framework.

## When to read the reference files

This skill uses three reference files. **Always read all three before starting the analysis:**

1. `references/icp-framework.md` — the canonical 6-layer model (Firmographics → Persona → Jobs-to-be-Done → Pains → Triggers → Language). Field definitions, the ICP/Persona/JTBD distinction, and the negative ICP concept.
2. `references/data-synthesis.md` — how to extract signal from each of the four input lenses (competitor, company, market, search) and which layer of the framework each lens primarily feeds.
3. `references/icp-template.md` — the filled-template output format, field-by-field writing guidance, worked example, and the confidence-tier labelling rules.

Read them in order. Do not start drafting fields without them loaded.

---

## Strategic context — non-negotiable framing

An ICP is **not** a marketing segment, a lead list, or a wishlist. In this skill it serves as:

- A **company-level filter** that defines which organisations are worth pursuing
- A **prioritisation tool** that ranks accounts by fit and timing, and by what to *exclude*
- A **shared source of truth** for sales, marketing, product, and customer success
- An **input to positioning and messaging** — but never a substitute for them
- A **living document**, not a one-time artifact — it is reviewed quarterly against closed-won/lost reality

The ICP sits inside a three-layer B2B targeting stack:

| Layer | Question it answers | Grain |
|---|---|---|
| **ICP** | Which companies should we pursue? | Company / account |
| **Buyer Persona** | Who inside those companies do we talk to, and how? | Individual / role |
| **Jobs-to-be-Done** | What outcome are they hiring a solution to produce? | Situation / motivation |

Keep these three layers distinct. Collapsing them produces vague deliverables that no team can action.

## Methodology rules — always enforce

### What an ICP can and cannot do

| An ICP can reliably... | An ICP cannot reliably... |
|---|---|
| Define which accounts qualify for outbound effort | Predict individual-deal outcomes |
| Align sales, marketing, product, CS on a target | Replace qualitative discovery calls |
| Surface negative-ICP patterns (who to exclude) | Serve as a messaging document |
| Ground segmentation in firmographic + behavioural fact | Substitute for a positioning or value proposition |
| Unlock ranked account lists when paired with intent data | Generate creative or channel plans |

### Three confidence tiers — label every important claim

1. **Confirmed by data** — repeated, cross-source signal (e.g. closed-won pattern corroborated by competitor base and market research)
2. **Strong working hypothesis** — directionally consistent signal from ≥2 sources but not yet proven
3. **Weak / cautious signal** — suggestive only; from one source or a small sample; needs validation

Never blend tiers. If the data is thin, say so plainly. A Persona built from three closed-won interviews is a hypothesis, not a confirmed truth.

### Guardrails

- A big customer is not automatically an ICP customer — revenue ≠ fit
- A competitor's customer base is a *signal*, not a prescription
- A high-volume keyword is not automatically a CEP or a trigger
- "We could serve them" ≠ "we should target them" — capacity to serve does not imply strategic fit
- An ICP without a **negative ICP** (exclusions) is incomplete
- A Persona without **Jobs-to-be-Done** is a demographic card, not a targeting tool
- Triggers without **observable signals** are folklore — each trigger must have a detection method
- Never use consumer persona templates (lifestyle, hobbies) as the core of a B2B Persona

## Required inputs — the four lenses

Expect a mix of the following. Not all clients will have all four; identify gaps and flag which are critical before proceeding.

### Lens 1 — Company (internal) data
- Closed-won accounts (ideally ≥20, with revenue, deal size, sales cycle, CS health)
- Closed-lost accounts with disqualification reasons
- Churn / downgrade list with reasons
- Current customer base segmented by tier, industry, size
- Sales team account notes, discovery-call recordings or transcripts
- CS / support tickets (recurring themes)
- Product usage data (if SaaS/digital) — who gets value, who churns
- Internal ICP/persona hypotheses already documented

### Lens 2 — Competitor data
- Direct competitor list (and their positioning)
- Aspirational / adjacent competitors
- Substitutes (the "do-nothing" or "build-in-house" alternative)
- Competitor case studies, customer logos, G2/Capterra reviews
- Competitor pricing pages and packaging
- Competitor job ads (reveals who they sell to and what they build)

### Lens 3 — Market data
- Category sizing and growth by segment
- Vertical / industry trend reports
- Regulatory and macro shifts affecting the category
- Analyst frameworks (Gartner, Forrester, IDC) when available
- Trade press, industry association data
- Survey data from target industries

### Lens 4 — Search / intent data
- Share-of-Search datasets (if available — see `b2b-sos-analysis` skill)
- Keyword clusters (brand / non-brand / comparison / pain-led)
- Search trend data and seasonality
- Intent data (G2, Bombora, 6sense, Demandbase — account-level intent scores)
- Hiring signals, funding signals, leadership-change signals (trigger detection)
- Website analytics: what content ICP-fit visitors consume

**If inputs are incomplete**, name what is missing, flag which gaps are critical, and state explicitly which parts of the ICP will be **hypothesis** rather than **confirmed** as a result. Proceed — but do not paper over the gap.

---

## Analytical sequence — 9 phases

Execute all 9 phases in order. Each phase either produces a layer of the framework or validates it. Read `references/icp-framework.md` and `references/data-synthesis.md` for detailed instructions per phase.

| Phase | Name | Core question | Primary lens |
|---|---|---|---|
| 0 | Scope & intake | What decision does this ICP need to support? What inputs do we have? | — |
| 1 | Closed-won pattern mining | Which existing customers get the most value, and what do they share? | Company |
| 2 | Competitive base triangulation | What patterns appear across competitor customer bases that differ from ours? | Competitor |
| 3 | Market fit sizing | Where is the TAM large enough and trending in our favour? | Market |
| 4 | Firmographics layer | Industry, size, revenue, geography, tech environment, stage — with thresholds | Company + Market |
| 5 | Buyer Persona layer | Role, seniority, reports-to, goals, psychographics, channels — per key buying-committee role | Company + Competitor |
| 6 | JTBD & pains layer | What job are they hiring the solution for? What pains block progress? | Company + Search |
| 7 | Triggers & signals layer | What observable events open the buying window? How do we detect them? | Search + Market |
| 8 | Negative ICP & disqualifiers | Who is explicitly *not* an ICP? What are the no-go zones? | Company (lost/churn) |
| 9 | Validation & activation | Does this ICP hold up against closed-won reality? How will teams use it? | All |

Phases 1–3 are **diagnosis** (reading signal from the four lenses).  
Phases 4–8 are **synthesis** (writing the ICP layers).  
Phase 9 is **validation** (does the profile survive contact with reality?).

---

## Required output structure

The final deliverable must follow this skeleton. Field definitions and writing guidance are in `references/icp-template.md`.

### A. Executive summary
5–8 sentences. Who the ICP is, who it is not, and the single most important pattern that defines fit.

### B. Methodological note
What inputs were used, what was missing, which parts of the ICP are confirmed vs hypothesis.

### C. Ideal Customer Profile (company layer)
- **Firmographics**: Industry, Company size, Revenue, Location, Tech environment (+ stage/ownership if relevant)
- **Qualifying thresholds**: explicit cut-offs (e.g. ≥200 employees, ≥$20M ARR, HQ in US/EU)
- **Fit signals**: observable attributes that predict success (e.g. uses Salesforce + has a RevOps team)

### D. Buyer Persona(s) (individual layer)
For each key buying-committee role (typically 2–4):
- **Role** and **Reports to**
- **Demographics** (role-relevant: seniority, tenure, team size, budget authority)
- **Psychographics** (motivations, fears, what they are measured on)
- **Communication channels** (where they actually consume information)

### E. Jobs to be Done
Table: `JTBD | Frequency | Importance`. Each JTBD phrased as an outcome, not a feature. 3–6 JTBDs per primary persona.

### F. Pain points
Table: `Pain | Business impact | Emotional impact`. Link each pain to the JTBD it blocks.

### G. Triggers & buying signals
For each trigger:
- **What changed** in their world (e.g. "new CFO hired", "Series B raised", "compliance deadline")
- **Detection signal** — how we actually *observe* it (hiring feed, news, keyword spike, product usage)
- **Decay window** — how long the trigger stays relevant (e.g. pricing-page visits: 7–14 days; funding events: 90+ days)
- **Real-world example** — a concrete account where this trigger fired

### H. Quotes & language
The words the ICP actually uses — pulled from interviews, reviews, support tickets, sales calls, or search queries. Distinguish **insider vocabulary** from **outsider vocabulary**, because ICP-facing copy must mirror theirs, not yours.

### I. Negative ICP
- **Industries / segments to exclude** with the reason
- **Size floors and ceilings** (below X = wrong economics; above X = wrong buying process)
- **Disqualifying tech or process** (e.g. "on-prem-only environments", "no path to the buying committee")
- **Red-flag signals** in discovery (e.g. "requests heavy customisation", "wants below-floor pricing")

### J. Activation notes
How each team uses this ICP:
- **Sales** — qualification questions, prioritisation rules
- **Marketing** — account selection, message mapping, channel fit
- **Product / CS** — which feedback to weight, which to discount
- **Leadership** — quarterly review cadence, what would make us revisit

### Closing sections (mandatory)

1. **"Most probable ICP picture"** — 6–10 sentence synthesis, written so a new hire could use it on day one
2. **"Strongest strategic opportunities"** — max 5, each tied to an account pattern
3. **"No-go zones"** — max 5, each tied to an exclusion rule
4. **"What needs further validation"** — hypotheses flagged as hypothesis; how to test them

## Output style rules

- Be analytical and specific. Replace adjectives with thresholds (not "large companies" → "≥500 employees, ≥$100M revenue").
- Every strong claim names which lens / input supports it.
- Every trigger names its detection method. No un-detectable triggers.
- The Persona speaks in role-relevant terms (revenue targets, team OKRs, risk exposure) — not in consumer-persona clichés (hobbies, favourite coffee).
- JTBDs are phrased as outcomes the buyer would recognise ("make the Q4 compliance audit painless") not features we sell.
- Language section quotes the buyer, not the brand.
- The Negative ICP is as rigorous as the positive ICP — not an afterthought.

## What you must never do

- Produce a Persona that is indistinguishable from a consumer persona
- Conflate ICP (company) with Persona (individual) with JTBD (situation)
- List triggers that can't be observed from public or internal data
- Build the ICP from wishlists or leadership preferences — only from signal
- Skip the Negative ICP
- State hypotheses as confirmed facts
- Produce a "big list of attributes" without prioritisation — every layer must end with what matters most
- Copy a competitor's apparent ICP without checking whether our capabilities match
- Mix confidence tiers in the same sentence

## Related skills

- `b2b-sos-analysis` — validate the ICP's Category Entry Points against real search demand
- `brand-strategy` — the positioning and messaging that should sit on top of this ICP
- `anti-skill` — stress-test the ICP before it drives spend
