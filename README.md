<div align="center">

# SKILLS

**AI Agent Skill 个人收藏库**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills Count](https://img.shields.io/badge/skills-11-orange.svg)](#-skill-收藏库)

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
│   ├── skill-creator/               # 创建、优化并评测 Agent Skill
│   │   ├── SKILL.md
│   │   ├── agents/
│   │   ├── assets/
│   │   ├── eval-viewer/
│   │   ├── references/
│   │   └── scripts/
│   ├── tdd/                         # 测试驱动开发（TDD）
│   │   ├── SKILL.md
│   │   ├── mocking.md
│   │   ├── refactoring.md
│   │   └── tests.md
│   ├── canvas-design/               # 生成精美视觉设计（.png/.pdf）
│   │   └── SKILL.md
│   ├── humanizer/                   # 去除文本 AI 生成痕迹
│   │   └── SKILL.md
│   ├── grill-me/                    # 对方案进行结构化追问
│   │   └── SKILL.md
│   ├── ask-me/                      # 先问清楚再动手，杜绝猜测式开发
│   │   └── SKILL.md
│   ├── holiday-enough/              # 评估旅行目的地需要几天才能玩好
│   │   ├── SKILL.md
│   │   └── scripts/
│   ├── time-calc/                   # 日期时间计算与解析
│   │   ├── SKILL.md
│   │   └── references/
│   ├── anthropic-diagram/           # Anthropic 博客风格编辑型图表（.drawio）
│   │   ├── skill.md
│   │   ├── references/
│   │   └── README.md
│   ├── anthropic-svg/               # Anthropic 博客风格编辑型图表（.svg）
│   │   ├── skill.md
│   │   ├── references/
│   │   └── README.md
│   ├── clarify-first/               # [已废弃] 已迁移至 ask-me
│   │   ├── SKILL.md
│   │   └── README.md
│   └── ui-design/                   # UI 前端设计 Skill 合集
│       ├── README.md
│       ├── frontend-design/         # 核心 Skill（含 reference/）
│       ├── audit/                   # 界面质量审计
│       ├── polish/                  # 发布前最终打磨
│       └── ...                      # 其余 17 个设计命令
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

将 Skill 文件夹整体复制到对应平台的指定路径，Agent 将根据 description 自动加载，或通过 `/skill-name` 手动调用：

| 平台 | 项目级路径（当前项目）| 用户级路径（所有项目）|
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

也可以使用 [vercel-labs/skills](https://github.com/vercel-labs/skills) 提供的 CLI 工具一键安装，支持 40+ 平台，会自动检测当前环境已安装的 Agent 并写入对应路径：

```bash
# 安装本仓库中的所有 Skill
npx skills add Mrlyk/SKILLS

# 仅安装指定 Skill
npx skills add Mrlyk/SKILLS --skill skill-creator

# 安装到全局（所有项目可用）
npx skills add Mrlyk/SKILLS -g

# 安装到指定平台
npx skills add Mrlyk/SKILLS -a claude-code -a cursor
```

### 3 · 使用附属文件（如有）

部分 Skill 包含以下标准目录：

| 目录 | 用途 |
|---|---|
| `scripts/` | 可执行代码（Python、Bash 等），Skill 运行时调用 |
| `references/` | 文档资料（API 指南、示例等），Claude 按需加载 |
| `assets/` | 模板、字体、图标等静态资源，用于生成输出 |

---

## Skill 收藏库

| Skill | 描述 | 来源 |
|---|---|---|
| [skill-creator](skills/skill-creator/SKILL.md) | 创建新 Skill、修改优化已有 Skill、评测 Skill 性能 | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/skill-creator) |
| [tdd](skills/tdd/SKILL.md) | 测试驱动开发（TDD），遵循红-绿-重构循环，适用于单元测试、功能测试及测试优先开发场景 | 个人整理 |
| [canvas-design](skills/canvas-design/SKILL.md) | 根据设计哲学生成精美视觉设计，输出 .png 和 .pdf 文件，适用于海报、插画等静态视觉创作 | [anthropics/skills](https://github.com/anthropics/skills) |
| [humanizer](skills/humanizer/SKILL.md) | 去除文本中的 AI 生成痕迹，消除夸大象征、宣传性语言、AI 词汇等模式，使文本更自然 | [blader/humanizer](https://github.com/blader/humanizer) |
| [grill-me](skills/grill-me/SKILL.md) | 对方案进行结构化、无情追问，逐一解决决策树每个分支，适用于方案评审与压力测试 | 个人整理 |
| [ask-me](skills/ask-me/SKILL.md) | 执行任务前主动追问不确定点，杜绝猜测式开发，适用于需求模糊或缺少关键上下文的场景 | 个人整理 |
| [holiday-enough](skills/holiday-enough/SKILL.md) | 评估旅行目的地需要几天才能玩好，判断假期时间是否充足，给出"充裕/刚好/偏紧"评估和精简方案建议 | 个人整理 |
| [time-calc](skills/time-calc/SKILL.md) | 日期时间计算与解析，7 个原子操作覆盖当前时间、日期元信息、相对星期、日期加减、时区转换、时间戳互转，支持 macOS/Linux/Windows | 个人整理 |
| [ui-design](skills/ui-design/README.md) | UI 前端设计 Skill 合集，含核心 Skill（frontend-design）和 20 个设计命令，覆盖诊断、结构优化、视觉增强、体验层、加固完整工作流 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [anthropic-diagram](skills/anthropic-diagram/skill.md) | 生成 Anthropic 博客风格的编辑型图表，输出 .drawio 文件，温暖简洁的语义化颜色系统，支持 12 种图表模式 | 个人整理 |
| [anthropic-svg](skills/anthropic-svg/skill.md) | 生成 Anthropic 博客风格的编辑型图表，输出原生 .svg 文件，无需安装额外软件，支持 10 种图表模式 | 个人整理 |

---

## Skill 整理规范

每个 Skill 按以下约定存放在 `skills/<skill-name>/` 文件夹中：

1. `SKILL.md` — Skill 主定义文件（格式参考 [anthropics/skills](https://github.com/anthropics/skills)）
2. 附属目录（`scripts/`、`references/`、`assets/`）随原始 Skill 一并收录
3. 在上方收藏库表格中补充一行索引

---

## 许可证

本项目基于 [MIT License](LICENSE)，欢迎自由使用、修改和分享。

---

<div align="center">
Made with ❤️ by <a href="https://github.com/Mrlyk">Mrlyk</a>
</div>
