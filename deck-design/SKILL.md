---
name: deck-design
description: Design presentation decks and slides that hold together — pitch decks, proposals, credentials, strategy readouts, workshop outputs, brand presentations, sales decks, investor decks, report layouts. Use this skill whenever the user asks to build, design, elevate, extend, restructure, or art-direct a deck, presentation, slide template set, or slide master — in Paper, Figma, Keynote, Google Slides, PowerPoint, or as HTML. Trigger on "deck", "presentation", "slides", "slide templates", "pitch deck", "proposal deck", "credentials deck", "keynote", "make this deck better", "design a template for our presentations". Also use when the user supplies reference slides and asks to derive a style, or supplies a brief/scope document and asks for a deck from it. Brand-agnostic — it extracts the visual language from whatever system already exists. Do NOT use for: brand guidelines documents, single marketing artworks, social posts, or long-form documents that are not paginated to a fixed frame.
---

# Deck Design

Build slide systems that survive contact with real content. A deck is not a series of pictures — it is one argument, paginated, running on a grid that was decided before anything was placed on it.

## The core principle

**Set the canvas, give it rules, then arrange content.** In that order, always. Deriving a new slide from a settled grid is nearly free; arranging content first and looking for a grid afterwards is how decks become 40 unrelated compositions. Every hard-won improvement in the source project for this skill came from moving a decision *earlier* in this sequence, never later.

## The layer model

Six layers. They are a **build order**, not a menu — each one constrains the next, and skipping down the stack produces work that has to be redone.

| | Layer | Question it answers | Reference |
|---|---|---|---|
| **0** | **Canvas** | What geometry is everything made of? | `references/00-canvas.md` |
| **1** | **Brand context** | Whose visual language is this, and where is it already written down? | `references/01-brand-context.md` |
| **2** | **Role & message** | What is this deck arguing, and what should each slide make someone feel? | `references/02-role-and-message.md` |
| **3** | **Content** | Is the copy true, short enough, and does it earn its slide? | `references/03-content-rules.md` |
| **4** | **Art direction** | How does the page behave — chrome, rules, images, colour, space? | `references/04-art-direction.md` |
| **5** | **Craft & review** | What must never slip, and how do we check? | `references/05-craft-and-review.md` |

Layout archetypes — the finite set of slide shapes every deck reduces to — live in `references/06-archetypes.md`. Read it alongside Layer 4.

## Workflow

### Phase 1 — Extract, don't invent [MANDATORY]

Before drawing anything, find the visual language that already exists. Run the extraction protocol in `references/01-brand-context.md`.

**The most expensive error in deck work is inventing a system the client already has.** Design tokens, a palette artefact, a live site, a Figma library, an existing deck — one of these almost always exists. Ask for it, or go and read it. Only invent when you have confirmed there is nothing to extract, and say so out loud when you do.

Stop and confirm what you found before continuing.

### Phase 2 — Set the canvas [MANDATORY, before any content]

Decide format, margins, cells, gutter, rows. Write the numbers down. Put a visible grid layer on the master slide. See `references/00-canvas.md`.

Do not proceed until span widths are computed and listed. If you find yourself estimating a width mid-layout, the canvas is not finished.

### Phase 3 — Establish the argument

Write the deck's spine as a list of headlines before designing any slide. If the headlines alone do not make the argument, no layout will rescue it. See `references/02-role-and-message.md`.

### Phase 4 — Draft, fork, reduce

Design **one** slide against the closest archetype. Then fork it into two or more genuinely different versions — different zone logic, not tweaks. Review side by side, name what each does well, and reduce to one master, folding the survivors in.

Where two fills are both legitimate, keep both as named options of one archetype rather than inventing a new archetype.

Then copy, adapt to the next content type, and repeat. This loop is the method; do not skip the fork.

### Phase 5 — Derive the set

Produce the full template set from the settled masters. Every slide is an instance of an archetype. If a slide will not fit one, the content is wrong before the layout is.

### Phase 6 — Test with real content [MANDATORY]

Build one real deck with real copy, real numbers and real images. **Template boards lie.** They are populated with copy chosen to fit. Real content is where you discover that a figure overflows its column, a headline needs three lines, or an image ratio destroys a screenshot.

Fix what breaks **in the master**, not only in the instance.

### Phase 7 — Review

Run the checklist in `references/05-craft-and-review.md`. Screenshot every slide. Trace the vertical lanes.

## Presets

`presets/diorama-v3.md` is a complete worked system — grid, tokens, archetypes, ratchets — from a real editorial-register studio deck. Use it as a reference implementation, or as a starting point when the brand context genuinely supports that register. It is not a default; extract the client's system first.

## Working in a design tool

The grid, zone and layer conventions are tool-agnostic, but the structural rule is not:

**Never auto-layout the slide frame itself.** It forces every inner object into absolute positioning and makes both content edits and slide derivation painful. Use exactly three absolutely-positioned nodes per slide — **Grid, Chrome, Content** — and let everything inside Content be flow/auto-layout.

Paper-specific mechanics, including the incremental `write_html` workflow and the image-fill traps, are noted at the end of `references/00-canvas.md`.

## Triggers and behaviours

- **"Make our deck better"** → Phase 1 first. Do not restyle before you know what system exists.
- **User supplies reference slides** → derive patterns before proposing anything; list what the references agree on, not what you like about them.
- **User supplies a brief or scope doc** → Phase 3 first. Turn it into an argument, then a headline spine, then slides.
- **User asks for one slide** → still set the canvas. A one-off on no grid becomes the thing everything else has to match.
- **Prices, dates, metrics, client facts** → never invent them. Use a visible placeholder (`€ —`) and flag it. Fabricated numbers in a commercial document are a serious error, not a rounding one.
