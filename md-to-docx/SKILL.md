# Markdown to DOCX

Convert a Markdown (.md) file to a clean Microsoft Word (.docx) document using python-docx. Preserves H1–H4 headings, GFM tables, bullet/numbered lists, bold/italic/inline-code, blockquotes, horizontal rules, and GitHub-style checkbox task lists. No pandoc or external binaries required.

## Usage

Point to a Markdown file:

```
@md-to-docx /path/to/document.md
```

With an explicit output path:

```
@md-to-docx /path/to/document.md /path/to/output.docx
```

By default the DOCX is written next to the source with the same stem.

## What This Skill Does

### Phase 1: Resolve paths
- Treat the first argument as the input `.md` file. Error out if it doesn't exist or doesn't end in `.md` / `.markdown`.
- If a second argument is provided, use it as the output path; otherwise write to `<input_stem>.docx` in the same directory as the input.
- Quote paths that contain spaces when invoking the converter.

### Phase 2: Verify dependencies
- Check the converter script exists — it is **not optional**, it ships with the skill. Use an enforcing check that stops the workflow if the script is missing:
  ```
  test -f ~/.claude/skills/md-to-docx/resources/md2docx.py || { echo "md-to-docx: converter missing at resources/md2docx.py — reinstall the skill" >&2; exit 1; }
  ```
  If missing, the skill installation is incomplete. Do not silently fall through. Either reinstall the skill or recreate `resources/md2docx.py` from the canonical reference before proceeding (see Troubleshooting).
- Check `python-docx` is importable:
  ```
  python3 -c "import docx" 2>/dev/null
  ```
- If missing, install it. On macOS Homebrew / recent Debian-family Python (PEP 668 "externally-managed-environment"), plain `pip install` is refused. Try in this order:
  ```
  python3 -m pip install --user python-docx
  # If PEP 668 blocks the above, prefer pipx or a venv:
  pipx install python-docx || (python3 -m venv ~/.venv/md-to-docx && ~/.venv/md-to-docx/bin/pip install python-docx)
  ```
  Only use `--break-system-packages` if the user explicitly authorizes it.

### Phase 3: Run the converter
- Invoke the bundled script via Bash (quote both paths end-to-end — Dropbox/OneDrive/iCloud paths frequently contain spaces):
  ```
  python3 ~/.claude/skills/md-to-docx/resources/md2docx.py "<input>" ["<output>"]
  ```
- The script is self-contained — no pandoc, no shell-outs, no network.

### Phase 4: Confirm
- Report the output path and file size. Do not open the file; let the user open it.

## Output Location

By default: `<same_directory>/<same_stem>.docx`. Overridable via the second positional argument.

## Supported Markdown

| Element | Rendered as |
|---|---|
| `#` … `######` | Word Heading 1–6 (navy, sized 22/16/13/12/11/10 pt) |
| `***bold-italic***`, `**bold**`, `*italic*`, `` `code` `` | Inline runs (code: Consolas 10 pt) |
| `[text](url)` | Clickable blue-underlined Word hyperlink |
| GFM tables (header row + `---` separator) | Word table, Light Grid Accent 1, dark-navy header with white text. Pipe tokenizer respects inline-code (`` `a|b` ``) and escaped pipes (`\|`). |
| `- item` / `* item` / `+ item` with 2-space-per-level nesting | List Bullet 1–3 |
| `1. item` with 2-space-per-level nesting | List Number 1–3 |
| `> quote` | Italic indented paragraph, grey |
| ```` ``` ```` or `~~~` fenced code blocks | Single paragraph, Consolas 10 pt, line breaks preserved |
| `---` / `***` / `___` on its own line | Horizontal rule |
| `- [x]` / `- [ ]` | ☒ / ☐ glyphs prepended |
| YAML frontmatter (`---` … `---` at start of file) | Skipped |
| UTF-8 BOM at start of file | Silently stripped |

Not supported (passed through as plain text): images, raw HTML, footnotes, definition lists, LaTeX math, reference-style links (`[text][id]` with separate `[id]: url` definitions).

## Tips for Best Results

- Use blank lines between paragraphs, tables, and lists — the parser is blank-line-sensitive.
- Table header separators must use at least three dashes per cell: `|---|---|`.
- For nested lists, indent exactly two spaces.
- If the output looks off, inspect the DOCX and compare to the source — most issues come from malformed tables (missing separator row) or mixed list indentation.
- The script is idempotent; re-running it overwrites the output.
- For non-ASCII paths or output containing em-dashes / smart quotes / checkbox glyphs, the script handles UTF-8 end-to-end.

## Troubleshooting

- **`[Errno 2] No such file or directory` on `resources/md2docx.py`.** The skill's converter script was not installed. It is required — the skill is shipped as `SKILL.md` + `resources/md2docx.py` and the script is not optional. Reinstall the skill, or recreate the script from its canonical source. If neither is available, stop and tell the user the install is broken rather than attempting a half-working fallback.
- **`ModuleNotFoundError: No module named 'docx'`.** Install with `python3 -m pip install --user 'python-docx>=0.8.11'`. On systems with PEP 668 "externally-managed-environment", use a venv or `--break-system-packages` only if the user authorizes it.
- **Table renders as a paragraph instead of a table.** The GFM separator row (`|---|---|`) is missing or malformed. The parser deliberately falls through to plain text rather than crashing. Fix the separator and re-run.
- **Bullets not nesting.** Nested list items must be indented by exactly two spaces; tabs or four-space indents are treated as a new top-level list.
- **Inline code loses styling inside bold/italic.** Inline code `` `...` `` is rendered as a Consolas 10pt run and overrides surrounding bold/italic on that run only; wrap the other emphasis outside the backticks if both are needed.
- **Output path has spaces and fails.** Always double-quote both input and output paths in the Bash invocation. Dropbox / OneDrive / iCloud Drive paths are the usual offenders.
- **Unexpected glyphs (☒, ☐, em-dash, smart quotes).** The script handles UTF-8 end-to-end. If glyphs render as `?`, the issue is font fallback in Word, not the converter — pick a font that has the glyph (e.g., Segoe UI Symbol).

## Regression Fixture

Before publishing converter changes, re-test with a synthetic fixture that exercises every supported feature:

- H1 through H6 headings
- YAML frontmatter at top of file
- UTF-8 BOM
- A fenced code block (```` ``` ````) containing a line that starts with `#` (must NOT become a heading)
- A GFM table containing a cell with `` `a|b` `` (pipe inside inline code) and another with `\|` (escaped pipe)
- Nested bullets at 2 and 4 space indent, and nested numbered lists
- `***bold-italic***`, `**bold**`, `*italic*`, `` `code` ``, and `[link](https://example.com)` on one paragraph
- A blockquote and a `---` horizontal rule
- A task list: `- [x] done` and `- [ ] todo`

Open the resulting DOCX in Word and verify: headings carry the right sizes, the fenced-code line starting with `#` is NOT a heading, the hyperlink is clickable, and all pipe-containing table cells split correctly.

## Continuous Improvement

After completing this workflow, invoke `@skill-reflect md-to-docx` to update this skill with validated learnings from the execution.

## User-Invocable

Yes — users can invoke this skill directly with `@md-to-docx`.

## Learnings

> Auto-updated from execution logs. Each entry is a validated, reusable insight.

- [2026-04-23] **Pitfall**: `resources/md2docx.py` missing from the skill install → Phase 3 fails with `[Errno 2]`. Phase 2 now runs an *enforcing* existence check (`|| exit 1`) before the dependency check, so future Claudes stop rather than silently fall through.
- [2026-04-23] **Edge case**: Tables without a GFM separator row fall through to paragraph rendering, not crash. The parser only commits to table rendering when the second row matches `:?-{3,}:?` per cell.
- [2026-04-23] **Pitfall**: Markdown hyperlinks `[text](url)` were silently lost on first real use (a References section with 10+ links). The converter now emits `w:hyperlink` runs so links are clickable in Word. If you add a new inline syntax, update `INLINE_PATTERN` *and* the Supported Markdown table.
- [2026-04-23] **Pitfall**: Fenced code blocks with a line starting with `#` were being parsed as Word headings. The converter now uses a state machine that suspends all line-level parsing between ```` ``` ```` / `~~~` fences. Content inside a fence is rendered verbatim in Consolas 10 pt.
- [2026-04-23] **Pitfall**: UTF-8 BOM at the start of a file prevented the first heading regex from matching (first char was `﻿`, not `#`). Read with `encoding="utf-8-sig"`, not `"utf-8"`.
- [2026-04-23] **Edge case**: Table cells containing inline-code pipes (`` `a|b` ``) or escaped pipes (`\|`) were split into extra columns. Pipe tokenization now respects backtick spans and `\|` escapes.
- [2026-04-23] **Scope gap → closed**: H5/H6, triple-emphasis `***both***`, nested numbered lists, and YAML frontmatter were all promised nowhere but expected everywhere. All four are now supported. If you extend the grammar again, also extend the regression fixture.
- [2026-04-23] **Tip**: On PEP-668 systems (Homebrew Python, recent Debian), `pip install --user` is refused. Fall back to `pipx install python-docx` or a venv before suggesting `--break-system-packages`.
