<div align="center">

# 🤖 SKILLS

**A curated personal collection of Agent Skills — reusable prompts and instructions for AI agents.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Mrlyk/SKILLS/pulls)
[![Skills Count](https://img.shields.io/badge/skills-1-orange.svg)](#-skill-library)

[English](#-about) · [简体中文](#-关于)

</div>

---

## 📖 About

**SKILLS** is a personal repository of AI agent skill prompts organized by category.
Each skill is a carefully crafted prompt (or prompt template) that can be dropped into any agent framework — [GitHub Copilot](https://github.com/features/copilot), [OpenAI Assistants](https://platform.openai.com/docs/assistants/overview), [Claude Projects](https://www.anthropic.com/index/claude-projects), [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT), and more.

> **Goal:** Stop rewriting the same prompts. Save, version, and reuse the best ones.

---

## 📖 关于

**SKILLS** 是一个按类别整理的 AI Agent Skill Prompt 个人收藏库。
每个 Skill 都是一个精心设计的提示词（或提示词模板），可以直接用于任何 Agent 框架，例如 [GitHub Copilot](https://github.com/features/copilot)、[OpenAI Assistants](https://platform.openai.com/docs/assistants/overview)、[Claude Projects](https://www.anthropic.com/index/claude-projects) 等。

> **目标：** 不再重复编写相同的提示词，统一保存、版本管理并复用最优的 Skill。

---

## 📁 Repository Structure

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
└── README.md
```

---

## 🚀 How to Use a Skill

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

## 📚 Skill Library

| Skill | Description | Source |
|---|---|---|
| [skill-creator](skills/skill-creator/SKILL.md) | Create new skills, modify and improve existing skills, and measure skill performance | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/skill-creator) |

---

## ➕ Adding a New Skill

1. Create a new folder under `skills/<skill-name>/`.
2. Add a `SKILL.md` as the main definition (see [anthropics/skills](https://github.com/anthropics/skills) for the standard format).
3. Include any supporting `agents/`, `scripts/`, `assets/`, or `references/` as needed.
4. Add a row to the table above.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and share the prompts.

---

<div align="center">
Made with ❤️ by <a href="https://github.com/Mrlyk">Mrlyk</a>
</div>
