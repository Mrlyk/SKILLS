# Dimension: Structure & Disclosure

Rules about how content inside SKILL.md and the surrounding folder is organized.

## Rules

| Severity | Rule | Source |
|----------|------|--------|
| critical | `README.md` exists in the skill folder (Anthropic PDF: "No README.md inside your skill folder") | Anthropic PDF |
| warn | SKILL.md references a nested file chain (SKILL.md → advanced.md → details.md); references must be one level deep only | Anthropic best practices |
| warn | A `references/` file exceeds 100 lines but has no table of contents at the top | Anthropic best practices |
| warn | SKILL.md contains a huge wall of rules that should be split by domain into `references/{domain}.md` (e.g., finance/sales/product in one file instead of three) | Anthropic best practices |
| warn | A `references/` file is never linked from SKILL.md (orphan file — the agent will never load it) | Authoring consistency |
| info | Link to a reference file without stating *when* to load it ("consult references/api-patterns.md" vs "if the API returns non-200, consult references/api-patterns.md") | Anthropic best practices |
| info | Section headings use inconsistent levels (H2 for one subsection, H3 for a sibling subsection) | Authoring consistency |

## Folder shape (Anthropic PDF canonical)

```
skill-folder/            # kebab-case
├── SKILL.md             # required, exact filename (case-sensitive)
├── scripts/             # optional, executable code
├── references/          # optional, documentation
└── assets/              # optional, templates, data files
```

No other top-level entries are expected. Penalize the presence of `README.md`, `__pycache__`, `.DS_Store`, or stray `.md` files at the folder root (info-level unless explicitly listed as critical above).

## Progressive-disclosure litmus

Load order the agent follows:

1. Metadata (`name`, `description`) — always loaded.
2. SKILL.md body — loaded when the agent decides the skill applies.
3. `references/*.md` — loaded only when SKILL.md links to it with a conditional trigger.
4. `scripts/*.py` — executed on demand, the code itself never enters the context unless Read.

A SKILL is well-structured when the bulk of information sits in level 3 or 4 and SKILL.md only acts as a router.

## Conditional-load phrasing template

Correct:

> When the API returns a non-200 status, load `references/api-errors.md` before retrying.

Incorrect (violates the rule):

> See `references/api-errors.md` for error handling.

The second form gives no trigger condition; the agent may load it every time or never.
