# agentic-paper-search

Tracks research papers on **agent memory** (LLM/multi-agent/RAG memory systems)
relevant to **security** (poisoning, privacy leakage, unauthorized access) or
**optimization** (compression, retrieval efficiency, forgetting policies).

- `papers/paper_list.md` — organized list, grouped under `## Security` / `## Optimization`
- `papers/seen_ids.json` — arXiv-ID dedup index; authoritative memory of what's recorded (daily arXiv scan only)
- `papers/conf_seen.json` — dedup index for conference papers (USENIX Security, IEEE S&P); kept separate from `seen_ids.json` so the two scans never clobber each other
- `papers/CHANGELOG.md` — dated log of what was added each run (shared by both scans; conference entries are prefixed `[Conference scan]`)

## Daily automation (local cron, not cloud)

A cloud routine (`RemoteTrigger`) was tried first but can't be used here: the
GitHub connection required for a cloud routine to push commits is blocked by
the team owner's connector policy. So this runs entirely on the local
machine instead — meaning **it only fires while this machine is on**.

**Crontab entries** (`crontab -l` to verify, `crontab -e` to edit):
```
0 9 * * * /data/yongwan/agentic-paper-search/scripts/daily_scan.sh
30 9 * * 1 /data/yongwan/agentic-paper-search/scripts/conf_scan.sh
```
The daily arXiv scan runs at 9:00 AM Asia/Seoul; the weekly conference scan runs
Mondays at 9:30 AM (offset 30 min so the daily run's commit/push finishes first).
If missing (e.g. after an OS reinstall or `crontab -r`), recreate them with:
```
(crontab -l 2>/dev/null; echo "0 9 * * * /data/yongwan/agentic-paper-search/scripts/daily_scan.sh"; echo "30 9 * * 1 /data/yongwan/agentic-paper-search/scripts/conf_scan.sh") | crontab -
```

**What it does** (`scripts/daily_scan.sh` → `claude --print` with `scripts/daily_prompt.txt`):
reads `seen_ids.json`, searches arXiv/web for new on-topic papers, verifies
each against its abstract page, appends new entries, updates the changelog,
commits + pushes to `origin/main`, and emails a summary via
`scripts/send_email.py` if anything new was found. Logs land in
`~/.local/state/agentic-paper-search/`.

**Weekly conference scan** (`scripts/conf_scan.sh` → `claude --print` with
`scripts/conf_prompt.txt`): continuous tracking of security-conference proceedings
(currently **USENIX Security** and **IEEE S&P / Oakland**), which publish in rolling
per-cycle batches rather than a daily stream — hence weekly, not daily. Reads
`conf_seen.json` (plus `seen_ids.json` and existing `paper_list.md` titles to avoid
re-adding a paper already tracked via its arXiv preprint), fetches each venue's official
accepted-papers pages, filters **strictly** to agent-memory papers (these are broad
security venues, so most papers are off-topic and a zero-result week is normal), appends
venue-aware entries to `paper_list.md`, records them in `conf_seen.json`, updates the
changelog, commits + pushes, and emails only if something new was added. Same
email/git/log infrastructure as the daily scan; conference logs are prefixed `conf_` in
`~/.local/state/agentic-paper-search/`. No new permissions needed in
`.claude/settings.local.json` — it reuses the same `papers/**` + git + `send_email.py`
scopes as the daily scan.

Conference-scan gotcha (first hit 2026-07-13): **USENIX returns HTTP 403 to a direct
`WebFetch`.** `conf_prompt.txt` therefore instructs a fallback via the `https://r.jina.ai/<url>`
reader proxy and tells the scan to flag an unreachable venue in the CHANGELOG rather than
silently reporting "no new papers". If USENIX coverage ever goes quiet, check the
`conf_*.log` for 403s and confirm the proxy fallback still resolves.

**Cron-environment gotchas already hit once (2026-07-03) — the 9am run
silently failed until these were fixed:**
- `scripts/daily_scan.sh` calls the **absolute path** `~/.local/bin/claude`,
  not bare `claude` — cron's minimal `PATH` doesn't include `~/.local/bin`.
  If `claude` binary location ever changes, update `CLAUDE_BIN` in the script.
- Git push uses a **dedicated SSH deploy key** (`~/.ssh/agentic_paper_search_deploy`,
  passphrase-less, write-access deploy key on this repo only — added at
  https://github.com/yw9865/agentic-paper-search/settings/keys), routed via
  an SSH config alias in `~/.ssh/config`:
  ```
  Host github-agentic-paper-search
    HostName github.com
    User git
    IdentityFile ~/.ssh/agentic_paper_search_deploy
    IdentitiesOnly yes
  ```
  The repo's `origin` remote points at `git@github-agentic-paper-search:...`
  (not the default `github.com` host) so it doesn't depend on your personal
  key or a running ssh-agent, which cron doesn't have access to. If push
  ever fails in cron logs with a publickey error, check `git remote -v`
  still points at the alias, and that the deploy key is still listed (with
  write access) on GitHub.
- Always sanity-check by simulating cron's environment before trusting a
  fix: `env -i HOME="$HOME" PATH="/usr/bin:/bin" bash scripts/daily_scan.sh`.

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
