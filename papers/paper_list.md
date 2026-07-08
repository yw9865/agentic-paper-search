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

### Beyond Similarity: Trustworthy Memory Search for Personal AI Agents
- **arXiv**: 2606.06054 ([link](https://arxiv.org/abs/2606.06054))
- **Date**: 2026-06-04
- **Category**: Security
- **Summary**: Shows semantic-similarity-based memory retrieval can surface contextually inappropriate memories, enabling cross-domain leakage and jailbreaks. Proposes MemGate, a lightweight neural plugin that gates memory admission between vector storage and the LLM (tested on A-Mem, Mem0, MemOS) without modifying the underlying model or database.

### Opal: Private Memory for Personal AI
- **arXiv**: 2604.02522 ([link](https://arxiv.org/abs/2604.02522))
- **Date**: 2026-04-02
- **Category**: Security
- **Summary**: Confines data-dependent reasoning over agentic memory to a trusted enclave using lightweight knowledge graphs, so untrusted external storage can't observe query patterns (ORAM-style). Reports 29x higher throughput and 15x lower infrastructure cost than secure baselines — security and optimization combined in one system.

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

### ADAM: A Systematic Data Extraction Attack on Agent Memory via Adaptive Querying
- **arXiv**: 2604.09747 ([link](https://arxiv.org/abs/2604.09747))
- **Date**: 2026-04-10
- **Category**: Security
- **Summary**: Introduces ADAM, a privacy attack extracting sensitive data from LLM agent memory/retrieval systems via adaptive querying, substantially outperforming prior attacks with up to 100% attack success rate. Underscores the need for privacy protections in current agent memory designs.

### Governing Evolving Memory in LLM Agents: Risks, Mechanisms, and the Stability and Safety Governed Memory (SSGM) Framework
- **arXiv**: 2603.11768 ([link](https://arxiv.org/abs/2603.11768))
- **Date**: 2026-03-12 (revised 2026-05-19)
- **Category**: Security
- **Summary**: Proposes SSGM, a governance architecture for dynamic agent memory combining consistency verification, temporal decay modeling, and dynamic access control. Aims to prevent both unauthorized data exposure and knowledge degradation (semantic drift) during iterative memory consolidation.

### Memory Poisoning Attack and Defense on Memory Based LLM-Agents
- **arXiv**: 2601.05504 ([link](https://arxiv.org/abs/2601.05504))
- **Date**: 2026-01-09 (v2: 2026-01-12)
- **Category**: Security
- **Summary**: Studies how adversaries inject harmful instructions via query-only interactions to corrupt agent long-term memory, using clinical data across multiple LLMs; finds existing legitimate memories reduce attack success. Proposes two defenses — composite trust-score moderation and memory sanitization with temporal decay filtering.

### Unveiling Privacy Risks in LLM Agent Memory
- **arXiv**: 2502.13172 ([link](https://arxiv.org/abs/2502.13172))
- **Date**: 2025-02-17 (revised 2025-06-03)
- **Category**: Security
- **Summary**: Introduces MEXTRA, a black-box attack that extracts private user information stored in LLM agent memory modules via crafted and automatically-generated prompts. Identifies key factors driving memory leakage and argues for protective measures at the memory-access layer.

### Always-On Agents: A Survey of Persistent Memory, State, and Governance in LLM Agents
- **arXiv**: 2606.30306 ([link](https://arxiv.org/abs/2606.30306))
- **Date**: 2026-06-29
- **Category**: Security
- **Summary**: Frames agent memories, task ledgers, permissions, credentials, and audit records as a unified "persistent-state" lifecycle (write, validate, retrieve, act, update, forget, audit, rollback), scored across six diagnostic axes (authority, scope, mutability, provenance, recoverability, actionability). Based on a 435-work coded corpus, finds the literature over-indexes on accumulating/retrieving state relative to governing, recovering, or relinquishing it, and proposes the AOEP-v0 evaluation protocol to make governance and forgetting obligations measurable.

### Agents That Know Too Much: A Data-Centric Survey of Privacy in LLM Agents
- **arXiv**: 2606.26627 ([link](https://arxiv.org/abs/2606.26627))
- **Date**: 2026-06-25
- **Category**: Security
- **Summary**: Data-centric survey of privacy leakage across LLM agent surfaces — issued queries, intermediate results, written memory, and inter-agent messages — organized by data source rather than attack type. Argues information-flow control alone can't stop compositional/cross-session inference leakage and flags the lack of benchmarks that evaluate agents across multiple data surfaces (including memory) under a unified privacy policy.

### FragFuse: Bypassing Access Control of Large Language Model Agents via Memory-Based Query Fragmentation and Fusion
- **arXiv**: 2606.15609 ([link](https://arxiv.org/abs/2606.15609))
- **Date**: 2026-06-14
- **Category**: Security
- **Summary**: Shows prohibited content can be split across benign-looking memory writes and later reconstructed at read time, bypassing access controls without triggering detection. Achieves an 86.3% average bypass rate across four agent configurations and three access-control mechanisms, with existing prompt-injection detectors proving ineffective.

### Selection Integrity for LLM Graph Memory: An Accumulability Criterion for Information-Flow-Blind Retrieval
- **arXiv**: 2606.12290 ([link](https://arxiv.org/abs/2606.12290))
- **Date**: 2026-06-10
- **Category**: Security
- **Summary**: Shows provenance-based memory defenses verify record authenticity but ignore how untrusted structural edits to a memory graph can redirect which authenticated facts get retrieved (e.g. misdirecting financial transfers via Personalized-PageRank rerouting). Introduces authselect, a defense recomputing selection over only authenticated subgraphs, which blocks the attack with minimal overhead.

### Deployment-Time Memorization in Foundation-Model Agents
- **arXiv**: 2606.10062 ([link](https://arxiv.org/abs/2606.10062))
- **Date**: 2026-06-08
- **Category**: Security
- **Summary**: Characterizes agent memory design as a privacy-utility continuum (summarization intensity, retrieval scope, deletion strategy) using Personalization Recall and Adversarial Extraction Rate metrics, plus a new Forgetting Residue Score. Finds aggressive summarization cuts canary extraction 64-76% without hurting personalization, but incomplete deletion leaves ~20% of "erased" info recoverable via memory summaries.

### MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection
- **arXiv**: 2605.23723 ([link](https://arxiv.org/abs/2605.23723))
- **Date**: 2026-05-22
- **Category**: Security
- **Summary**: Combines counterfactual memory-influence scoring with structural anomaly detection to find poisoned memory records after the fact. Reduces QA-attack success from 70% to 0% and RAP-attack success from 83.3% to 0% in testing.

### State Contamination in Memory-Augmented LLM Agents
- **arXiv**: 2605.16746 ([link](https://arxiv.org/abs/2605.16746))
- **Date**: 2026-05-16
- **Category**: Security
- **Summary**: Identifies "memory laundering" — toxic/adversarial context compressed into summaries that read as safe to standard detectors while still carrying hostile framing that influences future generations. Introduces the sub-threshold propagation gap (SPG) metric and shows sanitizing before summarization is far more effective than cleaning only the final summary.

### MemMorph: Tool Hijacking in LLM Agents via Memory Poisoning
- **arXiv**: 2605.26154 ([link](https://arxiv.org/abs/2605.26154))
- **Date**: 2026-05-24
- **Category**: Security
- **Summary**: Injects records disguised as technical documentation/policy into agent long-term memory to steer tool-selection toward attacker-preferred (malicious) tools. Achieves up to 85.9% attack success with only three injected records and remains effective against tested defenses.

### Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents
- **arXiv**: 2604.02623 ([link](https://arxiv.org/abs/2604.02623))
- **Date**: 2026-04-03 (v2: 2026-04-07)
- **Category**: Security
- **Summary**: Introduces eTAMP, the first web-agent memory-poisoning attack achieving cross-session, cross-site compromise without needing direct memory access — a single manipulated page view can silently contaminate memory and later trigger malicious behavior on an unrelated site. Finds more capable models (e.g. GPT-5-mini) are not more secure, and attack success rises under environmental stress.

### Trojan Hippo: Weaponizing Agent Memory for Data Exfiltration
- **arXiv**: 2605.01970 ([link](https://arxiv.org/abs/2605.01970))
- **Date**: 2026-05-03 (v3: 2026-05-15)
- **Category**: Security
- **Summary**: Plants a dormant instruction via a single untrusted source (e.g. a crafted email) that persists in agent memory and activates later when the user discusses sensitive topics, exfiltrating data. An adaptive red-teaming benchmark across four memory architectures finds 85-100% attack success against frontier models; tested defenses cut this to 0-5% but at varying utility cost.

### AgentLeak: A Benchmark for Internal-Channel Privacy Leakage in Multi-Agent LLM Systems
- **arXiv**: 2602.11510 ([link](https://arxiv.org/abs/2602.11510))
- **Date**: 2026-02-12
- **Category**: Security
- **Summary**: Argues output-only privacy audits miss leakage through inter-agent messages, shared memory, and function parameters. Across 1,000 scenarios and five commercial LLMs, finds multi-agent setups actually reduce final-output leakage (27.2% vs 43.2% single-agent) but overall system vulnerability rises to 68.9% once internal channels are counted — output-only evaluation misses 41.7% of breaches.

### SuperLocalMemory: Privacy-Preserving Multi-Agent Memory with Bayesian Trust Defense Against Memory Poisoning
- **arXiv**: 2603.02240 ([link](https://arxiv.org/abs/2603.02240))
- **Date**: 2026-02-17
- **Category**: Security
- **Summary**: Local-first (no cloud, no LLM calls) multi-agent memory system defending against poisoning via architectural isolation and Bayesian trust scoring, with per-agent provenance and adaptive re-ranking. Reports 72% trust-score degradation for sleeper-style attacks, 10.6ms median search latency, and GDPR Article 17 deletion support.

### Remembering More, Risking More: Longitudinal Safety Risks in Memory-Equipped LLM Agents
- **arXiv**: 2605.17830 ([link](https://arxiv.org/abs/2605.17830))
- **Date**: 2026-05-18
- **Category**: Security
- **Summary**: Introduces "temporal memory contamination" — memory-equipped agents accumulate risk across many independent, individually benign interactions, with violation rates rising as exposure length grows. Tests eight memory architectures across three deployment scenarios and argues memory safety must be evaluated longitudinally, not as a single-state snapshot.

### KidnapRAG: A Black-Box Attack for Hijacking Reasoning in Agentic Retrieval-Augmented Generation Systems
- **arXiv**: 2607.00422 ([link](https://arxiv.org/abs/2607.00422))
- **Date**: 2026-07-01
- **Category**: Security
- **Summary**: Introduces a black-box poisoning attack against Agentic RAG using three role-specific injected documents (an attention-grabbing bait, a query-redirecting chain-link, and a false-evidence document) to hijack the agent's iterative retrieval-and-reasoning loop without needing access to the query, memory store, or system internals. Shows that the iterative re-retrieval agentic RAG relies on for robustness can itself be exploited to progressively bias the agent toward attacker-controlled evidence, outperforming prior poisoning techniques under realistic black-box constraints.

### ElephantAgent: Contextual State Continuity in Agentic Systems
- **arXiv**: 2607.01919 ([link](https://arxiv.org/abs/2607.01919))
- **Date**: 2026-07-02
- **Category**: Security
- **Summary**: Proposes a defense protocol against tool- and memory-poisoning attacks by maintaining a trusted-hardware-backed, verifiable ledger of authorized state transitions, detecting out-of-band tampering, and providing "Historical Traceability" for post-hoc auditing and rollback to validated states. A concrete architectural countermeasure to the "poison now, exploit later" sleeper-style memory-poisoning pattern common in the recent attack literature.

### Forensic Trajectory Signatures for Agent Memory Poisoning Detection
- **arXiv**: 2606.30566 ([link](https://arxiv.org/abs/2606.30566))
- **Date**: 2026-06-29
- **Category**: Security
- **Summary**: Finds that memory-poisoning/exfiltration attacks leave detectable tool-call trajectory signatures — e.g. a `memory_recall_fact` → `email_send_email` transition that benign sessions rarely exhibit — because the attack's information-retrieval requirements force this pattern. A random-forest classifier over 19 trajectory features reaches AUC=0.9904 across nine models (7B-120B) without retraining, and a prefix-only variant (AUC=0.934) enables real-time detection distinguishing memory-channel attacks from ordinary prompt injection using tool-call logs alone.

### Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses
- **arXiv**: 2607.05029 ([link](https://arxiv.org/abs/2607.05029))
- **Date**: 2026-07-06
- **Category**: Security
- **Summary**: Introduces FARMA, an attack that poisons agent memory by injecting forged *reasoning traces* (not just factual entries) written in evasive language to slip past existing defenses. Proposes SENTINEL, a detection pipeline whose Reasoning Guard analyzes stored entries for authenticity, reporting near-perfect defense with zero false positives on benign traces — extending memory-poisoning defense from factual knowledge to the agent's reasoning history.

### PiSAs: Benchmarking Contextual Integrity in Multi-User Agentic Systems
- **arXiv**: 2607.05318 ([link](https://arxiv.org/abs/2607.05318))
- **Date**: 2026-07-06
- **Category**: Security
- **Summary**: Introduces PiSAs, a benchmark for unintentional privacy leaks in multi-user agentic systems, arguing sensitive information can leak not only through outputs to external recipients but internally across users via inter-agent messages and shared memory. Finds state-of-the-art LLMs struggle to reliably filter sensitive content or enforce access restrictions across these channels, extending contextual-integrity evaluation to the shared-memory leakage surface.

### MemLeak: Diagnosing Information Leaks in Multimodal Agent Memory
- **arXiv**: 2606.29788 ([link](https://arxiv.org/abs/2606.29788))
- **Date**: 2026-06-29
- **Category**: Security
- **Summary**: Shows that multimodal agents fail to fully forget deleted facts because the information remains recoverable from retained images via implicit visual cues in the vision-language model. Introduces an Information Provenance Graph framework and the MemLeak benchmark, demonstrating cross-modal privacy leakage where retained images enable 12.0% recovery of supposedly deleted text.

### When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration
- **arXiv**: 2606.28958 ([link](https://arxiv.org/abs/2606.28958))
- **Date**: 2026-06-27
- **Category**: Security
- **Summary**: Demonstrates that when collaborating agents share hidden KV-cache states alongside visible messages, a malicious agent can corrupt the latent memory to force wrong answers while keeping its visible commitments plausible, bypassing text-only verification. Proposes HMAC-SHA256 manifests to authenticate the opaque latent-memory transport channel.

### MEMPROBE: Probing Long-Term Agent Memory via Hidden User-State Recovery
- **arXiv**: 2606.24595 ([link](https://arxiv.org/abs/2606.24595))
- **Date**: 2026-06-23
- **Category**: Security
- **Summary**: Treats agent memory as an auditable artifact and measures how much hidden user state can be reconstructed from it after the agent provides assistance, reconstructing user attributes against ground truth. Shows memory-borne user-state recovery is a distinct privacy risk separate from task performance, stabilizing around 0.6 across memory systems.

### Governed Shared Memory for Multi-Agent LLM Systems
- **arXiv**: 2606.24535 ([link](https://arxiv.org/abs/2606.24535))
- **Date**: 2026-06-23
- **Category**: Security
- **Summary**: Formalizes four failure modes of shared memory in multi-agent LLM systems and proposes systems-level governance primitives — scoped retrieval, temporal supersession, provenance tracking, and policy-based propagation — implemented in a production service (MemClaw). Argues long-context retrieval alone is insufficient and that explicit access-control/governance mechanisms are required to prevent cross-agent leakage and stale-state propagation.

## Optimization

### Auditing Forgetting in Limited Memory Language Models
- **arXiv**: 2607.00605 ([link](https://arxiv.org/abs/2607.00605))
- **Date**: 2026-07-01
- **Category**: Optimization
- **Summary**: Introduces a causal auditing framework (FULL/DEL-ON/DEL-OFF interventions) that decomposes post-deletion behavior in externalized-memory (RAG-style) LLMs into parametric leakage, retrieval-mediated correctness, and retrieval-artifact rate, tested across 12,228 alias-closure deletions in 13 databases. Finds parametric leakage is near-zero but deleted facts commonly resurface via near-neighbor retrieval (0.7-13.6% depending on database design) — meaning the database's own topology, not the model, governs whether deletion actually holds.

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

### Onyx: Cost-Efficient Disk-Oblivious ANN Search
- **arXiv**: 2604.20401 ([link](https://arxiv.org/abs/2604.20401))
- **Date**: 2026-04-22
- **Category**: Optimization
- **Note**: _Adjacent infrastructure, not agent-specific_ — general-purpose oblivious approximate-nearest-neighbor search, not framed around LLM agents. Included as relevant retrieval infrastructure for vector-backed agent memory stores.
- **Summary**: Combines a compact intermediate representation that prunes bandwidth-intensive accesses with a locality-aware shallow tree design to reduce bandwidth and access counts for privacy-preserving ANN search on untrusted infrastructure. Reports significantly lower cost/latency than prior oblivious ANN approaches — relevant to any vector-store-backed agent memory needing confidential retrieval.

### Mandol: An Agglomerative Agent Memory System for Long-Term Conversations
- **arXiv**: 2606.29778 ([link](https://arxiv.org/abs/2606.29778))
- **Date**: 2026-06-29
- **Category**: Optimization
- **Summary**: Proposes a unified "memory-native" architecture (SemanticMap + SemanticGraph) that fuses key-value, vector, and graph structures to eliminate cross-database I/O, paired with LLM-free query-adaptive routing, denoising/conflict resolution, and token-budget-constrained context generation. Achieves the best overall accuracy among representative long-term agent memory systems on the LoCoMo and LongMemEval benchmarks.

### Neural Procedural Memory: Empowering LLM Agents with Implicit Activation Steering
- **arXiv**: 2606.29824 ([link](https://arxiv.org/abs/2606.29824))
- **Date**: 2026-06-29
- **Category**: Optimization
- **Summary**: Represents agent procedural memory as compact implicit activation-steering vectors distilled from past experience, instead of verbose explicit textual instructions, reducing memory representation overhead. Training-free method matches instruction-based memory across four agent benchmarks and improves further when combined with explicit memory.

### What Memory Do GUI Agents Really Need? From Passive Records to Active Task-Driving States
- **arXiv**: 2606.31612 ([link](https://arxiv.org/abs/2606.31612))
- **Date**: 2026-06-30
- **Category**: Optimization
- **Summary**: Introduces Active Task-Driving Memory (ATMem), which tracks each memory item's current functional status (pending/used/stale) rather than treating memory as a passive log, plus STR-GRPO, an online RL method that learns when invoking memory is actually worth its cost. Targets duplicated or overlooked actions caused by unmanaged long-horizon memory in mobile GUI agents.

### HyphaeDB: A Living Knowledge Topology for Agent-First Memory
- **arXiv**: 2606.28781 ([link](https://arxiv.org/abs/2606.28781))
- **Date**: 2026-06-27
- **Category**: Optimization
- **Summary**: Reimagines HNSW vector-index topology as a gossip-based communication fabric for multi-agent memory sharing, with agents as graph nodes and "memory diffs" propagated for emergent contradiction detection and consensus formation. Single-author preprint (PostgreSQL/pgvector implementation) proposing agent-native memory infrastructure as an alternative to passive, per-agent vector stores.

### Control-Plane Placement Shapes Forgetting: An Architectural Study of Agent Memory Across Thirteen System Configurations
- **arXiv**: 2606.15903 ([link](https://arxiv.org/abs/2606.15903))
- **Date**: 2026-06-14 (v2: 2026-06-16)
- **Category**: Optimization
- **Summary**: Benchmarks 13 memory-pipeline configurations on 385 adversarial forgetting cases via a new suite (ForgetEval), finding deterministic methods fail canonicalization, LLM-based inscription-time approaches nail canonicalization but miss intent-aware deletion, and mutation-time hooks perform best overall (91.7-93.2%). Confirms production memory systems suffer more from forgetting failures than recall failures, despite benchmarks emphasizing recall.

### Are We Ready For An Agent-Native Memory System?
- **arXiv**: 2606.24775 ([link](https://arxiv.org/abs/2606.24775))
- **Date**: 2026-06-23
- **Category**: Optimization
- **Summary**: Empirically evaluates 12 memory systems plus two baselines across 5 benchmark workloads/11 datasets, breaking memory into representation/storage, extraction, retrieval/routing, and maintenance. Finds no single design wins universally, and that localized maintenance is more cost-efficient than global reorganization.

### ContextSniper: AntTrail's Token-Efficient Code Memory for Repository-Level Program Repair
- **arXiv**: 2607.01916 ([link](https://arxiv.org/abs/2607.01916))
- **Date**: 2026-07-02
- **Category**: Optimization
- **Summary**: A memory layer for coding agents that ranks and filters repository context (files, search results, terminal output) through an "intention-aware context gate" to produce compact evidence packets instead of raw whole-file reads. Cuts tokens 51.5% (OpenClaw) / 38.9% (Claude Code) on SWE-bench Lite with only a modest resolution-rate drop.

### Active Context Compression: Autonomous Memory Management in LLM Agents
- **arXiv**: 2601.07190 ([link](https://arxiv.org/abs/2601.07190))
- **Date**: 2026-01-12
- **Category**: Optimization
- **Summary**: Introduces Focus, letting coding agents self-manage context by autonomously consolidating key insights into a persistent "Knowledge" block and discarding stale history, rather than relying on external summarization. On SWE-bench Lite, cuts tokens 22.7% (up to 57% on some tasks) with identical accuracy.

### Eywa: Provenance-Grounded Long-Term Memory for AI Agents
- **arXiv**: 2605.30771 ([link](https://arxiv.org/abs/2605.30771))
- **Date**: 2026-05-29
- **Category**: Optimization
- **Summary**: Separates immutable source evidence from derived facts and uses a deterministic retrieval path requiring zero LLM calls at read time, improving auditability and update/deletion support over systems that conflate evidence and belief. Reports 90.19% accuracy on LoCoMo and 88.2% on LongMemEval-S.

### Mem-π: Adaptive Memory through Learning When and What to Generate
- **arXiv**: 2605.21463 ([link](https://arxiv.org/abs/2605.21463))
- **Date**: 2026-05-20
- **Category**: Optimization
- **Summary**: Replaces similarity-based memory retrieval with a model that learns to generate concise task-specific guidance on demand — and to abstain when generation wouldn't help — via reinforcement learning, avoiding unnecessary retrieval overhead. Shows over 30% relative improvement on web-navigation tasks.

### Imprint: Online Memory Compression for Long-Horizon Egocentric QA
- **arXiv**: 2607.00696 ([link](https://arxiv.org/abs/2607.00696))
- **Date**: 2026-07-01
- **Category**: Optimization
- **Summary**: Reframes long-horizon egocentric agent memory as online compression rather than summarization, organizing observations into explicit, recurring "Interaction Records" selected via recurrence/recency/distinctiveness signals instead of collapsing them into coarse textual summaries. On the 7-day EgoLifeQA benchmark, improves accuracy 31.0%→35.8%, cuts memory footprint 2.3x, and reduces retrieval latency 11.8x versus EgoRAG.

### Memory Depth, Not Memory Access: Selective Parametric Consolidation for Long-Running Language Agents
- **arXiv**: 2606.26806 ([link](https://arxiv.org/abs/2606.26806))
- **Date**: 2026-06-25
- **Category**: Optimization
- **Summary**: Distinguishes retrieval-based "memory access" from parametrically-encoded "memory depth" (durable goal-oriented behavior), introducing a loop-drift protocol and EVAF, a surprise/valence-gated LoRA consolidation mechanism. Finds retrieval wins on factual recall while EVAF wins on goal persistence and post-context-loss recovery using only 2-3 parameter updates per 200 events.

### Self-GC: Self-Governing Context for Long-Horizon LLM Agents
- **arXiv**: 2607.00692 ([link](https://arxiv.org/abs/2607.00692))
- **Date**: 2026-07-01
- **Category**: Optimization
- **Summary**: Treats an agent's accumulated tool results, files, plans, and constraints as indexed, recoverable context objects rather than a disposable text suffix, using a side-channel planner to propose fold/mask/prune actions with safe commit boundaries. Prunes ~44% of prefix tokens while preserving ~85% of future-continuation correctness (vs. 55-70% for heuristic baselines), and cuts production daytime input tokens 10-20%.

### AutoMem: Automated Learning of Memory as a Cognitive Skill
- **arXiv**: 2607.01224 ([link](https://arxiv.org/abs/2607.01224))
- **Date**: 2026-07-01
- **Category**: Optimization
- **Summary**: Frames LLM memory management (what to encode, when to retrieve, how to organize) as a trainable "metamemory" skill, using file-system operations as first-class memory actions plus two automated optimization loops that jointly refine memory structure and the model's memory proficiency. Improves performance ~2-4x across three procedurally generated game environments (Crafter, MiniHack, NetHack) without changing task-action behavior.

### Memory-Orchestrated Semantic System (MOSS): An Auditable Agentic Memory Architecture
- **arXiv**: 2607.04391 ([link](https://arxiv.org/abs/2607.04391))
- **Date**: 2026-07-05
- **Category**: Optimization
- **Summary**: Proposes an auditable agent memory architecture that stores and queries information through a relational database with structured indexes rather than vector embeddings, logging every operation for "auditable, sovereign, structurally unbounded" memory. Demonstrated via a year-long production deployment managing a scholar's 44-million-token corpus, arguing auditability and reproducibility (not just speed/scale) are preconditions for long-lived agent memory.

### PLACEMEM: Toward a Compute-Aware Memory Plane for Lifelong Agents
- **arXiv**: 2607.04089 ([link](https://arxiv.org/abs/2607.04089))
- **Date**: 2026-07-05
- **Category**: Optimization
- **Summary**: Represents agent memory as versioned "capsules" unifying semantics, provenance, validity, and reusable runtime state, enabling persistent, correction-aware memory without redundant recomputation of prior history. Prototype is a vLLM-based control plane with persistent capsule state, invalidation, and routing — a compute-aware memory plane targeting efficiency for lifelong agents.

### SelfMem: Self-Optimizing Memory for AI Agents
- **arXiv**: 2607.03726 ([link](https://arxiv.org/abs/2607.03726))
- **Date**: 2026-07-04
- **Category**: Optimization
- **Summary**: Lets agents autonomously develop and refine their own memory strategies via memory tools plus feedback, instead of following predefined storage/retrieval heuristics. On the BEAM benchmark reports 40.8-48.7% gains over retrieval and compression baselines across conversation scales from 100K to 1M tokens.

### A-TMA: Decoupling State-Aware Memory Failures in Long-Term Agent Memory
- **arXiv**: 2607.01935 ([link](https://arxiv.org/abs/2607.01935))
- **Date**: 2026-07-02
- **Category**: Optimization
- **Summary**: Targets "ghost memory" — the failure where outdated, current, and transitional facts coexist in memory and mislead agents. Proposes ATMA, a state-aware overlay that keeps separate records per state, builds evidence packets by state, and explicitly labels temporal information; on the new LTP benchmark it improves handling of conflicting-fact scenarios over baselines.

### When Not to Write Memory: Governing False Promotion from Correlated Agent Traces
- **arXiv**: 2607.02579 ([link](https://arxiv.org/abs/2607.02579))
- **Date**: 2026-06-30
- **Category**: Optimization
- **Summary**: Argues agents should sometimes refrain from writing memory, since repeated observations across traces often reflect shared sources (copied content, common prompts, stale data) rather than independent evidence. Proposes GovMem, a dependency-aware write policy that distinguishes genuine corroboration from correlated noise, sharply reducing false memory promotion while keeping useful writes.

### Selective Memory Retention for Long-Horizon LLM Agents
- **arXiv**: 2606.29178 ([link](https://arxiv.org/abs/2606.29178))
- **Date**: 2026-06-28
- **Category**: Optimization
- **Summary**: Introduces TraceRetain, a bounded-memory framework that scores entries by interpretable features (age, frequency, specificity) and evicts the lowest-scoring ones. Shows selective forgetting is most valuable under noisy data streams, preserving task performance even at 75% contamination while cutting the memory footprint on constrained systems.

### Forget to Improve: On-Device LLM-Agent Continual Learning via Budget-Curated Memory
- **arXiv**: 2606.25115 ([link](https://arxiv.org/abs/2606.25115))
- **Date**: 2026-06-23
- **Category**: Optimization
- **Summary**: Proposes a unified "net-value-per-byte" score governing the memory lifecycle for on-device agents: evicting low-value entries within RAM/energy budgets, selectively sharing insights only when benefit exceeds transmission cost, and gating untrusted peer entries. Reports 2.7x lower memory footprint, 2.4x lower uplink usage, and injection-attack success driven to zero while maintaining accuracy.
