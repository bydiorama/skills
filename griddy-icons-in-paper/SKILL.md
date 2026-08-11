---
name: griddy-icons-in-paper
description: >
  Place real griddy-icons glyphs into a Paper (paper.design) artboard instead of
  hand-drawing approximations. Use whenever a Paper design needs an icon and the project
  uses griddy-icons — component sheets, handoff specs, app screens, or any mockup where
  the drawn icon has to be the one that ships. Trigger on "add an icon in Paper", "icon
  for this artboard", "griddy icon", "griddy-icons", "put the real icon in the design", or
  when working in a Paper file that needs iconography. Covers extracting path data from
  the installed package, the exact SVG markup Paper wants, layer-naming for handoff, the
  brand-mark trademark trap, and the token-ordering bug that silently drops a fill. The
  extraction technique generalises to any icon package that ships SVG path data; the Paper
  markup specifics do not. Do NOT use for choosing an icon set, designing new icons, or
  icon work in Figma.
---

# griddy-icons in Paper

A hand-drawn glyph is a lie in a handoff. It looks close enough to approve and
does not match what renders, so the sheet stops being a contract for the one
thing nobody re-checks. `griddy-icons` is an npm package sitting in
`node_modules` — the real path data is a `cat` away, and pasting it into Paper
costs no more than drawing a wrong one.

**Rule: never draw an icon by hand if the project has an icon set installed.**
Extract it.

## 0 · Setup

Both dependencies are public. [`griddy-icons`](https://github.com/griddy-icons/griddy-icons)
is a free MIT-licensed set; [Paper](https://paper.design) is a design tool whose canvas is
real HTML/CSS and which ships an MCP server for agents.

```bash
npm install griddy-icons
claude mcp add paper --transport http http://127.0.0.1:29979/mcp --scope user
```

Figures below are from `griddy-icons@0.2.0`. Counts drift between releases — the listing
command in step 1 is the source of truth, never a number written here.

## 1 · Confirm the name exists before you use it

1159 icons, so guessing produces a missing file rather than a wrong picture.
List them:

```bash
node --input-type=module -e "
import * as g from 'griddy-icons';
console.log(Object.keys(g).filter(k => /^[A-Z]/.test(k)).join(' '));
"
```

Grep that list for the concept, not for the word you have in mind — the set
names things by what they depict (`Colors`, `TextFont`, `UsersGroup`,
`ExpandSidebar`), not by the role you are filling.

## 2 · Extract the path data

Each icon is a directory with two weights. `regular` is the outline weight and
the default; `filled` is the solid one.

```bash
node -e '
const fs = require("fs");
const names = ["Home", "Search", "Colors"];        // <- your icons
const weight = "regular";                           // or "filled"
for (const n of names) {
  const p = `node_modules/griddy-icons/dist/icons/${n}/${weight}.js`;
  if (!fs.existsSync(p)) { console.log(n, "MISSING"); continue; }
  const ds = [...fs.readFileSync(p, "utf8").matchAll(/d:\s*"([^"]+)"/g)].map(m => m[1]);
  console.log("### " + n + "\n" + ds.join("\n"));
}'
```

**Take every `d`, not the first.** About 7% of the set (80 of 1159 in `0.2.0`) is two or
more subpaths — uncommon enough that you will not be expecting it, common enough that you
will hit it. One match gets you half an icon, which is harder to spot than none.

## 3 · The markup Paper wants

```html
<svg width="16" height="16" viewBox="0 0 24 24" fill="none">
  <path d="…" fill="var(--your-icon-token)" />
</svg>
```

Three things matter and each is a way to get it wrong:

- **`viewBox` stays `0 0 24 24`.** That is the coordinate space the path is
  authored in. Size the icon with `width`/`height`; rewriting the viewBox
  crops it.
- **Put `fill` on the `<path>`, not on the `<svg>`.** The package ships
  `fill="currentColor"`, which relies on CSS inheritance that Paper does not
  give you — the glyph comes out black, or invisible on a dark surface.
- **One `<path>` per `d`,** all sharing the same fill.

Most griddy icons are FILLED paths, not strokes. Do not add `stroke` or
`stroke-width`; you will get a bolder, wrong glyph.

## 4 · Name the layer after the icon — always

```html
<svg layer-name="Search" width="16" height="16" viewBox="0 0 24 24" fill="none">
```

**This is the whole handoff for an icon.** Path data is unreadable, so the
moment a glyph is drawn its identity lives in exactly one place: the layer
name. Get it right and the implementer reads `Search` off
`get_tree_summary` and writes `import { Search } from "griddy-icons"` with
nothing to decide. Get it wrong — leave it as Paper's default `SVG` — and the
only way back to the name is matching path data against 1159 candidates by
eye, which nobody does. They guess, and the guess is the icon the sheet was
supposed to settle.

Rules, and they are narrow on purpose:

- **The exact export name, nothing else.** `Search`, not `search`, not
  `Search icon`, not `Magnifier`. It is an identifier being carried through a
  design tool, so it has to survive a copy-paste into an import statement.
- **The name is the icon, not the role.** A row's leading glyph is
  `layer-name="ExpandSidebar"` — the fact that it expands the sidebar belongs
  to the row's layer name, one level up. Naming it `Expand toggle` loses the
  only thing the sheet knows that the implementer does not.
- **Say the weight when it is not `regular`** — `Home (filled)`. A filled glyph
  named `Home` sends someone to the outline one.
- Retro-fitting is cheap: `rename_nodes` takes a batch, and `find_nodes` with
  `{ styleName: "fill" }` will surface the unnamed ones.

## 5 · Traps

| Trap | What happens |
|---|---|
| A token referenced before it exists in the file | **Paper silently drops the declaration.** `fill="var(--x)"` with no `--x` yields a node with no fill at all, and the write reports success. Create the token first (`create_tokens`), or fix it afterwards with `update_styles` — and verify with `get_computed_styles`, because a screenshot of a missing fill looks like a rendering hiccup |
| Reaching for the name that "looks right" | `X` is the X/Twitter wordmark; the cross you want is `Close`. Same shape for several brand marks |
| Using a brand mark at all | See below — this one is a legal question, not a styling one |
| Scaling by changing the viewBox | Crops. Change `width`/`height` |
| Keeping `currentColor` | Renders black in Paper regardless of the surface |
| One `d` from a multi-path icon | Half a glyph, and it reads as a slightly odd icon rather than a broken one |
| Mixing hand-drawn and extracted icons on one sheet | The hand-drawn ones read as a different set — different stroke logic, different optical weight. Extract all of them or none |
| Leaving the layer called `SVG` | The icon's identity is GONE. Path data is not readable, so the layer name is the only record of which glyph this is, and recovering it means matching against 1159 candidates. The implementer guesses instead |
| Naming the layer for the ROLE | `Expand toggle` describes the row, not the glyph. The row's own layer already says that; the icon layer is the one place the icon's name can live |

## 6 · Brand marks are a separate decision

The set includes third-party logos — `Airbnb`, `Apple`, `Discord`, `Figma`, `Github`,
`Google`, `Meta`, `Notion`, `Slack`, `Spotify`, `X` and more. They behave differently from
the rest of the library in a way that is easy to read as a bug:

- **They hard-code `fill: "black"`** instead of `currentColor` (75 occurrences across 73
  icons in `0.2.0`). They will not take your token, and recolouring them is usually the
  wrong fix anyway — most trademark policies require the mark in its approved colours.
- **The library's MIT licence covers the library, not the trademarks it depicts.** A
  permissive licence on the SVG does not grant you permission to use someone's logo.

Before shipping one, check the owner's brand guidelines: most permit a plain unmodified
mark for factual reference ("sign in with X", an integrations grid) and prohibit it in
your own logo, in a way implying endorsement, or recoloured. When in doubt, put the
question in the handoff rather than deciding it on the artboard.

## 7 · Sizing

The slot size is the component's decision, not the icon's — set `width` and
`height` to whatever the design system's icon slot is (16px is a common
default; the package's own `IconBase` defaults to 24). If the sheet documents
an icon slot, use that number and say so in the annotation.

## Definition of done

Every glyph on the artboard came out of the installed package · **every icon
layer is named for its export** (`Search`, not `SVG`, not `Search icon`) · the
viewBox is untouched · `fill` is on each `<path>` and bound to a token that
already exists · any brand mark has been checked against its owner's guidelines or
flagged in the handoff · `get_computed_styles` confirms the fill resolved rather than
being dropped.

An icon whose layer is called `SVG` is not handed off, whatever it looks
like — nobody can tell which one it is.

## Related skills

- `brand-guidelines-site` — the same extract-don't-guess discipline, applied to a whole
  brand system rather than one glyph
- `brand-guidelines` — where a project's iconography rules get written down in the first
  place
