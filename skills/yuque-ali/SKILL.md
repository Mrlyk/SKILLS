---
name: yuque-ali
description: 阿里语雀文档读写工具。当用户需要读取、搜索、创建、更新语雀文档，查看知识库列表，或需要安装和配置语雀 MCP 时使用。触发词包括：「查一下语雀」「语雀上有没有」「帮我在语雀写」「帮我记到语雀上」「存到语雀」「更新一下语雀文档」「把这个写进语雀」「语雀上那篇文档」「去语雀找一下」「语雀文档」「配置语雀 MCP」「安装语雀」「语雀知识库」「语雀搜索」以及任何涉及阿里内部语雀平台的文档操作。
---

# 语雀 MCP（阿里内部）

## 第一步：确认当前使用的 AI 工具

你知道自己运行在哪个 AI 工具中（如 Claude Code、Cursor、VSCode、Codex、Qoder、CoPaw、QoderWork 等），直接根据自身身份确定当前工具类型，无需询问用户。仅当无法确定时才询问。

根据回答，按以下顺序查找启动脚本（`<proj>` 为当前项目目录，即当前工作目录）：

1. `<proj>/.<工具目录>/skills/yuque-ali/scripts/run_configure_mcp.sh`（项目级工具目录）
2. `<proj>/skills/yuque-ali/scripts/run_configure_mcp.sh`（项目级工具目录）
3. `~/<工具目录>/skills/yuque-ali/scripts/run_configure_mcp.sh`（用户级）

各工具的 `<工具目录>` 对应关系：

| 工具 | 项目级工具目录 | 用户级目录 |
|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Codex | `.codex/skills/` | `~/.codex/skills/` |
| Cursor | `.cursor/skills/` | `~/.cursor/skills/` |
| VScode | `.github/skills/` | `~/.github/skills/` |
| Qoder | `.qoder/skills/` | `~/.qoder/skills/` |
| QoderWork | — | `~/.qoderwork/skills/` |
| CoPaw | — | `~/.copaw/workspaces/default/customized_skills/` |
| 其他 | — | 请用户提供完整路径 |

**Cursor / VSCode / Qoder 额外兜底：** 若按上述顺序均未找到脚本，还需额外检查 `~/.claude/skills/yuque-ali/scripts/run_configure_mcp.sh`，因为 Cursor/VSCode/Qoder 原生加载 `~/.claude` 目录下的 skills。

依次执行 `ls <path>` 确认脚本存在，找到第一个有效路径即停止，记住该路径后续使用。

## 第二步：判断连接状态

使用前先调用 `skylark_user_info` 探测 MCP 连接状态：

**情况 A：调用成功** → 直接进入操作，读 `references/mcp-tools.md` 了解工具用法

**情况 B：工具不存在（MCP 未注册）** → 读 `references/setup.md`，**主动使用 Shell 工具逐步执行每一步**，不要只是描述步骤或告知用户去操作

**情况 C：工具存在但返回鉴权错误或连接失败** → 不要认为是没安装好。utoo-proxy 首次运行或 token 过期时需要浏览器重新授权，提示用户：

> 请重启当前 AI 工具，重启后会自动弹出浏览器授权页面，在授权页面完成登录后即可继续使用。

授权完成后重新调用 `skylark_user_info` 验证，成功再继续。

## 第三步：执行操作

连接正常后，读 `references/mcp-tools.md` 了解 17 个 MCP 工具的 API 名称、参数和常见操作链路。

**URL 域名注意：** 调用 `skylark_resolve_url` 时，`url` 参数必须使用 `yuque.antfin.com` 域名。若用户提供的链接是 `aliyuque.antfin.com` 开头，先将域名替换为 `yuque.antfin.com` 再传入，否则会报参数校验错误。
