# Preset — Diorama v3

A complete worked system from a studio pitch deck. Editorial register: tight margins, floating chrome, hairline rules, one highlight marker.

Use it as a reference implementation, or as a starting point when the brand context genuinely supports this register. **It is not a default.** Extract the client's own system first (Layer 1).

---

## Grid

| Property | Value |
|---|---|
| Format | 1920 × 1080 |
| Margin (L/R) | 56 |
| Chrome baseline | 32 from top |
| Grid top | 128 |
| Grid bottom | 1024 (56 from bottom) |
| Cell | 136 × 136, square |
| Gutter | 16, horizontal and vertical |
| Pitch | 152 |
| Grid | 12 × 6 = 1808 × 896 |
| Text offset | 152 / 304 / 456 as `padding-right` |

**Span(n) = 152n − 16** → `136 · 288 · 440 · 592 · 744 · 896 · 1048 · 1200 · 1352 · 1504 · 1656 · 1808`

The grid is anchored to the bottom: 128 above, 56 below. That asymmetry is where the tension comes from.

---

## Type

Saans (display + body), Aspekta (chrome only).

| Role | Size | Leading | Tracking |
|---|---|---|---|
| Chrome | 14 | 115% | +0.08em, uppercase |
| Body | 24 | 133% | 0 |
| Lead | 40 | 120% | −0.025em |
| Headline | 64 | 100% | −0.025em |
| Stat | 96 | 92% | −0.025em |
| Display | 120 | 93% | −0.035em |

Weights: 380 regular, 500 medium. Nothing above 500 — Saans stops at 600 and the deck never needs it.

---

## Colour

Runs entirely on the studio's `--ui-*` token set. No deck-specific colours exist.

**Neutral ramp (warm)**
`0 #1D1B19` · `10 #2F2C29` · `20 #423E3A` · `40 #69635D` · `60 #98918A` · `70 #B7B0A9` · `80 #DAD4CE` · `90 #EDE8E3` · `95 #F6F3F0` · `98 #FDFCFB` · `100 #FFFFFF`

**Accent — blue**
`20 #134553` · `40 #1B6C84` · `60 #5799B1` · `70 #79B8D3` · `80 #9EDBF3` · `90 #D2EBF8`

Additional ramps exist for orange, lavender, green and red — categorical use only.

**Deck roles**

| Role | Token |
|---|---|
| Ground (light) | `--ui-bg-surface` → neutral-98 |
| Ground (dark) | `--ui-bg-inverse` → neutral-0 |
| Text primary | `--ui-text-primary` → neutral-0 |
| Text metadata | `--ui-text-muted` → neutral-40 |
| Text on dark | `--ui-text-inverse` → neutral-95 |
| Rules | `--ui-border-subtle` / `--ui-border-strong` |
| **Marker** | `--ui-bg-accent` → blue-80 |

**The marker** is the single accent device: a highlight behind one continuous run of headline. Text inside it is always neutral-0, on light and dark grounds alike. Once per slide.

---

## Slide structure

```
Slide frame          plain, no flex, overflow clip
├ ⌗ Grid             absolute  56, 128   1808 × 896   cells at rgba(27,108,132,0.07)
├ Chrome / Top       absolute  56,  32   right 56
└ Content            absolute  56, 128   1808 × 896   ← everything inside is flex
```

Start any new slide by duplicating the starter board, which is those three layers and nothing else.

---

## Archetype dimensions

**SPLIT** — image ratio sets the caption width, two zones always total 12 cells:

| Image | Text zone |
|---|---|
| 6 × 6 (1:1) 896² | 6 cells, offset 304 |
| 8 × 6 (4:3) 1200 × 896 | 4 cells |
| 9 × 6 (3:2) 1352 × 896 | 3 cells |

**GALLERY row** — text above, gallery full width:

| Count | Cell width | Ratio | Height |
|---|---|---|---|
| 2-up | 896 | 3:2 | 592 |
| 3-up | 592 | 4:3 | 440 |
| 4-up | 440 | 1:1 | 440 |

**GALLERY block** — text beside a block of 440 squares: 4 (2×2, offset 304 or 152), 6 (3×2, no offset), 8 (4×2, no text).

**STACK** — rows one pitch tall (152), last row 136 so the block lands on the grid.

**Caption row** — exactly 152 tall, rule on top, so the image below starts on a row line.

---

## Template set

`00` Grid overlay · `00b` New-slide starter · `01` Title · `02` Contents · `03` Large quote · `04` Text content · `04b` Text-heavy · `05` Text + image · `06` Large image, small caption · `07` Large image, large caption · `08` Single image · `09` Process · `10–12` 2/3/4 images · `13` Mood board · `14` Table · `15` Closing · `16` Section divider · `17` Stat

---

## Register notes

What makes this system read the way it does, in case you are adapting rather than copying:

- Margins at 2.9% of width. Type large against them. The tension between the two is the whole effect.
- Chrome floating with no rule, tighter to the edge than the content.
- Structure entirely from hairlines and alignment. Zero border-radius, zero cards.
- One silence per slide, usually between statement and evidence.
- Dark grounds only on title, dividers and closing.
- One marker, one run, once.
