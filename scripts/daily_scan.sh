#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_DIR"

LOG_DIR="$HOME/.local/state/agentic-paper-search"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/$(date +%Y-%m-%d_%H%M%S).log"

claude --print \
  "$(cat scripts/daily_prompt.txt)" \
  >> "$LOG_FILE" 2>&1

echo "log: $LOG_FILE"
