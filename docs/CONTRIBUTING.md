# Contributing to SKILLS

Thank you for your interest in contributing! Every new skill makes this collection more useful for everyone. Please follow the guidelines below.

---

## 📋 Before You Start

- Check the existing skills to avoid duplicates.
- Make sure your skill is general-purpose enough to be reusable by others.
- Test the prompt with at least one AI model before submitting.

---

## 🛠️ Adding a Skill

### Step 1 — Choose a Category

Place your skill in one of these directories:

| Directory | What belongs here |
|---|---|
| `skills/code/` | Coding, debugging, refactoring, architecture |
| `skills/writing/` | Documentation, blog posts, emails, README |
| `skills/data-analysis/` | Data cleaning, exploration, visualization |
| `skills/research/` | Web research, literature review, summarization |
| `skills/productivity/` | Task planning, meeting notes, scheduling |

If your skill doesn't fit any of these, propose a new category in your PR.

### Step 2 — Create the File

```bash
cp docs/SKILL_TEMPLATE.md skills/<category>/<skill-name>.md
```

Use kebab-case for the file name (e.g., `sql-query-optimizer.md`).

### Step 3 — Fill in the Template

All sections in [`docs/SKILL_TEMPLATE.md`](SKILL_TEMPLATE.md) are required:

- **Overview** – category, compatible models, author, version.
- **Prompt** – the full prompt text. Use `{parameter}` for dynamic parts.
- **Parameters** – table describing each `{parameter}`.
- **Example Input / Output** – a concrete end-to-end example.
- **Notes** – caveats, tested models, tips.

### Step 4 — Update README.md

Add a row for your skill in the appropriate table in the [Skill Library](../README.md#-skill-library) section.

### Step 5 — Open a Pull Request

- Use a descriptive title: `feat: add SQL query optimizer skill`
- Describe what the skill does and which models you tested.

---

## ✅ Skill Quality Checklist

Before submitting, ensure:

- [ ] Prompt produces consistent, high-quality output
- [ ] All `{parameters}` are documented in the Parameters table
- [ ] At least one real Example Input / Output is provided
- [ ] README table is updated
- [ ] File name is in `kebab-case.md`

---

## 🐛 Reporting Issues

Found a skill that doesn't work well with a specific model? Open an [Issue](https://github.com/Mrlyk/SKILLS/issues) with:
- The skill name and file path
- The model you tested on
- What the expected vs actual output was

---

Thank you for helping grow this collection! 🚀
