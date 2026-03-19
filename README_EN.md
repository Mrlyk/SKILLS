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

Copy the skill folder to the designated path for your platform. The agent will load it automatically based on the description, or you can invoke it manually with `/skill-name`:

| Platform | Project-level path | User-level path |
|---|---|---|
| **Cursor** | `.cursor/skills/<name>/` | `~/.cursor/skills/<name>/` |
| **Claude Code** | `.claude/skills/<name>/` | `~/.claude/skills/<name>/` |
| **GitHub Copilot** | `.github/skills/<name>/` | `~/.copilot/skills/<name>/` |
| **OpenAI Codex** | — | `~/.codex/skills/<name>/` |
| **Gemini CLI** | `.gemini/skills/<name>/` | `~/.gemini/skills/<name>/` |
| **Kiro** | `.kiro/skills/<name>/` | `~/.kiro/skills/<name>/` |
| **Qwen Code** | `.qwen/skills/<name>/` | `~/.qwen/skills/<name>/` |
| **OpenClaw** | `skills/<name>/` | `~/.openclaw/skills/<name>/` |
| **Antigravity** | `.agent/skills/<name>/` | `~/.agent/skills/<name>/` |
| **Qoder** | `.qoder/skills/<name>/` | `~/.qoder/skills/<name>/` |

You can also use the [vercel-labs/skills](https://github.com/vercel-labs/skills) CLI to install in one step. It supports 40+ platforms and automatically detects installed agents to write to the correct path:

```bash
# Install all skills from this repository
npx skills add Mrlyk/SKILLS

# Install a specific skill
npx skills add Mrlyk/SKILLS --skill skill-creator

# Install globally (available across all projects)
npx skills add Mrlyk/SKILLS -g

# Install to specific agents
npx skills add Mrlyk/SKILLS -a claude-code -a cursor
```

### 3 · Use Supporting Files (if present)

Some skills include the following standard directories:

| Directory | Purpose |
|---|---|
| `scripts/` | Executable code (Python, Bash, etc.) invoked by the skill at runtime |
| `references/` | Documentation (API guides, examples, etc.) loaded by the agent as needed |
| `assets/` | Templates, fonts, icons, and other static resources used in output |

---

## Skill Library

| Skill | Description | Source |
|---|---|---|
| [skill-creator](skills/skill-creator/SKILL.md) | Create new skills, modify and improve existing skills, and measure skill performance | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/skill-creator) |

---

## Skill Organization Convention

Each skill lives in its own folder under `skills/<skill-name>/` following the structure below:

1. `SKILL.md` — main skill definition (refer to [anthropics/skills](https://github.com/anthropics/skills) for the standard format)
2. Supporting directories (`scripts/`, `references/`, `assets/`) are included when the original skill provides them
3. A row is added to the Skill Library table above for quick reference

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and share the prompts.

---

<div align="center">
Made with ❤️ by <a href="https://github.com/Mrlyk">Mrlyk</a>
</div>
