# ICP Framework — the 6-layer model

This file defines the canonical structure used to build a B2B Ideal Customer Profile and its companion Buyer Persona. The structure is deliberately **layered**: each layer depends on the ones above, and each answers a different targeting question. Collapsing layers produces vague profiles that no team can action.

---

## The three grains — keep them distinct

Before any field is written, separate these three concepts. They are routinely confused in practice and the resulting deliverable becomes unusable.

| Concept | Grain | Answers | Example |
|---|---|---|---|
| **ICP** | Company / account | Which organisations are worth pursuing? | "US-headquartered fintech, 200–2,000 employees, Series C+, uses AWS and Snowflake, dedicated RevOps team." |
| **Buyer Persona** | Individual / role | Who inside the account do we talk to, and how? | "VP RevOps, 3–7 years in role, reports to CRO, measured on pipeline velocity and forecast accuracy, reads The Revenue Collective, sceptical of vendor hype." |
| **JTBD** | Situation / outcome | What is this buyer hiring a solution to produce? | "When our forecast misses by >10%, I want a trusted pipeline signal so that I can intervene before the board meeting." |

Rule of thumb:
- ICP attributes are **observable from outside** the account (firmographic, technographic, tier).
- Persona attributes are **role-level** and describe an individual's goals, fears, and information diet.
- JTBDs are **verbs of outcome**, phrased in the buyer's voice.

---

## Layer 1 — Firmographics (company)

The company-level filter. Each field should end with a **threshold or qualifier**, not a vague adjective.

- **Industry** — named vertical(s) and sub-verticals. Prefer NAICS/SIC-level specificity ("healthcare payers" not "healthcare"). Name **included** and **excluded** verticals.
- **Company size** — headcount bands with explicit floor and ceiling ("200–2,000 FTE"). Note why the floor exists (below this, no budget / no buying committee) and why the ceiling exists (above this, the buying process is too slow or too customised).
- **Revenue** — ARR/annual revenue bands. Align with deal-size economics.
- **Location** — country/region with regulatory or GTM implications. If language, data-residency, or time-zone matter, state why.
- **Tech environment** — relevant platforms, infra, integrations, or tooling that must (or must not) be present. Examples: "uses Salesforce as system of record", "runs on AWS or GCP", "has data warehouse (Snowflake / BigQuery / Databricks)".
- **Stage / ownership** (optional but often decisive) — funding stage (Series B+), ownership type (PE-backed, public, bootstrapped), growth rate.

### Qualifying thresholds vs fit signals

A **threshold** is a hard floor/ceiling ("must have ≥500 FTE"). Fail it → not an ICP.
A **fit signal** is a correlated attribute ("has a Head of RevOps title"). Increases fit probability but is not itself a gate.

Write both. Thresholds gate outbound eligibility; fit signals score ranking.

---

## Layer 2 — Buyer Persona (individuals)

Each persona represents one **role on the buying committee**, not one imaginary person. Typical B2B buying committees include 6–13 internal stakeholders; pick the 2–4 roles that actually move or block the deal.

### Roles to consider per persona
- **Economic buyer** — approves the budget
- **Champion** — internal advocate who owns the problem
- **User** — operates the product day-to-day
- **Technical buyer** — validates integration, security, compliance
- **Blocker** — has veto power (legal, procurement, security)

### Fields per persona
- **Role** — exact title(s), including common variants ("VP RevOps / Head of Revenue Ops / Director, Sales Operations")
- **Reports to** — their manager's role. Reveals escalation path and budget owner.
- **Demographics (role-relevant only)** — seniority band, typical tenure in role, team size, budget authority, geographic base. Skip age / gender / ethnicity — not relevant in B2B targeting.
- **Psychographics** — what motivates them, what they fear, what they are personally measured on, their risk posture, their information diet (publications, podcasts, communities, peer networks, analysts they trust).
- **Communication channels** — where they actually consume information. Name the channel and the context. ("LinkedIn posts from peers, not brand content. Slack communities. Industry Slack groups. Skims analyst blogs. Ignores cold email; reads peer-forwarded emails.")

### What a Persona must *not* contain
- Stock photos presented as if they were real people
- Hobbies, favourite coffee, weekend routine — irrelevant to B2B targeting
- Generic "digital native" / "tech-savvy" labels
- Invented quotes — quotes go in the Language section and must be sourced

---

## Layer 3 — Jobs to be Done

A JTBD is a **situation → desired outcome → constraint** statement in the buyer's voice. It describes what the buyer is trying to accomplish, not what we sell.

### Canonical JTBD format
> When [situation], I want to [motivation / outcome], so I can [desired end state].

Example: *"When we open a new region, I want to stand up local pipeline reporting in under two weeks, so I can show the board we can scale without losing forecast accuracy."*

### Fields per JTBD
- **JTBD statement** — one sentence in the buyer's voice
- **Frequency** — how often this job arises (daily / monthly / quarterly / event-driven)
- **Importance** — how material the outcome is to the buyer's own performance (low / medium / high / existential)

### Rules
- 3–6 JTBDs per primary persona. More than that = not prioritised.
- Phrase in outcomes, not features. "Reduce forecast variance" ✓ / "Use our dashboards" ✗.
- JTBDs that repeat across personas with high importance are the strategic core of the ICP.
- Low-frequency + low-importance JTBDs are noise — cut them.

---

## Layer 4 — Pain points

Each pain must link to a JTBD it blocks. Pains are what makes the JTBD hard to complete *today*.

### Fields per pain
- **Pain** — concrete description in the buyer's voice
- **Business impact** — what it costs the company (revenue miss, compliance risk, cycle time, customer churn)
- **Emotional impact** — what it costs the individual (credibility, late nights, blame, career risk)

### Rules
- The business impact must be something the buyer's leadership cares about. If the C-suite wouldn't recognise it, it's not a material pain.
- The emotional impact is not optional in B2B. Careers and reputations drive urgency.
- Distinguish **surface pain** ("our dashboards are slow") from **underlying pain** ("I can't trust my numbers in board meetings"). The underlying pain is what the ICP is buying.

---

## Layer 5 — Triggers & buying signals

Triggers are the **observable events** that open the buying window. Without a trigger, even a perfect-fit ICP is not in-market. An ICP + a trigger = a prospect.

### Fields per trigger
- **What changed** — the event in the buyer's world
- **Detection signal** — how we observe it (public data, intent platform, product usage)
- **Decay window** — how long the trigger remains actionable
- **Example** — a real account where this trigger fired

### Canonical trigger categories
- **Leadership changes** — new CFO / CRO / CTO / CISO (90-day window of new-leader agenda-setting)
- **Funding events** — Series B+, especially growth rounds tied to GTM scale (≥90 days relevant)
- **Hiring signals** — job postings for ICP-relevant roles (30–60 days relevant)
- **Tech-stack changes** — adoption/removal of complementary or competitive tools
- **Regulatory deadlines** — compliance dates that force action
- **Competitive events** — a rival's outage, acquisition, price change
- **Behavioural** — pricing-page visits, comparison searches, demo requests (7–14 days — perishable)
- **Category / SoS signals** — a spike in branded or comparison search around a competitor

### Rules
- **No un-detectable triggers.** If you can't name the feed or signal, delete the trigger.
- Stacked signals (2–3 on the same account) convert materially higher than single signals — flag this in activation notes.
- Triggers have decay. Perishable signals (pricing page, demo) expire in days; structural signals (funding, regulation) persist for months.

---

## Layer 6 — Quotes & language

This is the buyer's vocabulary, pulled from real sources. It is the bridge between the ICP and the copy / sales scripts / content that will reach them.

### Where to pull from
- Discovery-call transcripts and sales-call recordings
- Support tickets and NPS verbatims
- G2 / Capterra / TrustRadius reviews of competitors
- Industry Slack / Reddit / LinkedIn threads
- Non-brand search queries (long-tail reveals phrasing)
- Customer interviews

### Distinguish insider vs outsider vocabulary
- **Insider vocabulary** — how the role actually talks ("pipeline hygiene", "forecast variance", "rev-ops stack")
- **Outsider vocabulary** — how the category talks at it ("AI-powered sales analytics") — avoid unless the buyer themselves uses it

### Rules
- 6–12 real quotes. Attribution can be redacted but the source type must be named ("VP RevOps, discovery call, Q1 2026").
- No invented quotes.
- If a phrase appears across ≥3 sources, flag it as category language worth mirroring.

---

## Negative ICP — the seventh (mandatory) layer

An ICP without explicit exclusions is not a targeting tool, it's a wishlist. The Negative ICP is constructed in parallel with the positive ICP and carries equal weight.

### Sources for Negative ICP
- Closed-lost deals clustered by disqualification reason
- Churned accounts clustered by churn reason
- Support / CS cost by segment (high-cost-to-serve = candidate exclusion)
- Sales cycle length by segment (very long cycles may not be economic)

### Categories of exclusion
- **Industry / vertical** — where the product misfits or compliance blocks entry
- **Size floor** — below this, no budget, no buying committee, lifetime value too low
- **Size ceiling** — above this, sales cycle and customisation cost exceed economics
- **Tech / architecture** — incompatibilities that cannot be worked around (e.g. "on-prem-only, no cloud")
- **Process red flags** — "no access to the buying committee", "procurement-led with required reverse-auction", "requires heavy customisation"
- **Commercial red flags** — budgets below the floor, unrealistic SLA demands, one-off procurement with no expansion path

### Rules
- Each exclusion carries the **reason** (closed-lost data, churn, unit economics).
- Exclusions are **as testable as inclusions** — a rep should be able to spot one in a 10-minute discovery call.
- Review exclusions quarterly. Some are structural; others may loosen as the product or GTM matures.

---

## Relationship between layers — how they reinforce each other

- A strong **firmographic** profile without **JTBD** is a demographic list, not a targeting strategy.
- A rich **Persona** without a **trigger** produces perpetual "nurture" with no conversion moment.
- A compelling **JTBD** without a **pain** fails to create urgency.
- A detected **trigger** on a **non-ICP** account is a distraction, not an opportunity.
- Real **language** makes every other layer legible to marketing and sales; without it, the deliverable dies in a Notion page.

The ICP is only useful when all seven layers (six positive + Negative ICP) are filled to consistent depth. Uneven depth — e.g., rich firmographics, empty triggers — signals a weak deliverable.
