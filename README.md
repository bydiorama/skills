# Brand & Strategy Skills for Claude

A small, opinionated set of [Agent Skills](https://code.claude.com/docs/en/skills) for the
work a brand studio actually does: strategy, positioning, guidelines, and the critical
review that should happen before any of it ships.

These were built and used on real engagements, then rewritten to be brand-agnostic so
anyone can run them. Eight skills, no dependencies beyond Python's standard library
(one skill additionally uses the public `griddy-icons` npm package and the Paper MCP
server, both optional and both noted in that skill).

## The skills

| Skill | What it does | Reach for it when |
|---|---|---|
| **[anti-skill](anti-skill/)** | Source-agnostic validation engine. Runs adversarial review modes over any deliverable and returns findings with concrete fixes. | Anything is about to go to a client, a board, or production |
| **[brand-guidelines](brand-guidelines/)** | Writes a full brand guidelines document through a canonical 8-section structure, with per-section references and three page tiers. | You need the brand book itself |
| **[b2b-icp](b2b-icp/)** | Builds a B2B Ideal Customer Profile and buyer persona across six layers, from four input lenses, with a mandatory negative ICP. | "Who are we actually selling to?" |
| **[griddy-icons-in-paper](griddy-icons-in-paper/)** | Extracts real glyphs from the `griddy-icons` package into a [Paper](https://paper.design) artboard, with the layer-naming and trademark rules that make a handoff hold. | An icon in a design has to be the one that ships |

## Install

Copy the skills you want into your skills directory:

```bash
git clone https://github.com/bydiorama/skills.git
cp -r skills/anti-skill ~/.claude/skills/
```

Use `~/.claude/skills/` for personal use, or a project's `.claude/skills/` to share them
with a repo. Claude loads each skill's `SKILL.md` and pulls the `references/` and
`resources/` files on demand.

Each skill is a self-contained directory — take one, take all eight, nothing depends on
anything outside its own folder.

## Which one to start with

**`anti-skill`** is the one to try first, and the one most likely to be useful outside a
studio. It is not about brands at all: it takes any output — a document, a plan, a
proposal, code — establishes what it was supposed to achieve, runs a set of validation
modes chosen for that output type, verifies factual claims by search, and reports findings
ranked by severity with a fix attached to each. It is deliberately hard to please.

## Conventions

Every skill follows the same shape:

- `SKILL.md` — YAML frontmatter (`name`, `description`) plus the operating procedure. The
  description is what Claude reads when deciding whether to load the skill, so it names the
  trigger phrases and the exclusions.
- `references/` — deep-dive material loaded on demand, not upfront.
- `resources/` — templates and scripts the skill executes.

If you use these skills on client work, the same discipline applies: name a framework,
don't copy it, and don't paste another agency's writing into your own.

**Trademarks.** "Diorama" and the Diorama logo are trademarks of the copyright holder. The
MIT licence covers the contents of this repository; it does not grant permission to use the
Diorama name or marks to identify derivative works. Fork freely — just ship it under your
own name.

## Contributing

Issues and pull requests welcome. If you are adding a skill, keep `SKILL.md` under ~200
lines — anything longer is usually two skills, or documentation wearing a skill's
frontmatter — and write the description as a trigger ("Use when…") rather than a summary. A
description that only says what a skill *is* will never fire, and the failure is silent.

## License

MIT — see [LICENSE](LICENSE).

Built by Diorama.
