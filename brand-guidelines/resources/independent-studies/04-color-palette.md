# Independent Study 4: Color Palette

> Analysis of color palette systems across 180 brand guideline documents (36 Diorama, 144 external).

---

## 1. Palette Size

### How Many Colors Do Brands Define?

The number of explicitly defined colors varies dramatically across the corpus, from minimalist 2-color systems to expansive 27+ color palettes. The distribution reveals a clear sweet spot.

| Palette Size | Frequency | % of Docs with Color Sections | Examples |
|---|---|---|---|
| **1-3 colors** | ~30 docs | ~20% | Snapchat (3), New School (3), ICFF (2), Rajska (3), ssleek (3), Harvard (2), Apple (2), New Museum (3), Ogden Museum (5), NeXT (2), NY Botanical Garden (1+B/W), Edwin Castillo (3: Street Black, CHNTWN Red, Stone Beige) |
| **4-6 colors** | ~56 docs | ~38% | GameJam (6), SHARK (6), LUCRON (6), DEUS (3+tints), Nordika (5), Eterno Cloud (5), Gerulata (4), BJD (6), Workin (5), Bumble (3), F1 (4), Hometree (5), Bytes (8), KOYOK (4) |
| **7-10 colors** | ~35 docs | ~24% | DSTRCT Berlin (6+2), REMPO (10+grays), CORWIN (14), Cisco (13+), Kia (6), ASICS (7), Burger King (6), Crafts Council (9), KALW (12), Howden (8+4), NMAAHC (4+18), Tramways Coffee (10 with flavor palette), Network Rail (8 spec systems) |
| **11-20 colors** | ~18 docs | ~12% | Queens 2023 (17), Tate (16), Slack (7+28), DPD (11), Detroit Institute of Arts (9), NorthAlley (12), Oktawave (2+64), Nike Empower (8+pairings) |
| **20+ colors** | ~9 docs | ~6% | Twitch (33), Channel Five (25), Tupperware (27), Oyster (30+), Slack (35 total), NMAAHC (22), NJ Transit (11+industrial), Havas (49: 7 families x 7 tints) |

### The Sweet Spot: 4-6 Colors

The most common palette size is **4-6 colors** (38% of documents), typically structured as:
- 1-2 primary brand colors
- 2-3 secondary/accent colors
- Black and white (often implicit, sometimes explicitly defined)

This aligns with cognitive research on color recall -- users can reliably remember and distinguish 4-6 brand colors. Smaller palettes (1-3) tend to belong to luxury, fashion, or minimal-identity brands (Calvin Klein, Apple, ICFF). Larger palettes (11+) appear in institutional, digital-product, or entertainment brands that need category coding or seasonal flexibility (Twitch, Tupperware, Slack, Tate).

### Primary vs. Secondary Structure

Virtually all documents with 4+ colors use a **tiered hierarchy**:

| Structure | Frequency | Pattern |
|---|---|---|
| **Primary + Secondary** | ~65% | Most common. 1-3 primary colors carry the brand; 2-6 secondary colors add range. |
| **Primary + Secondary + Tertiary** | ~12% | Three-tier systems for complex brands. ASICS, Aix-Marseille, SPACE10, NMAAHC. |
| **Primary + Extended/Accent** | ~15% | Flat primary palette with a loosely governed extended set. Corvus Atrium, Akera, Handshake. |
| **Flat (no hierarchy)** | ~8% | All colors treated equally. Channel Five, Tate, BJD. |

**Diorama vs. External:** Diorama projects average 5.4 defined colors per palette vs. 6.8 for external brands. This reflects Diorama's tendency toward focused, project-specific identities (real estate, hospitality) where restraint signals premium positioning. External brands with larger palettes tend to be tech platforms or institutions needing broader flexibility.

---

## 2. Color Naming

### Naming Approaches

Color naming is one of the most revealing indicators of brand personality and sophistication. Four distinct approaches emerge:

| Approach | Frequency | Examples |
|---|---|---|
| **Generic/Descriptive** | ~35% | "Blue," "Dark Green," "Light Grey," "Red." GameJam, REMPO, Gerulata, BJD, Brickline, Tokyo Olympics |
| **Branded/Evocative** | ~40% | Names that carry brand identity or emotional associations. Dominates premium and consumer brands. |
| **Coded/Systematic** | ~10% | Alphanumeric codes: "RED 1.0," "RED 2.0," "GRAY 1.0" (Generali Balans); "Color 80/60/20" (IBM Garage) |
| **Hybrid** | ~15% | Brand prefix + descriptor: "Kia Midnight Black," "Uber Green," "Bumble Yellow," "ASICS Blue," "Nordika Terracotta" |

### Branded/Evocative Naming -- The Best Examples

The most distinctive naming strategies transform color definitions into brand storytelling:

- **Kolinska Distrikt:** Food-themed names honoring the brand's former food factory heritage -- Cola, Avocado, Blueberry, Cookie, Wine (darks); Cream, Sugar, Frosting, Oat, Bubblegum (lights). Every name reinforces the brand narrative.
- **Corvus Atrium:** Bird-themed names -- Raven (dark brown), Owl (beige), Pigeon (off-white), Finch (olive), Flamingo (pink). Connects to the "Corvus" brand name.
- **Hometree:** Energy particle names -- Photon (yellow), Electron (cyan), Joule (dark teal), Watt (pale blue-grey), Kelvin (green). Directly ties to the energy company positioning.
- **Burger King:** Food-inspired names -- Fiery Red, Flaming Orange, BBQ Brown, Mayo Egg White, Crunchy Green, Melty Yellow. Every color name evokes the menu.
- **Twitch:** Gaming-culture names -- Black Ops, Worm, Isabelle, Pac-Man, Dragon, Cuddle, Bandit, Lightning, K.O., Mega, Osu, Sniper, Legend, Zero. Reinforces the gaming community identity.
- **LUCRON:** Nature-landscape names -- Sky Blue, Golden Sand, Dark Green Sea, Peanut Shell. Drawn from coastal landscape photography.
- **F1:** Motorsport-material names -- Warm Red, Carbon Black, Off-White, High-Vis White. Evokes the racetrack.
- **Howden:** Botanical/natural names -- Poppy, Pistachio, Rosewood, Moss Green, Teal, Cobalt Blue, Mustard.
- **Hudson Valley:** Season-derived names for rotating palettes -- Sky, Foliage, Grass, Terra Cotta, Shutter, Ivory Shadow.
- **Edwin Castillo:** Culturally-derived names -- Street Black, CHNTWN Red, Stone Beige. Each name connects to the designer's Chinatown cultural roots and urban context. Demonstrates how even a 3-color palette can carry deep narrative weight through naming.

### The Hybrid Pattern (Brand Prefix + Descriptor)

The most practical approach for toolkit generation is the **hybrid** model, where a brand prefix is followed by a descriptive or evocative name. This pattern:
- Makes colors immediately identifiable as belonging to the brand
- Maintains human readability
- Works well as design-token names

Examples: `Bumble Yellow`, `Kia Midnight Black`, `ASICS Blue`, `Nordika Terracotta`, `Supercell Green`, `Workin Purple`, `Rempo Blue`, `Marina Blue`, `DEUS Gold`, `Bolt Lightning Yellow`.

### Best Practice

Generic naming ("Blue," "Red") is acceptable only when a palette has 3 or fewer colors. For palettes with 4+ colors, branded or evocative naming significantly aids internal communication, design-token clarity, and brand recall. The hybrid approach (brand prefix + evocative descriptor) offers the best balance of clarity and personality.

---

## 3. Specification Formats

### Which Formats Appear?

| Format | Docs Providing | % of Color Sections | Notes |
|---|---|---|---|
| **HEX** | ~112 | ~76% | The most universally provided format. Digital-first brands almost always include it. |
| **RGB** | ~85 | ~58% | Often provided alongside HEX. Sometimes RGB is given without HEX (rare). |
| **CMYK** | ~77 | ~52% | Standard for any brand anticipating print usage. |
| **Pantone** | ~75 | ~51% | Strongly correlated with professional/agency-produced guidelines. |
| **RAL** | ~20 | ~14% | Exclusively in docs anticipating physical/architectural/signage applications. Heavily represented in Diorama real-estate projects. |
| **NCS** | ~2 | ~1% | Network Rail provides NCS alongside 7 other formats -- the broadest spec system in the corpus. |
| **HSL** | ~3 | ~2% | Network Rail provides HSL values; rare but increasingly relevant for CSS-native workflows. |
| **RGBA** | ~8 | ~5% | Rare. GameJam, SHARK, and a few others provide alpha-channel values. |
| **Oracal (vinyl)** | 2 | ~1% | FONA (Oracal 641 film codes), Network Rail (vinyl film specification). |
| **DuPont/PPG/3M** | 1 | <1% | NJ Transit -- industrial paint and film specifications for vehicles and signage. |
| **Pantone TCX/TPX** | 1 | <1% | IOC -- textile cotton/paper specifications for merchandise. |
| **Benjamin Moore** | 1 | <1% | ICFF -- architectural paint specification. |

### How Many Formats Per Document?

| Formats Provided | Frequency | Examples |
|---|---|---|
| **1 format** (HEX only) | ~20% | TECHBOX, ANYWHALE (partial), Byteminds, many minimal external docs |
| **2 formats** (HEX + RGB) | ~15% | Widelab, Eterno Cloud, Bytes, Akera |
| **3 formats** (HEX + RGB + CMYK) | ~20% | Noveba, Queens 2015, Advanced, North Face |
| **4 formats** (HEX + RGB + CMYK + Pantone) | ~30% | SHARK, DSTRCT Berlin, REMPO, LUCRON, DEUS, Uber, Cisco, Slack, ASICS, Twitch, Howden, Tramways Coffee, KOYOK |
| **5+ formats** (+ RAL or specialty) | ~15% | FONA (7 formats), Rajska (6), CORWIN (5+), ssleek (5), Marina Dorcol (6), Brickline (4+RAL), IOC (4+RAL+TCX), F1 (4+RAL), NJ Transit (6+ industrial), **Network Rail (8 formats: RAL, NCS, Pantone, CMYK, RGB, HEX, HSL, vinyl film -- MOST in corpus)** |

### The Minimum Acceptable Set

Based on the corpus, a **robust color specification should include at minimum**:

1. **HEX** -- universal digital reference
2. **RGB** -- screen reproduction
3. **CMYK** -- print reproduction
4. **Pantone** -- color-matching standard for print vendors

This four-format minimum covers ~95% of use cases. Adding **RAL** is essential for any brand with physical/architectural applications (signage, interiors, products). The Diorama portfolio consistently provides RAL values (~50% of Diorama docs include RAL), reflecting the real-estate and spatial nature of these projects.

### Diorama vs. External

Diorama projects average **4.1 specification formats** per color vs. **2.8 for external** brands. This is one of Diorama's strongest differentiators -- comprehensiveness of color specification -- and should be maintained or even elevated in the toolkit.

---

## 4. Tint/Shade Systems

### How Many Documents Define Tint Scales?

Of the ~148 documents with substantive color sections, approximately **48 (32%)** define explicit tint or shade scales. The remainder either provide only base color values or leave tinting to the designer's discretion.

| Tint System Type | Count | Examples |
|---|---|---|
| **Percentage-based tints** (adding white) | ~27 | SHARK (100/75/50/25/15/5%), FONA (90/75/50/25/10%), DEUS (100/75/50/25%), DSTRCT Berlin (100/80/60/40/20%), Gerulata (80/60/40/20%), Queens 2015 (75/50/25%), Howden (5-100% in 5% increments), Havas (100/60/40 tint system across 7 color families = 49 total colors) |
| **Named tonal scales** (Light/Mid/Dark) | ~10 | Queens 2023 (Light/Mid/Dark per family), Marina Dorcol (Medium/Light/ExtraLight), PROSIGHT (700/600/500/400/300), NMAAHC (Dark/Main/Light) |
| **Numbered scales** (100-900) | ~5 | WEM Wingman (100-900 nine-step), Widelab (Gray 50-1000 eleven-step), PROSIGHT (700-300) |
| **Opacity-based scales** | ~3 | Kolinska Distrikt (100/80/60/40/20/10% opacity) |
| **Full tonal ramps** (generated scales) | ~5 | WEM Private Fund (5-step light-to-dark for each color), Corvus Atrium (12-tone extended), Oktawave (8 shades per hue) |

### Step Sizes

The most common step intervals:

| Step Pattern | Frequency | Examples |
|---|---|---|
| **25% steps** (100/75/50/25) | Most common (~12 docs) | DEUS, Queens 2015, SHARK |
| **20% steps** (100/80/60/40/20) | Common (~8 docs) | DSTRCT Berlin, Gerulata, Kolinska |
| **5% steps** (fine-grained) | Rare (~2 docs) | Howden (5% increments from 5-100%), SHARK (includes 15% and 5%) |
| **10% steps** | Common for neutrals (~6 docs) | LUCRON (10% increments for grays), REMPO neutral palette, Widelab |
| **Material Design-inspired** (100-900) | Growing (~5 docs) | WEM Wingman, PROSIGHT, NMAAHC |

### Named Tint Levels

The most mature systems name their tint levels rather than using raw percentages:

- **PROSIGHT:** 700 (darkest), 600, 500 (base), 400, 300 (lightest) -- mirroring Material Design conventions
- **Queens 2023:** Light / Mid / Dark per color family
- **Marina Dorcol:** Medium / Light / ExtraLight per color family
- **NMAAHC:** Dark / Main / Light per hue family
- **WEM Wingman:** 100 (lightest) through 900 (darkest) -- nine-step scale

### Best Practice

A **five-step tint scale** (100%, 75%, 50%, 25%, 10%) provides sufficient range for most applications while remaining manageable. For digital-product brands, adopting the **100-900 numbered scale** (borrowed from Tailwind/Material Design conventions) offers better integration with design systems and CSS frameworks. Fine-grained 5% steps are overkill for most brands but valuable for enterprise-scale design systems (Howden's insurance context justifies the granularity).

---

## 5. Usage Ratios

### How Many Documents Specify Color Proportions?

Only approximately **24 documents (~16%)** provide explicit color usage ratios or proportional guidance. This is one of the most under-addressed aspects of color systems across the corpus.

| Type of Ratio Guidance | Count | Examples |
|---|---|---|
| **Explicit percentage splits** | ~11 | REMPO (50/29/21%), Noveba (70/20/10%), AB-InBev (60/20/15/5%), Supercell (70/30%), Bumble (70/20/10%), WEM (50/20/10+16+5%), Havas (60/30/10%) |
| **Dominant/accent verbal guidance** | ~8 | F1 ("Carbon Black and Off-White dominate; Warm Red in small amounts"), Nordika ("Terracotta dominates, Beige follows, Green as thin strip"), Kia ("Primary as main, Red as point, Secondary only when needed"), Adobe ("Red reserved primarily for mark") |
| **Usage hierarchy without percentages** | ~4 | PROSIGHT (color hierarchy from dominant to "extreme situations only"), ASICS ("primary and secondary in large areas; tertiary strictly as accents"), Kolinska ("max 2-3 colors per layout") |

### The 60/30/10 Rule and Variants

The classic **60/30/10** interior design ratio appears in various forms:

| Ratio | Brand | Breakdown |
|---|---|---|
| **70/20/10** | Noveba | Yellow/White/Black dominant, neutral grays 20%, functional accents 10% |
| **70/20/10** | Bumble | Bumble Yellow 70%, Black 20%, White 10% |
| **70/30** | Supercell | 70% primary (black/white), 30% accent colors |
| **60/20/15/5** | AB-InBev | Red 60%, White 20%, Blue 15%, Secondary 5% |
| **50/29/21** | REMPO | Primary Blue 50%, Dark Blue 29%, Secondary combined 21% |
| **50/20/10+** | WEM | Primary 50%, Secondary 20%, Accents distributed across remaining 30% |
| **60/30/10** | Havas | 60% dominant, 30% secondary, 10% accent -- the classic interior design ratio applied directly |
| **75/25** | Nike Empower | 75% Empower palette, 25% artist-unique colors |

### Best Practice

Providing a **suggested ratio** -- even an approximate one -- dramatically improves consistency across touchpoints and among different designers. The most practical format is a simple pie-chart or bar visualization showing approximate proportional targets, paired with verbal guidance explaining which colors "dominate" vs. "accent." Exact percentages are less important than establishing a clear hierarchy.

---

## 6. Accessibility

### How Many Documents Address Color Accessibility?

Only approximately **14 documents (~10%)** explicitly address color accessibility, contrast, or WCAG compliance. This is the single weakest area across the entire corpus.

| Accessibility Coverage | Count | Examples |
|---|---|---|
| **Full WCAG contrast ratios documented** | 3 | Brickline (full AAA/AA/AA-Large matrix with specific ratios), Research Ireland (contrast ratios 4.53:1 to 10.48:1, AA/AAA compliance noted), Slack (accessible combinations documented with contrast standards) |
| **Contrast rules stated** | 5 | Bumble ("no yellow text on white; no white text on yellow"), Tupperware (ADA compliance required for text-on-color), Art Institute Chicago (contrast rules page), Corvus Atrium ("only designed combinations with sufficient contrast"), Docusign (large text accessibility pass) |
| **Accessibility mentioned** | 4 | RAC (dedicated accessibility section 3.5), KALW (WCAG AA considered), Strava (contrast ratios defined), Corvus Atrium (web palette with wider range for accessibility/inclusive UX) |
| **Color blindness addressed** | 0 | No document in the corpus explicitly addresses color blindness, deuteranopia, or provides color-blind-safe alternatives. |
| **Not addressed at all** | ~124 | The vast majority. Explicitly noted as "Not covered" or simply absent. |

### The Accessibility Gap

This is a significant finding. Even among well-known global brands (Uber, Cisco, ASICS, Kia, IOC), explicit WCAG compliance documentation in the brand guidelines is rare. Several brands provide implicit accessibility through their color system design (high-contrast primary palettes, dark text on light backgrounds) but do not document or mandate it.

**Brickline** stands out as the gold standard -- providing a full contrast-ratio matrix (AAA, AA, AA Large) with specific numerical ratios for every color combination. **Research Ireland** is the runner-up, documenting exact contrast ratios and noting where combinations are large-text-only.

### Best Practice for the Toolkit

The toolkit should:
1. **Auto-generate contrast ratios** for every color combination
2. **Flag failing pairs** (below WCAG AA 4.5:1 for normal text, 3:1 for large text)
3. **Provide a pre-approved combinations table** showing which pairs pass at which level
4. Include a **color-blindness simulation** for the primary palette (deuteranopia, protanopia, tritanopia)

---

## 7. Dark Mode

### How Many Documents Address Dark Mode?

Only approximately **5 documents (~4%)** explicitly address dark mode or dark/light theme palettes:

| Document | Dark Mode Treatment |
|---|---|
| **Docusign** | Full light/dark themes defined with specific background, text, and accent color assignments for each. |
| **Opera** | References "User Interface Dark" and "User Interface Light" themes. |
| **Twitter/X** | "Dark mode Tweet treatments available as alternative to white." |
| **Widelab** | Three background modes defined: Purple background, Black background, White/gray background -- with specific text and outline colors for each. |
| **HSBC** | Digital color space section with separate treatment for apps/web, including background modes. |

### The Dark Mode Gap

This is perhaps the most significant temporal gap in the corpus. Many of the documents predate the mainstream adoption of dark mode (iOS 13, 2019). Even post-2019 documents from digital-native brands (Slack, Zoom, Strava, Spotify) do not include dark mode guidance in their brand-level guidelines, likely because dark mode is handled at the product/design-system level rather than the brand level.

### Implications

For the toolkit, dark mode should be addressed as an optional but recommended module:
- Auto-invert primary/secondary colors with adjusted saturation and lightness
- Provide a dark-surface background color (not pure black -- e.g., #1A1A2E or similar)
- Adjust accent colors for adequate contrast on dark surfaces
- Generate both light and dark theme tokens in a single export

---

## 8. Color Psychology

### How Many Documents Explain Color Reasoning?

Approximately **38 documents (~26%)** provide some rationale for their color choices. The depth ranges from single-sentence justifications to multi-paragraph cultural narratives.

| Depth Level | Count | Examples |
|---|---|---|
| **Rich narrative** (cultural, emotional, strategic) | ~10 | Vratna ("Violet reflects the local pasque flower; Forest Green represents Mala Fatra flora"), LUCRON ("colors from nature itself -- sky, sand, sea vegetation, shell"), Kolinska Distrikt (food factory heritage), Hometree (energy particle names), Kia ("perfection and harmony... sustainability, eco-friendliness"), Marina Dorcol (nature: sky/water, sand/stone, vegetation), F1 ("heat, power, passion... steely blue tint; cooling counterpoint"), Hudson Valley ("spirit of the Hudson Valley through color"), Edwin Castillo (culturally-derived from Chinatown urban context -- Street Black, CHNTWN Red, Stone Beige), Tramways Coffee (flavor palette tied to coffee product range) |
| **Brief justification** (1-2 sentences) | ~15 | Queens 2023 ("green represents fresh spirit, vitality, progress"), NASA ("a warm shade of red, a very active color... kinetic dimension"), Uber ("Safety Blue for support, assurance, and delight"), Snapchat ("one of our most important brand elements"), Art Institute Chicago ("emotional warmth"), Detroit Institute of Arts ("reflect the building interior; warm, welcoming aesthetic"), NMAAHC ("royalty, faith, prosperity, healing"), Corwin (each secondary color mapped to a city principle) |
| **Implicit/visual** (color shown with mood imagery) | ~12 | MICA (inspiration context page), British Museum (exhibition mood drives color), Oyster ("vibrancy and flexibility"), Arthaus (saturated accents signal creative energy), Akera ("gender-neutral, inclusive"), North Face ("snowbound mountain side facing north") |
| **No rationale** | ~105 | Colors presented as specifications only, without explanation. |

### The CORWIN Model

CORWIN's color system is notably sophisticated in its reasoning: each of five secondary colors is mapped to one of the project's five core urban principles (Healthy City = Calm Water blue, Green City = Grayish Green, Compact City = Sunset Orange, Diverse City = Pleasure pink, Flexible City = The Presence grey), with paired complementary tints for each. This creates a functional color vocabulary where color choice is driven by meaning, not aesthetics alone.

### Best Practice

Including brief (1-3 sentence) rationale statements alongside color definitions significantly elevates perceived quality and helps non-design stakeholders understand and respect the color system. The rationale need not invoke formal color psychology -- connecting colors to the brand's physical context (landscape, architecture, product) or cultural heritage is more authentic and memorable.

---

## 9. Best Examples

### Top 5 Color Palette Sections

**1. Brickline (E062)**
- 2 primary + 6 secondary colors with HEX, Pantone, and RAL
- Full WCAG contrast-ratio matrix (AAA/AA/AA-Large) with specific values
- Usage-spectrum guidance (serious tone = primary palette; playful tone = more secondary)
- Explicit pairing prohibitions ("dark green and brown never together")
- Why it excels: The only document to provide a complete accessibility matrix while maintaining clear creative direction.

**2. Howden (E067)**
- 8 primary + 4 secondary colors with HEX, PMS, and RAL
- Full tint range (5-100% in 5% increments) for all primary colors
- Color adjacency/grouping system with circular diagram
- Three hero pairings identified as "most ownable"
- Gradient rules (three-color, 60% opacity)
- RAG system for data tables
- Why it excels: The most comprehensive and systematic color section in the corpus. Covers every conceivable use case from brand expression to data visualization.

**3. REMPO (D009)**
- Three-tier palette (primary, secondary, neutral) with Pantone, CMYK, RGB, HEX
- Explicit percentage-based usage hierarchy (50/29/21%)
- Secondary colors mandated to appear only with primary palette
- 6-step neutral gray ramp for web/UI usage
- Why it excels: Perfect balance of specification completeness and usage clarity. The percentage ratios are practical and immediately actionable.

**4. CORWIN (D016)**
- 4 primary + 5 secondary + 5 complementary colors, each with HEX, RGB, CMYK, Pantone, RAL
- Each secondary color semantically mapped to a brand principle
- Paired complementary tints for every secondary
- Photography color guidance (recommended and avoid palettes)
- Why it excels: Demonstrates how color can encode brand meaning, not just brand aesthetics. The principle-to-color mapping creates a functional vocabulary.

**5. Tupperware (E125)**
- 27 colors in three tiers (Core/Tint/Shade) with full HEX, CMYK, RGB, Pantone
- Detailed pairing rules (shade-on-core OK, core-on-shade OK, tint+core NOT OK)
- ADA compliance mandated for text-on-color
- Blue-dominant packaging with dedicated variation pairings
- Why it excels: Proves that even a very large palette can be governed effectively through systematic pairing rules and tiered structure.

### Honorable Mentions

- **Kolinska Distrikt (D021):** Outstanding evocative naming system; max 2-3 colors per layout rule; paired dark+light tints; 6-step opacity scale.
- **Twitch (E044):** Bold 33-color system with gaming-themed names and clear tone guidance ("CMYK is the acronym of last resort").
- **NMAAHC (E159):** 22-color system with 6 hue families in dark/main/light; culturally grounded rationale; tinting rules for light shades only.
- **Queens 2023 (D014):** 5 color families each with Light/Mid/Dark -- excellent systematic structure for a mid-sized palette.
- **Slack (E071):** Core + 28 secondary colors with full specs; accessible combinations documented; clear text-color restrictions.
- **Network Rail (E084):** 8 specification formats per color (RAL, NCS, Pantone, CMYK, RGB, HEX, HSL, vinyl film) -- the most comprehensive spec system in the entire corpus. Sets the benchmark for physical/infrastructure brands.
- **Havas (E086):** 49 colors (7 families x 7 tints) with a 60/30/10 ratio rule. Demonstrates how a tint system can generate a massive usable palette from a restrained base.
- **Edwin Castillo (E087):** Only 3 colors, but each culturally derived (Street Black, CHNTWN Red, Stone Beige) -- proving that narrative depth compensates for palette size.
- **KOYOK (E079):** 4 colors with gradient specification (68% ratio) -- a rare example of codified gradient rules in the corpus.

---

## 10. Toolkit Implications

### Color System Generation Recommendations

Based on the analysis of 180 brand guideline documents, the Service Portal color toolkit should:

#### A. Palette Structure
1. **Default to a 5-6 color primary palette** plus black and white. This is the corpus sweet spot.
2. **Enforce a tiered hierarchy:** Primary (1-3 colors) > Secondary (2-4 colors) > Neutral (grayscale ramp). Optional: Tertiary/Extended.
3. **Allow palette expansion** through tint/shade generation rather than additional base colors.
4. **Cap total colors at 12 base hues** (excluding tints/shades). Even the most complex systems (Twitch at 33, Tupperware at 27) operate with 9 base hues -- the rest are systematic tints and shades.

#### B. Naming System
1. **Default to the hybrid model:** `[BrandName] [EvocativeDescriptor]` (e.g., "Nordika Terracotta," "Rempo Blue").
2. **Generate design tokens** using the hybrid name in kebab-case: `nordika-terracotta`, `rempo-blue`.
3. **Provide a naming prompt** that asks users whether they want generic, branded, or evocative names, with examples from the corpus.
4. **Auto-generate semantic aliases:** Map each color to functional roles (`--color-primary`, `--color-accent`, `--color-surface`, `--color-text`).

#### C. Specification Formats
1. **Always generate four formats minimum:** HEX, RGB, CMYK, Pantone (nearest match).
2. **Include RAL by default** for any brand with physical/spatial applications (architecture, signage, interiors, packaging). This is a Diorama differentiator.
3. **Consider NCS and HSL** for brands with signage/architectural scope. Network Rail's 8-format specification (RAL, NCS, Pantone, CMYK, RGB, HEX, HSL, vinyl film) sets a new high-water mark for format comprehensiveness.
4. **Offer optional specialty formats:** RGBA, HSL, CSS custom properties, Oracal/vinyl codes.
4. **Export as structured data:** JSON, CSS variables, Figma tokens, and Tailwind config.

#### D. Tint/Shade Generation
1. **Auto-generate a 5-step scale** for each base color: 100% (base), 75%, 50%, 25%, 10%.
2. **Offer a 9-step scale** (100-900) for digital-product brands, aligned with Tailwind/Material conventions.
3. **Name the steps** using both percentage and positional labels (e.g., "Marina Blue 500 (base)" / "Marina Blue 100 (lightest)").
4. **Generate both tints** (adding white) **and shades** (adding black/darkening) -- the Tupperware Core/Tint/Shade model is the gold standard.

#### E. Usage Ratios
1. **Include a default ratio suggestion** (60/30/10 or 70/20/10) in every generated palette.
2. **Visualize the ratio** as a simple bar or pie chart -- not just numbers.
3. **Link ratios to roles:** "Primary (60%) = backgrounds, large surfaces. Secondary (30%) = supporting elements, navigation. Accent (10%) = CTAs, highlights, alerts."

#### F. Accessibility
1. **Auto-generate a contrast matrix** for every color pair in the palette.
2. **Mark each pair** as AAA, AA, AA-Large, or Fail per WCAG 2.1.
3. **Provide an "approved combinations" shortlist** -- the 5-8 highest-contrast, most-usable pairs.
4. **Include color-blindness previews** (deuteranopia, protanopia, tritanopia simulations).
5. **This is the single biggest opportunity** -- only 10% of existing brand guidelines address accessibility, yet it is now a legal and ethical requirement for most digital applications.

#### G. Dark Mode
1. **Offer a "Generate Dark Theme" toggle** that auto-produces a dark-mode variant of the entire palette.
2. **Rules:** Reduce saturation slightly, adjust lightness for dark surfaces, ensure accent colors maintain adequate contrast (3:1+ for UI elements, 4.5:1+ for text).
3. **Provide a dark surface color** derived from the brand's darkest neutral rather than pure black.

#### H. Color Psychology / Rationale
1. **Include a "Why this color?" prompt** in the palette builder that encourages a 1-2 sentence justification per color.
2. **Offer contextual suggestions:** If the brand is in real estate, suggest nature/material-derived rationales. If tech, suggest innovation/energy associations.
3. **Store rationale as metadata** alongside each color definition for inclusion in generated brand guidelines.

#### I. Output Format Parity
Every color in the generated palette should be exportable as:
- **Print:** CMYK, Pantone (coated + uncoated), RAL (optional)
- **Digital:** HEX, RGB, RGBA, HSL
- **Design tools:** Figma variables, Adobe ASE/ACO, Sketch palette
- **Code:** CSS custom properties, Tailwind config, JSON tokens, Swift/Kotlin color constants
- **Physical:** RAL, Oracal/vinyl (optional), paint specification (optional)

---

## Appendix: Corpus Statistics

| Metric | Value |
|---|---|
| Total documents analyzed | 180 |
| Documents with substantive color sections | ~148 (82%) |
| Documents with no/minimal color data | ~32 (18%) |
| Average palette size (all docs) | ~6.3 colors |
| Average palette size (Diorama) | ~5.4 colors |
| Average palette size (external) | ~6.9 colors |
| Most common palette size | 4-6 colors (38%) |
| Documents with tint/shade systems | ~48 (32%) |
| Documents with usage ratios | ~24 (16%) |
| Documents with accessibility guidance | ~14 (9%) |
| Documents with dark mode guidance | ~5 (3%) |
| Documents with color rationale | ~38 (26%) |
| Average spec formats (Diorama) | 4.1 |
| Average spec formats (external) | 2.9 |
| Documents providing Pantone | ~75 (51%) |
| Documents providing RAL | ~20 (14%) |
| Most spec formats in single doc | 8 (Network Rail: RAL, NCS, Pantone, CMYK, RGB, HEX, HSL, vinyl film) |
