# Reverse-engineering a geometric system

Some brands encode a secondary system (an icon or insignia alphabet, a pattern
grammar) that only exists as a handful of shipped SVGs plus prose rules. To
extend it (a full alphabet, a generator) faithfully:

1. **Decode the primitives.** Read the shipped SVGs; extract the exact numbers —
   arc radius, stroke width, cell size, grid seams, canonical bar lengths. These
   are non-negotiable constants. (Render the shipped instances large and inspect
   them; the numbers are in the path data.)

2. **Name the grammar.** Express the system as a small vocabulary — e.g. "full
   circle, half circle, quarter-circle in four rotations, dash" on a fixed grid
   with fixed seams. Everything you build is a composition of that vocabulary.

3. **Anchor on canonical examples.** Where the brand already ships instances
   (the badges of named product lines), reproduce them **byte-for-byte** and
   treat them as ground truth; build everything else in the same grammar. Mark
   which outputs are canonical vs constructed so a reviewer knows what to trust.

4. **Generate programmatically, then render and eyeball every output.** For
   letterforms, differentiate glyphs that collide and keep them legible and
   on-grammar. A human review catches "letter F is off-brand" that code cannot —
   budget for at least one review round on generative output.

5. **For a live generator**, enforce the documented composition rules in the UI
   (min/max elements, orientation, once-per-surface). Respect that different
   modes may have different limits (e.g. a raw-segment insignia has a 3-minimum
   while a letter-substitution word may allow 2). Assemble downloads client-side
   and namespace all ids per element.

6. **For type-in-mark lockups**, generate the name text from the *real licensed
   font outlines* (via an OpenType library) at the spec's cap-height and
   tracking — don't approximate with a system font. Example:

   ```js
   import opentype from 'opentype.js';
   const buf = readFileSync(fontPath);
   const font = opentype.parse(buf.buffer.slice(buf.byteOffset, buf.byteOffset + buf.byteLength));
   const capHeight = font.tables.os2.sCapHeight;
   const fontSize = (TARGET_CAP / capHeight) * font.unitsPerEm;
   const path = font.getPath(name, textX, baseline, fontSize, { kerning: true, letterSpacing: -0.02 });
   const d = path.toPathData(3); // <path d="..."> at the exact spec
   ```

## Worked example (from the reference engagement)

A dark intelligence brand encoded insignias as **twelve segments** — full
circle, half circle, dash, and nine quarter-circle pair variants — cut from one
ring (radius 16.3, stroke 7.3 on a 40 px tile), arranged 3–5 per insignia,
vertically or horizontally, once per surface. Five canonical badges (the initials
of the product lines) were reproduced byte-for-byte; the rest of the a–z alphabet
was constructed in the same arc vocabulary. The generator exposed both a
**segments** mode (compose 3–5 of the twelve) and a **letters** mode (type a
2–5 letter word → set it in the alphabet), each downloading a standalone SVG.
