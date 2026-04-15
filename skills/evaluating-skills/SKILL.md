---
name: evaluating-skills
description: Evaluates a single SKILL.md against Anthropic and agentskills.io best practices, producing a severity-based scorecard with per-dimension scores and actionable rewrite suggestions. Use when the user explicitly asks to review, audit, evaluate, score, or critique a SKILL.md file (for example "check if this SKILL follows best practices", "score this skill doc", "audit ~/.claude/skills/foo/SKILL.md", "is this skill well written?", "帮我评估一下这个 SKILL", "这个 SKILL 写得怎么样", "帮我看看这个 SKILL 有什么问题", "这个 SKILL 能打多少分").
---

# Evaluating Skills

Reviewer for a single `SKILL.md` file. Scores it across six dimensions derived from three authoritative sources: Anthropic's official Skills best practices documentation, the agentskills best-practices guide, and Anthropic's *Complete Guide to Building Skills for Claude*.

Scope is strictly limited to the SKILL.md file. `references/`, `scripts/`, and `assets/` are NOT audited by this skill; run a dedicated pass on them if needed.

## When to Use

Trigger on explicit user intent only. Examples:

- "Evaluate / audit / review / score / critique this SKILL.md"
- "Does this skill follow Anthropic best practices?"
- "Grade this skill doc"
- "点评 / 打分 / 审查这个 SKILL"

Do NOT auto-trigger on any ordinary edit to a SKILL.md. The user must ask.

## Input Contract

Accept either form:

1. **File path**: The user points to a path such as `~/.claude/skills/foo/SKILL.md` or `.claude/skills/bar/SKILL.md`. Read the file with the Read tool.
2. **Inline content**: The user pastes the full SKILL.md content in the conversation. Use it directly.

Always confirm the target SKILL.md path (or "pasted content") in the first line of the report so the user can trace the scoring back to the correct file.

## Scoring Model

Six dimensions. Each dimension starts at 100 and loses points per violation. Dimension score floors at 0. **Final score = arithmetic mean of the six dimension scores**.

### Dimensions

| # | Dimension | Focus |
|---|-----------|-------|
| 1 | **Metadata** | frontmatter, `name`, `description`, naming conventions |
| 2 | **Context Budget** | file length, no agent-known boilerplate, no time-sensitive info, no redundancy |
| 3 | **Instruction Design** | specificity matched to fragility, default over menu, procedural over declarative, no heavy-handed MUST |
| 4 | **Structure & Disclosure** | progressive disclosure, one-level references depth, TOC for long files |
| 5 | **Patterns** | gotchas section, output templates, checklists, validation loops, packaged scripts |
| 6 | **Anti-patterns** | Windows paths, magic constants, too many options, punting to Claude, inconsistent terminology, nested refs |

### Severity Weights

| Severity | Deduction | Meaning |
|----------|-----------|---------|
| `critical` | -30 | Hard rule in Anthropic docs / violates loading contract / safety |
| `warn` | -10 | Degrades effectiveness or discoverability, best-practice violation |
| `info` | -3 | Style/consistency nit |

Each violation counts once per occurrence. A single dimension can receive multiple violations of the same severity.

## Top 10 Rules (checked in SKILL.md main file)

These are the highest-value rules, enforced by this skill for every evaluation. See `references/` for the full rule library per dimension.

| # | Severity | Rule |
|---|----------|------|
| 1 | critical | **Naming compliance**: the file must be `SKILL.md` (case-sensitive); the containing folder and the `name` frontmatter field must be kebab-case (no spaces, no uppercase, no underscores); the `name` must not start with platform-reserved keywords such as `claude` |
| 2 | critical | **`description` missing the WHAT+WHEN pair**: Anthropic docs require BOTH what the skill does AND when to use it (trigger conditions). Missing either half is critical |
| 3 | critical | **`description` lacks concrete trigger phrases**: only generic verbs ("helps with projects") with no example user phrasing; if the skill handles specific file types, those types must be named |
| 4 | critical | **`description` uses first- or second-person pronouns in the skill's own narration**: banned pronouns are I / we / us / my / our / you / your / yours, plus Chinese 我 / 我们 / 您 / 你 / 你们 when they refer to the skill itself or address the user. `the user` / `用户` third-person subjects are allowed. Pronouns that appear inside quoted user utterances used as trigger examples (e.g. `"帮我评估一下"`, `"help me with..."`) are NOT violations — Anthropic requires real user phrasing in the description |
| 5 | critical | **`description` violates hard constraints**: longer than **800 characters** (stricter than Anthropic's official 1024 — tighter descriptions score higher on discoverability), or contains XML angle brackets (`<` / `>`), or is empty / whitespace-only |
| 6 | critical | **SKILL.md body exceeds 5000 words OR 500 lines** (either threshold; Anthropic PDF warns that >5000 words triggers performance degradation) |
| 7 | critical | **Time-sensitive statements present**: phrases such as "before August 2025", "new API / legacy API", "as of Q3", version-dated migration notes. Move historical context into a collapsed `<details>` or `references/legacy.md` |
| 8 | warn | **`README.md` exists inside the skill folder**: Anthropic PDF rule — "No README.md inside your skill folder. All documentation goes in SKILL.md or references/" |
| 9 | warn | **Single strict-sequence workflow covers multiple user intents** OR **hard constraints mixed into workflow steps**: use conditional workflow (branch by intent) and hoist hard constraints into a dedicated `## Safety & Guardrails` or `## Gotchas` section |
| 10 | warn | **Abstract instructions instead of concrete runnable commands**: "validate the data" is weaker than `python scripts/validate.py --input <file>`. Anthropic PDF: "Code is deterministic; language interpretation isn't" |

## Report Template

Two templates live in `references/` — load exactly one based on the user's question language (see Gotcha #10):

- English report → `references/report-template-en.md`
- Chinese report → `references/report-template-zh.md`

Each file contains: the template body (emit verbatim, replace `<...>` placeholders) and its rating bands. Dimension names must match Gotcha #6 exactly.

Do NOT load both files in the same pass — that wastes context budget, and any single report uses one language end-to-end.

## Evaluation Workflow

Follow these steps strictly. Do not skip.

1. **Resolve the target.** If the user gave a path, Read it. If the user pasted content, use it. Record the target string for the report header.
2. **Extract frontmatter** between the first `---` / `---` fences. Parse `name`, `description`. Note whether YAML is well-formed.
3. **Apply the Top 10 rules to SKILL.md.** For each rule:
   - If it matches, record: `{rule_id, severity, dimension, evidence_excerpt}`.
   - Evidence must be a verbatim quote from the file, never a paraphrase.
4. **Apply the dimension-specific rule sets from `references/`:**
   - `references/metadata.md`
   - `references/context-budget.md`
   - `references/instruction-design.md`
   - `references/structure.md`
   - `references/patterns.md`
   - `references/anti-patterns.md`
   Load only the files whose dimension is relevant to the SKILL being evaluated (progressive disclosure).
5. **Compute dimension scores.** Start each dimension at 100; subtract 30 per critical, 10 per warn, 3 per info; floor at 0.
6. **Compute final score** as the arithmetic mean of the six dimension scores, rounded to the nearest integer.
7. **Read exactly one report template.** Decide the report language per Gotcha #10, then Read `references/report-template-en.md` OR `references/report-template-zh.md` — not both. Emit its template body verbatim with `<...>` placeholders filled in. For `critical` and `warn`, include a concrete rewrite (before → after). For `info`, one-line description only. Order violations within each severity group by dimension index (1 → 6) for stable output.

## Gotchas

1. **Never invent evidence.** Every rule violation must quote text that actually appears in the target SKILL.md. If uncertain, re-Read the file and search for the passage.
2. **Do not audit `references/`, `scripts/`, `assets/`** in the same pass. They have different rules (no frontmatter, no 500-line ceiling, etc.) and would produce false positives.
3. **Rating bands are on the final score**, not individual dimensions. Do not downgrade the whole skill because a single dimension happens to score low.
4. **`the user` / `用户` are third-person**, and NOT a pronoun violation. Only first-person (I / we / us / my / our / 我 / 我们) and second-person (you / your / yours / 您 / 你 / 你们) are banned.
5. **5000 words ≠ 500 lines.** A dense SKILL.md may hit 5000 words in ~350 lines; a code-heavy one may hit 500 lines at 2500 words. Check both.
6. **Do not fabricate dimension names.** English reports must use exactly: `Metadata` / `Context Budget` / `Instruction Design` / `Structure & Disclosure` / `Patterns` / `Anti-patterns`. Chinese reports must use exactly: `元数据` / `上下文占用` / `指令设计` / `结构与渐进式披露` / `指令模式` / `反模式`. Never mix languages within a single report, never coin other names.
7. **XML angle brackets in `description`** (rule 5) refer to literal `<` / `>` characters. Code fences, backticks, and markdown link syntax `[text](url)` are fine.
8. **If the file has no frontmatter at all**, score Metadata 0, add one critical violation "Missing frontmatter", and continue evaluating the body — do not abort the whole report.
9. **Time-sensitive clauses in a `<details>` block or a dedicated `references/legacy.md`** are acceptable; only top-level, uncollapsed time references count as violations.
10. **Emit the report in the same language the user spoke** (Chinese or English). The evidence excerpts always stay verbatim in the SKILL.md's original language.
