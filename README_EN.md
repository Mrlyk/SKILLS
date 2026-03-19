<div align="center">

# SKILLS

**A personal collection of AI Agent Skills**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills Count](https://img.shields.io/badge/skills-1-orange.svg)](#-skill-library)

[简体中文](README.md)

</div>

---

## About

**SKILLS** is a personal collection of AI agent skills, organized by category and shared publicly for reference.

Each skill is sourced from the community or crafted from personal experience. This repository serves as a personal bookmark — a place to keep track of useful skills worth remembering and revisiting.

> This is not a framework or tool. It is a curated reading list in repository form.

---

## Repository Structure

```
SKILLS/
├── skills/                          # All agent skills, organized by folder
│   └── skill-creator/               # Create, improve & benchmark agent skills
│       ├── SKILL.md                 # Main skill definition
│       ├── LICENSE.txt              # Apache 2.0 license
│       ├── agents/                  # Sub-agent prompts (analyzer, comparator, grader)
│       ├── assets/                  # HTML eval review template
│       ├── eval-viewer/             # Eval result viewer scripts
│       ├── references/              # Reference schemas
│       └── scripts/                 # Python helper scripts (run_eval, run_loop, etc.)
├── .gitignore
├── LICENSE
├── README.md
└── README_EN.md
```

---

## How to Use a Skill

Each skill lives in its own folder under `skills/`. The main definition is always `SKILL.md`.

### 1 · Read the Skill Definition

Open `skills/<skill-name>/SKILL.md`. The front-matter describes the skill's name and when it triggers, and the body explains how to use it.

### 2 · Use the Skill with an Agent

Copy the content of `SKILL.md` into your agent's system prompt or skill instruction field. Different platforms have different names for this:

| Platform | Where to paste |
|---|---|
| **GitHub Copilot** | `.github/copilot-instructions.md` or a chat session |
| **Claude Projects** | Project Instructions field |
| **OpenAI Assistants** | System instructions in the Assistants API |
| **LangChain / AutoGPT** | `SystemMessage` or agent description |

### 3 · Use Supporting Files (if present)

Some skills include:

| Directory | Purpose |
|---|---|
| `agents/` | Sub-agent prompt files invoked by the main skill |
| `scripts/` | Python helper scripts (e.g., run evals, generate reports) |
| `eval-viewer/` | Tools for reviewing skill evaluation results |
| `references/` | Schema definitions and reference documents |
| `assets/` | Static assets (HTML templates, etc.) |

---

## Skill Library

| Skill | Description | Source |
|---|---|---|
| [skill-creator](skills/skill-creator/SKILL.md) | Create new skills, modify and improve existing skills, and measure skill performance | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/skill-creator) |

---

## Skill Organization Convention

Each skill lives in its own folder under `skills/<skill-name>/` following the structure below:

1. `SKILL.md` — main skill definition (refer to [anthropics/skills](https://github.com/anthropics/skills) for the standard format)
2. Supporting directories (`agents/`, `scripts/`, `assets/`, `references/`) are included when the original skill provides them
3. A row is added to the Skill Library table above for quick reference

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and share the prompts.

---

<div align="center">
Made with ❤️ by <a href="https://github.com/Mrlyk">Mrlyk</a>
</div>
