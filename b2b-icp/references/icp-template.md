# ICP template — output format, field guidance, worked example

This file defines the exact output shape of the final ICP deliverable and gives field-by-field writing guidance. Use it after `icp-framework.md` and `data-synthesis.md` as the drafting scaffold.

The template mirrors the canonical B2B ICP + Buyer Persona layout: **Firmographics → Buyer Persona → Jobs to be Done → Pain points → Triggers → Quotes & Language**, plus **Negative ICP** and **Activation notes**.

---

## Template

Fill each section in order. Use the given field labels verbatim. Tables keep the format scannable for client review.

### A. Executive summary
> *One paragraph, 5–8 sentences. State the ICP in one line, the primary Persona in one line, the single most decisive fit signal, the core JTBD, and the headline Negative ICP exclusion. Written for a CEO who will read nothing else.*

### B. Methodological note
- **Inputs used:** which of the four lenses were available, with sample sizes (e.g. "42 closed-won deals, 18 closed-lost; 3 direct-competitor base scans; Forrester 2026 category report; 18-month SoS dataset; 6sense intent export").
- **Gaps:** which inputs were missing or thin, and which claims that downgrades.
- **Confidence tier distribution:** e.g. "Firmographics: Confirmed. Persona goals: Hypothesis. Triggers: Mixed — leadership-change and funding are Confirmed; tech-stack triggers are Hypothesis."

### C. Ideal Customer Profile (company layer)

#### C.1 Firmographics

| Attribute | Value | Tier |
|---|---|---|
| Industry | [named vertical(s), incl. sub-verticals] | [Confirmed / Hypothesis / Weak] |
| Company size | [FTE band, with floor and ceiling] | |
| Revenue | [ARR / annual revenue band] | |
| Location | [region(s), with reason if regulatory or linguistic] | |
| Tech environment | [platforms / integrations / infra that must or must not be present] | |
| Stage / ownership | [e.g. Series B+, PE-backed, public] | |

#### C.2 Qualifying thresholds (hard gates)
- [Threshold 1 — e.g. "≥500 FTE"]
- [Threshold 2 — e.g. "HQ in US, UK, DACH, or Nordics"]
- [Threshold 3 — e.g. "Uses a cloud data warehouse (Snowflake, BigQuery, Databricks, or Redshift)"]

#### C.3 Fit signals (scoring inputs, not gates)
- [Signal 1 — e.g. "Has a Head of RevOps or equivalent title"]
- [Signal 2 — e.g. "Raised ≥$50M in last 24 months"]
- [Signal 3 — e.g. "3+ job postings for data / analytics roles in last 90 days"]

### D. Buyer Persona(s)

Produce one block per persona (2–4 blocks total). For each key role on the buying committee:

#### D.1 Persona — [Role name]

- **Role:** [exact title + common variants]
- **Reports to:** [manager role]
- **Demographics (role-relevant):** [seniority, tenure, team size, budget authority, geography]
- **Psychographics:**
  - Motivated by: [what drives them professionally]
  - Fears: [what they worry about at work]
  - Measured on: [their KPIs / OKRs]
  - Risk posture: [innovation-first / risk-averse / depends on context]
  - Information diet: [publications, podcasts, analysts, communities, peer networks]
- **Communication channels:** [specific channels + context, e.g. "LinkedIn posts from peers; industry Slack groups; skims Bessemer / a16z research; ignores cold email, reads peer-forwarded"]

Repeat for each persona on the committee (economic buyer, champion, user, technical buyer, blocker — include the ones that actually move or block deals).

### E. Jobs to be Done

| JTBD (in the buyer's voice) | Frequency | Importance |
|---|---|---|
| [When X, I want to Y, so I can Z] | [daily / monthly / quarterly / event-driven] | [low / medium / high / existential] |
| … | … | … |

3–6 rows per primary persona. Cross-reference: flag any JTBD that is shared across ≥2 personas with high importance — it is the strategic core.

### F. Pain points

| Pain | Business impact | Emotional impact |
|---|---|---|
| [Concrete pain in buyer's voice] | [What it costs the company — revenue, risk, time, churn] | [What it costs the individual — credibility, blame, career risk] |
| … | … | … |

Link each pain to the JTBD it blocks (in brackets, e.g. "(blocks JTBD #2)").

### G. Triggers & buying signals

For each trigger:

#### Trigger [N] — [Short name, e.g. "New CFO in first 90 days"]
- **What changed:** [event description]
- **Detection signal:** [specific feed — LinkedIn title-change; Crunchbase; BuiltWith; intent platform; hiring board; press]
- **Decay window:** [e.g. "90–120 days while the new leader sets agenda"]
- **Real-world example:** [anonymised or named account where this trigger fired and converted]

3–6 triggers. At least one behavioural trigger (detectable via intent or web analytics) and at least one structural trigger (funding, leadership, regulation).

### H. Quotes & Language

#### H.1 Insider vocabulary (how the role talks)
- [Phrase 1 — with source type, e.g. "\"pipeline hygiene\" — sales-call transcript, VP RevOps, Q1 2026"]
- [Phrase 2]
- [Phrase 3]

#### H.2 Outsider vocabulary (how the category talks at them — use cautiously)
- [Phrase — with source, note whether buyers mirror it or not]

#### H.3 Verbatim quotes (6–12)
> "[Quote]" — [Role, source type, date]

No invented quotes. If a source is confidential, redact the name but keep the role and source type.

### I. Negative ICP

#### I.1 Industries / segments to exclude
| Exclusion | Reason (evidence) |
|---|---|
| [Vertical / segment] | [Closed-lost cluster, churn cluster, unit-economic miss, compliance block] |

#### I.2 Size floors and ceilings
- **Floor:** [below N FTE / $Y ARR → reason]
- **Ceiling:** [above N FTE / $Y ARR → reason]

#### I.3 Disqualifying tech / process
- [Exclusion with reason]

#### I.4 Red flags in discovery
- [Signal a rep can spot on a first call]

### J. Activation notes

#### J.1 Sales
- **Top-3 qualification questions** to confirm ICP fit
- **Prioritisation rule:** how to rank in-ICP accounts when paired with a trigger
- **Handoff criteria** from marketing to sales

#### J.2 Marketing
- **Account selection rule** — how to filter target account lists
- **Message map** — which JTBDs / pains anchor which campaigns
- **Channel fit** — derived from Persona D.1 communication channels

#### J.3 Product / CS
- **Feedback weighting** — whose input counts as ICP feedback vs out-of-ICP noise
- **Onboarding focus** — the JTBD that must be delivered in first 30/60/90 days
- **Expansion playbook** — which in-ICP patterns predict expansion

#### J.4 Leadership
- **Review cadence:** quarterly
- **Revisit triggers:** what would force a rewrite (product pivot, segment saturation, new competitor, macro shift)

### Closing sections

#### K. Most probable ICP picture
6–10 sentences. Written so a new hire could use it on day one. No jargon they wouldn't recognise. Names the ICP, the primary Persona, the core JTBD, the top pain, the most reliable trigger, and the clearest exclusion.

#### L. Strongest strategic opportunities
Max 5. Each tied to a specific account pattern and supported by ≥2 lenses.

#### M. No-go zones
Max 5. Each tied to an exclusion rule in Section I.

#### N. What needs further validation
Hypotheses flagged honestly. For each, state **how to test it** (which sample, which data, which question).

---

## Confidence-tier labelling rules (reminder)

Every claim in sections C–G carries a tier. Either inline (e.g. "Industry: fintech (Confirmed)") or per-section.

- **Confirmed** — ≥3 lenses agree; adequate sample
- **Hypothesis** — ≥2 lenses agree, or 1 lens with strong sample, not yet cross-validated
- **Weak** — 1 lens only; small or noisy sample; directionally suggestive

Never blur tiers. When the client pushes back on a Confirmed claim, they must be shown the triangulation.

---

## Worked example (abbreviated) — "RevSignal" (fictional, for reference only)

### A. Executive summary
RevSignal's ICP is **US and UK Series B–D B2B SaaS companies with $20–200M ARR, 200–2,000 FTE, operating a modern data stack (Snowflake/BigQuery/Databricks) and a dedicated RevOps function**. The primary persona is the **VP RevOps**, economic sponsor is the **CRO**, blocker is **VP Finance**. The core JTBD is *"When our forecast misses by >10%, I want a trusted pipeline signal so I can intervene before the board meeting."* The highest-converting trigger is a **new CRO in first 90 days** stacked with a **Snowflake adoption signal**. The clearest exclusion is **companies without a dedicated RevOps role** — they cannot operate the product and churn at 4× the ICP average.

### B. Methodological note
Inputs: 42 closed-won, 18 closed-lost, 9 churn accounts (24 months). 4 direct-competitor bases + G2 reviews. Forrester 2026 RevOps report. 18-month SoS dataset. 6sense intent export (90 days). Gap: thin international coverage (only 6 EU deals). Most claims Confirmed; EU-specific claims are Hypothesis.

### C.1 Firmographics

| Attribute | Value | Tier |
|---|---|---|
| Industry | B2B SaaS (product-led or sales-led); sub-verticals: devtools, martech, fintech | Confirmed |
| Company size | 200–2,000 FTE | Confirmed |
| Revenue | $20M–$200M ARR | Confirmed |
| Location | US (70% of ICP), UK/Ireland (20%), DACH (10%) | Confirmed (US/UK), Hypothesis (DACH) |
| Tech environment | Salesforce as CRM; Snowflake / BigQuery / Databricks as DW; Slack | Confirmed |
| Stage / ownership | Series B–D, VC-backed | Confirmed |

### C.2 Qualifying thresholds
- ≥200 FTE
- Dedicated RevOps role present (Head of RevOps / VP RevOps / Sr Director RevOps)
- Salesforce OR HubSpot Enterprise as system of record
- Cloud data warehouse present

### C.3 Fit signals
- Raised ≥$40M in last 24 months (expansion capital → RevOps tooling budget)
- 2+ data/analytics job postings in last 90 days
- Active users of dbt (indicates analytics-engineering maturity)

### D.1 Persona — VP RevOps (primary champion)
- **Role:** VP RevOps / Head of Revenue Operations / Sr Director, Revenue Operations
- **Reports to:** CRO (85% of cases); CFO (10%); COO (5%)
- **Demographics:** 3–7 years in RevOps; team of 3–12; $0.5–2M discretionary tooling budget
- **Psychographics:**
  - Motivated by: clean data, forecast accuracy, being the CRO's "truth layer"
  - Fears: forecast misses attributed to them; CFO dismantling their team in a downturn
  - Measured on: forecast accuracy, pipeline coverage ratio, sales-cycle velocity
  - Risk posture: pragmatic — evaluates 3+ vendors, heavily reference-dependent
  - Information diet: The Revenue Collective / Pavilion, Operators Guild Slack, select substacks (Kellblog, Jason Lemkin), G2 reviews, peer DMs
- **Communication channels:** LinkedIn (peer content), community Slacks, peer calls. Ignores cold email unless it references a specific peer or a named pain.

### E. Jobs to be Done (VP RevOps)

| JTBD | Frequency | Importance |
|---|---|---|
| When the board meeting is 2 weeks out, I want forecast variance ≤ 5% so I can defend the number. | Quarterly | Existential |
| When a new segment opens, I want pipeline reporting ready in ≤ 2 weeks so GTM can scale. | Event-driven | High |
| When a deal slips, I want to know *why* within 24 hours so I can coach the rep. | Weekly | High |

### F. Pain points (selection)

| Pain | Business impact | Emotional impact |
|---|---|---|
| "Our forecast is a spreadsheet exercise — reps mark stage, I trust or don't trust it." (blocks JTBD #1) | Board loses trust in numbers; valuation risk in fundraise | VP RevOps's credibility = forecast accuracy. They wear every miss. |
| "Every new region = 3 weeks of pipeline plumbing." (blocks JTBD #2) | Delays GTM expansion; lost competitive window | Feels like firefighting, not strategy |

### G. Triggers (selection)

#### Trigger 1 — New CRO in first 90 days
- **What changed:** New revenue leader sets a data / forecast agenda within first 90 days
- **Detection signal:** LinkedIn title-change feed filtered by ICP firmographics
- **Decay window:** 90–120 days
- **Example:** "Acme Corp" — new CRO hired Feb 2026; champion appeared in intent data within 45 days; closed Q2 2026

(Additional triggers: Series B+ funding; Snowflake adoption; comparison search against [Competitor X].)

### I. Negative ICP (selection)
- **Exclusion:** Companies without a dedicated RevOps role. **Reason:** 6 of 9 churns; average 7-month lifespan vs 38-month ICP average.
- **Floor:** <200 FTE. **Reason:** No buying committee; sole-founder deals average 18-month sales cycle and no expansion.
- **Ceiling:** >2,000 FTE / >$200M ARR. **Reason:** Custom-integration requests push CAC above LTV floor; enterprise procurement adds 4–6 months.

### K. Most probable ICP picture
RevSignal wins with US and UK Series B–D SaaS companies, 200–2,000 people, $20–200M ARR, running Salesforce + a cloud data warehouse, with a Head of RevOps in place. The deal opens when a new CRO sets a forecast agenda in their first 90 days. The VP RevOps champions, the CRO sponsors, the VP Finance blocks on security and ROI. The buyer is hiring us to turn forecast from a spreadsheet exercise into a trusted signal — their own credibility rides on the result. The clearest "no" is any company without a dedicated RevOps function, regardless of size or budget.

---

## Drafting checklist (use before delivering)

- [ ] Every firmographic attribute has a threshold, not just a label
- [ ] Every persona field is role-relevant (no hobbies, no stock photos)
- [ ] Every JTBD is an outcome in the buyer's voice
- [ ] Every pain links to a JTBD it blocks
- [ ] Every trigger names its detection feed and decay window
- [ ] Every quote has a source type (no invented quotes)
- [ ] Negative ICP is populated to the same depth as positive ICP
- [ ] Every claim carries a confidence tier
- [ ] Activation notes name what each team does with the ICP
- [ ] Executive summary (A) and closing picture (K) match — one is a compressed restatement of the other

If any checkbox is empty, the deliverable is incomplete — do not ship.
