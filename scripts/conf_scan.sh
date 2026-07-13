#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_DIR"

CLAUDE_BIN="$HOME/.local/bin/claude"

LOG_DIR="$HOME/.local/state/agentic-paper-search"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/conf_$(date +%Y-%m-%d_%H%M%S).log"

"$CLAUDE_BIN" --print \
  "$(cat scripts/conf_prompt.txt)" \
  >> "$LOG_FILE" 2>&1

echo "log: $LOG_FILE"
