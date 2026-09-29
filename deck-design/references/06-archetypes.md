# Layout archetypes

Every deck reduces to five slide shapes. If a slide will not fit one, the content is wrong before the layout is.

Keep the count at five. When two treatments are both legitimate, make them **named fills of one archetype** rather than a sixth archetype. Fills are cheap; archetypes are expensive, because each one is another thing to keep consistent.

---

## FULL — image bleeds all four edges

Chrome only, plus an optional caption bottom-left over a scrim.

**Fills**
- **Ambient** — image blurred into a ground. Title, section dividers, closing.
- **Sharp** — the photograph itself. Single-image slides.

**Covers** Title · Section divider · Single image · Large image with a small caption

**Notes** The grid sits under the image and is invisible; that is correct. Chrome colour follows the local luminance of the image, or the whole slide goes dark and chrome goes inverse.

---

## SPLIT — text zone beside an image zone

Both zones the full grid height, `space-between`, so they enclose the same rectangle.

**Fills**
- **Facts** — heading and body at top, label/value rows hanging from rules at the bottom.
- **Columns** — heading at top, two or three labelled paragraphs at the bottom.

**Covers** Text with image · Large image with a large caption · Case study

**Notes** The image ratio determines the text width — the two zones always total the full column count. Chrome lives entirely on the text side.

---

## STACK — headline top, ruled rows below

Rows hang from their own rules, filling from the bottom of the grid upward. The void sits between the headline and the first row.

**Fills**
- **Index** — number, title, page. Contents.
- **Phases** — number, title, description, timing. Process.
- **Table** — four columns, a rule-separated total row.
- **Stat** — two or three columns, big number over caption, each hanging from a rule.

**Covers** Contents · Process · Table · Stats and proof · Deliverables

**Notes** Each row is one pitch tall, the last one short by a gutter so the block lands on the grid. Stat columns get a smaller text offset than other columns — the number needs the width.

---

## GALLERY — text zone fixed, images fill the rest

The text zone stays put regardless of image count. This is what makes the family replicable.

**Orientations**
- **Row** — text above, gallery filling the width. 2-up 3:2, 3-up 4:3, 4-up 1:1.
- **Block** — text beside a square block of images. 4 (2×2), 6 (3×2), 8 (4×2, no text — the contact sheet).

**Covers** 2 / 3 / 4 image slides · Mood board · Work showcase

**Notes** Captions can hang above their image from a rule, in which case the caption row takes exactly one pitch. Media gutter tighter than layout gutter.

---

## STATEMENT — type only, edge to edge

**Fills**
- **Single** — one large utterance and one void; attribution hanging from a rule at the bottom.
- **Dense** — an anchor column (short heading top, large statement bottom) beside two columns of running copy.

**Covers** Large quote · Closing · Text-heavy content · Manifesto

**Notes** In the dense fill, the heading and the bottom statement can be the **same size** — hierarchy comes from the void between them. This is the one sanctioned exception to the size-contrast rule, and it works because the space does the work instead.

---

## Choosing

| The content is… | Archetype |
|---|---|
| One claim, nothing to prove yet | STATEMENT single |
| One claim plus 300+ words | STATEMENT dense |
| One claim plus one picture | SPLIT |
| One claim plus 2–4 pictures | GALLERY |
| A picture that needs the whole frame | FULL |
| A list, sequence, table or set of numbers | STACK |
| A beat between sections | FULL ambient, dark |

---

## Deriving a new slide

1. Name the content's shape, then pick the archetype from the table above.
2. Duplicate the archetype master — never start from a blank slide.
3. Swap content. Adjust only the offset and the image spans.
4. If you find yourself changing the zone logic, you have picked the wrong archetype. Go back to step 1.
