# Dimension: Anti-patterns

Rules that detect textual or structural smells the agent should flag. Every hit is a deduction in the Anti-patterns dimension.

## Rules

| Severity | Rule | Source |
|----------|------|--------|
| warn | Windows-style paths in SKILL.md or scripts (`scripts\helper.py`) — must be forward slash | Anthropic best practices |
| warn | Magic numbers / "voodoo constants" without a comment explaining *why* (`TIMEOUT = 47`, `RETRIES = 5` with no rationale) | Anthropic best practices |
| warn | "Too many options" — presenting N alternatives in prose without selecting a default | Anthropic best practices |
| warn | Punts to Claude instead of solving ("if errors occur, figure out how to handle them" without concrete recovery strategy) | Anthropic best practices |
| warn | Inconsistent terminology (same concept referred to by two or more names: "API endpoint" vs "URL" vs "route"; "field" vs "box" vs "control"; "extract" vs "pull" vs "fetch") | Anthropic best practices |
| warn | Assumes dependencies are pre-installed without an install command (e.g., uses `pypdf` but never says `pip install pypdf`) | Anthropic best practices |
| warn | Uses MCP tools without fully-qualified names (`bigquery_schema` alone instead of `BigQuery:bigquery_schema`) | Anthropic best practices |
| info | Emoji decoration that does not carry information | Authoring economy |
| info | Excessive emphasis markers (**bold**, *italic*) sprinkled on every line — signal loss | Authoring economy |
| info | Trailing whitespace, inconsistent list markers (`-` mixed with `*`) | Authoring polish |

## Terminology consistency check procedure

When evaluating, build a glossary of the nouns the SKILL uses for its core concepts. If two distinct tokens name the same referent, flag a warn. Evidence in the report: quote both occurrences with line references.

Example report finding:

> **Rule**: Inconsistent terminology.
> **Evidence**: Line 42 — "make the API call to the /users endpoint"; Line 77 — "the /users URL accepts POST". Two tokens (`endpoint`, `URL`) for the same referent.
> **Rewrite**: Pick one (`endpoint` recommended for REST semantics) and replace throughout.

## Punting detection

A punt is any sentence that defers decision-making to the agent without naming the options. Phrases that often indicate a punt:

- "handle accordingly"
- "use your judgment"
- "figure out the right approach"
- "as appropriate"

Not every "as appropriate" is a punt; context decides. When the skill could have listed the approaches or shipped a validator, the phrase is a punt.

## Magic-number exception

`HTTP_OK = 200` and similar well-known protocol constants are NOT voodoo constants even without a comment. The rule targets constants whose value is a tuning decision, not a standard.
