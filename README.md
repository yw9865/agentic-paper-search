# Agentic Paper Search

Automated tracker for research papers on **agent memory** systems, focused on
**security** and **optimization** angles (e.g. memory poisoning, privacy leakage,
retrieval/compression efficiency, cost reduction, long-context memory optimization).

A scheduled cloud agent searches arXiv and the web daily, adds newly found
papers to [`papers/paper_list.md`](papers/paper_list.md), and tracks which
papers have already been seen in [`papers/seen_ids.json`](papers/seen_ids.json)
so it only reports genuinely new ones each run.

## Structure

- `papers/paper_list.md` — organized, human-readable list of papers (grouped by topic)
- `papers/seen_ids.json` — machine-readable dedup index (arXiv IDs / stable URLs already recorded)
- `papers/CHANGELOG.md` — log of what was added on each run
