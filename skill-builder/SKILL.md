# Skill Builder

A meta-skill for capturing workflows and processes from Claude Code conversations and distilling them into reusable, well-structured skill files. Analyzes what happened in a session, extracts the process into a SKILL.md that follows established conventions, and saves it to `~/.claude/skills/`.

## Usage

Invoke after completing a workflow worth capturing:

```
@skill-builder
```

With a name hint:

```
@skill-builder [skill-name]
```

To create a skill from a description (no prior conversation needed):

```
@skill-builder --from-description
```

## What This Skill Does

### Phase 1: Determine Source

Decide where the skill content comes from:

- **From conversation (default)**: Scan the current conversation to extract the workflow performed. Do not re-read the full conversation — scan for structural signals only (Phase 2).
- **From description (`--from-description`)**: Ask the user to describe the workflow in 3-5 sentences. Then ask targeted follow-up questions (max 3) to fill gaps: What triggers the skill? What are the inputs? What does it produce?

If `[skill-name]` is provided, use it as the directory name. Otherwise, derive a kebab-case name from the identified workflow and confirm with the user.

### Phase 2: Extract Workflow Signals

Scan the conversation (or user description) in a single pass. Extract structured data, not a narrative summary.

**Process signals**: Sequential steps followed, decision points, branching logic, iterations that refined output.

**Tool signals**: Which tools were used (Read, Write, Bash, WebSearch, etc.), file types read or produced, external services or APIs called, commands executed.

**Input signals**: What the user provided at the start, what was asked for mid-process (missing inputs), what format inputs arrived in.

**Output signals**: What artifact was produced, where it was saved, what format it took, what quality checks were applied.

**Domain signals**: Specialized terminology, frameworks or methodologies applied, industry or domain context.

### Phase 3: Deduplicate Against Existing Skills

Before creating a new skill:

1. List directories in `~/.claude/skills/`
2. Read only the first 5 lines (title + description) of each existing SKILL.md
3. If the new skill overlaps significantly with an existing one, inform the user and ask: create new skill, or extend the existing one?

If extending, read the existing skill, identify gaps, and propose targeted additions. Do not rewrite.

### Phase 4: Assemble the Skill File

Build the SKILL.md using this structure. Every section is mandatory unless marked optional.

1. **`# [Title]`** — clear name (2-5 words)
2. **Opening paragraph** — what the skill does, what it transforms, what it produces
3. **`## Usage`** — invocation syntax with code block examples
4. **`## What This Skill Does`** — 3-5 phased steps using `### Phase N: Name` format. Each phase: action verb title, bullet sub-steps, concrete instructions, tool/file references where applicable
5. **`## Output Location`** — where the artifact is saved
6. **`## Quality Assurance`** *(optional)* — validation checks, include only if the workflow has them
7. **`## Tips for Best Results`** — 3-7 practical items
8. **`## Continuous Improvement`** — include:
   ```
   After completing this workflow, invoke `@skill-reflect [skill-name]` to update this skill with validated learnings from the execution.
   ```
9. **`## User-Invocable`** — `Yes - users can invoke this skill directly with @[skill-name]`

**Writing rules**:
- Imperative form (verb-first instructions)
- Front-load critical steps
- Under 200 lines for simple workflows, under 300 for complex
- Every line carries information — no padding
- Reference files and tools by exact name

### Phase 5: Present and Save

1. Show the complete SKILL.md to the user in a code block
2. Ask: "Does this capture your workflow correctly? Any changes before I save?"
3. On approval:
   - Create `~/.claude/skills/[skill-name]/`
   - Write SKILL.md
   - If resources were identified, create `resources/` and note which files the user should add
4. Confirm file location and skill name
5. Invoke `@skill-reflect skill-builder` to capture learnings from this execution

## Efficiency Rules

- **Scan, don't summarize**: Extract signals from the conversation — do not produce a narrative summary as an intermediate step
- **One-pass extraction**: Collect all signal categories in a single scan of the conversation
- **Minimal reads for dedup**: Read only title and description of existing skills, not full content
- **No speculative content**: Only include workflow steps that actually occurred or were explicitly described
- **Template-driven assembly**: Use the Phase 4 structure directly — no draft-revise-redraft cycles
- **Ask once**: Consolidate all clarifying questions into a single message

## Edge Cases

- **Conversation too short**: If fewer than 3 clear workflow steps can be extracted, inform the user and offer `--from-description` mode
- **Multiple workflows**: If the conversation contains multiple distinct workflows, list them and ask which to capture
- **Resources needed**: If the workflow depends on reference files or templates, create placeholder entries in `resources/` and instruct the user on what to add
- **Extending existing skill**: Read the existing skill, identify what the new workflow adds, propose targeted additions rather than a rewrite

## Continuous Improvement

After completing this workflow, invoke `@skill-reflect skill-builder` to update this skill with validated learnings from the execution.

## User-Invocable

Yes - users can invoke this skill directly with `@skill-builder`
