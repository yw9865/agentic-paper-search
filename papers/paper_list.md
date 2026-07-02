# Agent Memory Papers — Security & Optimization

Organized list of papers on agent memory systems (LLM agents, multi-agent
systems, RAG-based agents, etc.) relevant to **security** (e.g. memory
poisoning/injection, privacy leakage, unauthorized memory access, adversarial
persistence) or **optimization** (e.g. memory compression, retrieval
efficiency, cost/latency reduction, long-horizon memory management).

Entries are deduplicated against `seen_ids.json`. See `CHANGELOG.md` for what
was added on each run.

Format per entry:

```
### <Title>
- **arXiv**: <id> (<link>)
- **Date**: <published date>
- **Category**: Security | Optimization
- **Summary**: 1-3 sentence summary of the contribution and why it's relevant.
```

---

## Security

### Securing LLM-Agent Long-Term Memory Against Poisoning: Non-Malleable, Origin-Bound Authority with Machine-Checked Guarantees
- **arXiv**: 2606.24322 ([link](https://arxiv.org/abs/2606.24322))
- **Date**: 2026-06-23
- **Category**: Security
- **Summary**: Shows that existing memory-poisoning defenses based on content analysis or derivation history can be bypassed via laundering attacks (summarization, trusted-tool echoes, corroboration). Proposes TMA-NM, a non-malleable information-flow control system that achieves zero attack success across eight frontier models while preserving legitimate functionality.

### From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents
- **arXiv**: 2606.04329 ([link](https://arxiv.org/abs/2606.04329))
- **Date**: 2026-06-03 (v2: 2026-06-18)
- **Category**: Security
- **Summary**: Identifies four memory write channels and nine structural weaknesses across model design and system architecture, organized into a taxonomy of six attack classes. Introduces MPBench, a benchmark showing aggressive memory operations increase exploitability and that existing prompt-injection defenses don't transfer to memory poisoning.

### Defense effectiveness across architectural layers: a mechanistic evaluation of persistent memory attacks on stateful LLM agents
- **arXiv**: 2605.08442 ([link](https://arxiv.org/abs/2605.08442))
- **Date**: 2026-05-08 (v3: 2026-06-23)
- **Category**: Security
- **Summary**: Tests six defensive approaches across four architectural layers on nine open-source models against RAG-injected persistent memory attacks. Finds input/retrieval-level filtering ineffective, while tool-gating at the memory layer ("Memory Sandbox") cuts attack success rate to 0% for 8 of 9 models — though one reasoning model showed unexpected behavior inversion under this defense.

### Plant, Persist, Trigger: Sleeper Attack on Large Language Model Agents
- **arXiv**: 2605.28201 ([link](https://arxiv.org/abs/2605.28201))
- **Date**: 2026-05-27
- **Category**: Security
- **Summary**: Introduces a dormant threat where adversarial content planted via external sources sits inactive in agent memory/session context/skills across multiple interactions before a later benign query triggers it. Evaluated on 1,896 test instances across 7 LLMs, showing state-of-the-art agents remain vulnerable even when hardened against single-turn injection.

### Hidden in Memory: Sleeper Memory Poisoning in LLM Agents
- **arXiv**: 2605.15338 ([link](https://arxiv.org/abs/2605.15338))
- **Date**: 2026-05-14 (v2: 2026-05-18)
- **Category**: Security
- **Summary**: Demonstrates delayed-activation ("sleeper") memory poisoning where manipulated external content injects fabricated memories that persist across sessions. Poisoned memories drove attacker-intended actions in 60–89% of cases once retrieved.

### A Survey on Long-Term Memory Security in LLM Agents: Attacks, Defenses, and Governance Across the Memory Lifecycle
- **arXiv**: 2604.16548 ([link](https://arxiv.org/abs/2604.16548))
- **Date**: 2026-04-17 (revised 2026-06-11)
- **Category**: Security
- **Summary**: Survey introducing a "Memory Lifecycle Framework" mapping threats across six operational phases and four security dimensions. Argues for "Verifiable Memory Governance" — safeguards built into the storage layer itself rather than only at retrieval/execution time.

### Memory Poisoning Attack and Defense on Memory Based LLM-Agents
- **arXiv**: 2601.05504 ([link](https://arxiv.org/abs/2601.05504))
- **Date**: 2026-01-09 (v2: 2026-01-12)
- **Category**: Security
- **Summary**: Studies how adversaries inject harmful instructions via query-only interactions to corrupt agent long-term memory, using clinical data across multiple LLMs; finds existing legitimate memories reduce attack success. Proposes two defenses — composite trust-score moderation and memory sanitization with temporal decay filtering.

## Optimization

### MemRefine: LLM-Guided Compression for Long-Term Agent Memory
- **arXiv**: 2606.13177 ([link](https://arxiv.org/abs/2606.13177))
- **Date**: 2026-06-11
- **Category**: Optimization
- **Summary**: Compresses agent memory within a fixed storage budget using an LLM judge (rather than surface-level similarity alone) to decide whether entries should be deleted, merged, or preserved based on factual content. Shows consistent gains across multiple memory frameworks and benchmarks, especially under tight memory constraints.

### Remember the Decision, Not the Description: A Rate-Distortion Framework for Agent Memory
- **arXiv**: 2605.10870 ([link](https://arxiv.org/abs/2605.10870))
- **Date**: 2026-05-11
- **Category**: Optimization
- **Summary**: Argues memories should preserve distinctions needed for good decisions rather than descriptive accuracy, formalized via a rate-distortion framework identifying what can be safely forgotten. Introduces DeMem, an online algorithm that refines memory partitions only on detected decision conflicts, with regret guarantees and empirical validation.

### Experience Compression Spectrum: Unifying Memory, Skills, and Rules in LLM Agents
- **arXiv**: 2604.15877 ([link](https://arxiv.org/abs/2604.15877))
- **Date**: 2026-04-17 (revised 2026-06-25)
- **Category**: Optimization
- **Summary**: Unifies agent memory and skill-discovery research along a single "increasing compression" axis, showing existing systems operate at fixed compression points without adaptive cross-level support. Lays out design principles for scalable agent learning systems spanning memory, procedural skills, and declarative knowledge.

### MemMachine: A Ground-Truth-Preserving Memory System for Personalized AI Agents
- **arXiv**: 2604.04853 ([link](https://arxiv.org/abs/2604.04853))
- **Date**: 2026-04-06
- **Category**: Optimization
- **Summary**: Open-source memory architecture combining multiple memory layers with contextualized retrieval to keep personalization and factual accuracy over long interactions. Reports reduced token consumption vs. existing solutions while preserving conversational ground truth.

### Anatomy of Agentic Memory: Taxonomy and Empirical Analysis of Evaluation and System Limitations
- **arXiv**: 2602.19320 ([link](https://arxiv.org/abs/2602.19320))
- **Date**: 2026-02-22 (revised 2026-05-20)
- **Category**: Optimization
- **Summary**: Surveys memory architectures for long-horizon LLM agents and identifies that current benchmarks are underscaled and metrics misaligned with semantic utility. Highlights practical constraints (cross-model performance variability, computational overhead) that keep systems short of their theoretical potential.
