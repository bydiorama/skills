# Extended Elements

Use extended sections to address operational, digital, compliance, and governance needs beyond the canonical eight sections.

Include these for **Comprehensive tier** projects, or for any brand with a digital product, or when targeting enterprise-scale stakeholders.

## Core extended areas

| Area | Why it matters |
|------|----------------|
| Accessibility | Supports inclusive use and may be legally required |
| Dark mode / responsive | Keeps the system coherent across devices and display modes |
| AI usage policy | Defines safe, transparent, and on-brand use of AI tools |
| Sustainability | Connects production choices to environmental commitments |
| Design tokens / dev handoff | Translates brand decisions into implementation-ready values |

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

### Recommended practices

- Thread accessibility through every section rather than isolating it
- Ship a pairing matrix for large palettes, marking which combinations pass
- Document contrast ratios alongside the swatches, not in an appendix
- Give concrete, testable rules rather than a statement of intent

## 2. Dark mode

Include dark-mode rules for any brand with a digital product that supports or expects dark interfaces.

### Required content

- **Dark-mode color tokens** — equivalents for each light-mode token, defined as relationships not duplicates
- **Background hierarchy** — a 4-level background system (base, raised, overlay, accent) is the pattern worth copying
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

Define a substantive policy with clear qualification, review, disclosure, and accountability requirements.

### Required content

- **Permitted uses** — drafting, summarization, ideation, image-prompt generation
- **Prohibited uses** — generating final-public-facing copy without human review; AI-generated images presented as photography of real people / events; AI-generated quotes attributed to real individuals
- **Disclosure rules** — when to label AI-assisted content
- **Brand voice in AI prompts** — sample prompts that reliably produce on-voice output
- **AI tool whitelist** — which tools are sanctioned (Claude, ChatGPT, Midjourney, etc.) and at which tier (free, business, enterprise)
- **Data safety** — never input customer PII or proprietary product info into consumer AI tools
- **Hallucination protection** — fact-check rules; brand-claim verification process

### Forward-looking elements

- AI image generation: when allowed, when not, what style
- AI voice generation: synthetic voice rules; authorized voices; disclosure
- AI agents: rules for branded AI assistants (chatbot persona alignment to TOV)

## 4. Sustainability / environmental

Barely any guidelines address sustainability with substance. Mandatory direction for ESG-reporting brands.

### Required content

- **Materials policy** — preferred substrates (recycled paper, FSC-certified, soy inks)
- **Production efficiency** — print-on-demand vs warehouse; minimum-order thresholds
- **Digital sustainability** — image weight budgets, dark mode for energy savings, web font subsetting
- **Lifecycle considerations** — disposal, recyclability of branded merchandise
- **Supplier certifications** — FairTrade, B Corp, recycled-content thresholds
- **Carbon accounting** — an estimate of the emissions attributable to design production

## 5. Design tokens and developer handoff

Connect the brand guidelines to design tokens so approved values can flow directly into implementation.

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

### Recommended practices

- `Family.Weight` typographic naming that maps straight onto tokens
- Cubic-bezier animation curves published as named tokens
- A modular scaffolding framework rather than fixed layouts

## 6. Motion and animation

Include motion guidance when animation is part of the brand's product or communications experience.

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

### Recommended practices

- Frame-rate specifications (24+ fps) alongside the motion style
- Cubic-bezier easing values, not adjectives like "smooth"
- Motion given its own dedicated section rather than a paragraph in graphics
- A named, indexed motion system so animators can request a specific behaviour

## 7. Brand architecture

For multi-brand / multi-product / acquired-brand portfolios.

### Required content

- **Architecture model** — branded house / house of brands / endorsed / hybrid
- **Sub-brand rules** — when to create one, when to extend
- **Lockup hierarchy** — primary brand position relative to sub-brand
- **Co-branding / partnership** — approval process, lockup rules
- **Acquired-brand transition** — how to phase from acquired identity to parent
- **Naming conventions** — "[Parent] [Sub-brand]" vs "[Sub-brand] by [Parent]" vs "[Sub-brand]" alone

### Recommended practices

- A multi-entity system, version-controlled, with a rule per entity type
- A transition-branding protocol covering what happens during and after an acquisition
- A dual-market strategy where the same product carries different names by territory
- A dedicated sub-brand section rather than ad-hoc exceptions

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

### Recommended practices

- A "who to talk to" governance section, plus a named internal asset resource
- A published version history spanning several years
- Version control with a visible changelog
- An explicit statement that the document is always a work in progress

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
For **Comprehensive** tier, include every extended area relevant to the brand's products, markets, and operations.
