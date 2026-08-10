# Extended Elements (Modern Best Practice)

Beyond the canonical 8 sections, modern brand guidelines increasingly include extended sections that the corpus identifies as **systemic gaps** — areas where adoption is below 10% but where adoption confers a meaningful competitive edge.

Include these for **Comprehensive tier** projects, or for any brand with a digital product, or when targeting enterprise-scale stakeholders.

## The five industry gaps (from corpus meta-analysis)

| Gap | Corpus coverage | Opportunity |
|-----|----------------:|-------------|
| Accessibility | ~8% | Largest compliance risk in the industry; mandatory in some jurisdictions |
| Dark mode / responsive | ~10% | Universal device diversity; almost no documents address |
| AI usage policy | ~1% | Adobe alone (E019) addresses substantively; Wave (E064) uses Midjourney |
| Sustainability | ~3% | SPACE10, Nike Circularity, DEUS only — ESG mandatory soon |
| Design tokens / dev handoff | ~5% | Marina Dorcol (D008), Widelab examples — efficiency opportunity |

A toolkit-generated document that includes ALL FIVE places ahead of 92%+ of the existing market.

## 1. Accessibility

WCAG 2.2 (current as of 2024) is the global de facto standard. Reference the 2.1 baseline at minimum.

### Required content

- **Statement of intent** — "[Brand] is committed to WCAG 2.2 AA compliance across all digital touchpoints."
- **Color contrast ratios** — for every text/background pair, document AA / AAA pass / fail
- **Type minimum sizes** — 16px body minimum; 14px caption maximum-down
- **Focus states** — visible focus indicators (3:1 contrast against adjacent colors)
- **Touch targets** — 44 × 44px minimum on touch interfaces
- **Alt text guidance** — what to write, what to skip (decorative images get `alt=""`)
- **Captions / transcripts** — required for all video and audio content
- **Motion reduction** — respect `prefers-reduced-motion`
- **Multi-modal cues** — never use color alone to convey information

### Validation tools

- Stark Contrast Checker (Figma plugin)
- Colour Contrast Analyser (TPGi)
- axe DevTools
- WebAIM Contrast Checker

### Top corpus examples

- **E074 Docusign** (5/5) — accessibility threaded throughout
- **E125 Tupperware** (4.5/5) — full ADA-compliant pairing matrix for 27 colors
- **E141 Research Ireland** — accessibility section
- **E090 Strava** (5/5) — contrast ratios documented
- **E159 NMAAHC** (4.5/5) — concrete accessibility guidelines

## 2. Dark mode

Almost no corpus document covers this. For any brand with a digital product, dark mode is now table-stakes.

### Required content

- **Dark-mode color tokens** — equivalents for each light-mode token, defined as relationships not duplicates
- **Background hierarchy** — Twitch (E044) uses a 4-level background system; copy that pattern
- **Inversion rules** — which colors invert (text/background) and which are theme-stable (brand color, semantic warning)
- **Logo behavior** — when to switch to reversed variant; whether to color-shift the brandmark
- **Image treatment** — photos may need a darker overlay in dark mode
- **Contrast re-validation** — same WCAG checks must pass in BOTH modes

### Default token mapping

```
TOKEN                    LIGHT MODE        DARK MODE
surface.background       #FFFFFF           #0A0B0D
surface.subdued          #F5F5F7           #15171A
surface.elevated         #FFFFFF           #1F2226
text.primary             #0F1115           #F2F4F6
text.secondary           #4A4F58           #B0B6BF
text.muted               #6B7280           #8A929A
border.default           #E5E7EB           #2B2F36
brand.primary            #2F73DB           #5B9CFF      (often lifted in dark)
```

## 3. AI usage policy

Only Adobe (E019) addresses this with substance. Pattern this section after Adobe's "qualification process for Adobe Sensei AI claims" and extend.

### Required content

- **Permitted uses** — drafting, summarization, ideation, image-prompt generation
- **Prohibited uses** — generating final-public-facing copy without human review; AI-generated images presented as photography of real people / events; AI-generated quotes attributed to real individuals
- **Disclosure rules** — when to label AI-assisted content
- **Brand voice in AI prompts** — sample prompts that produce on-voice output (Wave's Midjourney pattern, E064)
- **AI tool whitelist** — which tools are sanctioned (Claude, ChatGPT, Midjourney, etc.) and at which tier (free, business, enterprise)
- **Data safety** — never input customer PII or proprietary product info into consumer AI tools
- **Hallucination protection** — fact-check rules; brand-claim verification process

### Forward-looking elements

- AI image generation: when allowed, when not, what style
- AI voice generation: synthetic voice rules; authorized voices; disclosure
- AI agents: rules for branded AI assistants (chatbot persona alignment to TOV)

## 4. Sustainability / environmental

Only three corpus documents (SPACE10, Nike Circularity E153, DEUS D006) address sustainability with substance. Mandatory direction for ESG-reporting brands.

### Required content

- **Materials policy** — preferred substrates (recycled paper, FSC-certified, soy inks)
- **Production efficiency** — print-on-demand vs warehouse; minimum-order thresholds
- **Digital sustainability** — image weight budgets, dark mode for energy savings, web font subsetting
- **Lifecycle considerations** — disposal, recyclability of branded merchandise
- **Supplier certifications** — FairTrade, B Corp, recycled-content thresholds
- **Carbon accounting** — design production emissions estimate (SPACE10 pattern)

## 5. Design tokens and developer handoff

The bridge from "brand guidelines PDF" to "design tokens JSON" is the largest efficiency opportunity in the industry.

### Required content

- **Token JSON** — the W3C Design Tokens Format Module structure:

```json
{
  "color": {
    "brand": {
      "primary": { "$value": "#2F73DB", "$type": "color" }
    }
  },
  "size": {
    "spacing": {
      "xs": { "$value": "4px", "$type": "dimension" }
    }
  }
}
```

- **CSS custom properties** export
- **Tailwind config** export
- **Figma variables** library
- **Naming convention** — scale.tier.purpose.state (e.g. `color.brand.primary.hover`)
- **Token doc** — auto-generated from the tokens file

### Top corpus examples

- **D008 Marina Dorcol** — Family.Weight typographic naming
- **E047 Widelab** — cubic-bezier animation curves as tokens
- **E063 IBM Garage** — modular "Scaffolding" framework

## 6. Motion and animation

Only ~10% of corpus covers motion. Increasingly important for digital brands.

### Required content

- **Easing curves** — named, with cubic-bezier values
  ```
  brand-default:    cubic-bezier(0.4, 0.0, 0.2, 1)
  brand-emphasis:   cubic-bezier(0.34, 1.56, 0.64, 1)
  brand-decelerate: cubic-bezier(0.0, 0.0, 0.2, 1)
  ```
- **Duration scale** — 100ms / 200ms / 400ms / 800ms typical; tied to use cases
- **Frame rate target** — 60fps minimum; 24+ fps for cinematic
- **Animation principles** — what's the brand's relationship to motion? Confident, playful, restrained?
- **Loop behavior** — for ambient animations
- **Reduced-motion compliance** — `prefers-reduced-motion` mapped to alternative

### Top corpus examples

- **D033 NOVEBA** (4.5/5) — 24+ fps frame-rate specs
- **E047 Widelab** — Cubic-bezier values
- **E088 Virgin Media** — Motion as a separate dedicated section
- **E104 NatGeo** — Index motion system

## 7. Brand architecture

For multi-brand / multi-product / acquired-brand portfolios.

### Required content

- **Architecture model** — branded house / house of brands / endorsed / hybrid
- **Sub-brand rules** — when to create one, when to extend
- **Lockup hierarchy** — primary brand position relative to sub-brand
- **Co-branding / partnership** — approval process, lockup rules
- **Acquired-brand transition** — how to phase from acquired identity to parent
- **Naming conventions** — "[Parent] [Sub-brand]" vs "[Sub-brand] by [Parent]" vs "[Sub-brand]" alone

### Top corpus examples

- **E082 HSBC** (5/5) — Multi-entity system, version-controlled
- **E067 Howden** (5/5) — Transition branding protocol for acquisitions
- **E075 AB InBev** (5/5) — Dual market strategy (Budweiser/Bud)
- **D016 Corwin** — Sub-brand section

## 8. Governance

Who owns the brand, who approves uses, how disputes resolve.

### Required content

- **Brand owner** — named role/team, contact channel
- **Approval workflow** — for new applications, partnerships, exceptions
- **Asset request process** — how to get logo files, request a new asset
- **Misuse reporting** — how to flag a violation (internal or external)
- **Update cadence** — when guidelines are reviewed (annually / per major release)
- **Version + changelog** — current version, last-major-update date
- **Contact** — single point of contact for brand questions

### Top corpus examples

- **E015 RAC** (5/5) — "Who to talk to" governance section + Media Garage internal asset resource
- **E001 DPD** — version history 2007–2013
- **E082 HSBC** — version-controlled with changelog
- **E054 Smithsonian** — self-described "always a work-in-progress"

## When to include extended elements

| Brand has... | Include |
|--------------|---------|
| Any digital product | Accessibility, dark mode, design tokens, motion |
| Public/regulated context | Accessibility, governance, multi-language |
| Multi-product portfolio | Brand architecture, governance |
| ESG mandate | Sustainability |
| AI in production / marketing | AI usage policy |
| Live brand evolution | Governance + version + changelog |
| Multi-market | Localization (TOV section) + multi-script (Type section) |

For **Compact** tier, skip all extended sections except a brief governance footer.
For **Standard** tier, include accessibility + governance at minimum; design tokens if digital.
For **Comprehensive** tier, include all relevant gaps. This positions the document above 90%+ of the market.
