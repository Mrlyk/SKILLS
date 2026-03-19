<div align="center">

# SKILLS

**AI Agent Skill 个人收藏库**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills Count](https://img.shields.io/badge/skills-1-orange.svg)](#-skill-收藏库)

[English](README_EN.md)

</div>

---

## 关于

**SKILLS** 是一个按类别整理的 AI Agent Skill 个人收藏库，公开分享供参考。

每个 Skill 来源于社区或个人实践积累，本仓库的定位是个人书签——记录那些值得保留和复用的 Skill，方便随时查阅。

> 这不是一个框架或工具，只是一份以仓库形式维护的个人整理清单。

---

## 目录结构

```
SKILLS/
├── skills/                          # 所有 Skill，按文件夹分类
│   └── skill-creator/               # 创建、优化并评测 Agent Skill
│       ├── SKILL.md                 # Skill 主定义文件
│       ├── LICENSE.txt              # Apache 2.0 协议
│       ├── agents/                  # 子 Agent 提示词
│       ├── assets/                  # 静态资源
│       ├── eval-viewer/             # 评测结果查看脚本
│       ├── references/              # 参考 Schema
│       └── scripts/                 # Python 辅助脚本
├── .gitignore
├── LICENSE
├── README.md
└── README_EN.md
```

---

## 如何使用 Skill

每个 Skill 存放在 `skills/` 下各自独立的文件夹中，主定义文件统一为 `SKILL.md`。

### 1 · 阅读 Skill 定义

打开 `skills/<skill-name>/SKILL.md`，文件头部描述该 Skill 的名称与触发时机，正文说明具体使用方式。

### 2 · 接入 Agent 平台

将 `SKILL.md` 的内容复制到对应平台的系统提示词或 Skill 指令字段中：

| 平台 | 填写位置 |
|---|---|
| **GitHub Copilot** | `.github/copilot-instructions.md` 或对话窗口 |
| **Claude Projects** | Project Instructions 字段 |
| **OpenAI Assistants** | Assistants API 的 System instructions |
| **LangChain / AutoGPT** | `SystemMessage` 或 agent description |

### 3 · 使用附属文件（如有）

部分 Skill 包含以下目录：

| 目录 | 用途 |
|---|---|
| `agents/` | 主 Skill 调用的子 Agent 提示词 |
| `scripts/` | Python 辅助脚本（评测、报告生成等） |
| `eval-viewer/` | 评测结果查看工具 |
| `references/` | Schema 定义与参考文档 |
| `assets/` | 静态资源（HTML 模板等） |

---

## Skill 收藏库

| Skill | 描述 | 来源 |
|---|---|---|
| [skill-creator](skills/skill-creator/SKILL.md) | 创建新 Skill、修改优化已有 Skill、评测 Skill 性能 | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/skill-creator) |

---

## Skill 整理规范

每个 Skill 按以下约定存放在 `skills/<skill-name>/` 文件夹中：

1. `SKILL.md` — Skill 主定义文件（格式参考 [anthropics/skills](https://github.com/anthropics/skills)）
2. 附属目录（`agents/`、`scripts/`、`assets/`、`references/`）随原始 Skill 一并收录
3. 在上方收藏库表格中补充一行索引

---

## 许可证

本项目基于 [MIT License](LICENSE)，欢迎自由使用、修改和分享。

---

<div align="center">
Made with ❤️ by <a href="https://github.com/Mrlyk">Mrlyk</a>
</div>
