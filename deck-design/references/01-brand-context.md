# Layer 1 — Brand context and visual language

Whose language is this, and where is it already written down?

---

## The rule that matters most

**Extract. Do not invent.**

The most expensive error in deck work is designing a visual system for a client who already has one. It wastes the work, it produces something the client's other materials will contradict, and it signals that nobody looked.

Almost every client has one of these, and usually several:

- a **design token set** (`--ui-*`, `--color-*`, a Tailwind theme, a Figma variable collection)
- a **palette artefact** — a swatch board, a colour page in a brand book
- a **live product or site** whose CSS is readable
- an **existing deck** whose type and colours can be sampled
- a **component library**

Find it before you draw. If the file you are working in has design tokens, read them first — they are the brand, already decided.

---

## Extraction protocol

Run in order. Stop and report what you found before designing.

1. **Read the tokens.** In Paper: `get_basic_info` returns the token list. In a repo: find the theme file. In Figma: read the variable collections.
2. **Find the palette artefact.** Ask: "is there a colour page, swatch board, or brand deck?" If there is one in the file, extract it — `get_jsx` on a swatch group returns both the hex and the token name in one call.
3. **Sample the live product** if one exists. It is the most honest record of what actually ships.
4. **Read the type.** Confirm which weights genuinely exist before specifying any (`get_font_family_info` in Paper). Specifying a weight the family does not have produces silent synthetic rendering.
5. **Note what is deliberately absent.** If the palette has no yellow, do not introduce one. If the type system has three weights, the deck gets at most two of them.

---

## What to extract

### Colour

Capture the full structure, not just the hexes:

| Group | What to look for |
|---|---|
| **Neutral ramp** | 8–11 steps from ink to paper. Note whether it is warm or cool — this sets the whole deck's temperature. |
| **Accents** | Full ramps per hue, not single values. |
| **Semantic aliases** | `text-primary`, `text-muted`, `bg-surface`, `border-subtle`, `border-strong`. These tell you the client's own intent and should drive the deck's roles directly. |
| **Contrast pairs** | Which border/text steps the system considers safe on which grounds. |

Then map deck roles onto them. Do not create parallel deck-specific colours; alias to what exists.

### Type

- Families and their **actual** available weights
- The existing size scale, if any
- Which family is display and which is utility

### The accent device

Every strong deck has exactly one coloured moment per slide. Decide what it is, in the client's palette:

- a **highlight marker** behind a run of headline
- a single coloured glyph or figure
- one tinted field

Pick one. A device that appears twice on a slide is decoration.

---

## When the register is genuinely open

Sometimes there is no system and none is coming. Then, and only then, commit to a register before choosing values — and say out loud that you are inventing.

Name a **physical scene**, then derive every colour from a named object in it. "Press room" gives you soy-ink black, uncoated stock, plate-marking fluorescent. "Maritime" gives you fog grey and deep navy. If you cannot name an object for a role, the palette is abstract and will look glued together.

Avoid the current clichés: warm off-white with terracotta; charcoal with electric purple; tinted warm grounds under high-chroma accents.

---

## Grounds

Decks need at most two grounds:

- **Light** — the working ground. Every content slide.
- **Dark** — the beats only. Title, section dividers, closing. Never the working slides.

A third ground is a decision nobody will maintain.

**The ground follows the image.** Dark photograph, dark slide. Light photograph, light slide. Never fight the picture.

---

## Failure modes

| Symptom | Cause |
|---|---|
| Deck looks unrelated to the client's product | System invented instead of extracted |
| Colours look "designed" rather than owned | Accent chosen for taste, not from the ramp |
| Type renders slightly wrong at some weights | Weight specified that the family does not have |
| Deck contradicts the client's website | Nobody sampled the live product |
| Palette feels glued together | Invented without a scene to derive from |
