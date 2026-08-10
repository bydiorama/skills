---
name: case-study-writer
description: >
  Write a publication-ready project case study for a design studio, brand agency, or any
  professional services firm, from raw materials — interview transcripts, press releases,
  project documentation, decks, and client communications. Use whenever the user asks to
  write, draft, or structure a case study, project story, portfolio piece, work page, or
  "write up this project" for a website. Trigger on "case study", "project write-up",
  "portfolio piece", "work page", "client story", "success story", or when the user
  uploads project materials and asks to turn them into something publishable. Also use to
  rewrite or tighten an existing case study. Do NOT use for: sales proposals, pitch decks,
  press releases, marketing campaign briefs, or academic case studies. The deliverable is
  narrative marketing content about completed work.
---

# Case Study Writer

Turn raw project materials — interviews, press releases, documentation, decks — into a
polished case study ready to publish.

## Usage

```
@case-study-writer
@case-study-writer [path-to-materials]
```

## What This Skill Does

1. **Gathers Resources**: Collects and analyzes all available project materials including:
   - Interview transcripts
   - Press releases
   - Project documentation
   - Presentation slides
   - Links and reference materials
   - Client communications
   - Media coverage
   - Website content

2. **Extracts Key Information**: Identifies and organizes:
   - Project title and description
   - Client details (name, industry, stage, country, year)
   - Client team composition and credentials
   - Challenge and objectives (including research data and statistics)
   - Strategy and approach
   - Processes and methodologies
   - Scope of collaboration
   - Timeline and constraints
   - Results, outcomes, and impact
   - Hard data and metrics (when available)
   - Services provided
   - Team credits
   - Press mentions and media recognition

3. **Crafts Case Study**: Creates a structured case study with:
   - Compelling title (short project description)
   - Engaging narrative covering challenge, strategy, process, and outcomes
   - Project metadata (client, year, country, industry, stage, project type)
   - Services provided list
   - Added value and impact section
   - Credits section (if available)
   - Press and media recognition (if available)
   - Client website link

4. **Fact-Checks Content**: Verifies all information against source materials to ensure accuracy

5. **Saves Markdown File**: Creates a well-formatted Markdown file in the appropriate project directory

## Case Study Structure

Each case study follows this structure:

### Header Section
```markdown
# [Compelling Title: Short Project Description]

**Client**: [Client Name]  
**Year**: [Year]  
**Country**: [Country]

**Industry**: [Industry]  
**Stage**: [Startup/Scale-up/Enterprise/etc.]  
**Project Type**: [Type]

---
```

### Narrative Sections

**Challenge** (2-3 paragraphs)
- Client background and team composition with specific credentials
- Market research, user research, or validation data (with statistics)
- Core problem or opportunity
- Timeline and budget constraints
- Strategic context

**Strategy** (2-3 paragraphs)
- Positioning and strategic framing
- Key decisions and rationale
- Approach to constraints
- Collaboration model
- How agency work aligns with client goals

**Process** (3-4 paragraphs with subheadings)
- Specific deliverables and how they were created
- Technical and creative approaches
- Problem-solving and innovative methods
- Tools, technologies, or methodologies employed
- Focus on agency methodology and expertise

**Scope** (1 paragraph)
- Timeline
- Key deliverables summary
- Nature of engagement

**Results & Impact** (2-3 paragraphs)
- Quantitative outcomes (when available)
- Qualitative impact
- How deliverables achieved client goals
- Market response or validation

**Added Value** (1-2 paragraphs)
- What the agency delivered beyond the brief
- Innovative approaches or methodologies
- Strategic insights or frameworks
- Relationship and collaboration quality

### Supporting Sections

**Services Provided**
```markdown
- Service 1
- Service 2
- Service 3
```

**Credits** (if available)
```markdown
Team members and roles
```

**Press & Recognition** (if available)
```markdown
Media mentions and awards
```

**Footer**
```markdown
---

**Visit**: [clientwebsite.com](http://clientwebsite.com)
```

## Writing Style

The skill produces case studies that feel like a conversation with a smart, passionate colleague—candid, insightful, and genuinely engaged with the work. The writing should feel human first, professional second.

### Tone & Voice

- **Conversational and candid**: Write like you're talking to someone who gets it. Share real reactions and honest observations. Don't be afraid to acknowledge the messy parts of creative work—the nerves, the uncertainty, the moments where you just had to trust your gut.

- **Self-aware without being precious**: A little self-deprecation goes a long way. If you're going long, own it. If something sounds like jargon, call it out and explain what you actually mean.

- **Enthusiastic but grounded**: When something worked beautifully, let that excitement come through. "Two shapes, and suddenly we could build anything" is more compelling than "the visual system offered extensive possibilities."

- **Specific over generic**: "She walked it down to legal that afternoon" beats "the approval process was initiated." Real details create trust and interest.

- **Partnership-minded**: We see the world through our clients' eyes—their challenges become our challenges, their wins are shared wins. The case study tells the story of a collaboration, not a service delivery. We're partners working toward the same goal, and that mutual investment should come through in how we talk about the work.

### Prosody & Rhythm

- **Mix short punchy sentences with longer flowing ones**: Creates energy and keeps readers moving. "He got it immediately. Sold, on the spot. Which left only the small matter of convincing everyone else."

- **Use fragments strategically**: "Just a conversation, to start." "A cost, and not only a creative one." These create emphasis and conversational rhythm.

- **Embrace parenthetical asides**: They add intimacy and personality — a quick aside about what the team was actually feeling, or what nobody knew yet at that point in the project.

- **Em dashes for emphasis and digression**: They're your friend for conversational breaks and added context.

### Vocabulary & Phrasing

- **Plain language elevated by specificity**: Don't reach for fancy words. Reach for precise ones. "We wrote it so clients would know how we work before the first call" beats "We developed this resource to provide potential partners with a comprehensive summary."

- **Colloquialisms have a place**: Informal phrasing makes writing feel alive. Use it where it fits naturally, not as decoration.

- **Unpack jargon, don't hide behind it**: If you must use an industry term, take a beat to explain it in plain words before moving on.

- **Avoid the sea of sameness**: Generic phrases like "leveraging synergies," "best-in-class solutions," or "innovative approaches" say nothing. Find the real words for what actually happened.

### Structural Patterns

- **Lead with relatable context**: Start with something human—a problem everyone recognizes, a common frustration, a real moment. Then move into the specifics.

- **Reveal process including the uncertainty**: Don't pretend you knew everything would work. Admitting "we were fairly sure they would never approve it" is honest and engaging storytelling.

- **Use analogies that connect**: Comparing a brand's relationship with its audience to an ordinary human relationship makes an abstract idea tangible.

- **Let the work breathe**: Not everything needs to be explained or justified. Sometimes you show what you made and trust the reader to see why it matters.

### What to Avoid

- Corporate-speak and hollow superlatives ("world-class," "cutting-edge," "seamless")
- Overly formal constructions that create distance
- Hiding behind process descriptions without personality
- Making everything sound easy or inevitable (the tension is what makes it interesting)
- Writing that could describe any agency working on any project
- Use em-dash only on rare occasions

## Content Priorities

### What to Emphasize
1. **Agency deliverables and process** (primary focus)
2. **Client context and challenges** (supporting frame)
3. **Problem-solving and methodology** (shows expertise)
4. **Specific credentials and data** (builds credibility)
5. **Strategic thinking** (demonstrates value)
6. **Collaboration approach** (relationship quality)

### What to De-emphasize
- Lengthy product feature descriptions
- Superlatives and marketing language
- Generic statements about "quality" or "excellence"
- Overly technical jargon without context

## When Hard Data Isn't Available

When metrics or numbers are unavailable, the skill promotes based on:
- Quality and craft of deliverables
- Innovative approach or methodology
- Breadth and depth of services
- Strategic thinking and insights
- Client credentials and stature
- Complexity of challenge addressed
- Collaboration model and relationship
- Industry recognition or awards

## Quality Assurance

The skill includes mandatory fact-checking:
- Cross-references all claims with source materials
- Flags any information that cannot be verified
- Ensures consistency across all case study sections
- Validates dates, names, credentials, and factual details
- Verifies statistics and research data
- Confirms website URLs and links

## Output Location

The skill should:
1. Identify or ask for the project directory
2. Create a Markdown file named `[ClientName]-Case-Study.md`
3. Save to the appropriate subdirectory in the case studies folder
4. Confirm file location to the user

## What good looks like

A finished case study should read as:
- Accessible yet elevated in tone
- Agency-focused in narrative, client-grounded in context
- Concrete in its details and credentials
- Balanced in how much product context it carries
- Clearly structured, with a scannable hierarchy
- Fact-verified end to end

## Tips for Best Results

1. **Provide Complete Materials**: The more context available, the richer the case study
2. **Include Client Voice**: Interview transcripts add authenticity and uncover details
3. **Share Metrics**: Hard data makes impact more credible
4. **Document Process**: Behind-the-scenes insights demonstrate expertise
5. **Note Recognition**: Awards and press coverage add third-party validation
6. **Gather Presentations**: Slide decks often contain structured data and visuals
7. **Access Live Work**: Review the actual website/product to understand execution quality

## Related skills

- `brand-strategy` — the strategic work a case study is often describing
- `anti-skill` — stress-test the draft before it is published

## Sourcing and rights

Everything in the case study must trace to a supplied source. Do not quote a client, a
partner, or a press article without confirming the studio has permission to publish it, and
do not lift phrasing from another agency's published writing — describe the pattern and
write it fresh.
