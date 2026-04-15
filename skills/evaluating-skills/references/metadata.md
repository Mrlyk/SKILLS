# Dimension: Metadata

Rules beyond the top-10 naming / description checks. Apply every time SKILL.md has frontmatter.

## Rules

| Severity | Rule | Source |
|----------|------|--------|
| critical | YAML frontmatter malformed (missing `---` fences, unparseable YAML) | Anthropic PDF |
| critical | `name` field longer than 64 characters | Anthropic docs |
| critical | `description` field longer than **800 characters** (stricter than Anthropic's official 1024 cap — tighter descriptions score higher on discoverability) | Anthropic docs + project convention |
| critical | `description` empty or only whitespace | Anthropic docs |
| warn | `name` is vague (`helper`, `utils`, `tools`, `documents`, `data`, `files`) | Anthropic best practices |
| warn | `description` starts with "I", "我", "You", "您" (first-/second-person subject rather than a third-person verb) | Anthropic best practices |
| warn | `description` mentions file types or tools but the SKILL body never references them (dangling trigger) | Authoring consistency |
| info | `name` is not in gerund form (`processing-pdfs`) nor a clear noun phrase (`pdf-processing`); `process-pdfs` is acceptable but less preferred | Anthropic best practices |
| info | `description` missing a concrete example phrase that a user would actually say | Anthropic PDF |

## What counts as a "concrete trigger phrase"

A phrase a real user would type or speak, typically quoted: `"推荐北京酒店"`, `"查看这家酒店详情"`, `"score this SKILL"`, `"extract text from PDF"`. Generic verbs ("help with", "manage", "handle") without a user phrasing do NOT count.

## What counts as "WHAT + WHEN"

- **WHAT**: concrete capability described in third person. Example: "Evaluates a single SKILL.md against best practices and produces a scored report."
- **WHEN**: one or more trigger conditions. Example: "Use when the user asks to audit, evaluate, score, or critique a SKILL.md."

Both halves must be present in the same `description`.

## Allowed third-person subjects

`the user` / `the agent` / `Claude` / `用户` — none of these count as pronoun violations. Only first- and second-person forms are banned.
