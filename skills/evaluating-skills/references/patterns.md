# Dimension: Patterns

Rules that reward the presence of high-value instructional patterns: gotchas, templates, checklists, validation loops, plan-validate-execute, packaged scripts.

## Rules (positive presence, missing → deduction)

| Severity | Rule | Source |
|----------|------|--------|
| warn | No `## Gotchas` (or equivalent) section naming the non-obvious environment-specific facts | agentskills.io: "the highest-value content in many skills is a list of gotchas" |
| warn | No output template for structured outputs the skill must produce, but the SKILL description implies one | Anthropic best practices |
| warn | Multi-step destructive or batch operation described without a plan-validate-execute pattern (no intermediate plan file, no dry-run check) | Anthropic best practices |
| warn | Multi-step workflow with validation gates but no explicit checklist the agent can tick off | Anthropic best practices |
| warn | Logic that the agent is asked to re-implement each invocation could have been bundled as a `scripts/` entry — duplication risk | Anthropic PDF |
| info | No error-handling section / no guidance on what to do when a step fails | Anthropic PDF |
| info | Good examples exist but are buried in prose rather than set off as `**Before:**` / `**After:**` or fenced blocks | Authoring economy |

## Gotchas section — what counts

A passing Gotchas section contains items shaped like:

- environment-specific facts ("on macOS the `date` command uses `-v +1d` not `-d +1day`")
- counter-intuitive truths ("put_row is full-row overwrite, not upsert — missing fields are erased")
- corrections to plausible assumptions that the agent would otherwise make wrong

Generic safety advice ("always validate input") does NOT count as a gotcha. Gotchas must be concrete.

## Output template — what counts

When the skill promises structured output (report, JSON, markdown section), SKILL.md must provide a copy-paste skeleton the agent emits verbatim. Freehand instruction like "emit a nicely formatted summary" does not satisfy the rule.

## Validation-loop pattern

Look for the shape:

1. Execute action.
2. Run validator.
3. If validator fails, read the error; fix; re-run validator.
4. Continue only when validator passes.

Presence of this loop for quality-critical tasks earns no deduction; absence when it is warranted is a warn.

## Plan-validate-execute pattern

For batch or irreversible operations, the skill should ask the agent to:

1. Produce an intermediate plan file (machine-checkable format preferred).
2. Validate the plan against the real source of truth (filesystem, schema, DB).
3. Only then execute.

Skipping directly to execution for destructive operations is a warn-level violation.
