# Changelog

Log of paper additions from each scheduled run. Newest first.

---

## 2026-07-04 (scheduled scan)

Searched arXiv (cs.AI, cs.CL, cs.CR, cs.LG, cs.MA) and the web for new agent-memory papers published/revised in the last 3 days. Found 3 new, verified, on-topic papers.

**Security (2):**
- KidnapRAG: A Black-Box Attack for Hijacking Reasoning in Agentic RAG Systems (2607.00422) — 2026-07-01
- ElephantAgent: Contextual State Continuity in Agentic Systems (2607.01919) — 2026-07-02

**Optimization (1):**
- Auditing Forgetting in Limited Memory Language Models (2607.00605) — 2026-07-01

## 2026-07-03 (scheduled scan)

Searched arXiv (cs.AI, cs.CL, cs.CR, cs.LG, cs.MA) and the web for new agent-memory papers. Only one paper fell inside the strict last-3-days window (2026-06-30 to 2026-07-03: ContextSniper, 2607.01916), so the search was widened, which surfaced a substantial backlog of clearly on-topic, previously-untracked papers from Feb–Jun 2026 that earlier runs' searches had missed. All 17 were individually verified against their arXiv abstract pages before inclusion. 17 new papers confirmed and added.

**Security (11):**
- FragFuse: Bypassing Access Control of LLM Agents via Memory-Based Query Fragmentation and Fusion (2606.15609) — 2026-06-14
- Selection Integrity for LLM Graph Memory (2606.12290) — 2026-06-10
- Deployment-Time Memorization in Foundation-Model Agents (2606.10062) — 2026-06-08
- MemAudit: Post-hoc Auditing of Poisoned Agent Memory (2605.23723) — 2026-05-22
- State Contamination in Memory-Augmented LLM Agents (2605.16746) — 2026-05-16
- MemMorph: Tool Hijacking in LLM Agents via Memory Poisoning (2605.26154) — 2026-05-24
- Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents / eTAMP (2604.02623) — 2026-04-03
- Trojan Hippo: Weaponizing Agent Memory for Data Exfiltration (2605.01970) — 2026-05-03
- AgentLeak: A Benchmark for Internal-Channel Privacy Leakage in Multi-Agent LLM Systems (2602.11510) — 2026-02-12
- SuperLocalMemory: Privacy-Preserving Multi-Agent Memory with Bayesian Trust Defense (2603.02240) — 2026-02-17
- Remembering More, Risking More: Longitudinal Safety Risks in Memory-Equipped LLM Agents (2605.17830) — 2026-05-18

**Optimization (6):**
- Control-Plane Placement Shapes Forgetting / ForgetEval (2606.15903) — 2026-06-14
- Are We Ready For An Agent-Native Memory System? (2606.24775) — 2026-06-23
- ContextSniper: Token-Efficient Code Memory for Repository-Level Program Repair (2607.01916) — 2026-07-02
- Active Context Compression: Autonomous Memory Management in LLM Agents / Focus (2601.07190) — 2026-01-12
- Eywa: Provenance-Grounded Long-Term Memory for AI Agents (2605.30771) — 2026-05-29
- Mem-π: Adaptive Memory through Learning When and What to Generate (2605.21463) — 2026-05-20

**Near-misses considered and excluded:**
- Memory Contagion: Cross-Temporal Propagation of Evaluator Bias via Agent Memory (2606.23195, 2026-06-22) — bias-propagation phenomenon through shared memory, not an adversarial poisoning/privacy attack or a compression/efficiency technique.

## 2026-07-02 (scheduled scan)

Searched arXiv (cs.AI, cs.CL, cs.CR, cs.LG, cs.MA) and the web for new agent-memory papers, focused on the last ~3 days (2026-06-29 to 2026-07-02), with two clearly relevant papers included just outside that window (2026-06-25, 2026-06-27). 6 new papers confirmed and added.

**Security (2):**
- Always-On Agents: A Survey of Persistent Memory, State, and Governance in LLM Agents (2606.30306) — 2026-06-29
- Agents That Know Too Much: A Data-Centric Survey of Privacy in LLM Agents (2606.26627) — 2026-06-25

**Optimization (4):**
- Mandol: An Agglomerative Agent Memory System for Long-Term Conversations (2606.29778) — 2026-06-29
- Neural Procedural Memory: Empowering LLM Agents with Implicit Activation Steering (2606.29824) — 2026-06-29
- What Memory Do GUI Agents Really Need? From Passive Records to Active Task-Driving States (2606.31612) — 2026-06-30
- HyphaeDB: A Living Knowledge Topology for Agent-First Memory (2606.28781) — 2026-06-27

**Near-misses considered and excluded:**
- MemDelta: Controlled Baselines and Hidden Confounds in Agent Memory Evaluation (2606.29914, 2026-06-29) — benchmarking-methodology critique, not itself an attack or optimization technique.
- Analytic Concept-Centric Memory for Agentic Embodied Manipulation (2606.29774, 2026-06-29) — robotics/embodied-manipulation memory, different subfield from textual/RAG agent memory security or optimization.
- DMV-Bench: Diagnosing Long-Horizon Multimodal Agents' Visual Memory with Incidental Cue Injection (2606.27499, 2026-06-25) — visual-memory retention robustness benchmark, not a privacy/poisoning attack or a compression/efficiency method.
- CogniFold: Always-On Proactive Memory via Cognitive Folding (2605.13438, latest revision 2026-06-17) — outside the recency window.
- Governed Shared Memory for Multi-Agent LLM Systems (2606.24535, 2026-06-23) and Forget to Improve (2606.25115, 2026-06-23) — relevant but outside the recency window; left for a future run if still novel then.

## 2026-07-02 (user-submitted, single paper)

- Opal: Private Memory for Personal AI (2604.02522) — confirmed on-topic, ORAM-style trusted-enclave memory for agentic systems combining privacy and efficiency gains.

## 2026-07-02 (user-submitted batch)

User submitted 6 candidates to verify; 5 confirmed and added, 1 skipped as off-topic.

**Security (4):**
- ADAM: A Systematic Data Extraction Attack on Agent Memory via Adaptive Querying (2604.09747)
- Governing Evolving Memory in LLM Agents / SSGM (2603.11768)
- Beyond Similarity: Trustworthy Memory Search for Personal AI Agents / MemGate (2606.06054)
- Unveiling Privacy Risks in LLM Agent Memory / MEXTRA (2502.13172)

**Optimization (1, flagged as adjacent infra):**
- Onyx: Cost-Efficient Disk-Oblivious ANN Search (2604.20401) — general oblivious ANN search, not agent-specific; included at user's request as retrieval infra relevant to vector-backed agent memory.

**Skipped:**
- USENIX Security '25 "Found in Translation: A Generative Language Modeling Approach to Memory Access Pattern Attacks" (jia-grace) — about OS-level memory-paging side-channel attacks, not LLM agent memory. Keyword-collision false positive.

## 2026-07-02 (manual seed run)

Seeded the tracker with 12 papers found via arXiv/web search, covering agent
memory security (poisoning/injection attacks and defenses) and optimization
(compression, retrieval efficiency, forgetting policies) published Jan–Jun 2026.

**Security (7):**
- Securing LLM-Agent Long-Term Memory Against Poisoning (2606.24322)
- From Untrusted Input to Trusted Memory (2606.04329)
- Defense effectiveness across architectural layers (2605.08442)
- Plant, Persist, Trigger: Sleeper Attack on LLM Agents (2605.28201)
- Hidden in Memory: Sleeper Memory Poisoning in LLM Agents (2605.15338)
- A Survey on Long-Term Memory Security in LLM Agents (2604.16548)
- Memory Poisoning Attack and Defense on Memory Based LLM-Agents (2601.05504)

**Optimization (5):**
- MemRefine: LLM-Guided Compression for Long-Term Agent Memory (2606.13177)
- Remember the Decision, Not the Description (2605.10870)
- Experience Compression Spectrum (2604.15877)
- MemMachine: A Ground-Truth-Preserving Memory System (2604.04853)
- Anatomy of Agentic Memory (2602.19320)
