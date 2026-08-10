# Extraction Playbook

Concrete commands for pulling a brand system out of a live website and a Figma file.
Brand-agnostic — substitute the target URL / fileKey / nodeId.

---

## A. Website extraction

### 1. Brand overview (narrative)
```
WebFetch(url, "Extract brand identity: what the company does, tagline/slogan, services,
tone of voice, and any visible colours/fonts.")
```

### 2. Find the real stylesheet(s)
```bash
curl -sL "<site-url>" -o /tmp/site.html
grep -oE '<link[^>]*stylesheet[^>]*>' /tmp/site.html       # find CSS hrefs
```
Common patterns: a single theme bundle (e.g. WordPress
`/wp-content/themes/<theme>/.../app.css`), or a hashed build asset. Fetch the main one:
```bash
curl -sL "<main-css-url>" -o /tmp/app.css
```

### 3. Ground-truth UI styles (the site CSS is authoritative)
```bash
# Buttons
grep -oE '\.[a-z0-9_-]*button[a-z0-9_-]*\s*\{[^}]*\}' /tmp/app.css

# Cards / radius / shadow
grep -oE '\.[a-z0-9_-]*(card|rounded|shadow)[a-z0-9_-]*\s*\{[^}]*\}' /tmp/app.css
grep -oE 'border-radius:[^;!}]*' /tmp/app.css | sort | uniq -c | sort -rn

# Named colour scale (Tailwind-style tokens → rgb)
grep -oE '\.(text|bg|border)-[a-z]+-[0-9]+\{[^}]*\}' /tmp/app.css \
  | grep -oE '[a-z]+-[0-9]+|[0-9]+,[0-9]+,[0-9]+' | paste - - | sort -u
```
Capture from the button rule: `border-radius`, `padding`, `background-color`,
`color`, `gap`, `font-weight`/`font-size`, `box-shadow`, and any `:hover` variant
(a frequent pattern: a dark button that flips to the accent on hover).

### 4. Logo usage across the site
```bash
grep -oE '<img[^>]*(logo|Logo)[^>]*>' /tmp/site.html
```
Note which file is used over dark vs light backgrounds (often `*-light.svg` for dark
backgrounds / hero / footer, `*-dark.svg` for the light scrolled nav). Confirm the
symbol colour stays constant while the wordmark text swaps.

### 5. Font kit (confirm slugs + available weights — do not assume)
```
WebFetch("<typekit-or-font-css-url>",
  "List every @font-face: exact font-family in quotes, font-weight, font-style.")
```
A kit often ships only a subset of weights (e.g. 400/700) even when the design uses
Thin/Medium/SemiBold. Record family slugs exactly (e.g. `"quiche-sans"`, `"new-reason"`).

---

## B. Figma extraction (MCP)

URL → ids: `https://figma.com/design/:fileKey/:name?node-id=375-2763`
⇒ `fileKey = :fileKey`, `nodeId = 375:2763`.

### 1. Structure only (geometry, no styles)
```
get_metadata(fileKey, nodeId)
```
Returns node IDs / names / x,y,w,h — **no colours, no text, no fonts**. If the output is
huge (it often is), have a subagent slice it with `jq`/python and return just the named
frames + IDs you need (logo, sections, buttons, swatches).

### 2. Tokens + type (the reliable source)
Call `get_design_context` on **small leaf content nodes** — a heading, a stat number, a
button, a footer line:
```
get_design_context(fileKey, "<small-node-id>")
```
The response contains real CSS, e.g.
`font-['Quiche_Sans:Thin'] text-[56px] leading-[64px] tracking-[-1.68px]
text-[color:var(--fawn,#F7B267)]` plus a "styles contained" summary
(`Font(family, style, size, weight, lineHeight, letterSpacing)`). Harvest:
- colour hexes **with their `var(--name,...)` token names**,
- font families + weights + sizes + line-heights + tracking.

Do this across a few representative nodes (hero heading, stat, body, button, footer) to
cover the whole scale. Large nodes overflow context — keep nodes small.

### 3. Visual reference
```
get_screenshot(fileKey, nodeId, maxDimension=1200)   # returns a URL; curl it to inspect
```
`get_variable_defs` needs a live selection in the desktop app and commonly errors — rely
on the inline `var(--name,#hex)` names from `get_design_context` instead.

---

## C. Logo asset extraction

### 1. Get + download
```
get_design_context(fileKey, "<symbol-node-id>")     # → asset URL(s) in the code
get_design_context(fileKey, "<wordmark-node-id>")
```
```bash
curl -s -o assets/logo-symbol.png "<figma-asset-url>"
file assets/*                      # Figma "png" is often actually SVG → rename to .svg
```
⚠️ Asset URLs **expire (~7 days)** — download during the build, never rely on the URL later.

### 2. Make recolourable + inline
```bash
# var(--fill-0,#hex)  ->  currentColor
sed -E 's/var\(--fill-0, #[0-9A-Fa-f]+\)/currentColor/g' assets/logo-symbol.svg > /tmp/sym.cc.svg
```
Inline the paths into an SVG `<symbol>` sprite in the HTML.
**CRITICAL bug to avoid:** every inlined `<path>` must have `fill="currentColor"`. Paths
with no `fill` render **black** and ignore CSS `color`. If you batch-add fills, skip paths
that already declare a `fill`/`stroke` (e.g. `fill="none"` icons) and watch multi-line
`<path>` tags so you don't create duplicate `fill` attributes.

### 3. Generate colour variants (self-contained SVGs)
Compose `symbol paths` + `wordmark paths` into one viewBox, with explicit fills:
- **primary**  = accent symbol + dark text (light backgrounds)
- **reversed** = accent symbol + light text (dark backgrounds)
- **mono-dark / mono-light** = single colour
- **symbol-only**

Lockup layout that matches most Figma exports: symbol in a `120×120` box at x0; wordmark
(`W×H`) centred vertically and offset right by `symbolW + gap`; viewBox
`0 0 (symbolW+gap+W) 120`.

### 4. Favicon (multi-size)
```bash
# favicon.svg = symbol on a rounded brand tile; keep padding tight so it reads at 16px
qlmanage -t -s 256 -o /tmp favicon.svg          # render a 256px master PNG (macOS)
python3 - <<'PY'
from PIL import Image
im = Image.open('/tmp/favicon.svg.png').convert('RGBA')
im.save('favicon.ico', format='ICO',
        sizes=[(16,16),(32,32),(48,48),(64,64),(128,128),(256,256)])
im.resize((180,180), Image.LANCZOS).save('assets/favicon-180.png')   # apple-touch
PY
```
Always inspect the 16px extraction — if the mark is muddy, reduce the tile padding so the
symbol fills more of the canvas.

---

## D. Reconcile

Figma tokens and site CSS describe the same system — they should agree. Where the site CSS
adds tints not obvious in Figma (e.g. a pale accent for muted buttons), keep them as extra
supporting tokens. Where the font kit lacks design weights, document it rather than fake it.
