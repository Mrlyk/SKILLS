# 语雀 MCP 安装配置执行指南

本文档是给 Claude 的执行指令，按步骤主动运行命令，不要只描述步骤。
需要用户手动操作的步骤会单独标注，遇到时告知用户并等待其确认后再继续。

---

## 第一步：检查 utoo-proxy 是否已安装

执行以下命令：

```bash
which utoo-proxy || ls ~/.utoo-proxy/utoo-proxy 2>/dev/null
```

- 有输出 → utoo-proxy 已安装，记录路径，跳到第二步
- 无输出 → 执行第一步安装

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

使用 SKILL.md 第零步已确认的脚本路径，执行：

```bash
python <第零步确认的 configure_mcp.py 路径>
```

脚本会自动检测已安装的 AI 工具并列出配置计划，**在脚本提示"继续？(y/n)"时，将提示内容展示给用户，等待用户输入 y 或 n 后再继续。**

---

## 第三步：首次浏览器授权

**此步骤需要用户手动完成。** 告知用户以下内容后等待其确认：

> utoo-proxy 首次运行需要浏览器登录授权。请在**有图形界面的终端**里手动执行以下命令，完成浏览器登录后告诉我已完成：
>
> ```bash
> ~/.utoo-proxy/utoo-proxy
> ```
>
> 如路径不对，先运行 `which utoo-proxy` 确认实际位置。
>
> 注意：此步骤不能在无头服务器或纯 SSH 环境里完成。

用户确认授权完成后继续第四步。

---

## 第四步：验证连接

告知用户重启对应的 AI 工具后，调用 `skylark_user_info` 验证连接：

- 返回用户信息 → 配置成功，更新主记忆说明语雀 MCP 已可用
- 仍然报错 → 检查是情况 B（MCP 未注册）还是情况 C（鉴权失败），按 SKILL.md 中的分支处理
