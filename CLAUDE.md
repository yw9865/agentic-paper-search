# agentic-paper-search

Tracks research papers on **agent memory** (LLM/multi-agent/RAG memory systems)
relevant to **security** (poisoning, privacy leakage, unauthorized access) or
**optimization** (compression, retrieval efficiency, forgetting policies).

- `papers/paper_list.md` — organized list, grouped under `## Security` / `## Optimization`
- `papers/seen_ids.json` — arXiv-ID dedup index; authoritative memory of what's recorded
- `papers/CHANGELOG.md` — dated log of what was added each run

## Daily automation (local cron, not cloud)

A cloud routine (`RemoteTrigger`) was tried first but can't be used here: the
GitHub connection required for a cloud routine to push commits is blocked by
the team owner's connector policy. So this runs entirely on the local
machine instead — meaning **it only fires while this machine is on**.

**Crontab entry** (`crontab -l` to verify, `crontab -e` to edit):
```
0 9 * * * /home/yongwan/Workspace/agentic-paper-search/scripts/daily_scan.sh
```
Runs daily at 9:00 AM Asia/Seoul. If missing (e.g. after an OS reinstall or
`crontab -r`), recreate it with:
```
(crontab -l 2>/dev/null; echo "0 9 * * * /home/yongwan/Workspace/agentic-paper-search/scripts/daily_scan.sh") | crontab -
```

**What it does** (`scripts/daily_scan.sh` → `claude --print` with `scripts/daily_prompt.txt`):
reads `seen_ids.json`, searches arXiv/web for new on-topic papers, verifies
each against its abstract page, appends new entries, updates the changelog,
commits + pushes to `origin/main`, and emails a summary via
`scripts/send_email.py` if anything new was found. Logs land in
`~/.local/state/agentic-paper-search/`.

**Permissions**: scoped in `.claude/settings.local.json` (gitignored, local
machine only — recreate manually if lost): file edits limited to `papers/**`,
Bash limited to `git add/commit/push/status/diff` and running
`scripts/send_email.py`. No blanket Bash/Write access. If this file is
missing, the daily cron job will silently fail its file/git operations —
check `~/.local/state/agentic-paper-search/*.log` if papers stop updating.

**Email credentials**: live outside this repo at
`~/.config/agentic-paper-search/email.env` (SMTP_USER, SMTP_APP_PASSWORD,
SMTP_TO — Gmail app password). Never committed. If missing, recreate using
the template at `~/.config/agentic-paper-search/email.env.template`.

A cloud routine ("Agent Memory Paper Scan") exists on claude.ai but is
**disabled** — it was the original attempt before the connector restriction
was discovered, kept only as a dormant fallback shell.
