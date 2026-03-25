---
name: yuque-ali
description: 阿里语雀文档读写工具。当用户需要读取、搜索、创建、更新语雀文档，查看知识库列表，或需要安装和配置语雀 MCP 时使用。触发词包括：「查一下语雀」「语雀上有没有」「帮我在语雀写」「帮我记到语雀上」「存到语雀」「更新一下语雀文档」「把这个写进语雀」「语雀上那篇文档」「去语雀找一下」「语雀文档」「配置语雀 MCP」「安装语雀」「语雀知识库」「语雀搜索」以及任何涉及阿里内部语雀平台的文档操作。
---

# 语雀 MCP（阿里内部）

## 第零步：确认当前使用的 AI 工具

如果无法自动确认当前使用的 AI 工具，则询问用户："您目前在哪个 AI 工具里执行本次操作？（Claude Code / Codex / Cursor / Qoder / CoPaw / QoderWork / 其他）"

根据回答，按以下顺序查找脚本（`<proj>` 为当前项目目录，即当前工作目录）：

1. `<proj>/.<工具目录>/skills/yuque-ali/scripts/configure_mcp.py`（项目级工具目录）
2. `<proj>/skills/yuque-ali/scripts/configure_mcp.py`（项目级通用目录）
3. `~/<工具目录>/skills/yuque-ali/scripts/configure_mcp.py`（用户级）

各工具的 `<工具目录>` 对应关系：

| 工具 | 项目级工具目录 | 用户级目录 |
|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Codex | `.codex/skills/` | `~/.codex/skills/` |
| Cursor | `.cursor/skills/` | `~/.cursor/skills/` |
| Qoder | `.qoder/skills/` | `~/.qoder/skills/` |
| QoderWork | — | `~/.qoderwork/skills/` |
| CoPaw | — | `~/.copaw/workspaces/default/customized_skills/` |
| 其他 | — | 请用户提供完整路径 |

依次执行 `ls <path>` 确认脚本存在，找到第一个有效路径即停止，记住该路径后续使用。

## 第一步：判断连接状态

使用前先调用 `skylark_user_info` 探测 MCP 连接状态：

**情况 A：调用成功** → 直接进入操作，读 `references/mcp-tools.md` 了解工具用法

**情况 B：工具不存在（MCP 未注册）** → 读 `references/setup.md`，**主动使用 Shell 工具逐步执行每一步**，不要只是描述步骤或告知用户去操作

**情况 C：工具存在但返回鉴权错误或连接失败** → 不要认为是没安装好。utoo-proxy 首次运行或 token 过期时需要浏览器重新授权，提示用户：

> utoo-proxy 需要浏览器授权。请在有图形界面的终端里手动运行一次 utoo-proxy，完成浏览器登录后重试。
>
> 运行命令：`~/.utoo-proxy/utoo-proxy`（路径以实际安装位置为准，可用 `which utoo-proxy` 查找）

授权完成后重新调用 `skylark_user_info` 验证，成功再继续。

## 第二步：执行操作

连接正常后，读 `references/mcp-tools.md` 了解 17 个 MCP 工具的 API 名称、参数和常见操作链路。
