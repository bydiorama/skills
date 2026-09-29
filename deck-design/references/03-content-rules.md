# Layer 3 — Content rules, validation and editing

Writing the copy, then proving it earns its slide.

---

## Writing

### Headlines

The headline is **the claim**, not the topic. "Approach" is a topic. "Awareness was never the problem" is a claim.

- One sentence. Full stop included.
- Say the thing, do not announce that you will say it.
- Specific beats general: a number, a name, a verb.
- If it could appear in any deck for any client, rewrite it.

### Body

The body is **the evidence**. It exists to make the headline survive a sceptic.

- Lead with the claim, then elaborate. The first sentence of a paragraph should be readable alone.
- Concrete nouns. Working details. "Three designers, one strategist" beats "a dedicated team".
- Two to four sentences per block. Longer belongs in two blocks.

### Captions and metadata

- Label, then value. `Scope — Identity, editorial system, CMS templates`
- Sentence case. Uppercase belongs to chrome only.
- A caption states what the thing is, not what you think of it.

### Numbers

- Round to what is true and legible. `594 000 €`, not `593,847.22 €`.
- **A stat must fit one line at its display size.** This is a hard constraint, not a preference — see the failure log below.
- The unit lives with the number if it fits, in the caption if it does not.

---

## The type budget

Every slide is constrained to:

- **Maximum four type styles**, chrome included. Three is better.
- **Maximum two weights.**
- **Maximum two colours.**

These are not aesthetic preferences. Exceeding them reliably produces weaker work, because each additional variable claims a distinction the content does not actually have.

Use the two colours as **content vs metadata** — primary for what is being said, muted for what labels it. Use the second weight for the one label the eye should land on first.

When you need more contrast, reach for **space before size, and size before weight, and weight before colour.**

---

## Measure

Body measure lands between **45 and 60 characters**. At 24px that is roughly 560–650px.

- Text-heavy slides use **two columns** of that measure. One wide column of running copy is unreadable regardless of how much room there is.
- Headlines can run wider — up to about 1200px — because they are read in one glance, not scanned.
- If a column is wider than its comfortable measure, absorb the surplus with a column offset (Layer 0), not by letting the line run.

---

## Validation

Run all of these before design is called finished.

### 1. The spine test
Read the headlines alone, in order. Do they argue? If not, the deck is not ready to look at.

### 2. The role test
Name each slide's job — assert, prove, quantify, explain, orient, ask. Any slide you cannot name is a slide to cut or split.

### 3. The three-second test
Show a slide briefly. Ask what it said, what was noticed first, what second. If the answers differ from your intent, fix the hierarchy — do not explain the slide.

### 4. The stranger test
Would this sentence appear in a competitor's deck for a different client? If yes, it is not saying anything.

### 5. The evidence test
Every claim has proof somewhere in the deck, or is removed. A deck of assertions is a brochure.

### 6. The fit test
Every number, headline and label fits its zone at its real size, with real content. Not lorem, not the string you chose because it fit.

---

## Editing

### Cut a fifth
After a draft reads complete, remove roughly 20% of its non-essential elements and reassess. It almost always improves. This applies to slides, paragraphs, and elements within a slide.

### Merge, don't append
Two thin slides on the same idea are one slide. Adding a slide is the default reflex and is usually wrong.

### Kill the empty ordinal
A `01 / 02 / 03` that maps to a section, a step, or a page is navigation. One that decorates three unrelated tags is an empty embellishment — delete it.

### Placeholder discipline
**Never invent prices, dates, metrics, headcounts or client facts.** In a commercial document this is a serious error, not a rounding one.

Use a visibly incomplete placeholder — `€ —`, `[dátum]` — and flag it in your report. A structure with honest gaps is usable; a structure with invented numbers is dangerous.

Mark placeholder imagery the same way. If a reference slide uses a stand-in image, say which.

---

## Language

- Write in the audience's language. If the client is Slovak, the deck is Slovak — including the chrome.
- Keep proper nouns and established industry terms in their original form; do not translate `paywall`, `handoff`, `template` into something nobody says.
- Check diacritics character by character after any bulk text operation. A wrong `ʹ` for `ť` survives review and looks careless.

---

## Failure log

Real failures worth not repeating:

| What happened | Rule it produced |
|---|---|
| `594 000 €` at 96px broke to two lines inside a padded column | A stat must fit one line; check with the real figure, in the real zone |
| Body, secondary and muted used on one slide | Two colours, content vs metadata |
| Chrome, caption, meta table and labels all uppercase | Uppercase belongs to chrome only |
| Caption placed under an image, below a rule | Rules go above content; a rule under a block reads as a lid |
| Slide headline was "Approach" | The headline is the claim, not the topic |
| Copy written to fit the template | Test with real content, then fix the master |
