# Dimension: Context Budget

Everything loaded from SKILL.md consumes the model's context window. Rules below enforce the "add what the agent lacks, omit what it knows" principle.

## Rules

| Severity | Rule | Source |
|----------|------|--------|
| critical | SKILL.md body exceeds **5000 words** (Anthropic PDF: performance degrades beyond this) | Anthropic PDF |
| critical | SKILL.md body exceeds **500 lines** (Anthropic best practices: the soft ceiling) | Anthropic docs |
| critical | Contains time-sensitive statements at top level (e.g., "before August 2025", "new API", "legacy as of Q3") | Anthropic best practices |
| warn | Explains general knowledge the model already has (e.g., "PDF is a file format", "JSON consists of key-value pairs") | Anthropic best practices |
| warn | Redundant sections: the same rule or concept is stated in multiple places (e.g., repeated in Overview, Rules, and Gotchas) | agentskills.io |
| warn | Heavy-handed `MUST` / `必须` / `强制` scattered across the file without explaining *why* | Anthropic best practices |
| info | Long verbose prose paragraph where a table or bullet list would compress the same information | Authoring economy |
| info | Contains low-signal filler ("This skill is great at...", "Here is how to...") | Authoring economy |

## Self-test for every paragraph

Ask: **"Would the agent get this wrong without this paragraph?"** If no, delete.

## Time-sensitive content escape hatches

These do NOT count as violations when used correctly:

- A section wrapped in `<details><summary>Legacy pattern</summary>...</details>` — collapsed historical context
- A link to `references/legacy.md` — pushed out of the main file
- A version number in YAML frontmatter (acceptable because it is metadata, not instruction)

## Word vs line counting

- Line count: `wc -l SKILL.md`
- Word count: `wc -w SKILL.md` (both Chinese and English words; CJK is counted by character-block so the effective ceiling for Chinese is lower — treat the 5000-word budget as ~8000 Chinese characters for practical purposes)

Record both numbers in the Metadata dimension of the report header so downstream fixes can target the overflow precisely.
