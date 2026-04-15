# English Report Template

Load this file when the user asks in English (see SKILL.md Gotcha #10). Emit the template body below **verbatim**, replacing only the `<...>` placeholders with actual values. Section headings and `**bold**` labels are part of the contract — do not translate or reword them.

## Template body

Dimension names must match SKILL.md Gotcha #6 exactly: `Metadata` / `Context Budget` / `Instruction Design` / `Structure & Disclosure` / `Patterns` / `Anti-patterns`.

````markdown
# SKILL.md Evaluation Report

**Target**: `<path or "pasted content">`
**Final score**: **<N>/100** (<rating>)
**Scored at**: <YYYY-MM-DD HH:MM>

## Dimension Scores

| # | Dimension | Score | Critical | Warn | Info |
|---|-----------|-------|----------|------|------|
| 1 | Metadata | <n>/100 | <c> | <w> | <i> |
| 2 | Context Budget | <n>/100 | <c> | <w> | <i> |
| 3 | Instruction Design | <n>/100 | <c> | <w> | <i> |
| 4 | Structure & Disclosure | <n>/100 | <c> | <w> | <i> |
| 5 | Patterns | <n>/100 | <c> | <w> | <i> |
| 6 | Anti-patterns | <n>/100 | <c> | <w> | <i> |

## Critical Violations

### <short-rule-name> [dimension: <name>]

**Evidence** (quote from SKILL.md):
> <exact excerpt>

**Why it fails**: <one or two sentences citing the rule from Anthropic / agentskills.io>

**Rewrite**:
```
<before>
---
<after>
```

(Repeat for each critical violation.)

## Warn Violations

### <short-rule-name> [dimension: <name>]

**Evidence**:
> <excerpt>

**Why it fails**: <one sentence>

**Rewrite**:
```
<before>
---
<after>
```

(Repeat for each warn violation.)

## Info Violations

- [<dimension>] <short description> (e.g., "magic constant `TIMEOUT = 47` has no comment explaining the value")
- [<dimension>] <short description>

(List only. No rewrite required for info-level findings.)
````

## Rating bands

- 90-100: Excellent — ships as-is
- 75-89: Good — minor polish recommended
- 60-74: Acceptable — address warn-level before heavy reuse
- 40-59: Needs work — one or more critical violations; fix before distribution
- 0-39: Broken — rewrite required
