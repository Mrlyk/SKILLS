# Dimension: Instruction Design

Rules for how instructions inside SKILL.md should read. Anchored on "match specificity to fragility" and "favor procedures over declarations".

## Rules

| Severity | Rule | Source |
|----------|------|--------|
| critical | Abstract instruction without a concrete runnable command where code would be deterministic (e.g., "validate the data" instead of `python scripts/validate.py --input <file>`) | Anthropic PDF: "Code is deterministic; language interpretation isn't" |
| warn | Presents multiple approaches as a menu without selecting a default (e.g., "you can use pypdf, pdfplumber, PyMuPDF, or pdf2image") | Anthropic best practices |
| warn | Specificity is mismatched to fragility: fragile / ordered / safety-critical tasks are described with vague wording; or multi-path tasks are over-constrained | Anthropic best practices |
| warn | Declarative statement ("the output should be X") where a procedural instruction ("to produce X, do step 1, then step 2") would generalize | Anthropic best practices |
| warn | Pseudocode or algorithm that re-implements logic the bundled scripts already encapsulate (duplication between prose and scripts) | Anthropic PDF |
| info | Verb-only instruction ("ensure", "make sure", "properly") without a concrete check; should reference a script or a specific string to look for | Anthropic PDF |
| info | Missing *why* next to a non-obvious constraint (e.g., "always retry three times" — why three?) | agentskills.io |

## Fragility ladder

| Task type | Recommended specificity |
|-----------|-------------------------|
| Safety-critical / irreversible / strict sequence required | Prescriptive script or exact command; minimal wording |
| Deterministic transformation with stable input | Specific steps + example I/O |
| Multiple valid approaches | General guidance + a named default + a one-line escape hatch for the alternative |
| Exploratory / creative | High-level goal only; let the agent reason |

A violation exists when a skill applies a level of specificity from the wrong row.

## Default over menu — concrete rewrite pattern

**Before (menu):**
> You can use pypdf, pdfplumber, PyMuPDF, or pdf2image depending on your needs.

**After (default + escape hatch):**
> Use `pdfplumber` for text extraction. If the PDF is scanned, fall back to `pdf2image` + `pytesseract` for OCR.

Always prefer the "after" form in rewrite suggestions.

## Procedural rewrite pattern

**Before (declarative):** "The commit message should be concise and descriptive."

**After (procedural):** "To write the commit message: (1) name the subsystem in the first colon-separated token; (2) keep the summary line under 72 characters; (3) use imperative mood ('add', not 'added'); (4) omit trailing period."

Declarative wording generalizes poorly across instances; procedural wording does.
