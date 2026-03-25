#!/usr/bin/env sh

set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PYTHON_BIN=""

if command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_MAJOR=$(python - <<'PY'
import sys
print(sys.version_info[0])
PY
)
  if [ "$PYTHON_MAJOR" = "3" ]; then
    PYTHON_BIN="python"
  fi
fi

if [ -z "$PYTHON_BIN" ]; then
  echo "[错误] 未找到可用的 Python 3 解释器，请先安装 python3 后重试。"
  exit 1
fi

exec "$PYTHON_BIN" "$SCRIPT_DIR/configure_mcp.py" "$@"
