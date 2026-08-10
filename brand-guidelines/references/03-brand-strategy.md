# Section 1 — Brand Strategy

The single strongest predictor of guideline quality. Documents WITH formal strategy average 4.1/5; those without average 3.0/5 — a 1.1-point gap, the largest correlation in the entire 180-document corpus.

Position 1 (96% consensus). Always opens the document.

## Companion skill

A separate `brand-strategy` skill exists for running the deeper strategy work. If the brand has no strategy defined and the user wants to develop it as part of this project, hand off to `brand-strategy` first, then return here to document the output.

This reference is for **documenting** strategy in the guidelines, not developing it from scratch.

## Required subsections

| Element | Frequency in corpus | Required? |
|---------|--------------------:|-----------|
| Positioning / tagline | 62% | Always — at minimum |
| Brand personality | 38% | Standard tier and above |
| Values | 33% | Standard tier and above |
| Mission | 28% | When defined |
| Vision | 21% | When defined |
| Purpose | 17% | When defined (philosophical "why") |
| Target audience | 18% | Comprehensive tier |
| Brand pillars / principles | 15% | Optional |
| Brand architecture | 14% | When multi-brand |
| Archetypes | 7% | Rare; only if strategically defined |

## Default cascade (validated by IOC, Strava, Vratna)

```
Purpose      →  why we exist (philosophical)
   ↓
Vision       →  the future we work toward
   ↓
Mission      →  what we do today
   ↓
Values       →  3–5 named, with anti-definitions where possible
   ↓
Personality  →  4–6 traits, ideally as "X but not Y" pairs
   ↓
Positioning  →  1-line distinctive promise
```

You can shorten this to {Mission, Values, Personality, Positioning} for Compact tier.

## How many of each

Drawn from corpus distributions:

| Element | Sweet spot | Examples |
|---------|-----------|----------|
| Values | **3–5** (3 most common at 35%, 4 at 30%) | IOC: Excellence/Respect/Friendship; Channel 4: Innovative/Independent/Irreverent |
| Personality traits | **4–6** with anti-definitions | "Confident but not arrogant"; "Warm but not soft"; "Sharp but not clinical" |
| Pillars | 3–5 if used | Adobe's three personality tenets; Cisco's Brand Palette modular framework |
| Archetypes | 1 primary + up to 2 secondary | NOVEBA: Guardian primary, Artist secondary, Sage tertiary |

**Avoid 7+ values.** Documents with 7+ "values" are usually mixing values with principles, pillars, or design tenets. Force the user to consolidate.

## Format on the page

For each strategic element:

- **Heading**: the named element (e.g. "Our Purpose")
- **The statement**: 1 short sentence, in the brand's voice. Punchy.
- **The unpack**: 1–2 sentences explaining what it means and why it's true *for this brand specifically*
- **In practice**: 1 line on what this looks like in everyday decisions

**Example structure (Vratna D017, scored 5/5):**

```
## Our Purpose
To turn an Alpine valley into a place where time slows down.

We don't compete with city resorts. We don't compete with five-star urban
hotels. We compete with the idea that vacation is a hectic checklist. Vratna
exists because mountain time should mean fewer notifications, longer dinners,
and slower mornings.

In practice: when in doubt, choose the slower option.
```

## Personality with "X but not Y"

The strongest personality articulations use anti-definitions because they force precision. Examples worth modeling:

- "Confident but not arrogant"
- "Modern but not trendy"
- "Sophisticated but not exclusive"
- "Playful but not childish"
- "Direct but not blunt"
- "Premium but not snobbish"

Avoid generic: "innovative, dynamic, customer-focused" — every brand claims these. They mean nothing.

## Tagline / positioning line — minimum bar

If the brand resists everything else, get them to commit to ONE LINE that captures the distinctive promise. The corpus shows 62% of documents have at least a positioning line, often when nothing else strategic is documented.

Test the line:
- Does it work as the first thing a stranger reads about the brand?
- Could it be said about a competitor? (If yes, it's not distinctive.)
- Does the brand's behavior (product, service, prices, channels) actually back it up?

## Audience definition — when included

Comprehensive tier should include audience. Two formats work:

1. **Demographic + psychographic profile** (1–2 paragraphs per primary segment)
2. **MHM segmentation** (Smithsonian E054 model — Mindset / Heart / Mission segments based on motivation, not demographics)

For B2B: pair with the existing `b2b-icp` skill if the user wants formal personas.

## Document the strategic context, not the slogans

The most common failure mode is documenting strategy as polished marketing copy. The point of strategy in guidelines is **decision-making leverage** — when a designer or copywriter has to make a judgment call (which font weight? which photo? which adjective?), they should be able to look at the strategy section and find the answer.

**Test**: for each strategy element written, ask "could a designer use this to settle a debate at 11pm?" If no, rewrite for actionability.

## Anti-patterns

- **Generic mission statements.** "To deliver world-class X to discerning customers." Cut entirely.
- **Vision as a press release.** "By 2030, we will be the global leader in..." If it sounds like an analyst quote, rewrite.
- **Values without anti-definitions.** "Integrity" tells me nothing. "We tell clients the unflattering truth even when it costs us the project" tells me everything.
- **Strategy detached from product.** If the strategy could plausibly belong to any brand in the category, it's not a strategy — it's a wishlist.

## Reference examples from the corpus

- **D017 Vratna** (5/5) — Tradition / Comfort / Symbiosis values; tied to physical place
- **D021 Kolinska Distrikt** (5/5) — Sensory food strategy; every color named after food
- **E102 Finland** — National brand identity grounded in concrete cultural traits
- **E090 Strava** — "Athletes, never users" language policy as strategic anchor
- **E061 Bumble** — Personality on a vulnerable-to-hopeful spectrum
- **E041 Stella Artois** — 600+ years of brewing history as positioning anchor
- **E156 The Sea Ranch** — Environmental philosophy as brand foundation
