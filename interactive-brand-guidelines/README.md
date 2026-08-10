# interactive-brand-guidelines (skill)

A standalone, brand-agnostic skill for generating an **elevated, interactive
brand-guidelines page that lives inside a product's own design system** — not a
generic one-pager. Distilled from a real engagement.

## Layout

```
interactive-brand-guidelines/
├── SKILL.md                          # entry point (frontmatter + operating procedure)
└── resources/
    ├── pipeline.md                   # extraction → data model → build → verify
    ├── interactive-patterns.md       # copy-to-clipboard, downloads, generators, MD export
    ├── geometry-systems.md           # reverse-engineering an icon/insignia alphabet
    └── anti-footguns.md              # the mistakes that cost review rounds
```

## Install

Drop the `interactive-brand-guidelines/` folder into your skills directory
(e.g. `~/.claude/skills/` or a project's `.claude/skills/`). The agent loads
`SKILL.md` and pulls the `resources/*.md` files on demand.

This folder is deliberately kept **outside any product repository** — it is
tooling, not brand content.
