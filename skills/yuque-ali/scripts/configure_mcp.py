#!/usr/bin/env python3
"""
configure_mcp.py — 为已安装的 AI 工具注入语雀 MCP 配置

用法：
  python configure_mcp.py              # 自动检测并配置所有已安装工具
  python configure_mcp.py --tool cursor  # 只配置指定工具
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

YUQUE_MCP_URL = (
    "https://mcpgwoffice-prod.alipay.com/mcpgw/v1/shttpproxy/message/"
    "MAIN_CHAIR_mcp.ant.faas.skylarkmcpserver.skylarkmcpserver"
)
SERVER_NAME = "yuque-ali"

MCPSERVERS_ENTRY = {
    "type": "stdio",
    "command": "",  # 运行时填入 utoo_path
    "args": [YUQUE_MCP_URL, "-t", "STREAMABLE_HTTP"],
}

COPAW_ENTRY = {
    "name": SERVER_NAME,
    "description": "阿里语雀文档读写 MCP",
    "enabled": True,
    "transport": "stdio",
    "url": "",
    "headers": {},
    "command": "",  # 运行时填入 utoo_path
    "args": [YUQUE_MCP_URL, "-t", "STREAMABLE_HTTP"],
    "env": {},
    "cwd": "",
}


# ── utoo-proxy 路径探测 ──────────────────────────────────────────────────────

def find_utoo_proxy() -> str:
    """返回 utoo-proxy 可执行文件的绝对路径，找不到则退出。"""
    # 1. PATH 里找
    result = shutil.which("utoo-proxy")
    if result:
        return result
    # 2. 默认安装目录
    default = Path.home() / ".utoo-proxy" / "utoo-proxy"
    if default.exists():
        return str(default)
    print("[错误] 未找到 utoo-proxy，请先完成安装。")
    print("  macOS/Linux: curl -L -o- https://registry.antgroup-inc.cn/@alipay/utoo-proxy/latest/files/setup.sh | bash")
    sys.exit(1)


# ── 工具检测 ─────────────────────────────────────────────────────────────────

def detect_tools() -> dict:
    """
    返回 {tool_name: True/False} 表示工具是否已安装。
    按"工具本身是否安装"判断，不依赖配置文件是否存在。
    """
    tools = {}

    tools["claude"] = bool(shutil.which("claude"))
    tools["codex"] = bool(shutil.which("codex"))
    tools["cursor"] = (Path.home() / ".cursor").is_dir()

    vscode_app = Path("/Applications/Visual Studio Code.app")
    tools["vscode"] = bool(shutil.which("code")) or vscode_app.exists()

    tools["qoder"] = (Path.home() / "Library" / "Application Support" / "Qoder").is_dir()
    tools["qoderwork"] = (Path.home() / ".qoderwork").is_dir()
    tools["copaw"] = (Path.home() / ".copaw").is_dir()

    return tools


# ── 已配置检测 ────────────────────────────────────────────────────────────────

def is_already_configured_json(config_path: Path, key_path: list) -> bool:
    """检查 JSON 文件中 key_path 路径下是否已有 SERVER_NAME。"""
    if not config_path.exists():
        return False
    try:
        data = json.loads(config_path.read_text(encoding="utf-8"))
        node = data
        for k in key_path:
            node = node.get(k, {})
        return SERVER_NAME in node
    except Exception:
        return False


def is_already_configured_cli(tool: str) -> bool:
    """检查 CLI 工具是否已注册 SERVER_NAME。"""
    try:
        cmd = ["claude", "mcp", "list"] if tool == "claude" else ["codex", "mcp", "list"]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        return SERVER_NAME in result.stdout
    except Exception:
        return False


# ── JSON 配置注入 ─────────────────────────────────────────────────────────────

def backup_and_write_json(config_path: Path, data: dict):
    """写入前备份，然后写入新内容。"""
    if config_path.exists():
        bak = config_path.with_suffix(config_path.suffix + ".bak")
        shutil.copy2(config_path, bak)
        print(f"  已备份：{bak}")
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def configure_mcpservers_json(config_path: Path, utoo_path: str, tool_label: str):
    """向标准 mcpServers 格式的 JSON 文件注入配置。"""
    if is_already_configured_json(config_path, ["mcpServers"]):
        print(f"  [{tool_label}] 已配置 {SERVER_NAME}，跳过")
        return

    data = {}
    if config_path.exists():
        try:
            data = json.loads(config_path.read_text(encoding="utf-8"))
        except Exception:
            pass

    entry = dict(MCPSERVERS_ENTRY)
    entry["command"] = utoo_path
    data.setdefault("mcpServers", {})[SERVER_NAME] = entry
    backup_and_write_json(config_path, data)
    print(f"  [{tool_label}] 配置成功 → {config_path}")


def configure_copaw(utoo_path: str):
    """向 CoPaw agent.json 的 mcp.clients 注入配置。"""
    config_path = Path.home() / ".copaw" / "workspaces" / "default" / "agent.json"

    if is_already_configured_json(config_path, ["mcp", "clients"]):
        print(f"  [CoPaw] 已配置 {SERVER_NAME}，跳过")
        return

    if not config_path.exists():
        print(f"  [CoPaw] 未找到配置文件 {config_path}，跳过")
        return

    try:
        data = json.loads(config_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"  [CoPaw] 读取配置失败：{e}，跳过")
        return

    entry = dict(COPAW_ENTRY)
    entry["command"] = utoo_path
    data.setdefault("mcp", {}).setdefault("clients", {})[SERVER_NAME] = entry
    backup_and_write_json(config_path, data)
    print(f"  [CoPaw] 配置成功 → {config_path}")


def configure_cli(tool: str, utoo_path: str):
    """通过 CLI 命令注入配置。"""
    if is_already_configured_cli(tool):
        print(f"  [{tool}] 已配置 {SERVER_NAME}，跳过")
        return

    if tool == "claude":
        cmd = [
            "claude", "mcp", "add",
            "--transport", "stdio",
            SERVER_NAME,
            "--",
            utoo_path,
            YUQUE_MCP_URL,
            "-t", "STREAMABLE_HTTP",
        ]
    else:  # codex
        cmd = [
            "codex", "mcp", "add",
            SERVER_NAME,
            "--",
            utoo_path,
            YUQUE_MCP_URL,
            "-t", "STREAMABLE_HTTP",
        ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print(f"  [{tool}] 配置成功")
        else:
            print(f"  [{tool}] 配置失败：{result.stderr.strip()}")
    except Exception as e:
        print(f"  [{tool}] 执行命令失败：{e}")


# ── 主流程 ────────────────────────────────────────────────────────────────────

TOOL_CONFIGS = {
    "claude": lambda utoo: configure_cli("claude", utoo),
    "codex":  lambda utoo: configure_cli("codex", utoo),
    "cursor": lambda utoo: configure_mcpservers_json(
        Path.home() / ".cursor" / "mcp.json", utoo, "Cursor"
    ),
    "vscode": lambda utoo: configure_mcpservers_json(
        Path.home() / "Library" / "Application Support" / "Code" / "User" / "mcp.json",
        utoo, "VSCode"
    ),
    "qoder": lambda utoo: configure_mcpservers_json(
        Path.home() / "Library" / "Application Support" / "Qoder" / "SharedClientCache" / "mcp.json",
        utoo, "Qoder"
    ),
    "qoderwork": lambda utoo: configure_mcpservers_json(
        Path.home() / ".qoderwork" / "mcp.json", utoo, "QoderWork"
    ),
    "copaw":  lambda utoo: configure_copaw(utoo),
}

TOOL_LABELS = {
    "claude": "Claude Code",
    "codex":  "Codex",
    "cursor": "Cursor",
    "vscode": "VSCode",
    "qoder":     "Qoder",
    "qoderwork": "QoderWork",
    "copaw":  "CoPaw",
}


def main():
    parser = argparse.ArgumentParser(description="为已安装的 AI 工具注入语雀 MCP 配置")
    parser.add_argument(
        "--tool",
        choices=list(TOOL_CONFIGS.keys()),
        help="只配置指定工具（claude/codex/cursor/vscode/qoder/qoderwork/copaw）",
    )
    args = parser.parse_args()

    utoo_path = find_utoo_proxy()
    print(f"utoo-proxy 路径：{utoo_path}\n")

    # 确定要配置的工具列表
    DEFAULT_TOOLS = ["claude", "codex", "cursor"]

    if args.tool:
        targets = {args.tool: True}
    else:
        detected = detect_tools()
        targets = {k: True for k in DEFAULT_TOOLS if detected.get(k)}

        if not targets:
            print("[错误] 未检测到 Claude Code、Codex 或 Cursor。")
            print(f"请使用 --tool 明确指定，可选值：{' / '.join(TOOL_CONFIGS.keys())}")
            print("示例：python configure_mcp.py --tool cursor")
            sys.exit(1)

    labels = [TOOL_LABELS[t] for t in targets]
    print("即将配置以下工具：" + "、".join(labels))
    print()
    for tool in targets:
        TOOL_CONFIGS[tool](utoo_path)

    print("\n完成。请重启对应的 AI 工具使配置生效。")
    print("首次使用时 utoo-proxy 会弹出浏览器授权页面，请在有图形界面的终端里完成登录。")


if __name__ == "__main__":
    main()
