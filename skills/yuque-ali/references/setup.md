# 语雀 MCP 安装配置执行指南

本文档是安装分支的执行指令。按步骤主动运行命令，不要只描述步骤。
需要用户手动操作的步骤会单独标注，遇到时告知用户并等待其确认后再继续。

## 第一步：确定当前 AI 工具并定位启动脚本

先根据自身身份判断当前工具类型；仅当无法确定时才询问用户。

当前工具类型已确定后，按以下顺序查找启动脚本（`<proj>` 为当前项目目录，即当前工作目录）：

1. `<proj>/.<工具目录>/skills/yuque-ali/scripts/run_configure_mcp.sh`
2. `<proj>/skills/yuque-ali/scripts/run_configure_mcp.sh`
3. `~/<工具目录>/skills/yuque-ali/scripts/run_configure_mcp.sh`

各工具的 `<工具目录>` 对应关系：

| 工具 | 项目级工具目录 | 用户级目录 | `--tool` 参数 |
|---|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` | `claude` |
| Codex | `.codex/skills/` | `~/.codex/skills/` | `codex` |
| Cursor | `.cursor/skills/` | `~/.cursor/skills/` | `cursor` |
| VSCode | `.github/skills/` | `~/.github/skills/` | `vscode` |
| Qoder | `.qoder/skills/` | `~/.qoder/skills/` | `qoder` |
| QoderWork | — | `~/.qoderwork/skills/` | `qoderwork` |
| CoPaw | — | `~/.copaw/workspaces/default/customized_skills/` | `copaw` |
| 其他 | — | 请用户提供完整路径 | — |

**Cursor / VSCode / Qoder 额外兜底：** 若按上述顺序均未找到脚本，还需额外检查 `~/.claude/skills/yuque-ali/scripts/run_configure_mcp.sh`。

依次执行 `ls <path>` 确认脚本存在，找到第一个有效路径即停止。

---

## 第二步：检查 utoo-proxy 是否已安装

执行以下命令：

```bash
which utoo-proxy || ls ~/.utoo-proxy/utoo-proxy 2>/dev/null
```

- 有输出 → utoo-proxy 已安装，记录路径，跳到第二步
- 无输出 → 执行以下安装命令

**安装 utoo-proxy（macOS / Linux）：**

```bash
curl -L -o- https://registry.antgroup-inc.cn/@alipay/utoo-proxy/latest/files/setup.sh | bash
```

**安装 utoo-proxy（Windows PowerShell）：**

```powershell
Invoke-WebRequest -Uri 'https://registry.antgroup-inc.cn/@alipay/utoo-proxy/latest/files/setup.ps1' -UseBasicParsing -OutFile setup.ps1; powershell.exe -ExecutionPolicy Bypass -File setup.ps1; rm setup.ps1
```

安装后执行以下命令确认路径：

```bash
which utoo-proxy || echo ~/.utoo-proxy/utoo-proxy
```

---

## 第三步：注入 MCP 配置

使用第一步已确认的启动脚本路径执行配置：

- **若当前工具类型已确定**，映射为 `--tool <name>` 后执行：

  ```bash
  sh <第一步确认的 run_configure_mcp.sh 路径> --tool <对应参数值>
  ```

- **仅当当前工具类型无法确定**，才允许不带 `--tool` 执行，回退到默认安装 Claude Code / Codex / Cursor：

  ```bash
  sh <第一步确认的 run_configure_mcp.sh 路径>
  ```

## 第四步：浏览器授权

**此步骤需要用户手动完成。** 告知用户以下内容后等待其确认：

- **Claude Code / Codex：** 请重启当前 AI 工具，重启后会自动弹出浏览器授权页面，在授权页面完成登录后告诉我已完成。
- **其他工具（Cursor / VSCode / Qoder / QoderWork / CoPaw）：** 请在自动弹出的授权页面完成登录后告诉我已完成，无需重启。

用户确认授权完成后继续第五步。

## 第五步：验证连接

调用 `skylark_user_info` 验证连接：

- 返回用户信息 → 配置成功，更新主记忆说明语雀 MCP 已可用
- 仍然报错 → 检查是情况 B（MCP 未注册）还是情况 C（鉴权失败），按 SKILL.md 中的分支处理
