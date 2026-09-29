# Layer 0 — Canvas

The geometry everything else is made of. Decided first, written down, and made visible.

---

## Why this is Layer 0 and not a graphic-design rule

A grid decided *after* content is a description of what you already did. A grid decided *before* content is a machine for making the next fifty decisions. The difference shows up as speed: on a settled grid, a new slide type takes minutes and lands correctly; without one, every slide is an argument with itself.

The test: **if you are estimating a width mid-layout, the canvas is not finished.** Stop and finish it.

---

## Square cells

Make the cell square. This is the highest-leverage decision in the whole system, because it converts image sizing from a judgement into arithmetic.

When the cell is square, every conventional image ratio becomes an integer rectangle of cells:

| Ratio | Cells |
|---|---|
| 1:1 | 3 × 3, 4 × 4, 6 × 6 |
| 4:3 | 4 × 3, 8 × 6 |
| 3:2 | 3 × 2, 6 × 4, 9 × 6 |
| 4:5 | 4 × 5 |
| 2:3 | 2 × 3 |
| golden | 8 × 5 (approx.) |

Nobody has to compute a crop. They count cells.

---

## Deriving a grid

Work in this order:

1. **Format.** 1920 × 1080 is the modern default and maps to every presentation tool. A4 landscape survives for print-first work.
2. **Margin.** Tight. 3–5% of width. This is where tension comes from — see Layer 4.
3. **Cell + gutter.** Pick a gutter first (it should be small — 16px at 1920 is a good default), then solve for a cell size that divides the content width into whole columns.
4. **Rows.** Same cell edge, same gutter. Square cells means rows and columns share a number.
5. **Vertical anchor.** Give the grid *unequal* top and bottom margins. More air above than below reads as deliberate placement; equal margins read as centring, which is inert.

### Worked example (1920 × 1080)

```
margin        56          →  content width 1808
cell          136 × 136      (square)
gutter        16
columns       12          →  12 × 136 + 11 × 16 = 1808 ✓
rows          6           →   6 × 136 +  5 × 16 = 896
grid top      128            (deliberately > bottom margin)
grid bottom   1024           (= 1080 − 56)
chrome        y 32           (tighter than content — see Layer 4)
```

**Span(n) = pitch × n − gutter**, where pitch = cell + gutter = 152.

`136 · 288 · 440 · 592 · 744 · 896 · 1048 · 1200 · 1352 · 1504 · 1656 · 1808`

List these. They are the only widths anyone is allowed to use.

---

## The grid is a live layer, not a reference board

Put the grid **on every slide** as its first layer, at a low tint (6–8% of an accent). Reasons:

- Offsets become readable. You can count the columns a text zone gives back.
- Misses become obvious. An image edge that missed a cell line is visible instead of theoretical.
- It makes "set the canvas first" the literal first action when someone starts a new slide.

Keep a **starter slide** — grid, chrome, empty content zone, nothing else — for duplicating.

Visible enough to be useful is also visible enough to remind you to hide it before export. A grid you can barely see is a grid nobody checks. Build the hide step into the export routine.

On full-bleed slides the grid sits under the image and is therefore invisible. That is correct — hide the image for a moment if you need to place against it. Do not float the grid over artwork; every treatment strong enough to read over a photograph also damages the photograph.

---

## Slide structure

Exactly three absolutely-positioned nodes, in this order:

| Layer | Position |
|---|---|
| **Grid** | left `margin`, top `grid-top`, size `content × grid-height` |
| **Chrome** | left `margin`, top `chrome-y`, right `margin` |
| **Content** | left `margin`, top `grid-top`, size `content × grid-height` |

Everything inside **Content** is flow/auto-layout.

**Never auto-layout the slide frame itself.** It forces every child into absolute positioning, which makes content edits and slide derivation painful and is the single most common structural mistake in tool-built decks.

---

## Zone enclosure

When two zones sit side by side — text beside a gallery, text beside an image — give both the **full grid height** and `justify-content: space-between`.

Their tops and bottoms then lock to the same rectangle. The void between the top and bottom items becomes the composition instead of leftover space. This one rule is the difference between a slide that looks composed and one that looks arranged.

---

## The offset

When a gallery leaves a text zone more width than the copy needs, absorb the surplus as **whole columns of `padding-right`** — one, two, or three pitches.

More text → smaller offset. Less text → bigger offset. The gallery stays locked to the grid; only the measure moves. This is the adjustable variable in an otherwise rigid system.

---

## Paper-specific mechanics

- Build incrementally with `write_html` — roughly one visual group per call. The user watches it appear.
- `<x-paper-clone node-id="…">` reuses existing nodes cheaply.
- Remote image URLs work in `<img src>`; `get_fill_image` returns the `originalUrl` of any existing image fill, which is how you reuse assets already in the file.
- Duplicate a master and `set_text_content` rather than rewriting HTML — far cheaper, and `descendantIdMap` gives you every cloned child ID immediately.
- Screenshots fail intermittently on large files. When they do, verify by `get_computed_styles` — on a cell grid the geometry is deterministic, so computed values are sufficient proof. Say so rather than claiming a visual check you did not make.
- `filter: blur()` works and is the cleanest way to make an ambient photographic ground.
