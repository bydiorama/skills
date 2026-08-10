# Data synthesis — reading signal from the four lenses

This file explains how to extract ICP signal from each of the four input lenses, and which layer of the framework each lens primarily feeds. Use it alongside `icp-framework.md`.

The four lenses are:

1. **Company** — internal data (closed-won/lost, churn, CRM, CS, product usage)
2. **Competitor** — competitor bases, positioning, pricing, reviews, job posts
3. **Market** — category sizing, vertical trends, analyst coverage, regulatory shifts
4. **Search / Intent** — SoS, keywords, intent platforms, hiring/funding feeds

No single lens produces a valid ICP. A profile built only on internal data calcifies the past; only on competitors produces a copy of their strategy; only on market data is disconnected from what we can serve; only on search data mistakes volume for fit. **Triangulation across ≥3 lenses is the minimum bar for a "Confirmed" tier claim.**

---

## Lens 1 — Company (internal) data

### What it is best at
- Proving which customer types actually **succeed** (expand, renew, refer)
- Surfacing the **negative ICP** — who churns, who was lost, who is expensive to serve
- Anchoring firmographic thresholds in real economics (CAC, LTV, sales-cycle length)
- Capturing the **real voice of the customer** (sales calls, tickets, reviews)

### Primary layers fed
- Firmographics (Layer 1) — via closed-won patterns
- Persona (Layer 2) — via discovery-call transcripts and CS notes
- JTBD + Pains (Layers 3–4) — via sales call transcripts, support tickets, NPS verbatims
- Negative ICP — via closed-lost and churn analysis

### Method: closed-won pattern mining
Take the last 20–50 closed-won deals. For each, record:
- Industry, sub-vertical, size, revenue, HQ, tech stack (as known)
- Deal size, sales-cycle length, number of stakeholders
- Time-to-value in CS, expansion / renewal, referral behaviour
- The triggering event (as recorded in the CRM or sales notes)
- The role of the champion and the economic buyer

Then cluster. Look for attributes that:
- Appear in ≥60% of deals (candidate **thresholds**)
- Appear in ≥30% of deals and correlate with higher deal size / retention (candidate **fit signals**)
- Appear in ≤10% of deals but produced outsized value (candidate **aspirational** ICP variants — flag separately, do not confuse with core ICP)

### Method: closed-lost and churn mining
For the last 20+ closed-lost + churned accounts, record the **disqualification reason** in the CRM or as reconstructed by the rep. Cluster. Patterns to watch for:
- Size-floor clusters (below N FTE, the buying committee didn't exist)
- Size-ceiling clusters (above N FTE, procurement/customisation broke the economics)
- Vertical clusters (compliance / regulatory misfit)
- Tech clusters (integration gap)
- Process clusters (no champion access / required feature we don't build)

Each cluster becomes a candidate Negative ICP entry, with the loss count as supporting evidence.

### Traps to avoid
- **Survivorship bias** — your current customer base reflects past *sales motion*, not ideal fit. Correct by weighting successful expansions/referrals, not just "who bought".
- **Biggest customer ≠ ICP customer** — a single whale can distort thresholds. Flag outliers separately.
- **Missing data fields** — if CRM doesn't capture the attributes you need (tech stack, trigger, committee roles), say so in the methodological note and lower the confidence tier for affected claims.

---

## Lens 2 — Competitor data

### What it is best at
- Revealing **who else** thinks these accounts are worth pursuing
- Surfacing **positioning contrasts** — where competitors claim fit and where we could claim better fit
- Showing **category vocabulary** — the words the market uses when our product is not in the room
- Detecting **aspirational** and **adjacent** segments we may be underweighting

### Primary layers fed
- Firmographics (Layer 1) — via competitor customer logos, case studies, G2 filters
- Persona (Layer 2) — via competitor testimonials and review attribution
- Language (Layer 6) — via reviews, comparison pages, sales enablement content
- Triggers (Layer 5) — via competitor job posts and press (reveals their bets on which segments are heating up)

### Method: competitor base triangulation
For each direct competitor:
- Scrape/list public customer logos and case studies
- Pull G2 / Capterra / TrustRadius reviewer firmographics (company size, industry, reviewer role)
- Read 10–20 verbatim reviews per competitor — note the role, the JTBD mentioned, the pain the product solved, the language used
- Scan competitor pricing / packaging pages — who is each tier designed for?
- Scan competitor job ads — which verticals / roles / integrations are they hiring to serve?

Compare across competitors:
- **Overlapping** segments — the category consensus on who the buyer is (often safest, most competitive)
- **Differentiated** segments — where one competitor dominates and others don't (clues to our own positioning)
- **Ignored** segments — accounts that fit our capabilities but sit outside mainstream competitor focus (candidate **white space**, but verify against market data before getting excited)

### Method: substitute / do-nothing analysis
The hardest competitor to beat is **status quo**. Document:
- What does the target buyer do *today* if our category didn't exist? (manual process, spreadsheet, in-house build, a tool from an adjacent category)
- What are the pain-points of that substitute that surface in reviews and Reddit / community threads?

The substitute is often the *real* alternative, not a named competitor. An ICP that hasn't accounted for "do-nothing" will overestimate addressable demand.

### Traps to avoid
- **Copying a competitor's apparent ICP** — their ICP reflects their product and GTM, not ours. Use it as signal, not prescription.
- **Review-site selection bias** — reviewers skew toward enterprise users willing to opt in; SMB patterns may be under-represented.
- **Logo-wall flattery** — a logo doesn't mean the account is profitable or expanding for the competitor. Treat logos as leads, not truth.

---

## Lens 3 — Market data

### What it is best at
- Validating that the segment is **large enough and growing**
- Surfacing **structural shifts** (regulation, macro, tech adoption) that create or close buying windows
- Providing **analyst taxonomies** that align with how buyers self-identify
- Checking whether the client's **self-defined category** matches how the market defines it

### Primary layers fed
- Firmographics (Layer 1) — via TAM by vertical, revenue band, region
- Triggers (Layer 5) — via regulatory deadlines, macro shifts, category adoption curves
- Negative ICP — via market structure (some verticals structurally misfit)

### Method: market-fit sizing
For each candidate segment emerging from Lens 1 + Lens 2:
- How many companies match the firmographic thresholds in the target region(s)?
- What is the segment's growth rate vs the broader category?
- What is the analyst/trade-press narrative about this segment — expanding budget, consolidating, contracting?
- Are there regulatory or macro events in the next 12–24 months that will force action?

Rank segments by `(segment size) × (growth rate) × (our fit probability)`. The highest-ranked segments become the **core ICP**. Next-ranked become **secondary** (named separately — see `icp-template.md`).

### Method: category definition check
Search reports and analyst frameworks for the **category label** the client uses. Three possibilities:
1. The category exists and the client's definition matches — proceed.
2. The category exists but the client's definition is narrower/broader — name the discrepancy, decide whether to re-anchor.
3. The category does not exist as named — the client may be in a sub-segment of a larger category, or a nascent space. Flag implications (mental availability is harder when the buyer hasn't named the category).

### Traps to avoid
- **Analyst taxonomies are lagging** — they describe yesterday's buyers. Cross-check with search signals.
- **TAM inflation** — "everyone who could theoretically buy" is not the ICP. Filter by realistic thresholds before sizing.
- **Over-weighting US / EU coverage** — most analyst data skews to these regions. If the ICP extends elsewhere, flag data gaps.

---

## Lens 4 — Search / intent data

### What it is best at
- Surfacing the **live vocabulary** buyers use (non-brand search is honest)
- Detecting **in-market** accounts in real time (intent platforms, pricing-page visits)
- Validating **JTBD and pain** language against search demand
- Identifying **trigger signals** (funding, hiring, leadership changes, tech-stack adoption)

### Primary layers fed
- JTBD (Layer 3) — via pain-led and outcome-led query clusters
- Pains (Layer 4) — via problem-expression keywords and substitute-frustration searches
- Triggers (Layer 5) — via intent-platform account signals, hiring feeds, funding feeds, keyword spikes
- Language (Layer 6) — via long-tail non-brand queries

### Method: keyword-to-ICP mapping
For each retained keyword cluster:
- Does the **searcher profile implied** by the query match the ICP? (A query like "enterprise CRM for healthcare payers" signals a different account than "free CRM for small business".)
- What **funnel stage** does the query suggest? (Problem-aware → solution-aware → vendor-aware → purchase-intent)
- Does it name a **competitor** (comparison or alternative)? These are late-stage, high-intent signals — tie them to triggers.

Prefer clusters that align with both the ICP firmographic profile and a clear JTBD/pain.

### Method: trigger signal construction
For each candidate trigger in Layer 5, define the **detection feed**:

| Trigger category | Detection feed examples |
|---|---|
| Leadership change | LinkedIn title-change feed, Crunchbase exec updates, news releases |
| Funding event | Crunchbase, Pitchbook, press |
| Hiring signal | LinkedIn job posts, company careers page, Indeed feed |
| Tech-stack change | BuiltWith, Wappalyzer, G2 stack data, vendor press releases |
| Regulatory deadline | Regulatory agency calendars, trade-press analysis |
| Behavioural | Intent platforms (6sense, Bombora, Demandbase, G2 intent), website analytics |
| Category search spike | SoS tooling, Google Trends, keyword-research platforms |

If you cannot name the feed, the trigger is not operational — drop it.

### Method: decay-window assignment
Every trigger needs a decay window (how long the signal remains actionable). Use these defaults unless you have better data:

| Signal | Typical decay |
|---|---|
| Pricing-page visit, demo request | 7–14 days |
| Comparison-keyword search | 14–30 days |
| Job posting for ICP-relevant role | 30–60 days |
| Leadership change | 60–120 days (new-leader agenda window) |
| Funding event | 90–180 days |
| Regulatory deadline | Inverse to deadline date |

### Traps to avoid
- **Volume ≠ fit** — a high-volume keyword that pulls non-ICP searchers is noise.
- **Single-signal accounts** — one signal is weak. Stacked signals (≥2 correlated on the same account in a short window) are the high-conversion pattern.
- **Branded search inflation** — a spike in your own brand queries often follows your own marketing, not market demand. Separate owned media effects.
- **Intent platform black boxes** — vendor scoring can be opaque. Insist on the underlying signal, not just the score.

---

## Triangulation rules — assigning confidence tiers

Apply these rules when labelling each claim in the deliverable.

| Confidence tier | Triangulation requirement |
|---|---|
| **Confirmed by data** | Signal appears in ≥3 lenses AND is consistent in direction; sample size is adequate (e.g. ≥20 closed-won deals; competitor signal from ≥3 competitors; search signal sustained over ≥6 months) |
| **Strong working hypothesis** | Signal appears in ≥2 lenses AND is consistent; OR in 1 lens with very strong sample; not yet validated by a second independent source |
| **Weak / cautious signal** | Signal appears in 1 lens only; sample is small, noisy, or ambiguous; directionally suggestive only |

Every finding in the deliverable carries its tier label. Never mix tiers within a claim. When downgrading a finding (e.g. moving "Confirmed" → "Hypothesis"), state the reason.

---

## When inputs are thin — fallback modes

Clients rarely arrive with all four lenses populated. Adapt without pretending:

- **No internal data (pre-launch or new segment):** Rely on Lens 2 (competitor) + Lens 3 (market) + Lens 4 (search). Clearly mark the entire ICP as "hypothesis pending validation against first 10–20 closed deals."
- **No competitor data (emerging category):** Use Lens 1 (if available) + Lens 3 + Lens 4. Treat substitutes ("do-nothing") as the competitive field.
- **No market data (niche / local category):** Use Lens 1 + Lens 2 + Lens 4. Substitute trade-press and community sources for analyst coverage.
- **No search data (offline category, low digital footprint):** Use Lens 1 + Lens 2 + Lens 3 + qualitative research. Triggers must be reconstructed from news, trade press, and direct interviews. Flag that behavioural signals will not be available for activation.

In every fallback mode, name what's missing in the methodological note, and list what would need to be collected to upgrade the confidence tier.
