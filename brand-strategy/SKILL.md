# Brand Strategy

A skill for developing comprehensive brand strategies for Diorama's clients. Transforms raw inputs — client interviews, workshop outputs, briefs, and online category research — into a structured brand strategy deliverable ready for client presentation.

## Usage

Invoke this skill when you need to develop a brand strategy:

```
@brand-strategy
```

Or with specific materials:

```
@brand-strategy [path-to-materials]
```

## What This Skill Does

### Phase 1: Client Intake

Gathers and organizes all available inputs:

- **Workshop outputs**: PMI results, Rhetorical Triangle mapping, Values, Brand Personality sliders, CEPs Canvas, Future Vision, Priority Matrix, Parking Lot notes (see `resources/brand-workshop-structure.md` for framework definitions)
- **Interview transcripts**: Client interviews, stakeholder conversations, team discussions
- **Briefs and documentation**: Project briefs, existing brand guidelines, pitch decks, previous strategy work
- **Client context**: Company name, industry/category, geography/market, stage (startup, rebrand, refresh, extension), project type and scope

If materials are incomplete, prompt the user for the missing essentials:
1. What is the company/brand name and what do they do?
2. What industry/category are they in, and what market(s) do they serve?
3. What stage is this — new brand, rebrand, refresh, or extension?
4. What is the scope — full brand strategy, positioning only, messaging only, or specific components?
5. Are there workshop outputs, interview transcripts, or briefs to work from?

### Phase 2: Category Research

Use WebSearch to conduct comprehensive category research. Follow the research pattern established in `resources/brand-strategy-prompts.md`, adapted to the client's specific category:

- **Category structure**: Identify main categories, subcategories, and category entry points (the situations or triggers that prompt people to seek out this category)
- **Competitive landscape**: Map leading brands (national and regional), emerging players, product/service models, technology trends, and positioning approaches
- **Category norms**: Analyze typical pricing, service models, customer support, transparency, educational resources, and brand positioning within the category
- **Short-term trends**: Current shifts in consumer behavior, technology adoption, market dynamics
- **Long-term trends**: Structural changes, demographic shifts, regulatory evolution, cultural movements affecting the category
- **Customer expectations and frustrations**: What drives decision-making, what pain points exist, what gaps remain unaddressed
- **Regulatory and industry context**: Compliance requirements, industry standards, emerging regulations (where relevant)
- **Competitor positioning and tone**: How competitors communicate — language, tone, visual direction, frequently used messaging

Synthesize findings into actionable insights and identify areas of opportunity or differentiation the client can leverage.

### Phase 3: Strategic Analysis

Apply Diorama's workshop frameworks to structure the strategic analysis. Use all available inputs (workshop outputs, interviews, research) to build each layer:

**Plus / Minus / Interesting (PMI)**
Identify what makes the brand interesting, its core strengths, and any weaknesses or vulnerabilities. Use this as the foundation for all subsequent analysis.

**Rhetorical Triangle**
Map the brand's positioning across Aristotle's three pillars:
- **Ethos**: What makes the brand trustworthy, credible, and reliable? Credentials, track record, expertise, certifications.
- **Pathos**: What emotional connection does the brand create? Empathy, aspiration, belonging, expectation.
- **Logos**: What logical evidence supports the brand? Data, proof points, case studies, rational benefits.
- **Overlap (Brand Trust)**: Where do these pillars reinforce each other?

The brand should leverage at least two pillars strongly to build trust.

**Values Mapping**
Define the brand's core values — what it stands for and adheres to. If the workshop or intake surfaces more than five values, cluster and compress them into 3–5 core values. Each value should be distinct and non-overlapping — if two values describe similar territory (e.g., "trust" and "reliability"), merge them under the stronger term with a clear definition that captures both. Fewer, sharper values are more useful than a long list that dilutes meaning.

Equally important: define the anti-values — what the brand disdains, rejects, or refuses to be associated with. Anti-values do not need the same compression — list as many as are genuine.

**Brand Personality**
Position the brand on the 11 attribute sliders:
1. Masculine ←→ Feminine
2. Simple ←→ Complex
3. Conservative ←→ Experimental
4. Accessible ←→ Authoritative
5. Inclusive ←→ Exclusive
6. Fun ←→ Serious
7. Professional ←→ Casual
8. Modern ←→ Traditional
9. Young ←→ Mature
10. Natural (Analogous) ←→ Technological (Digital)
11. Uptight ←→ Loose

Provide a clear position on each slider with rationale. This is not a midpoint exercise — take a stance.

**Brand Archetype**
Identify three brand archetypes using the Pearson-Mark model (reference `resources/brand-archetypes_1-s2.0-S0007681322001355-main.pdf` and `resources/brand-archetypes.png`). For each archetype, also identify one complementary archetype — an archetype from a neighboring quadrant on the archetype wheel that balances or enriches the primary expression.

The Pearson-Mark model organizes 12 archetypes across four motivational quadrants:
- **Independence & Fulfillment**: Innocent, Sage, Explorer
- **Mastery & Risk**: Hero, Magician, Outlaw/Rebel
- **Belonging & Enjoyment**: Jester, Lover, Everyman/Regular
- **Stability & Control**: Caregiver, Ruler, Creator

Archetype relationships on the wheel:
- **Same quadrant** = shared core motivation (e.g., Caregiver and Ruler both seek stability)
- **Neighboring quadrants** = complementary — goals that can coexist and enrich each other (e.g., Caregiver + Everyman, Hero + Explorer, Creator + Sage)
- **Opposing quadrants** = tension — opposing forces that can create nuanced positioning when blended deliberately (e.g., Explorer vs. Ruler = freedom vs. stability)

For each of the three archetypes, define:
1. **The archetype**: Name, quadrant, core desire, core fear, and primary strategy
2. **How it manifests**: Specific behaviors, communication patterns, and brand decisions this archetype drives
3. **Complementary archetype**: Which neighboring-quadrant archetype balances it, and how that balance shows up in practice

The three archetypes should serve distinct roles:
- **Primary archetype**: The dominant personality — drives the majority of brand behavior and communication
- **Secondary archetype**: Supports and enriches the primary — adds depth without contradicting the core
- **Tertiary archetype**: A lighter influence that surfaces in specific contexts (e.g., certain audience segments, content types, or brand moments)

Real-world examples for reference:
- Nike: Hero (primary) + Magician (complementary) — mastery through transformation
- Apple: Creator (primary) + Outlaw (complementary) — lasting value through rule-breaking
- Dove: Caregiver (primary) + Innocent (complementary) — nurturing through simplicity

**CEPs Canvas (Category Entry Points)**
Map the 8 dimensions of when and why the market should think of this brand:
1. **Why?** — Motives and benefits driving purchase
2. **How?** — Solutions and services the brand offers
3. **When?** — Timing and urgency triggers
4. **Where?** — Channels and touchpoints (online/offline)
5. **Who?** — Why choose this brand over competitors
6. **What?** — Specific products and services to buy
7. **While?** — Co-activities and contexts during purchase
8. **With whom?** — Who influences or benefits from the purchase

**Competitive Differentiation**
Based on research and analysis, identify the white space — where category pain points, dissatisfaction, or gaps exist that the client can own. Define how the brand can differentiate on substance, not just messaging.

### Phase 4: Strategy Formulation

Synthesize research and analysis into clear strategic recommendations:

- **Brand positioning statement**: A clear, concise articulation of what the brand is, who it's for, and why it matters — distinct from competitors
- **Brand promise / value proposition**: The core promise the brand makes to its audience
- **Target audience definition**: Primary and secondary audiences with behavioral and attitudinal profiles, not just demographics
- **Brand personality and voice guidelines**: How the brand speaks, acts, and presents itself — derived from the personality sliders and archetype work
- **Key messages and messaging framework**: Core messages for each audience segment, organized by CEPs
- **Communication priorities**: Using the Priority Matrix, determine which communication activities to prioritize now vs. later
- **Growth and opportunity recommendations**: Strategic recommendations from both brand and business perspectives

### Phase 5: Deliverable Assembly

Compile the full brand strategy into a structured document. Reference the PDF deliverables in `resources/` as benchmarks for depth and quality:
- `brand-strategy_20250123_IMS_Brand-Concept_v01.pdf` — B2B brand concept example
- `brand-strategy_20251003_GEORGE-HILLARY_Personal-Brand-Guidelines_Round-02_v01.pdf` — Personal brand guidelines example

## Brand Strategy Deliverable Structure

```markdown
# [Client Name] Brand Strategy

**Client**: [Name]
**Year**: [Year]
**Country/Market**: [Market]
**Industry**: [Industry]
**Stage**: [Startup / Rebrand / Refresh / Extension]
**Project Type**: [Full Strategy / Positioning / Messaging / etc.]

---

## Executive Summary
Brief overview of the strategic direction, key insights, and primary recommendations. This should stand alone as a summary for stakeholders who won't read the full document.

## Category Landscape
- Category structure and entry points
- Short-term and long-term trends
- Regulatory and industry context (where relevant)
- Key takeaways for the client's positioning

## Competitive Analysis
- Key competitors and how they position themselves
- Category norms and conventions
- Tone, language, and visual positioning patterns
- White space and opportunity areas

## Audience
- Primary and secondary target audience profiles
- Key needs, frustrations, and decision drivers
- Category Entry Points (CEPs Canvas)
- What drives them to act, switch, or choose

## Brand Foundation
- Brand purpose / mission
- Core values (3–5, clustered and compressed) and anti-values
- Brand personality (attribute slider positions with rationale)
- Brand archetypes (three archetypes, each with a complementary archetype, using the Pearson-Mark model)
- Plus / Minus / Interesting summary

## Brand Positioning
- Positioning statement
- Brand promise / value proposition
- Key differentiators
- Rhetorical Triangle mapping (Ethos, Pathos, Logos)

## Messaging Framework
- Key messages by audience segment
- Tone of voice guidelines
- Language do's and don'ts
- Example messaging and proof points

## Strategic Recommendations
- Communication priorities (Priority Matrix)
- Growth and business opportunities
- Future vision (5-year horizon)
- Next steps

## Appendix
- Research sources and references
- Workshop outputs (if applicable)
- Supporting data and evidence
```

## Writing Style

The strategy should be clear, direct, and insight-driven. Write for an audience of business owners and marketing leaders who need to make decisions — not for other strategists.

### Tone & Voice

- **Clear and decisive**: Take a stance. Strategy is about making choices, not listing options. "You should position as X because Y" is more useful than "You could consider positioning as X."
- **Insight over information**: Don't just report what the research found — interpret it. Every finding should connect to a recommendation or implication for the brand.
- **Candid and honest**: If the brand has weaknesses, name them. If the market is crowded, say so. Credibility comes from honesty, not optimism.
- **Specific and grounded**: Use real competitor names, real data points, real examples. "Your three closest competitors all lead with price transparency" is more useful than "the market is competitive."
- **Partnership-minded**: This is a strategic partner talking to a client, not a consultant delivering a report. The tone should feel collaborative — "we" not "they."

### What to Avoid

- Generic strategy language that could apply to any brand ("leverage your unique value proposition")
- Hollow superlatives ("world-class," "best-in-class," "industry-leading")
- Hedging and equivocation — if you're not sure, say what you'd need to become sure
- Jargon without explanation — if you use a term like "CEP" or "brand architecture," unpack it
- Treating strategy as a checklist — every section should build on the previous one

## Adaptability

This skill adapts to different project types and scopes:

- **Full brand strategy**: All phases, all sections, maximum depth
- **Positioning only**: Focus on Phases 2-4, deliver Category Landscape through Brand Positioning
- **Messaging only**: Lighter research phase, focus on audience, voice, and messaging framework
- **Personal brands**: Adapt language from "company" to "individual" — personality sliders and archetype work become especially central
- **B2B vs. B2C**: Adjust research focus and audience definition accordingly
- **Startup vs. rebrand**: Startups need more foundational work; rebrands need more competitive differentiation and repositioning rationale

Not all sections are required for every project. The scope determines the depth. Ask the user to confirm scope before beginning.

## Quality Assurance

The skill includes mandatory quality checks:
- Cross-reference all research claims with sources
- Ensure consistency between analysis sections and recommendations
- Verify that the positioning statement is genuinely differentiated from competitors identified in research
- Confirm that messaging examples align with the defined tone of voice
- Check that CEPs map to real audience behaviors, not assumptions
- Flag any areas where more client input or research would strengthen the strategy

## Output Location

1. Ask for or identify the project directory
2. Create a Markdown file named `[ClientName]-Brand-Strategy.md`
3. Save to the appropriate project directory
4. Confirm file location to the user

## Resource References

- **Workshop framework**: `resources/brand-workshop-structure.md` — definitions of all workshop exercises (PMI, Rhetorical Triangle, Values, Personality, CEPs, Future Vision, Priority Matrix)
- **Research prompt patterns**: `resources/brand-strategy-prompts.md` — example research briefs showing depth and scope expected for category research
- **Brand archetypes**: `resources/brand-archetypes.png` and `resources/brand-archetypes_1-s2.0-S0007681322001355-main.pdf` — archetype theory and visual reference
- **Example deliverables**: `resources/brand-strategy_20250123_IMS_Brand-Concept_v01.pdf` (B2B) and `resources/brand-strategy_20251003_GEORGE-HILLARY_Personal-Brand-Guidelines_Round-02_v01.pdf` (personal brand) — reference for output depth and quality

## Tips for Best Results

1. **Provide workshop outputs**: The more structured input from workshops, the stronger the analysis
2. **Share interview transcripts**: Raw client voice adds nuance and authenticity to the strategy
3. **Specify the market/geography**: Category research is dramatically different by market — be specific
4. **Define the scope upfront**: A full strategy vs. a positioning exercise have very different deliverables
5. **Include existing materials**: Current brand guidelines, website, or marketing materials help identify what to build on vs. change
6. **Name competitors**: If the client already knows their competitive set, share it — it accelerates research
7. **Share the ambition**: The Future Vision exercise (5-year headline) shapes the entire strategic direction

## Continuous Improvement

After completing a brand strategy, invoke `@skill-reflect brand-strategy` to update this skill with validated learnings from the execution.

## User-Invocable

Yes - users can invoke this skill directly with `@brand-strategy`
