# Build Patterns

Reusable, framework-free patterns for the one-pager. Substitute the extracted tokens,
fonts and logo. Keep it dependency-free (no build step).

---

## File layout

```
index.html · styles.css · script.js · README.md
favicon.svg · favicon.ico
assets/  (logo source SVGs, colour-variant lockups, favicon PNGs)
```

## `<head>` essentials

```html
<link rel="stylesheet" href="<font-kit-url>">          <!-- e.g. Adobe Typekit -->
<link rel="stylesheet" href="styles.css">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="assets/favicon-180.png">
<meta name="theme-color" content="<dark-token-hex>">
```

## CSS tokens — mirror the Figma variable names

```css
:root {
  /* keep the source's own token names so the doc is self-documenting */
  --accent:   #...;   /* e.g. site "orange-300" */
  --accent-soft: #...;/* tints found only in the site CSS (muted buttons/chips) */
  --ink:      #...;   /* primary text / dark surfaces */
  --ink-2:    #...;   /* secondary text */
  --surface:  #...;   /* warm/neutral background */
  --white:    #fff;
  --shadow-xl: 0 20px 25px -5px rgba(0,0,0,.1), 0 8px 10px -6px rgba(0,0,0,.1); /* from site */
  --font-display: "<display-slug>", Georgia, serif;     /* exact kit slug + fallback */
  --font-sans:    "<sans-slug>", system-ui, sans-serif;
  --radius: 12px;     /* site rounded-xl */
}
```

## Buttons — copy the live site's `.button` exactly

```css
.btn {                       /* base = site primary */
  display: inline-flex; align-items: center; justify-content: center; gap: 8px;
  background: var(--accent); color: var(--ink);
  font-family: var(--font-sans); font-weight: 600; font-size: 16px; line-height: 1.5;
  padding: 12px 24px; border: 0; border-radius: var(--radius); cursor: pointer;
  transition: background-color .15s ease, color .15s ease;   /* site duration-150 */
}
.btn--dark  { background: var(--ink); color: var(--white); }
.btn--dark:hover { background: var(--accent); color: var(--ink); }  /* common site hover flip */
.btn--muted { background: var(--accent-soft); color: var(--ink); }
.btn--muted:hover { background: var(--accent); }
```

## Recolourable logo via inline `<symbol>` sprite

```html
<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="sun" viewBox="0 0 240 240">
    <!-- EVERY path MUST have fill="currentColor" or it renders black -->
    <path fill="currentColor" d="..."/>
  </symbol>
  <symbol id="wordtext" viewBox="0 0 W H"><path fill="currentColor" d="..."/></symbol>
</svg>

<svg class="mark"><use href="#sun"/></svg>          <!-- colour via CSS `color` -->
```
```css
.mark { width: 26px; height: 26px; color: var(--accent); }   /* currentColor → accent */
```
Hero uses the **primary** lockup file on a light surface; footer uses the **reversed** file
on a dark surface (use the generated `assets/*-primary.svg` / `*-reversed.svg` as `<img>`).

## Colour swatch + copy-to-clipboard

```html
<button class="swatch" data-hex="#F7B267" style="--c:#F7B267">
  <span class="swatch__chip"></span>
  <span class="swatch__name">Accent</span>
  <span class="swatch__hex">#F7B267</span>
  <span class="swatch__var">--accent</span>
</button>
```
```css
.swatch__chip { position: relative; background: var(--c); }
.swatch__copy {                 /* always-visible affordance injected by JS */
  position: absolute; top: 10px; right: 10px;
  display: inline-flex; gap: 6px; align-items: center;
  padding: 6px 10px; border-radius: 8px;
  background: rgba(0,0,0,.86); color: #fff; font-size: 12px; font-weight: 600;
}
.swatch.is-copied .swatch__copy { background: var(--accent); color: var(--ink); }
```
```js
function copyHex(hex){
  if (navigator.clipboard?.writeText) return navigator.clipboard.writeText(hex);
  return new Promise((res,rej)=>{                       // file:// / non-secure fallback
    try{const t=document.createElement('textarea');t.value=hex;t.style.position='fixed';
        t.style.opacity='0';document.body.appendChild(t);t.select();
        document.execCommand('copy');document.body.removeChild(t);res();}catch(e){rej(e);}
  });
}
document.querySelectorAll('.swatch').forEach(sw=>{
  const chip=sw.querySelector('.swatch__chip');
  const badge=document.createElement('span');
  badge.className='swatch__copy';
  badge.innerHTML='<svg aria-hidden="true"><use href="#copy"/></svg><span>Copy HEX</span>';
  chip?.appendChild(badge);
  sw.addEventListener('click',()=>copyHex(sw.dataset.hex).then(()=>{
    sw.classList.add('is-copied');
    badge.innerHTML='<svg aria-hidden="true"><use href="#check"/></svg><span>Copied</span>';
    setTimeout(()=>{sw.classList.remove('is-copied');
      badge.innerHTML='<svg aria-hidden="true"><use href="#copy"/></svg><span>Copy HEX</span>';},1500);
  }));
});
```

## Nav scroll-spy + footer year

```js
const links=[...document.querySelectorAll('.nav__links a')];
const obs=new IntersectionObserver(es=>es.forEach(e=>{
  if(e.isIntersecting) links.forEach(l=>l.classList.toggle('is-active',
    l.getAttribute('href')==='#'+e.target.id));
}),{rootMargin:'-45% 0px -50% 0px'});
links.map(l=>document.querySelector(l.getAttribute('href'))).filter(Boolean).forEach(s=>obs.observe(s));
document.getElementById('date').textContent =
  new Date().toLocaleDateString('en',{month:'long',year:'numeric'});
```

## Typography section — render real specimens + an honest kit note

- Show one specimen per family (display + sans) with the **available** kit weights.
- Document the design-intent weights even if the kit lacks them, e.g.:
  > Kit `<id>` ships weights 400 & 700 only; enable Thin/Medium/SemiBold in the font
  > provider to match headings. Fallback: `<display>` → Georgia; `<sans>` → system-ui.
- Build a type-scale table from the extracted styles (Heading / Title / Body / Button:
  font · size/line · tracking). Use dotted dividers if the source does.

## Sections (essentials, in canonical order)

Hero (primary lockup + essence) → At-a-glance (positioning + personality chips) →
Logo (lockups light/dark, clear space, min size, do/don'ts, **download buttons** for the
variant SVGs) → Typography (specimens + scale + kit note) → Colour (swatch cards with
hex/token/role + click-to-copy + pairing/contrast) → Tone of voice (4–5 principles with
do/don't lines from real site copy) → Footer (reversed lockup + source + date).
