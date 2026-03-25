# 语雀 MCP 安装配置执行指南

本文档是给 AI 工具的执行指令，按步骤主动运行命令，不要只描述步骤。
需要用户手动操作的步骤会单独标注，遇到时告知用户并等待其确认后再继续。

---

## 第一步：检查 utoo-proxy 是否已安装

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

## 第二步：注入 MCP 配置

使用 SKILL.md 第一步已确认的启动脚本路径，执行：

- **若用户已告知当前使用的 AI 工具**，将工具名映射为 `--tool` 参数后执行：

  | 工具 | 对应参数 |
  |---|---|
  | Claude Code | `--tool claude` |
  | Codex | `--tool codex` |
  | Cursor | `--tool cursor` |
  | Qoder | `--tool qoder` |
  | QoderWork | `--tool qoderwork` |
  | CoPaw | `--tool copaw` |
  | VSCode | `--tool vscode` |

  ```bash
  sh <第一步确认的 run_configure_mcp.sh 路径> --tool <对应参数值>
  ```

- **若用户未指定工具**，直接执行（脚本将自动检测并安装 Claude Code / Codex / Cursor）：

  ```bash
  sh <第一步确认的 run_configure_mcp.sh 路径>
  ```

启动脚本会自动选择可用的 Python 3 解释器，然后调用 `configure_mcp.py` 完成配置。

---

## 第三步：首次浏览器授权

**此步骤需要用户手动完成。** 告知用户以下内容后等待其确认：

> 请重启当前 AI 工具，重启后会自动弹出浏览器授权页面，在授权页面完成登录后告诉我已完成。

用户确认授权完成后继续第四步。

---

## 第四步：验证连接

调用 `skylark_user_info` 验证连接：

- 返回用户信息 → 配置成功，更新主记忆说明语雀 MCP 已可用
- 仍然报错 → 检查是情况 B（MCP 未注册）还是情况 C（鉴权失败），按 SKILL.md 中的分支处理
