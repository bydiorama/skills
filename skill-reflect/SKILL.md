# Skill Reflect

A sub-skill for improving other skills after execution. Analyzes what just happened and surgically updates the source skill file with validated learnings.

## Usage

Reference at the end of any other skill:

```
After completing the above, invoke @skill-reflect to update this skill based on what you observed.
```

Or invoke directly after a skill runs:

```
@skill-reflect [skill-name]
```

Where `[skill-name]` matches the directory name under `~/.claude/skills/`.

## What This Skill Does

### Step 1: Locate Target Skill

Resolve the skill path:
- If `[skill-name]` is provided: `~/.claude/skills/[skill-name]/SKILL.md`
- If invoked inline (no argument): the skill whose SKILL.md referenced `@skill-reflect`
- Read **only the final sections** of the skill file (Tips, Learnings, Pitfalls) — not the full file — to minimize token use

### Step 2: Rapid Execution Audit

Scan the current conversation for signals — do not re-read or summarize the entire history. Look for:

**Friction signals**:
- Steps that required clarification or back-and-forth
- Assumptions that turned out wrong
- Missing inputs that stalled progress
- Tools or approaches that failed and were retried

**Flow signals**:
- Steps that worked smoothly without clarification
- Shortcuts or patterns that accelerated the work
- Inputs that produced especially good output

**Output signals**:
- User corrections or adjustments to the output
- Explicit feedback (positive or negative)
- Sections the user accepted without modification

**Scope signals**:
- Tasks the skill attempted but wasn't designed for
- Instructions in the skill that were never triggered
- Gaps between what the skill promised and what was delivered

### Step 3: Distill Insights

From the audit, extract **only non-obvious, reusable insights** — not things already covered by the skill.

Discard:
- Observations that duplicate existing skill instructions
- One-off anomalies unlikely to recur
- Vague impressions without actionable implication

Keep (maximum 5 per run):
- Concrete patterns: "When X input is missing, Y step fails"
- Sharper instructions: "Step N should specify Z more explicitly"
- New tips: "Doing A before B saves significant back-and-forth"
- Edge cases: "If the user provides P, skip Q entirely"
- Anti-patterns: "Avoid Z approach — it produces low-quality output and requires correction"

### Step 4: Update the Skill File

Apply changes surgically — **do not rewrite sections that don't need updating**.

**If a `## Learnings` section exists**: append new non-duplicate entries.

**If no `## Learnings` section exists**: append it at the end of the file.

**Format**:

```markdown
## Learnings

> Auto-updated from execution logs. Each entry is a validated, reusable insight.

- [YYYY-MM-DD] **Pattern**: When [condition], [action produces better result than alternative].
- [YYYY-MM-DD] **Tip**: [Concrete actionable instruction].
- [YYYY-MM-DD] **Pitfall**: [What went wrong] → [How to avoid it].
- [YYYY-MM-DD] **Edge case**: If [condition], [adjusted behavior].
- [YYYY-MM-DD] **Scope gap**: Skill doesn't handle [X] — consider adding [approach].
```

**Additionally**, if an insight is important enough to improve the main skill body (not just a footnote), apply a targeted edit:
- Update a vague instruction to be more specific
- Add a missing input to the intake checklist
- Add a new tip to "Tips for Best Results"
- Clarify an ambiguous step

Do **not** restructure, reformat, or expand sections beyond the targeted edit.

### Step 5: Confirm

Output a brief summary (3–5 lines max):
- Which skill was updated
- How many insights were added
- The most significant change made
- Skip verbose explanation — the skill file is the artifact, not this summary

## Efficiency Rules

- **Read minimally**: Only read the tail of the skill file (last 100 lines) unless a targeted edit requires reading a specific section. Use `offset` parameter.
- **Write minimally**: Prefer `Edit` over `Write`. Never rewrite the full file.
- **Extract fast**: Do not summarize the whole conversation — scan for signals only.
- **One pass**: Do not iterate. If uncertain whether an insight is valid, omit it.
- **No hallucination**: Only write learnings grounded in actual events from this execution. If nothing notable happened, write nothing.

## When to Skip

Do not update the skill file if:
- The execution was routine with no friction, surprises, or corrections
- All observed patterns are already covered in the skill
- The conversation provided no meaningful signal (e.g., user cancelled mid-task)

In these cases, output: `skill-reflect: no new learnings from this execution.`

## User-Invocable

Yes - users can invoke this skill directly with `@skill-reflect [skill-name]`
