# Layer 5 — Craft and review

What must never slip, and how to check.

---

## Rules, guides and ratchets

Three grades, used deliberately.

- **Ratchet** — never loosens. Breaking it is a bug, not a choice.
- **Rule** — holds unless there is an argument.
- **Guide** — a default worth having a reason to leave.

Grading matters. A document where everything is mandatory gets ignored entirely; one where everything is advisory produces drift.

---

## Ratchets

### Structure
- Every slide carries a live grid layer as its first child.
- Three absolutely-positioned nodes per slide — Grid, Chrome, Content. Never auto-layout the slide frame.
- Chrome carries no rule, border or background.
- Rules sit above content. A rule below a block is forbidden.
- Border-radius is 0 on every structural element and every image.
- Chrome and content share one left edge.
- Every image edge lands on a cell line. Full-bleed excepted.

### Type
- Maximum four type styles per slide, chrome included.
- Maximum two weights and two colours per slide.
- Leading is a percentage, never a pixel value. It tightens as size grows.
- Uppercase belongs to chrome only.

### Colour and image
- One accent moment per slide, on one continuous run.
- Image ratios come from the cell table.
- Never invent prices, dates, metrics or client facts.

---

## Rules

- Chrome is three items.
- On a split, chrome lives on the text side.
- Body copy is the primary text colour; muted is for metadata only.
- A caption row occupies exactly one pitch.
- Ground follows the image.
- Text over an image needs a scrim or an ambient blur.
- Narrow media gutters require internal padding on adjacent text.
- Text-heavy slides use two columns of comfortable measure, never one wide one.
- Reach for space before size, size before weight, weight before colour.
- A pattern applies to every slide of its type, or it is not a pattern.

---

## Guides

- Content hangs off the top and sits on the bottom; silence in the middle.
- Sequence the deck loud → quiet → dense → loud.
- Ambient grounds mark the beats; sharp images do the work.
- Numbered lists are navigation, not decoration.
- Headline measure 592–1200px; body measure 560–650px.

---

## Review checklist

Screenshot every slide. Then:

**Argument**
- Read the headlines alone. Do they argue?
- Can you name each slide's job?
- Does every claim have proof somewhere?

**Composition**
- Is there one silence per slide, in the right place?
- Do side-by-side zones share top and bottom edges?
- Trace vertical lines through icons, numbers and trailing elements across repeated rows — do they align?
- Does anything sit off a cell line?

**Type**
- Count the type styles on the busiest slide. Four or fewer?
- Count weights and colours. Two or fewer each?
- Any uppercase outside chrome?
- Any line longer than about 60 characters?

**Content**
- Does every number, headline and label fit its zone at real size?
- Any placeholder left unflagged?
- Any invented fact?
- Diacritics correct throughout?

**Rhythm**
- Are there five loud slides in a row?
- Are the section boundaries marked?
- Does the deck end on the ask?

---

## The loop

The method, not a nicety. Skipping the fork is how decks end up with one idea repeated.

1. **Draft** one slide against the closest archetype.
2. **Fork** into two or more genuinely different versions — different zone logic, not tweaks.
3. **Review** side by side. Write down what each one does well; usually both contribute.
4. **Reduce** to one master, folding the survivors in. Where two fills are both legitimate, keep both as named options.
5. **Copy, adapt, repeat** for the next content type.

---

## Test with real content

**Template boards lie.** They carry copy chosen to fit. Build one real deck with real copy, real numbers and real images before calling the system finished.

Then fix what breaks **in the master**, not only in the instance. A bug found in a real deck and patched only on that slide will reappear in every future deck.

Things real content reliably surfaces that templates never do:

- a figure that overflows its column at display size
- a headline that needs three lines where the template had two
- an image ratio that destroys a particular kind of image
- a caption that collides with the next column
- a language whose diacritics or word lengths break a lane

---

## Common failure modes

| Symptom | Cause | Layer |
|---|---|---|
| Deck looks unrelated to the client | System invented, not extracted | 1 |
| Every slide a different composition | Grid decided after content | 0 |
| Complete but forgettable | Built from an outline, not an argument | 2 |
| Reads as bluster | All assertion, no proof | 2 |
| Busy and tiring | Type budget exceeded | 3 |
| Looks arranged, not composed | Zones not enclosing a shared rectangle | 0 |
| Looks like a default template | Margins too generous, type too modest | 4 |
| Caption unreadable on one slide only | Trusted a crop instead of a scrim | 4 |
| Screenshot unreadable in a gallery | Content-awareness ignored | 4 |
| System breaks on the second deck | Never tested with real content | 5 |
