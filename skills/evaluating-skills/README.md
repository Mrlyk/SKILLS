# evaluating-skills · Claude Code SKILL 评测器

> 一句话：**对照 Anthropic 三份权威 best practices 给一份 SKILL.md 打分**，6 维度评分 + 扣分原文证据 + before/after 改写建议，让团队 SKILL 质量有客观尺度。

## 一、价值

- **从主观到客观**：人审一份 SKILL 至少 30 分钟，每个人标准还不一样。本 skill 10 秒出结构化分数 + 改写建议，团队 PR review 直接对齐
- **规则有出处**：每条扣分都引用 Anthropic 官方 docs / agentskills.io / Anthropic Skill Building Guide 原句，不是 LLM 主观打分
- **可追溯**：每条扣分都附 SKILL.md 的逐字原文证据 + 改写前/后对比示例

## 二、使用方式

### 安装

```bash
npx ali-skills add liaoyikang.liaoyik/skills --skill evaluating-skills
```

### 触发

直接在对话里说，**用户必须显式触发**（不会在普通编辑 SKILL.md 时自动跳出）：

| 提问示例 | 输入方式 |
|---|---|
| `帮我评估一下这个 SKILL ~/.claude/skills/foo/SKILL.md` | 给路径 |
| `这个 SKILL 写得怎么样？路径在 ~/.claude/skills/bar/SKILL.md` | 给路径 |
| `帮我看看这个 SKILL 有什么问题`（粘贴 SKILL.md 全文）| 直接粘贴 |
| `这个 SKILL 能打多少分？`（粘贴 SKILL.md 全文）| 直接粘贴 |

### 输出格式

```
# SKILL.md 评测报告

**审查对象**: `~/.claude/skills/foo/SKILL.md`
**总分**: 78/100（良好）

## 维度评分
| # | 维度 | 分数 | Critical | Warn | Info |
| 1 | 元数据 | 100/100 | 0 | 0 | 0 |
| 2 | 上下文占用 | 70/100 | 1 | 0 | 0 |
| 3 | 指令设计 | ... | ... |
...

## Critical 违规
### description 含第一人称代词 [维度: 元数据]
**原文证据**: > description: "I help you analyze..."
**违反原因**: ...
**建议改写**:
<修改前> I help you analyze ...
<修改后> Analyzes ... when the user asks ...
```

## 三、原理

### 评分模型

- **6 维度**，每维度 100 分起扣，扣到 0 封底
- **severity 权重**：critical -30 / warn -10 / info -3
- **总分** = 6 维度分数的算术平均，四舍五入

### 6 维度（中英对照）

| # | 中文 | English | 关注点 |
|---|------|---------|--------|
| 1 | 元数据 | Metadata | frontmatter / `name` / `description` / 命名规范 |
| 2 | 上下文占用 | Context Budget | 篇幅、冗余、时间敏感、不写常识 |
| 3 | 指令设计 | Instruction Design | 精度匹配脆弱度、给默认而非菜单、过程式优于陈述式 |
| 4 | 结构与渐进式披露 | Structure & Disclosure | 引用一级深度、长文件目录、按需加载 |
| 5 | 指令模式 | Patterns | gotchas / 输出模板 / checklist / 校验循环 / 脚本打包 |
| 6 | 反模式 | Anti-patterns | Windows 路径、魔数、术语不一致、推卸给 Claude 等 |

### Top 10 强规则（每次必查）

1. **命名合规**：`SKILL.md`（区分大小写）+ folder/`name` kebab-case + 不以 `claude` 等保留字开头
2. **description 含 WHAT + WHEN 双要素**
3. **description 含具体触发短语**（用户真实会说的话）
4. **description 不用第一/第二人称代词**叙述自身能力
5. **description 硬约束**：≤800 字符、不含 XML `<>`、非空
6. **SKILL.md ≤ 5000 字 且 ≤ 500 行**
7. **不含时间敏感语句**（"2025 年前"等）
8. **skill 文件夹内不含 README.md**（注：本 README 是分发用的"商品介绍页"，安装后建议放仓库根目录而非 skill 目录内）
9. **强序 workflow 不应覆盖多意图** / 硬约束与流程混叙要拆分
10. **抽象指令应改为可执行命令**（`python scripts/x.py` > "validate the data"）

### 规则来源

本 skill 对照以下三份权威指南打分：

1. [Anthropic 官方 SKILL 最佳实践（中文）](https://platform.claude.com/docs/zh-CN/agents-and-tools/agent-skills/best-practices)
2. [agentskills.io · Skill Creation Best Practices](https://agentskills.io/skill-creation/best-practices)
3. [The Complete Guide to Building Skills for Claude (PDF)](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)

## 四、完整示例

以下是对 [skills/humanizer/SKILL.md](../humanizer/SKILL.md) 的一次真实评测输出，可作为报告形态的参考。

````markdown
# SKILL.md 评测报告

**审查对象**: `/Users/liaoyikang/Personal/SKILLS_github/skills/humanizer/SKILL.md`
**总分**: **93/100**（优秀 — 可直接发布）
**评测时间**: 2026-04-15 10:00

## 维度评分

| # | 维度 | 分数 | Critical | Warn | Info |
|---|------|------|----------|------|------|
| 1 | 元数据 | 97/100 | 0 | 0 | 1 |
| 2 | 上下文占用 | 87/100 | 0 | 1 | 1 |
| 3 | 指令设计 | 97/100 | 0 | 0 | 1 |
| 4 | 结构与渐进式披露 | 80/100 | 0 | 2 | 0 |
| 5 | 指令模式 | 100/100 | 0 | 0 | 0 |
| 6 | 反模式 | 97/100 | 0 | 0 | 1 |

## Critical 违规

（无）

## Warn 违规

### 工作流指令重复三份 [维度: 上下文占用]

**原文证据**（引自 SKILL.md）：
> ## Your Task
> When given text to humanize:
> 1. **Identify AI patterns** - Scan for the patterns listed below
> 2. **Rewrite problematic sections** - Replace AI-isms with natural alternatives
> ...
> ## Process
> 1. Read the input text carefully
> 2. Identify all instances of the patterns above
> 3. Rewrite each problematic section
> ...
> ## Output Format
> Provide:
> 1. Draft rewrite
> 2. "What makes the below so obviously AI generated?" (brief bullets)

**违反原因**：「Your Task」「Process」「Output Format」三个小节描述的是同一个执行流程，仅粒度不同。重复占用上下文预算，且让模型难以判断哪份是权威版本。

**建议改写**：
```
保留「Your Task」的 6 步高层流程 + 「Output Format」的 4 项交付物列表。
---
删除「## Process」整节（第 393-408 行），合并进「Your Task」的 6 步中。
最终只剩两个小节：Your Task（做什么）+ Output Format（交付什么）。
```

### 488 行长文未做渐进式披露 [维度: 结构与渐进式披露]

**原文证据**：
> ## CONTENT PATTERNS
> ### 1. Undue Emphasis on Significance, Legacy, and Broader Trends
> ...
> ### 24. Generic Positive Conclusions

**违反原因**：24 个 pattern 全部平铺于主 SKILL.md，488 行 / 3386 词。Anthropic 渐进式披露原则要求主文件只保留触发与总览，详细 pattern 库应迁入 `references/patterns.md`。

**建议改写**：
```
主 SKILL.md 保留：frontmatter + Your Task + Output Format + 全流程示例。
Pattern 库保留一个带分类标题的索引表（1 行描述 + 链接）。
---
新建 references/patterns-content.md（含 pattern 1-6）
新建 references/patterns-language.md（含 pattern 7-12）
新建 references/patterns-style.md（含 pattern 13-18）
新建 references/patterns-communication.md（含 pattern 19-24）
主文件指令改为：「识别疑似 pattern 后，Read references/patterns-<类别>.md 查阅 before/after 示例」。
```

### 接近 500 行但无目录 [维度: 结构与渐进式披露]

**原文证据**：
> # Humanizer: Remove AI Writing Patterns
> You are a writing editor that identifies and removes signs of AI-generated text...
> ## Your Task

**违反原因**：文件达到 488 行，已逼近 Anthropic 建议的 500 行硬上限，但首部无 TOC / 章节索引。读者与 LLM 都难以定位到具体 pattern。

**建议改写**：
```
H1 下直接进入 "Your Task"。
---
在 H1 下补一个目录：

## Sections
- [Your Task](#your-task)
- [Personality and Soul](#personality-and-soul)
- [Content Patterns (1-6)](#content-patterns)
- [Language and Grammar Patterns (7-12)](#language-and-grammar-patterns)
- [Style Patterns (13-18)](#style-patterns)
- [Communication Patterns (19-21)](#communication-patterns)
- [Filler and Hedging (22-24)](#filler-and-hedging)
- [Full Example](#full-example)
```

## Info 违规

- [元数据] frontmatter 含 `version: 2.2.0` 字段，Anthropic 官方 spec 未定义该字段，建议删除或移入 CHANGELOG。
- [上下文占用] 第 163 行 "These words appear far more frequently in post-2023 text" 属弱时间锚点，随时间推移会显得陈旧，可改为 "in LLM-generated text"。
- [指令设计] 第 32 行 "Add soul — Don't just remove bad patterns; inject actual personality" 过于抽象，虽在下文 PERSONALITY AND SOUL 节展开，但放在 6 步高层任务列表中显得空洞。
- [反模式] 第 22 行 "You are a writing editor that identifies and removes signs..." 采用角色扮演式开场，Anthropic 更推荐祈使式指令（"Identify and remove..."）。
````

---

