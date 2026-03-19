<div align="center">

# 🤖 SKILLS

**A curated personal collection of Agent Skills — reusable prompts and instructions for AI agents.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](docs/CONTRIBUTING.md)
[![Skills Count](https://img.shields.io/badge/skills-3-orange.svg)](#-skill-library)

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
├── skills/                    # All skill prompts, organized by category
│   ├── code/                  # Coding & engineering skills
│   │   └── code-review.md
│   ├── writing/               # Writing & documentation skills
│   │   └── readme-generator.md
│   ├── data-analysis/         # Data analysis & visualization skills
│   │   └── data-summary.md
│   ├── research/              # Research & information retrieval skills
│   └── productivity/          # Workflow & productivity skills
├── examples/                  # End-to-end usage examples
├── docs/
│   ├── SKILL_TEMPLATE.md      # Template for adding new skills
│   └── CONTRIBUTING.md        # Contribution guidelines
├── .gitignore
└── README.md
```

---

## 🚀 How to Use a Skill

### 1 · Copy the Prompt

Open any skill file under `skills/`, copy the prompt block, and paste it into your agent's system prompt or instruction field.

### 2 · Fill in Parameters

Each skill prompt uses `{parameter}` placeholders. Replace them with your actual input before sending.

```markdown
<!-- Example: skills/code/code-review.md -->
{code} → paste your code snippet here
```

### 3 · Run with Your Agent

You can use these skills with:

| Platform | How to Use |
|---|---|
| **GitHub Copilot** | Paste into a `.github/copilot-instructions.md` or a chat session |
| **OpenAI Assistants** | Add as system instructions in the Assistants API |
| **Claude Projects** | Paste into the Project Instructions field |
| **LangChain / AutoGPT** | Use as a `SystemMessage` or agent description |
| **Any Chat Interface** | Paste directly as your first message |

---

## 📚 Skill Library

### 💻 Code

| Skill | Description | Model |
|---|---|---|
| [Code Review](skills/code/code-review.md) | Multi-dimension code review covering correctness, security, and performance | GPT-4o / Claude 3.5 |

### ✍️ Writing

| Skill | Description | Model |
|---|---|---|
| [README Generator](skills/writing/readme-generator.md) | Generate a professional GitHub README from a project description | GPT-4o / Claude 3.5 |

### 📊 Data Analysis

| Skill | Description | Model |
|---|---|---|
| [Data Summary](skills/data-analysis/data-summary.md) | Summarize a CSV/JSON dataset and surface key insights | GPT-4o |

---

## ➕ Adding a New Skill

1. Copy [`docs/SKILL_TEMPLATE.md`](docs/SKILL_TEMPLATE.md) to the appropriate `skills/<category>/` folder.
2. Fill in every section (overview, prompt, parameters, examples).
3. Add a row to the table in this README.
4. Open a Pull Request — contributions are welcome!

See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed guidelines.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and share the prompts.

---

<div align="center">
Made with ❤️ by <a href="https://github.com/Mrlyk">Mrlyk</a>
</div>
