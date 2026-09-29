# Layer 4 — Art direction

How the page behaves: chrome, rules, type, images, colour, space.

---

## Chrome

The running head that tells the audience where they are.

- **Three items.** Page number far left, section label indented, document title far right. A fourth means something else should have been cut.
- **No rule, no border, no background. Ever.** Chrome sitting in a box reads as a header bar; chrome floating near the bleed reads as a printed page. Every strong reference in the corpus does the latter.
- **Tighter to the edge than the content is.** If content sits at y 128, chrome sits at y 32. That difference is what makes the content feel *placed* rather than defaulted.
- **Same left edge as the content.** One vertical axis for the whole deck.
- Uppercase, tracked, small — around 0.75% of the frame width.

On a split slide, keep all chrome on the text side. Never over the image: legibility then depends on which photograph got dropped in, which is not a system.

---

## Rules

- **A rule sits above the content it belongs to.** Content hangs *from* a rule. A rule under a block reads as a lid and closes it off.
- A rule is a hairline. Structure comes from alignment, not from weight.
- **No boxes, no cards, no border-radius.** Radius is 0 on every structural element and every image. Information lives on the surface, not inside containers.
- Where a caption row precedes an image, give the row exactly one pitch of height so the image below starts on a row line.

---

## Type

Two families at most: one display, one utility. Utility carries chrome only.

Six roles, no more:

| Role | Size (at 1920) | Leading | Job |
|---|---|---|---|
| Chrome | 14 | 115% | Page number, section, doc title |
| Body | 24 | 133% | Running copy, table cells, captions |
| Lead | 40 | 120% | Large captions, contents entries, anchor columns |
| Headline | 64 | 100% | The one statement per slide |
| Stat | 96 | 92% | Numbers only |
| Display | 120 | 93% | Title, dividers, quotes |

**Leading is always relative, expressed as a percentage.** It keeps the scale proportional if a size moves, and nobody recomputes pixels by hand.

**Leading tightens as size grows.** 133% at body, solid at headline, negative above. Display type at these sizes wants compressing, not air. Numerals set tighter still — they have no descenders.

Ratios against body: **0.6 : 1 : 1.7 : 2.7 : 4 : 5**. There is nothing at 1.2×. Two things differ clearly or not at all.

---

## Space

**Tight margins plus big type is the differentiator.** The tension between a near-flush edge and a large headline is the most transferable quality in editorial reference work. Generous margins with modest type is what a default template looks like.

- Content hangs off the top and sits on the bottom; the silence goes in the middle.
- Related things closer, unrelated things further. Related is not "adjacent" — it is "one idea".
- After a layout is complete, remove a fifth of its non-essential elements and look again.

---

## Images

### Ratios
From the cell table only (Layer 0). A full-bleed panel is exempt because the format dictates it.

### The ratio sets the caption width
On a split slide the two zones always total the full column count. Choosing the picture chooses how much you get to say:

| Image | Text zone |
|---|---|
| 6 × 6 (1:1) | 6 cells, with a 2-column offset |
| 8 × 6 (4:3) | 4 cells |
| 9 × 6 (3:2) | 3 cells |

### Count sets the crop
As the count rises, the crop gets squarer and the band shortens:

| Count | Ratio |
|---|---|
| 2-up | 3:2 |
| 3-up | 4:3 |
| 4-up | 1:1 |

### Content-awareness
This is the rule people skip, and it is the one that matters:

- **Cluttered imagery** — screenshots holding several UI screens, contact sheets, brand boards — gets **one** frame, at split or full-bleed scale. A square crop on a screenshot destroys the thing it was meant to show.
- **Photographs and close-ups** can take square crops and go up to eight.

Look at the image before choosing the layout. The slide's layout must be aware of its content.

### Gutters
The media gutter is **tighter than the layout gutter**. A narrow gutter makes a band of images read as one object and creates tension; a wide one makes them read as separate pictures on the same slide.

When the gutter tightens, captions and body text take their own internal `padding-right` — usually one column — so they never optically touch the neighbouring image.

### Text over images
Any text over an image needs a scrim, or the image needs to be blurred into an ambient ground. Never trust a crop to stay legible; the next image will be lighter exactly where the caption sits.

An **ambient ground** — the image blurred to abstraction — is the cleanest treatment for title slides and dividers. Reserve sharp full-bleed for the actual single-image slides.

---

## Colour

- **One accent, once per slide.** One intense moment is stronger than five.
- Two text colours: content and metadata. A third is a mistake, not a nuance.
- Dark grounds mark the beats — title, dividers, closing. Never the working slides.
- Tint fields, where used at all, should have a job — one slide family, not decoration.

---

## What not to do

| Don't | Because |
|---|---|
| Put chrome in a ruled band | Reads as a UI header, not a printed page |
| Put a rule under a block | Closes the block instead of hanging it |
| Use cards to group information | Boxes replace alignment with containers |
| Add an intermediate type size | Weak hierarchy is worse than none |
| Centre a composition to avoid deciding | Centring is inert; it is not a decision |
| Fill the empty area | The empty area already has a job |
| Use a square crop on a screenshot | Destroys the content the image was chosen for |
| Set uppercase outside chrome | Volume without rhythm |
