# Case Study Writer

A skill for creating compelling case studies for design studios and brand communication agencies. Transforms raw materials like interviews, press releases, and project documentation into polished case studies ready for website publication.

## Usage

Invoke this skill when you need to create a case study from project materials:

```
/case-study-writer
```

Or with specific materials:

```
/case-study-writer [path-to-materials]
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

- **Enthusiastic but grounded**: When something worked beautifully, let that excitement come through. "We could do so so so much with just these two shapes" is more compelling than "the visual system offered extensive possibilities."

- **Specific over generic**: "Took it straight to the legal department" beats "initiated the approval process." Real details create trust and interest.

- **Partnership-minded**: We see the world through our clients' eyes—their challenges become our challenges, their wins are shared wins. The case study tells the story of a collaboration, not a service delivery. We're partners working toward the same goal, and that mutual investment should come through in how we talk about the work.

### Prosody & Rhythm

- **Mix short punchy sentences with longer flowing ones**: Creates energy and keeps readers moving. "He got the vision. He was sold on the spot. Now we just needed to get buy-in from 16 different CEOs."

- **Use fragments strategically**: "Just a chance to get to know each other." "A creative and financial one." These create emphasis and conversational rhythm.

- **Embrace parenthetical asides**: They add intimacy and personality. "(and also my nervous system)" "(not knowing if this was even part of the product at all)"

- **Em dashes for emphasis and digression**: They're your friend for conversational breaks and added context.

### Vocabulary & Phrasing

- **Plain language elevated by specificity**: Don't reach for fancy words. Reach for precise ones. "We put it together to give prospective clients an overview" is better than "We developed this resource to provide potential partners with a comprehensive summary."

- **Colloquialisms have a place**: "Big guns," "sold on the spot," "bud"—these make writing feel alive. Use them where they fit naturally.

- **Unpack jargon, don't hide behind it**: If you must use industry terms, take a beat to explain. "Let's begin by unpicking the jargon a little…" is a great move.

- **Avoid the sea of sameness**: Generic phrases like "leveraging synergies," "best-in-class solutions," or "innovative approaches" say nothing. Find the real words for what actually happened.

### Structural Patterns

- **Lead with relatable context**: Start with something human—a problem everyone recognizes, a common frustration, a real moment. Then move into the specifics.

- **Reveal process including the uncertainty**: Don't pretend you knew everything would work. "There's no way they are going to let us get away with this" is honest and engaging storytelling.

- **Use analogies that connect**: "A relationship between a brand and its audience is no different from personal relationships" makes abstract concepts tangible.

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

## Example Output

See the TYO case study as the reference template:
- Accessible yet elevated tone
- Agency-focused narrative
- Concrete details and credentials
- Balanced product context
- Structured sections with clear hierarchy
- Fact-verified content

## Tips for Best Results

1. **Provide Complete Materials**: The more context available, the richer the case study
2. **Include Client Voice**: Interview transcripts add authenticity and uncover details
3. **Share Metrics**: Hard data makes impact more credible
4. **Document Process**: Behind-the-scenes insights demonstrate expertise
5. **Note Recognition**: Awards and press coverage add third-party validation
6. **Gather Presentations**: Slide decks often contain structured data and visuals
7. **Access Live Work**: Review the actual website/product to understand execution quality

## Continuous Improvement

After completing a case study, invoke `@skill-reflect case-study-writer` to update this skill with validated learnings from the execution.

## User-Invocable

Yes - users can invoke this skill directly with `/case-study-writer`
