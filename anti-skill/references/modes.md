# Validation Modes

When multiple modes catch the same issue, report it once under whichever mode has the stronger framing.

**Severity scale used across all modes:**
- **Critical** — Fundamentally undermines the output's purpose. Must fix.
- **Important** — Weakens effectiveness significantly. Should fix.
- **Minor** — Suboptimal but functional. Consider fixing.

---

## 1. Intent Alignment

Does the output accomplish what it's supposed to?

Check for: goal drift (starts on-topic, wanders), incomplete delivery (covers X and Y but not Z), mismatch (answers a different question), buried lead (key info hidden deep), unstated assumptions (assumes reader knowledge the intent implies they lack).

For each misalignment: state what intent required → what output delivered → the gap.

## 2. Challenger (Devil's Advocate)

Argue against the output's conclusions, assumptions, and framing with the strongest counterarguments a smart, informed skeptic would raise.

For each of the 2-5 core claims, ask: Is the evidence sufficient or cherry-picked? What's the strongest real counterargument? What hidden assumptions does this rest on? What would need to be true for this to be wrong?

Watch for: confirmation bias, false dichotomy, appeal to authority without specifics, survivorship bias, scope creep in conclusions, correlation as causation.

Rate each counterargument: strong / moderate / speculative. Include what the author could do to address it.

**Research enhancement:** When challenging claims, search for real counterevidence — published critiques of the methodology cited, competing data that contradicts the output's figures, or documented failures of the approach being advocated. A counterargument with a source is 10x more useful than a hypothetical one.

**Deep depth sub-agents:** Skeptical Expert, Affected Stakeholder, Devil's Advocate Generalist (see agent-prompts.md).

## 3. Consistency & Logic Audit

Internal contradictions and logical errors — things objectively wrong within the output's own framework.

Check: numbers that don't add up, claims that conflict across sections, inconsistent definitions, recommendations that don't follow from analysis, logical fallacies (post hoc, slippery slope, etc.), reasoning gaps where steps are skipped, inappropriate qualifiers ("always"/"never"), structural flow and detail consistency.

For structured data (JSON, schemas, configs, spreadsheets): check type consistency, missing required fields, referential integrity, naming convention consistency, and values outside valid ranges.

Be precise: quote the contradictory passages, explain the error, suggest the fix.

## 4. Audience & Context Fit

Is the output appropriate for its intended audience?

Check: jargon the audience wouldn't know (or over-explanation that's condescending), formality level match, tone consistency with purpose, cultural considerations, format conventions for the genre, length appropriateness, actionability (if action is expected, is the next step clear?).

This mode often generates clarification questions to surface to the user before concluding ("Is the audience technical?", "This reads internal but you said it's for a client").

## 5. Completeness & Gap Analysis

What's missing that the audience would need or expect?

Check by output type — proposals need: problem, solution, timeline, cost, risks, team. Reports need: summary, methodology, findings, recommendations. Code needs: error handling, edge cases, docs, tests. Plans need: objectives, steps, owners, timeline, success criteria, contingencies. Data/configs need: validation rules, defaults for optional fields, migration notes, example usage.

Then check: implicit questions a reader would have, stakeholders affected but not mentioned, missing risk/limitation acknowledgment, unclear next steps.

**Research enhancement:** Search for industry standards, best practices, or regulatory requirements relevant to the output's domain. If a proposal omits something that standard frameworks require (e.g., NIST, ISO, OWASP, GDPR), that's a Completeness finding backed by an authoritative source.

**Deep depth sub-agents:** End-User, Decision-Maker, Implementer lenses (see agent-prompts.md).

## 6. Stress Test

What edge cases or adversarial conditions would break this? Primarily for functional outputs (code, processes, plans) but also for arguments/strategies.

Four categories:
- **Boundaries:** Empty/max/negative inputs, compressed/extended timelines, 10x scale up/down.
- **Adversarial:** How could someone game, exploit, or deliberately break this?
- **Environmental shifts:** Market, regulatory, technology, or team changes.
- **Dependency failures:** What if an external service, data source, or prerequisite breaks?

For each: scenario → likelihood (likely/possible/unlikely-but-high-impact) → what breaks → mitigation.

**Deep depth sub-agents:** Boundary Explorer, Adversarial Thinker, Black Swan Hunter (see agent-prompts.md).

## 7. Evidence Check

Are the output's factual claims actually true? This mode uses web search to verify or contradict.

### Process

1. **Extract verifiable claims.** Scan the output for statements that can be checked against external sources. Focus on: statistics and numbers, named entity attributes (founding dates, headquarters, leadership), market/industry claims, regulatory or legal references, attributed quotes or study results, current-state assertions ("X is the market leader").

2. **Triage by impact.** Not every claim is worth a search. Prioritize claims that: the output's argument depends on (if wrong, the conclusion falls apart), the audience would likely cross-check, seem surprising or too-good-to-be-true, are presented with false precision ("exactly 47.3%") without a source.

3. **Search and verify.** For each prioritized claim:
   - Search with a specific, targeted query (the claim itself or its core assertion)
   - Look for authoritative sources (government data, peer-reviewed research, primary sources, established reporting)
   - Check recency — a claim citing 2021 data in a 2026 document may be outdated
   - Search for contradicting evidence too, not just confirmation

4. **Classify each checked claim:**
   - **Verified** — evidence supports the claim. Note the source.
   - **Contradicted** — evidence directly conflicts. State the actual figure/fact and cite the source. Severity depends on impact.
   - **Outdated** — claim was once true but is no longer current. Note what changed.
   - **Unverifiable** — no authoritative source found either way. Flag as "could not verify — consider adding a source."
   - **Unsourced but plausible** — consistent with general knowledge but no specific source confirms the exact figure.

5. **Report format for findings:**
   - Claim: [what the output states]
   - Verdict: Verified / Contradicted / Outdated / Unverifiable
   - Evidence: [what search found, with source]
   - Impact: [how this affects the output's credibility if wrong]
   - Suggested fix: [correct the figure / add a citation / remove the unsupported claim]

### Severity Guide
- Core argument rests on a contradicted claim → **Critical**
- Supporting claim is wrong but conclusion still holds → **Important**
- Minor factual error that doesn't affect the argument → **Minor**
- Claim is plausible but unsourced in a context that demands sourcing → **Important**

**Deep depth sub-agents:** Fact-Checker (see agent-prompts.md).
