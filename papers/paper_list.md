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
- **Venue**: USENIX Security 2026
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

### When Claws Remember but Do Not Tell: Stealthy Memory Injection in Persistent Personal Agents
- **arXiv**: 2607.05189 ([link](https://arxiv.org/abs/2607.05189))
- **Date**: 2026-07-06
- **Category**: Security
- **Summary**: Introduces "stealth memory injection," where a single malicious email causes a persistent personal agent to secretly write a fabricated fact or preference into its long-term memory while keeping the user-facing response innocuous. Proposes WhisperBench (108 test cases across five risk categories) and MemGhost, a reward-guided payload generator, achieving 87.5% attack success against OpenClaw/GPT-5.4 and 71.4% against Claude Code SDK/Sonnet 4.6 despite existing defenses.

### When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents
- **arXiv**: 2607.06595 ([link](https://arxiv.org/abs/2607.06595))
- **Date**: 2026-07-06
- **Category**: Security
- **Summary**: Introduces GhostWriter, a two-phase (injection then activation) memory-poisoning attack against LLM personal assistants with long-term memory, reaching ~98% injection success and ~60% activation rates. Proposes Agentic Memory Sentry (AM-Sentry), a memory-governance defense that substantially reduces attack effectiveness while preserving agent functionality.

### StateFuse: Deterministic Conflict-Preserving Memory for Multi-Agent Systems
- **arXiv**: 2607.05844 ([link](https://arxiv.org/abs/2607.05844))
- **Date**: 2026-07-07
- **Category**: Security
- **Summary**: Argues that collapsing conflicting observations across multi-agent branches/replicas via silent overwrites hides tampering and disagreement. Proposes a conflict-aware replicated memory contract (standard OpSet/CRDT merge, immutable history, explicit conflict objects) that surfaces contradictions rather than resolving them early, enabling safer abstention and correction — a memory-integrity/auditability mechanism for multi-agent memory.

### The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory
- **arXiv**: 2607.10608 ([link](https://arxiv.org/abs/2607.10608))
- **Date**: 2026-07-12
- **Category**: Security
- **Summary**: Studies how agents behave when retrieved memory conflicts with the task (the downstream failure mode of poisoned/stale memory), tracing where memory first changes an action, whether the change carries forward, and whether the agent recovers. Using WebArena and a new MemTrapBench, finds agents tend to "comply" with the conflicting memory at the first decision point and then collapse to a low success floor, with stronger models losing more absolute capability — arguing retrieval-quality/final-success metrics miss this reliability risk.

### Agents Don't Just Agree, They Remember: Benchmarking Persistent Sycophancy in Stateful Personal Agents
- **arXiv**: 2607.10526 ([link](https://arxiv.org/abs/2607.10526))
- **Date**: 2026-07-12
- **Category**: Security
- **Summary**: Introduces PASB, a 1,600-task benchmark showing that when user claims are written into durable agent memory, downstream failure rates jump from 45% (session-only memory) to 71.9% (persistent storage), via status promotion, attribution removal, and scope broadening during storage. Frames agent sycophancy as a state-writing governance problem requiring safety controls at the memory-storage layer rather than only at response generation.

### MemPoison: Uncovering Persistent Memory Threats and Structural Blind Spots in LLM Agents
- **arXiv**: 2607.14651 ([link](https://arxiv.org/abs/2607.14651))
- **Date**: 2026-07-16
- **Category**: Security
- **Summary**: Introduces MemPoison, a benchmark of 1,227 validated cases probing injection attacks against persistent external memory across multiple memory systems and model families. Defines three escalating attack levels — direct corruption, compositional corruption, and context-triggered dormant attacks — and shows standard static-filtering defenses fail against the more sophisticated variants, arguing for context-aware defenses instead.

### Token-Flow Firewall: Semantic Runtime Auditing for Persistent AI Agents
- **arXiv**: 2607.08395 ([link](https://arxiv.org/abs/2607.08395))
- **Date**: 2026-07-09
- **Category**: Security
- **Summary**: Proposes TokenWall, a runtime defense that treats persistent memory updates (alongside tool arguments and inter-component messages) as a semantic attack surface, intercepting risky natural-language flows before they reach privileged runtime sinks. Reports reducing attack success rate to 12.5% at a 97.4% benign pass rate with ~0.69s latency overhead, targeting attack propagation through long-lived agent memory.

### Bad Memory: Evaluating Prompt Injection Risks from Memory in Agentic Systems
- **arXiv**: 2607.14611 ([link](https://arxiv.org/abs/2607.14611))
- **Date**: 2026-07-16
- **Category**: Security
- **Summary**: Empirically evaluates prompt-injection risks arising from the persistent state (memory files, behavioral preferences, knowledge bases) that agentic systems carry across sessions, testing two agent platforms with four models in a controlled sandbox. Finds agents largely resist being tricked into overwriting their own memory with external content, but payloads *already residing* in memory files are effective attack vectors for both current and future interactions, with success rates and payload longevity varying by system, model, attack objective, and sequence complexity.

### Do Agents Dream of False Memories? Black-box Visual Attacks on Long-term Memory in Multimodal AI Agents
- **arXiv**: 2607.15657 ([link](https://arxiv.org/abs/2607.15657))
- **Date**: 2026-07-17
- **Category**: Security
- **Summary**: Introduces Lucid, a black-box adversarial framework that attacks the long-term memory of multimodal AI agents using imperceptible image perturbations, extending memory poisoning/injection threats from text to the visual channel. Demonstrates two attack modes — memory poisoning (corrupting stored visual memories) and memory injection — achieving 61.6% and 58.4% success respectively across multiple memory architectures without white-box access.

### ChannelGuard: Safe Models Do Not Compose into Safe Multi-Agent Systems
- **arXiv**: 2607.19430 ([link](https://arxiv.org/abs/2607.19430))
- **Date**: 2026-07-20
- **Category**: Security
- **Summary**: Shows every hop between agents in a multi-agent pipeline (planner, workers, verifier, synthesizer) is an unmonitored channel for smuggling instructions, and that an undefended pipeline scoring 0.000 attack success on tool- and memory-poisoning owes that safety almost entirely to the cloud provider's server-side filter (54 of 60 blocks on Azure GPT-5) — a dependence that outcome-only reporting hides. Proposes ChannelGuard, training-free information-bottleneck gates on each inter-agent channel that pass/compress/block text by embedding similarity to an adversarial phrase bank with no extra LLM call, blocking Tool Poisoning 30/30 at the application layer across three backends and halving prompt-injection success, though white-box adaptive paraphrase evades every embedding gate.

### The Chronos Vulnerability: A Taxonomy of Temporal Persistence and Memory-Based Deception in Agentic AI
- **arXiv**: 2607.19433 ([link](https://arxiv.org/abs/2607.19433))
- **Date**: 2026-07-20
- **Category**: Security
- **Summary**: Formalizes the "Chronos Vulnerability" — memory-based attacks that compromise an agent's internal belief system and decouple the attack from its effects in time — cataloguing memory injection attacks, sleeper agents, and "Dynamics Blindness". Evaluation in the World of Workflows benchmark finds traditional content filters inadequate for stateful agents, and the paper surveys defenses spanning diagnostic trajectory guardrails, formal temporal verification, immunological memory consensus, and GPU-TEE / zero-trust memory architectures.

### ConsistencyGate: Preventing Memory Contamination in LLM Agents via Self-Consistency Admission Control
- **arXiv**: 2607.22962 ([link](https://arxiv.org/abs/2607.22962))
- **Date**: 2026-07-25
- **Category**: Security
- **Summary**: Targets memory contamination in multi-turn LLM agents, where a hallucinated fact written once persists as a false premise for every subsequent step. Proposes ConsistencyGate, a fine-tuning-free write-time admission gate that queries the model repeatedly and stores a candidate fact only when its average support score clears a threshold; three new benchmarks (LoCoMo-Contam, MSC-Contam, MemContam) show reduced contamination across the board, with a trade-off on implicitly-stated facts.

### MemTX: Transactional Belief Commit for Stateful Agent Memory
- **arXiv**: 2607.23929 ([link](https://arxiv.org/abs/2607.23929))
- **Date**: 2026-07-27 (v2 2026-07-28)
- **Category**: Security
- **Summary**: Argues a memory write should not constitute a belief commitment: in shared-memory multi-agent systems one agent's write becomes another's premise and eventually a side-effecting tool call, so a polluted tool result, stale update, or half-finished teammate note can silently drive an irreversible action. MemTX is a transactional protocol where records carry evidence, permissions, provenance, and validity — writes run in snapshot-isolated transactions through validation and commit stages, irreversible tool calls are gated on the current belief state, and retracting a belief triggers cascading repair of dependent records and tool effects, reporting zero downstream harm across five backbones.

### Isolated but Exposed: Persistence-Based Memory Extraction Attack on LLM Agents
- **arXiv**: 2607.23444 ([link](https://arxiv.org/abs/2607.23444))
- **Date**: 2026-07-26
- **Category**: Security
- **Summary**: Shows that per-user memory isolation, the standard production defense against long-term memory extraction, does not close the tool interface: a malicious tool can exfiltrate private memory smuggled inside invocation parameters without ever violating user-level isolation. The SPORE attack decouples adversarial commands (parked in short-term memory) from semantically neutral retrieval anchors issued in tool responses, restoring retrieval accuracy and enabling geometric optimization over embedding space to sweep unexplored memory regions, while persisted reactivation payloads continue the attack within and across sessions — 80.0% record extraction with unlimited triggers, 47.0% with only 20, and in multi-user deployments extracted records can be re-attributed to specific user identities.

### ContainmentBench: Trace-Based Evaluation of Post-Injection Containment in Tool-Using LLM Agents
- **arXiv**: 2607.23999 ([link](https://arxiv.org/abs/2607.23999))
- **Date**: 2026-07-27 (v2 2026-07-28)
- **Category**: Security
- **Summary**: Argues that terminal attack/policy outcomes hide what actually happened after exposure — identical "no committed harm" endpoints can conceal very different memory contamination traces and very different losses of authorized utility. ContainmentBench is a sandboxed, trace-based benchmark that scores endpoint policy compliance, logged propagation, recovery instrumentation, and authorized structured-action completion separately; across 17,640 Qwen2.5-7B-Instruct rollouts, 73.5% of matched active-tainted pairs diverge in trajectory or utility despite identical endpoints, and taint-only enforcement collapses authorized tainted-workflow completion to 0.1642 versus 0.8567 for a trusted-ledger policy.

### MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence and Repair
- **arXiv**: 2607.27080 ([link](https://arxiv.org/abs/2607.27080))
- **Date**: 2026-07-29
- **Category**: Security
- **Summary**: Benchmarks memory poisoning as a lifecycle rather than a single success/failure event, using a Write-Execute-Forget protocol over 310 cases spanning code, science, daily-activity, and workplace scenarios to separate whether malicious content persists, whether it drives a downstream execution chain, and whether it can be selectively repaired. Injected content persists in 84.2% of cases with 50.3% full attack success; among compromised systems 59.6% complete the execution chain and only 56.1% permit selective repair, and across 24 memory-system configurations attack success spreads 16.1 points while repair capability spreads 41.3 points — architecture, not just filtering, determines both propagation and recoverability.

### MIND: Lightweight and Effective Memory Injection Defense for LLM Agents via Intent-Aware Information Bottleneck
- **arXiv**: 2607.28103 ([link](https://arxiv.org/abs/2607.28103))
- **Date**: 2026-07-30
- **Category**: Security
- **Summary**: Targets the cost side of memory-injection defense: existing mechanisms either pay for repeated LLM auditing of every retrieved memory or drown in the redundancy of multi-turn context. A preliminary analysis shows benign and poisoned trajectories differ in how subsequent behavior relates to the initial user intent, so MIND trains an intent-aware information bottleneck that compresses intent-behavior pairs into representations preserving cross-turn attack signal while filtering task-irrelevant repetition, with a lightweight detector flagging malicious memories from those representations. On ReAct-StrategyQA it cuts mean ASR-r and ASR-a by 55.4% and 55.3% while matching the undefended agent on average accuracy and latency.

### MemTxn: A Transaction Boundary for Source-Supported Updates and Complete-State Recovery in Agent Memory
- **arXiv**: 2607.27834 ([link](https://arxiv.org/abs/2607.27834))
- **Date**: 2026-07-30
- **Category**: Security
- **Summary**: Observes that writable persistent memory lacks the one primitive databases take for granted — a transaction boundary — so an unsupported or corrupted write silently persists and contaminates future sessions. MemTxn is a governance layer outside the answer model that validates each write against its cited source (Ordered PatchTest), selects the visible version when facts conflict (Temporal Resolver), and restores the application-visible state after a fault from a durable snapshot journal. It accepts all 60 supported originals while rejecting all 179 hard negatives, restores the complete declared active map under persistent multi-key faults on LongMemEval-S and LoCoMo without knowing the actual physical write set, and leads MemoryAgentBench FactConsolidation across all twelve answer-model configurations.

### Auditing Provenance Sensitivity in LLM Agent Action Selection
- **arXiv**: 2607.20827 ([link](https://arxiv.org/abs/2607.20827))
- **Date**: 2026-07-23
- **Category**: Security
- **Summary**: Asks whether an agent's tool and parameter choices are actually driven by context it is authorized to act on, given a prompt that mixes user requests, tool outputs, retrieved records, memory, and untrusted text. The audit holds task and evidence content fixed and varies only provenance across 450 controlled tasks and several open-weight models: trusted and untrusted variants produce different actions in 5.4% of competing cases versus 1.7% of supporting cases, and under controlled degradation unauthorized evidence shifts the outcome in roughly 2.4% of comparisons (95% CI 2.1-3.0%) — models do react to textual source-authority cues, but do not reliably confine influence to authorized sources.

### Self-State Attacks on Self-Hosted AI Agents: How Far Can OS Defenses Go?
- **arXiv**: 2607.17986 ([link](https://arxiv.org/abs/2607.17986))
- **Date**: 2026-07-20
- **Category**: Security
- **Summary**: Self-hosted agents continuously rewrite their own memory and configuration files, so an adversary issuing ordinary OS system calls can compromise the agent by corrupting its own state rather than by injecting prompts. The paper formalizes these self-state attacks over four dimensions (Target, Mechanism, Granularity, Temporal), instantiates 43 concrete operations against real agent state files, and finds that access-control prevention plus workload-conditioned detection plus periodic backups mitigates most of them — while a residual surface remains structurally indistinguishable from legitimate agent writes at the OS level, arguing OS-level defense alone cannot close the gap.

### MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents
- **arXiv**: 2606.10742 ([link](https://arxiv.org/abs/2606.10742))
- **Date**: 2026-06-09
- **Category**: Security
- **Summary**: Identifies multimodal memory poisoning as an overlooked attack surface in web agents whose graph-structured external memory stores coordinated text-image evidence. MemVenom is a black-box two-stage attack: a trigger-conditioned retrieval attack that guarantees high-probability recall of the malicious memory, then post-retrieval attack induction using adversarial perturbations and stealthy OCR injection to override the user's original objective — persistent, reusable, and goal-agnostic without touching model parameters. Reaches up to 99.15% end-to-end success on GPT-5-family web agents with minimal benign-performance impact, transferring across architectures and model scales.

### SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems
- **arXiv**: 2606.12703 ([link](https://arxiv.org/abs/2606.12703))
- **Date**: 2026-06-10
- **Category**: Security
- **Summary**: Names Multi-Session Memory Poisoning (MSMP) — an adversary using only normal channels injects memories that steer responses for *future* users — and shows static-corpus defences (RobustRAG, ReliabilityRAG) assume a fixed knowledge base while heuristic filters fall to fluent enterprise-style text. SMSR pairs HMAC-SHA256 write-time provenance with query-time randomised memory ablation and verdict-based majority voting, proving no provenance-free retrieval-time filter can certify against adaptive injection and deriving a hypergeometric certificate; it also formalizes the Consistent Minority Effect, where a consistent adversarial answer wins string-based voting as a numerical minority. Across 15 enterprise scenarios (3,150 trials) provenance cuts unsigned attack success from 93-100% to 0%, and an end-to-end query-only attack drops from 65.3% to 5.3%.

### When Does Belief-Based Agent Memory Help? Reliability-Conditional Updating and Provenance-Capped Poisoning Defense
- **arXiv**: 2606.22030 ([link](https://arxiv.org/abs/2606.22030))
- **Date**: 2026-06-20 (revised 2026-07-16)
- **Category**: Security
- **Summary**: Nous represents entity-attribute pairs as categorical probability distributions updated by Bayesian inference, but the central finding is negative: belief updating alone barely beats naive last-write-wins because existing conversational memory benchmarks rarely contain contradictory or differently reliable evidence. Adding reliability-conditioned updating and provenance-capped belief updating turns probabilistic memory into a poisoning defense, and the benefit shows up specifically under conflicting, differently trustworthy evidence rather than in standard recall. Also documents a sizable evaluation discrepancy between token-F1 and LLM-as-judge scoring.

### Manufactured Confidence: How Memory Consolidation Turns Hearsay into Confident Facts
- **arXiv**: 2606.29279 ([link](https://arxiv.org/abs/2606.29279))
- **Date**: 2026-06-28
- **Category**: Security
- **Summary**: Memory products (mem0, LangMem) rewrite conversation into stored "facts", and that rewriting manufactures confidence — a casual hedged remark becomes a confident dated assertion the agent then obeys, granting every above-clearance request, with no attacker required. Isolating the trigger shows the agent responds not to source (attributed, unattributed, and forged "system of record" claims all grant alike) but to phrasing confidence, with the evidential register least discounted ("reportedly" obeyed like a flat assertion on most models). Obvious fixes fail — a passive "unverified" tag is ignored and an active distrust instruction escalates even correct memory — while the constructive finding is that a single load-bearing memory is the hazard and one redundant source restores correct decisions.

### Membrane: A Self-Evolving Contrastive Safety Memory for LLM Agent Defense
- **arXiv**: 2606.05743 ([link](https://arxiv.org/abs/2606.05743))
- **Date**: 2026-06-04
- **Category**: Security
- **Summary**: Fine-tuned safety classifiers cannot track evolving jailbreaks while adaptive memory-based guardrails over-refuse benign queries resembling stored attacks; Membrane's Contrastive Safety Memory stores cells that pair the conditions for blocking a harmful query with those for permitting a superficially similar benign one, indexed by attack strategy so one cell generalizes across topical variants. It evolves without retraining by distilling each harmful interaction and its benign counterpart into a new contrastive cell. Highest F1 on all six jailbreak attacks across HarmBench and AgentHarm, with benign refusal held to 7-14% against prior guards' 28-85%, 87-88% F1 under cross-attack transfer, and stability under memory poisoning.

### Hijacking Agent Memory: Stealthy Trojan Attacks Through Conversational Interaction
- **arXiv**: 2605.29960 ([link](https://arxiv.org/abs/2605.29960))
- **Date**: 2026-05-28
- **Category**: Security
- **Summary**: Prior memory poisoning assumes injected content is stored verbatim, ignoring the selective extraction and rewriting stages of modern memory pipelines that make those methods ineffective in realistic settings. MemPoison injects triggerable backdoors through ordinary dialogue using a semantic relational bridge that binds trigger and payload so they are extracted together, entity masquerading that shapes triggers to mimic named entities and survive rewriting, and joint embedding optimization that clusters trigger-injected text tightly while keeping it isolated from benign embeddings. Attack success up to 0.95 across agent domains and memory mechanisms; mechanistic analysis traces it to embedding-space anisotropy and attention shifts, and evaluated defenses show fundamental limitations.

### MRMMIA: Membership Inference Attacks on Memory in Chat Agents
- **arXiv**: 2605.27825 ([link](https://arxiv.org/abs/2605.27825))
- **Date**: 2026-05-27
- **Category**: Security
- **Summary**: Membership inference has been studied against training corpora and retrieval databases but not against agent memory, even though that memory holds sensitive user-agent interactions, retrieved facts, and stated preferences. Multi-Recall Memory MIA issues multiple recall probes to the agent to extract a membership signal for a candidate memory unit, unified across black-box, gray-box, and white-box access. Consistently outperforms baselines and supplies an initial evaluation framework for membership leakage in chat-agent memory systems.

### The Misattribution Gap: When Memory Poisoning Looks Like Model Failure in Agentic AI Systems
- **arXiv**: 2605.22842 ([link](https://arxiv.org/abs/2605.22842))
- **Date**: 2026-05-12
- **Category**: Security
- **Summary**: Formalizes Semantic Norm Drift as a third path to agent misconduct distinct from emergent misalignment and collusion: a policy-formatted document enters a shared vector store through a normal upload and later reappears as trusted system context after provenance is lost through a Trust Laundering Chain, so memory-layer attacks look exactly like model failure and defenders apply the wrong remediation. Across 64 documented failures attribution systems consistently blamed the model, four safety classifiers (one trained on memory poisoning) produced zero detections across 510 checkpoints, and agents explicitly cited the injected document as normative authority in 59 of 65 valid cases — with no trigger, model access, or repeated interaction needed. Counterfactual Composition Testing identifies the causal entry at 87.5% accuracy with zero false positives, Memory-Persistent Information-Flow Control blocks 97% of attacks at the cross-session boundary, and the SND Corpus is released as an adversarial memory benchmark with temporal persistence.

### OEP: Poisoning Self-Evolving LLM Agents via Locally Correct but Non-Transferable Experiences
- **arXiv**: 2605.18930 ([link](https://arxiv.org/abs/2605.18930))
- **Date**: 2026-05-18
- **Category**: Security
- **Summary**: Existing agentic memory attacks need privileged access or explicit malicious content and are caught by advanced safety filters; OEP instead asks whether an adversary can induce the agent to generate experiences that look locally correct and semantically plausible yet generalize harmfully during reflection. Obsessive Experience Poisoning is a low-privilege black-box attack that constructs clean edge-cases combining locally correct solutions, non-transferable methods, and severe but plausible hypothetical consequences, biasing reflection toward risk-averse rule formation so consolidation distills localized experience into over-generalized high-priority rules. Above 50% ASR with GPT-4o agents across three domains, outperforming existing attacks under LLM auditing defense.

### MemLineage: Lineage-Guided Enforcement for LLM Agent Memory
- **arXiv**: 2605.14421 ([link](https://arxiv.org/abs/2605.14421))
- **Date**: 2026-05-14
- **Category**: Security
- **Summary**: Treats untrusted content re-entering later sessions as an instruction as a chain-of-custody problem rather than a filtering problem, attaching cryptographic provenance and LLM-mediated derivation lineage to every memory entry. Six modules built around an RFC-6962 Merkle log over per-principal Ed25519-signed entries: a weighted derivation DAG records which retrieved entries influenced each new memory, a max-of-strong-edges propagation rule makes Untrusted-Path Persistence hold, and a sensitive-action gate refuses dispatches whose active justification descends from an external ancestor while still permitting benign recall. The only configuration driving all three memory-poisoning workloads to zero ASR at sub-millisecond per-operation overhead, with an AgentDojo bridge reducing strict ASR to zero on all six banking pairs where no-defense and signature-only baselines fail.

### ShadowMerge: A Novel Poisoning Attack on Graph-Based Agent Memory via Relation-Channel Conflicts
- **arXiv**: 2605.09033 ([link](https://arxiv.org/abs/2605.09033))
- **Date**: 2026-05-09 (revised 2026-05-15)
- **Category**: Security
- **Summary**: Existing agent-memory poisoning targets flat textual records and fails against graph memory, where malicious relations are typically not extracted, not merged into the target anchor neighborhood, or not retrieved for the victim query. ShadowMerge exploits relation-channel conflicts — a poisoned relation shares the query-activated anchor and canonicalized relation channel with benign evidence while carrying a conflicting value — and the AIR pipeline converts that conflict into an ordinary interaction the graph-memory system will extract, merge, and retrieve. 93.8% average ASR on Mem0 across PubMedQA, WebShop, and ToolEmu (+50.3 absolute points over the best baseline) with negligible impact on unrelated benign tasks; input-side defenses are shown insufficient and the findings were responsibly disclosed to graph-memory vendors.

### Observable Channels, Not Just Storage: Evaluating Privacy Leakage in LLM Agent Pipelines
- **arXiv**: 2603.22751 ([link](https://arxiv.org/abs/2603.22751))
- **Date**: 2026-03-24 (revised 2026-03-30)
- **Category**: Security
- **Summary**: Privacy leakage in LLM agents is usually studied one component at a time — memory module, retrieval pipeline, or tool-mediated artifact — which makes it impossible to compare how private internal dependence becomes externally recoverable across heterogeneous pipelines. CIPL (Channel Inversion for Privacy Leakage) is a channel-oriented measurement interface representing a target through its sensitive source, selection, assembly, execution, observation, and extraction stages under one protocol. Memory turns out to be a near-saturated high-risk special case, while retrieval-mediated targets leak frequently but incompletely and tool-mediated targets depend heavily on the exposed observation surface — leakage is governed by channel conditions rather than by any universally dominant attack recipe.

### HijackKV: New Threat in Position-Independent KV Cache Reuse
- **Venue**: USENIX Security 2026
- **arXiv**: 2607.19957 ([link](https://arxiv.org/abs/2607.19957))
- **Link**: https://www.usenix.org/conference/usenixsecurity26/presentation/zhang-yichi
- **Date**: 2026-08-12 (USENIX Security '26 symposium)
- **Category**: Security
- **Summary**: Position-independent KV cache reuse lets a serving system reuse the cached KV of any identical text chunk regardless of where it appears, but that cached KV still encodes the context in which it was originally computed — so a chunk that looks benign can carry an attacker-controlled prefix into a later victim query. HijackKV optimizes such a prefix so the KV computed for a common benign chunk encodes the attacker's goal while the chunk's text stays unchanged (preserving future cache hits), hijacking behavior with no attacker text in the victim's input. Reports ~94% single-attempt success, survives realistic conditions (10% hit rate, 50% recomputation), persists across multi-turn interactions, and transfers across models in black-box settings — making the reused KV cache a persistent poisoned-memory substrate rather than a purely performance-layer concern.

### When Memory Becomes a Vulnerability: Towards Multi-turn Jailbreak Attacks against Text-to-Image Generation Systems
- **Venue**: USENIX Security 2026
- **arXiv**: 2504.20376 ([link](https://arxiv.org/abs/2504.20376))
- **Link**: https://www.usenix.org/conference/usenixsecurity26/presentation/zhao-shiqian
- **Date**: 2026-08-12 (USENIX Security '26 symposium)
- **Category**: Security
- **Summary**: Modern text-to-image systems (e.g. DALL-E 3) keep a memory of prior turns so multi-turn requests generate faithfully, and this paper shows that mechanism is itself an attack surface. Inception plants malicious intent at the start of a session's memory and reaches it through segmentation (decomposing a prohibited prompt along sentence structure into individually filter-passing turns) and recursion (re-applying the decomposition to sub-prompts that still trip filters), so the harmful semantics are assembled from memory rather than present in any single prompt. Achieves a 20.0 percentage-point attack-success-rate margin over prior methods on a purpose-built platform and on commercial systems — the same fragmentation-across-memory-writes pattern seen in agent access-control bypasses, here against a deployed multimodal generation service.

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

### Memory in the Loop: In-Process Retrieval as Extended Working Memory for Language Agents
- **arXiv**: 2607.05690 ([link](https://arxiv.org/abs/2607.05690))
- **Date**: 2026-07-06
- **Category**: Optimization
- **Summary**: Moves memory access inside the agent's observe-reason-act loop instead of querying it externally, cutting retrieval latency from tens-hundreds of milliseconds (networked stores) to roughly 100 microseconds (in-process store, ~40us with a local embedder). Shows redundant agent actions rise monotonically with memory latency and that fast enough memory functions as "extended working memory" rather than a consulted tool, improving recall from 0/5 to 3.6-4.8/5 across GPT-5-class models.

### From Passive Retrieval to Active Memory Navigation: Learning to Use Memory as a Structured Action Space
- **arXiv**: 2607.05794 ([link](https://arxiv.org/abs/2607.05794))
- **Date**: 2026-07-07
- **Category**: Optimization
- **Summary**: Proposes NapMem, which organizes user history into a linked multi-granularity "memory pyramid" (raw conversations, typed records, topic tracks, profiles) and trains an RL policy to navigate it at the right level of detail instead of passively retrieving fixed context. Improves retrieval-efficiency/accuracy tradeoffs on PersonaMem-v2, LongMemEval, and LoCoMo while preserving general reasoning ability.

### Forget to Improve: On-Device LLM-Agent Continual Learning via Budget-Curated Memory
- **arXiv**: 2606.25115 ([link](https://arxiv.org/abs/2606.25115))
- **Date**: 2026-06-23
- **Category**: Optimization
- **Summary**: Proposes a unified "net-value-per-byte" score governing the memory lifecycle for on-device agents: evicting low-value entries within RAM/energy budgets, selectively sharing insights only when benefit exceeds transmission cost, and gating untrusted peer entries. Reports 2.7x lower memory footprint, 2.4x lower uplink usage, and injection-attack success driven to zero while maintaining accuracy.

### Akashic: A Low-Overhead LLM Inference Service with MemAttention
- **arXiv**: 2607.05708 ([link](https://arxiv.org/abs/2607.05708))
- **Date**: 2026-07-07
- **Category**: Optimization
- **Summary**: Targets multi-turn LLM agent systems that accumulate context across turns, tool calls, and cross-session workflows, where replaying the full history per request is impractical. Organizes history into bounded, semantically-linked chunks and applies hardware-software co-designed memory placement to co-locate likely co-retrieved chunks, reporting up to +10.2 points task accuracy, 1.21x throughput, and 1.88x sustainable request rate.

### Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory
- **arXiv**: 2607.05511 ([link](https://arxiv.org/abs/2607.05511))
- **Date**: 2026-07-06
- **Category**: Optimization
- **Summary**: Replaces iterative retrieval/reasoning in long-horizon multimodal agents with a reflexive design built in a single forward pass: episodic memories are hierarchically merged into a bounded, continuously-consolidated global script paired with a parametric latent state that drives actions. Reports 12.1x speedup and 2.6x lower GPU memory alongside a 2.4% accuracy gain over M3-Agent, making it a memory-consolidation/efficiency contribution.

### What to Keep, What to Forget: A Rate-Distortion View of Memory Compaction in LLMs and Agents
- **arXiv**: 2607.08032 ([link](https://arxiv.org/abs/2607.08032))
- **Date**: 2026-07-09
- **Category**: Optimization
- **Summary**: Unifies KV-cache eviction, prompt pruning, architectural state limiting, and agent memory consolidation as instances of a single rate-distortion problem: what context-derived information to retain, at what fidelity, under a resource budget. Contributes one compaction objective, a seven-axis taxonomy, cross-layer transfer mechanisms, and a benchmark for repeated compaction in agent workflows, arguing that attention-magnitude/recency heuristics discard information before knowing whether future queries need it.

### A Hierarchical Memory Architecture Overcomes Context Limits in Long-Horizon Multi-Agent Computational Modeling
- **arXiv**: 2607.07666 ([link](https://arxiv.org/abs/2607.07666))
- **Date**: 2026-07-08
- **Category**: Optimization
- **Summary**: Presents Ensemble QSP, a multi-agent system whose three-layer memory hierarchy keeps context bounded across extended multi-session workflows via strategic eviction of completed work, holding token usage stable (median ~301 tokens) regardless of project duration. A concrete long-horizon memory-management and cost-control contribution for multi-agent LLM workflows.

### Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation
- **arXiv**: 2607.07608 ([link](https://arxiv.org/abs/2607.07608))
- **Date**: 2026-07-08
- **Category**: Optimization
- **Summary**: Proposes LaMem-VLA, which embeds historical experience directly into a VLA model's native latent space via a curator that organizes it into complementary short-term and long-term memory vaults with coordinated retrieval/integration. Maintains bounded context windows while accessing rich history and eliminates external memory-management overhead — a long-horizon memory-efficiency contribution for embodied agents.

### NativeMEM: Native Memory Compression for Long-Horizon Robotic Manipulation
- **arXiv**: 2607.06678 ([link](https://arxiv.org/abs/2607.06678))
- **Date**: 2026-07-07
- **Category**: Optimization
- **Summary**: Repurposes a VLA model's existing vision encoder to compress historical frames into single memory tokens, letting the pretrained policy attend over long-term history with negligible latency overhead and no external memory module. Reports large success-rate gains on long-horizon manipulation (e.g. 32.4%->84.0% in simulation) at low latency and GPU cost — a memory-compression/efficiency contribution for embodied agents.

### Shared Selective Persistent Memory for Agentic LLM Systems
- **arXiv**: 2607.09493 ([link](https://arxiv.org/abs/2607.09493))
- **Date**: 2026-07-10
- **Category**: Optimization
- **Summary**: Instead of persisting whole conversation histories (token-inefficient and quality-degrading), retains only four categories of reusable context (task specs, data schemas, tool configs, output constraints) while discarding session-specific reasoning traces, and shares this memory across users via role-based access control. A complementary zero-token data-refresh mechanism decouples generated programs from runtime data; reports 96% task completion (vs. 79% without memory, 71% with full history), 14x task-time reduction, and 97x lower per-invocation token cost.

### Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents
- **arXiv**: 2607.08716 ([link](https://arxiv.org/abs/2607.08716))
- **Date**: 2026-07-09
- **Category**: Optimization
- **Summary**: Addresses long-horizon tasks where decision-relevant state is scattered across an expanding trajectory. A separate memory agent monitors the action agent's trajectory, maintains a structured memory bank, and selectively injects reminders only when needed, showing that selective intervention outperforms passive memory-bank exposure (+8.3 and +6.8 points on two benchmarks) — a long-horizon memory-management/efficiency contribution.

### MemDecay: Region-Aware KV Cache Eviction for Efficient LLM Agent Inference
- **arXiv**: 2607.10582 ([link](https://arxiv.org/abs/2607.10582))
- **Date**: 2026-07-12
- **Category**: Optimization
- **Summary**: A training-free KV-cache eviction strategy for LLM agents that recognizes different context regions (system instructions, plans, tool outputs, scratchpad) have different importance lifecycles rather than applying uniform rules. Reports that attention patterns differ by an order of magnitude across regions (system instructions persist ~10-12x longer than intermediate scratchpad), and assigns region-specific priorities to protect critical sections while evicting the lowest-priority pages under memory constraints — a memory/latency-efficiency contribution for agent inference.

### AAFLOW+: Stateful Operator Abstraction with Zero-Copy Distributed KV Cache Orchestration for Multi-Agent Workflows
- **arXiv**: 2607.10987 ([link](https://arxiv.org/abs/2607.10987))
- **Date**: 2026-07-13
- **Category**: Optimization
- **Summary**: Treats the KV cache as a distributed-systems primitive rather than a local per-agent artifact, letting agents in a multi-agent workflow share cached context across the network without recomputation via zero-copy transfers and stateful operator abstraction. Targets redundant-computation cost in collaborative multi-agent reasoning — a cost/latency-efficiency contribution for multi-agent memory/state reuse.

### ToolAtlas: Learning Once, Reusing Everywhere with Tool-Side Memory
- **arXiv**: 2607.11126 ([link](https://arxiv.org/abs/2607.11126))
- **Date**: 2026-07-13
- **Category**: Optimization
- **Summary**: Builds a persistent provider-side "tool memory" — a graph of tool capabilities, failure boundaries, and cross-tool compositions distilled through execution verification and accessed via adaptive traversal — so agents reuse learned tool knowledge across environments and frameworks without task-time exploration or retraining. Reports up to 21.61% pass@1 improvement, framing reusable tool-knowledge memory as a retrieval-efficiency/cost-reduction contribution.

### Speculate with Memory: Lossless Acceleration for LLM Agents
- **arXiv**: 2607.12236 ([link](https://arxiv.org/abs/2607.12236))
- **Date**: 2026-07-14
- **Category**: Optimization
- **Summary**: Accelerates LLM-agent execution losslessly by giving the speculative predictor a memory of past agent trajectories — a transition table, episodic memory, and error tracker — so it learns to predict the agent's next actions more accurately as the memory grows (19-39% relative action-prediction accuracy gain). Speculation runs during idle periods at zero added wall-clock cost, framing trajectory memory as a cost/latency optimization for agents.

### Oracle Agent Memory as an Enterprise Memory Substrate for Long-Horizon AI Agents
- **arXiv**: 2607.13157 ([link](https://arxiv.org/abs/2607.13157))
- **Date**: 2026-07-14
- **Category**: Optimization
- **Summary**: Presents a database-native agent-memory substrate with a full lifecycle (ingestion through removal) and a layered architecture with scope controls, aimed at retaining task state and user-specific facts across extended interactions in enterprise deployments. Reports ~93.8% accuracy while using about 10.7x fewer tokens than flat-history baselines — a memory compression and cost-efficiency contribution for long-horizon agents.

### Memory as a Controlled Process: Learned Adaptive Memory Management for LLM Agents
- **arXiv**: 2607.13591 ([link](https://arxiv.org/abs/2607.13591))
- **Date**: 2026-07-15
- **Category**: Optimization
- **Summary**: Proposes MemCon, which treats memory operations as a Markov Decision Process and learns an adaptive policy — via lightweight contextual bandits, without pretraining — deciding when to retrieve, inject plans, or consolidate/forget rather than using fixed retrieval strategies. Reports cutting token consumption by 5-20% while improving task success by up to 15.2 points — a retrieval-efficiency and consolidation-policy optimization contribution.

### Experience Memory Graph: One-Shot Error Correction for Agents
- **arXiv**: 2607.13884 ([link](https://arxiv.org/abs/2607.13884))
- **Date**: 2026-07-15
- **Category**: Optimization
- **Summary**: Reformulates agent failure recovery as a graph-matching problem: it distills successful workflows by comparing failed and expert trajectories and stores correction guidance in an Experience Memory Graph with task-specific and cross-task edges, enabling one-shot correction. By reusing stored corrections instead of iterative self-reflection loops, it eliminates test-time trial-and-error and reduces API calls and execution latency — a cost/latency-efficiency contribution built on a reusable agent-memory structure.

### Track, Rank, Crack: Epistemic Working Memory Scales Multi-Hop Reasoning in Language Agents
- **arXiv**: 2607.12267 ([link](https://arxiv.org/abs/2607.12267))
- **Date**: 2026-07-14
- **Category**: Optimization
- **Summary**: Introduces SLEUTH, which maintains a structured epistemic working memory (Confirmed Facts, Active Hypotheses, Open Questions) to counteract context dilution as reasoning chains lengthen. Shows that organizing and managing working-memory state — not raw model capability — is what lets agents scale to longer multi-hop chains, with gains growing from +5 to +11 points as task difficulty rises; a long-horizon memory-management contribution.

### MemoHarness: Agent Harnesses That Learn from Experience
- **arXiv**: 2607.14159 ([link](https://arxiv.org/abs/2607.14159))
- **Date**: 2026-07-14
- **Category**: Optimization
- **Summary**: Decomposes the agent harness into six controllable dimensions and adds a dual-layer experience bank that learns reusable control patterns from prior executions, retrieving them at inference without test-time feedback. Reports beating fixed harnesses on task performance while keeping compute competitive via cached experience retrieval — an experience-memory consolidation-and-reuse contribution.

### MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations
- **arXiv**: 2607.12893 ([link](https://arxiv.org/abs/2607.12893))
- **Date**: 2026-07-14
- **Category**: Optimization
- **Summary**: Reformulates conversational memory as a sequence of lifecycle operations (remembering, forgetting, updating, reflecting) and evaluates systems via structured operation traces rather than final-answer accuracy. Across retrieval-based, parametric, and managed-memory approaches, it exposes failures in ordered memory-state reconstruction and session-level retrieval organization — a diagnostic tool for long-horizon memory management.

### Profile-Graph Memory for LLM Agents: Implicit Cross-Entity Traversal through Narrative Profiles
- **arXiv**: 2607.19359 ([link](https://arxiv.org/abs/2607.19359))
- **Date**: 2026-06-01
- **Category**: Optimization
- **Summary**: Argues existing long-term memory benchmarks mostly test single-hop recall, leaving multi-hop association unmeasured, and introduces MemHop (1,000 questions across five hop depths). Proposes ProGraph, a two-layer memory architecture combining narrative profile expansion with compression residuals so cross-entity traversal happens implicitly rather than via explicit graph queries, reaching 80.1% on MemHop and 78.4% on LoCoMo.

### LazyMem: Retrieve Broadly, Construct Selectively for Efficient Long-Term Agent Memory
- **arXiv**: 2607.22690 ([link](https://arxiv.org/abs/2607.22690))
- **Date**: 2026-07-17 (v2 2026-07-28)
- **Category**: Optimization
- **Summary**: Defers memory construction from ingestion time to query time: a lightweight model runs over overlapping parallel segments of the retrieved candidate pool and condenses only query-pertinent material, trained by SFT plus RL with a reward for both locating relevant exchanges and producing accurate query-helpful summaries. LazyMem-4B reaches 0.85 LLM-judge accuracy on LongMemEval using 213 answer-context memory tokens — 21.0x fewer than the baseline — and transfers to LoCoMo without task-specific training while improving latency over prior query-time methods.

### Beyond Memory Leaderboards: Evaluating Scientific Memory as Budgeted Context Restoration
- **arXiv**: 2607.16848 ([link](https://arxiv.org/abs/2607.16848))
- **Date**: 2026-07-18
- **Category**: Optimization
- **Summary**: Introduces two full-text scientific-memory benchmarks (PAIM, PTr) and shows memory leaderboards are uninterpretable without the full protocol — ingestion granularity, raw-text preservation, retrieval budget, retrieval modality, and judge choice all move rankings. Concretely, Graphiti's win on PAIM disappears once retrieval budget is controlled (it consumed 2.6M characters of context per query), and sparse-dense hybrid retrieval is the single most significant intervention on PTr, arguing memory should be scored as budgeted, modality-aware context restoration.

### Mechanistic Attention Guidance for Agent Memory Refinement
- **arXiv**: 2607.17621 ([link](https://arxiv.org/abs/2607.17621))
- **Date**: 2026-07-20
- **Category**: Optimization
- **Summary**: Notes that self-evolving memory systems refine memory from textual signals (trajectories, reflections) alone, never checking how retrieved memory is actually used, which yields unreliable error attribution and hallucinated memory edits. Shows retrieval-head attention aggregated over memory segments and decision steps forms a context-utilization matrix exposing memory-use patterns, and builds AGMR on it to make targeted segment-level updates (correct/enhance after failures, simplify after successes, verify by re-execution), improving both task performance and memory efficiency.

### Supra Cognitive Modes: A Routed Architecture for Agent Memory
- **arXiv**: 2607.19096 ([link](https://arxiv.org/abs/2607.19096))
- **Date**: 2026-07-21
- **Category**: Optimization
- **Summary**: Routes each query among distinct retrieval/synthesis payloads — fused lexical-dense lookup, graph or iterative multi-hop handling, and stratified long-form synthesis — over one shared ingest substrate of multi-granularity embeddings, extracted triples, and fact-version metadata, dispatched by a frozen semantic classifier and runtime gates. Reports 84.87% on LoCoMo factoid categories, 61.49% on MemoryAgentBench, and 86.00% on LongMemEval, but explicitly states token ledgers and end-to-end timing are unavailable, so claimed efficiency gains and causal routing effects remain unverified.

### MemTools: A Unified Research Framework for Interoperable Agent Memory
- **arXiv**: 2607.21404 ([link](https://arxiv.org/abs/2607.21404))
- **Date**: 2026-07-23
- **Category**: Optimization
- **Summary**: Addresses architectural fragmentation in agent memory research, where implementations couple memory-lifecycle stages, entangle evaluation logic with specific datasets, and handle heterogeneous memory types poorly. MemTools standardizes the lifecycle via declarative data contracts so components from different systems can be swapped in, separates benchmark datasets from execution protocols for controlled comparison, and provides one runtime interface coordinating symbolic, neural, and multimodal memory — infrastructure for isolating individual memory design variables.

### Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings
- **arXiv**: 2607.21962 ([link](https://arxiv.org/abs/2607.21962))
- **Date**: 2026-07-24
- **Category**: Optimization
- **Summary**: Inverts benchmark construction — facts with validity intervals and volatility classes are generated first, then rendered into chat/email by an LLM and verified, so questions derive mechanically from the script and ground truth is correct by design (~380 questions, 15 categories, including temporal validity windows, sent-vs-received trust distinctions, and injection probes). The headline result is a tenure crossover: memory-architecture rankings invert as history lengthens, with a budgeted curated-map system leading early but losing 24 points of recall by nine weeks while a provenance-typed graph climbs to 90% (p=0.031), released as the Veracium library.

### Keep It InMind: Benchmarking the Implicit-Association Blind Spot in Agent Memory
- **arXiv**: 2607.24368 ([link](https://arxiv.org/abs/2607.24368))
- **Date**: 2026-07-27
- **Category**: Optimization
- **Summary**: Names the "implicit-association blind spot": retrieval assumes a needed memory resembles the query needing it, which breaks when world knowledge is the bridge (a tree-nut allergy should block a macaron request via almond flour, yet the texts share no retrievable cue). The InMind benchmark (125 expert-verified tasks, ten life domains) uses paired controls to separate never-stored from missing-bridging-knowledge from stored-but-not-surfaced, finding backbones answer 84.0% of indirect queries with the memory in context but six vector/graph/agentic memory systems reach at most 14.4% when it must be retrieved — locating the failure in the query-conditioned interface and framing routing as the open problem.

### MemChain: Learning Interpretable Memory Traces for Memory-Augmented LLM Agents
- **arXiv**: 2607.24097 ([link](https://arxiv.org/abs/2607.24097))
- **Date**: 2026-07-27
- **Category**: Optimization
- **Summary**: Challenges the retrieval-as-evidence paradigm, in which raw retrieved memories are fed straight to the answer model, leaving it to resolve redundancy, conflicts, and weak relevance at substantial context cost. MemChain is a trainable post-retrieval policy that generates a question-conditioned evidence plan, builds an ordered grounded evidence trace organized by semantic role and dependency, then executes explicit memory actions to emit a compact evidence context — trained by supervised trace learning plus Trace-Guided Memory Policy Optimization, reaching state of the art on LoCoMo and LongMemEval-S while substantially shrinking the memory context.

### UniMem: Complementary Episodic-to-Parametric Memory for Boundary-Agnostic Task Streams
- **arXiv**: 2607.26017 ([link](https://arxiv.org/abs/2607.26017))
- **Date**: 2026-07-28
- **Category**: Optimization
- **Summary**: Frames deployment over boundary-agnostic evolving task streams as a stability-plasticity dilemma: retrieval memory absorbs new evidence fast but never internalizes recurring execution patterns and pays inference-time retrieval overhead, while parametric memory is stable and cheap but needs explicit task boundaries and fixed parameter budgets. UniMem uses learnable routing tokens as memory controllers to keep novel or sparse tasks in an episodic buffer while consolidating recurring reliable patterns into expandable parametric memory, growing on demand without deployment task labels or uncontrolled parameter growth (+4.0 EM average across three backbones).

### RSMeM: Knowledge-Enhanced Memory Evolution for Remote Sensing Agents with Systematic Evaluation
- **arXiv**: 2607.24772 ([link](https://arxiv.org/abs/2607.24772))
- **Date**: 2026-06-11 (announced late July 2026)
- **Category**: Optimization
- **Summary**: Addresses the fact that general-purpose LLM agents in remote sensing fail on multi-step tool execution and never consolidate those failures into reusable experience. RSMeM pairs Hierarchical Knowledge Grounding (taxonomy-aware retrieval over a hierarchical domain corpus to guide planning and tool selection) with Failure-Aware Experience Refinement, which distills failure-annotated tool-use traces into reusable constraints for the next round — a high-density consolidation strategy that on EarthBench yields a 6% accuracy gain on DeepSeek-V3.2 for under 1% additional experience tokens.

### IFCMemoryBench: Evaluating Long-Term Memory of LLM-Based Agents in BIM Information Retrieval
- **arXiv**: 2607.26072 ([link](https://arxiv.org/abs/2607.26072))
- **Date**: 2026-07-13 (announced 2026-07-29)
- **Category**: Optimization
- **Summary**: Argues that conversational-recall benchmarks understate the real test of long-term memory: reusing prior-session context while acting over a live, structured, domain-specific environment. IFCMemoryBench seeds missing project context (specifications, client decisions, engineering conventions) across 4,016 prior sessions and then poses probe questions answerable only by combining remembered context with live IFC queries — 143 multi-session tasks over 19 projects, decomposed into ingestion, retrieval, and utilization. The strongest system reaches only 32.4% answer accuracy under realistic ingestion scope, with failures traced to memory that retrieves topically relevant context but stores project knowledge as fragmented facts.

### ACM: Agentic Context Management for Long Horizon Tasks
- **arXiv**: 2607.23809 ([link](https://arxiv.org/abs/2607.23809))
- **Date**: 2026-07-26
- **Category**: Optimization
- **Summary**: Attacks the two failure modes of automatic context compression in long-horizon agents — lossy degradation and rigid trigger heuristics that ignore the agent's shifting analytical needs. ACM instead exposes context management as tools the agent invokes itself, deciding when to compress, offloading the removed span to external memory, and retrieving it on demand so that no information is destroyed; a companion training recipe synthesizes high-quality context-management trajectories, and the result lowers peak token pressure, sustains longer explorations, and improves run-to-run reliability on agentic search and coding.

### MemLens: A Value-Aware Memory Management System with Interactive Analytics for LLM-based Agents
- **arXiv**: 2607.25992 ([link](https://arxiv.org/abs/2607.25992))
- **Date**: 2026-07-28
- **Category**: Optimization
- **Summary**: Observes that current LLM memory systems are utility-agnostic, treating heterogeneous interaction records uniformly so that redundant and low-impact entries accumulate in the repository. MemLens promotes memory records to first-class data objects and provides an end-to-end interactive dashboard over the full lifecycle — Shapley-style valuation of individual memories, value-aware storage, and memory-assisted response — letting users inspect memory value, visualize hierarchical structure, and compare management strategies on response quality, retrieval latency, and token consumption.

### A Graph-Native Bitemporal Memory Store for Conversational AI Agents
- **arXiv**: 2607.26520 ([link](https://arxiv.org/abs/2607.26520))
- **Date**: 2026-07-29
- **Category**: Optimization
- **Summary**: Implements cross-session persistent memory as a Neo4j graph with vector indexing rather than a context-window dump or an external service, storing each memory as an immutable identity node linked to versioned content nodes carrying two clocks — valid time (when the fact held in the world) and transaction time (when the store recorded it) — so retrieval can be replayed at any past point without erasing history, with semantic links maintained at write time via cosine similarity over 1024-dimensional embeddings. On LongMemEval, current-state retrieval reaches 46.7% R@10 overall and 80% on knowledge-update questions while temporal queries lag, and the paper enumerates the design changes needed to close that gap.

### Living-Harness Is an Interactive-Agent Evolver
- **arXiv**: 2607.26598 ([link](https://arxiv.org/abs/2607.26598))
- **Date**: 2026-07-29
- **Category**: Optimization
- **Summary**: Notes that agents recover from failures within an episode yet repeat the same execution errors forever, because post-episode feedback never modifies the persistent harness that governs future runs. Living-Harness converts completed trajectories and evaluator signals into bounded harness updates under a domain-level Evolution-SOP, writing two complementary forms of procedural knowledge — episodic memory recording trigger conditions and recovery actions, plus a state graph of repair edges and transition rules — while tools and base context stay frozen, gaining 10.07 and 9.91 points over baselines across eight interactive environments with the evolved harness state transferable across model backbones.

### Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability
- **arXiv**: 2607.26637 ([link](https://arxiv.org/abs/2607.26637))
- **Date**: 2026-07-29
- **Category**: Optimization
- **Summary**: Studies the increasingly common deployment pattern of holding long-term agent memory as a directory tree of markdown files, formalizing three roles over a shared memory filesystem: one integrating incoming content, one retrieving with citations, and one supplying task sequences converted into reusable skills. Organized stores roughly halve retrieval cost once the material is large, but agents cannot sustain that organization as content accumulates, and the tooling handed to the agent shapes the resulting structure as much as the backbone model does — so filesystem organization is a design parameter to be tuned, not a free win.

### Metis: Memory Foundation Model
- **arXiv**: 2607.26760 ([link](https://arxiv.org/abs/2607.26760))
- **Date**: 2026-07-29
- **Category**: Optimization
- **Summary**: Proposes moving agent memory inside the backbone instead of bolting on an external module, defining native memory as a persistent, dynamically evolving memory state within the model plus native memory procedures that store and use information through ordinary model computation. Metis is a first prototype: a native memory state compressing historical information, accessed via memory attention, trained with purpose-built datasets and multiple objectives, and at inference the weights stay frozen while memory states are transformed autonomously by the forward pass — claiming architectural, end-to-end-optimization, and efficiency advantages over external memory systems, with checkpoints released.

### Setoka: A Benchmark for Hierarchical User Understanding in Personalized Agents over Heterogeneous Data
- **arXiv**: 2607.27056 ([link](https://arxiv.org/abs/2607.27056))
- **Date**: 2026-07-29
- **Category**: Optimization
- **Summary**: Argues existing memory benchmarks stop at explicit fact retrieval and therefore cannot say whether a personalized agent actually understands its user. Setoka defines four ascending levels — semantic memory, episodic memory, behavior pattern, and personality trait — and uses psychology-grounded principles to synthesize user data and queries at scale while sidestepping privacy constraints; across three backbones and five memory systems over ten synthetic users, performance is strong on semantic memory and degrades sharply on the other three levels, indicating that user understanding demands cross-source integration and abstraction over long-term behavior rather than retrieval.

### MemHarness: Memory Is Reconstructed, Not Replayed
- **arXiv**: 2607.28272 ([link](https://arxiv.org/abs/2607.28272))
- **Date**: 2026-07-30
- **Category**: Optimization
- **Summary**: Identifies verbatim replay as the core defect of memory-augmented agents: retrieved experiences are injected into context regardless of whether they fit the current situation, so the gap between abstract stored experience and concrete decision-time state produces negative transfer. MemHarness has a unified policy model critique and reconstruct each retrieved experience conditioned on the present state, emitting context-grounded guidance before acting, with the reconstructive ability emerging from end-to-end GRPO training rather than hand-written rules. It substantially beats pure RL and static memory-augmented baselines on ALFWorld and WebShop, stays robust out of distribution, and the reconstruction objective doubles as latent training guidance that improves intrinsic reasoning.

### RRM: Experience-Driven Reflective Retrieval Memory for Long-Horizon Multimodal Reasoning
- **arXiv**: 2607.28156 ([link](https://arxiv.org/abs/2607.28156))
- **Date**: 2026-07-30
- **Category**: Optimization
- **Summary**: Points out that multimodal long-term memory agents concentrate on what to store and have no mechanism to diagnose retrieval failures or adapt future search strategy when retrieval repeatedly returns useless evidence. RRM augments an entity-centric multimodal memory graph with a reflective experience memory that distills transferable procedural retrieval knowledge from historical trajectories and converts it into query-level guidance, while answer generation stays conditioned only on factual evidence newly retrieved from the current video; a lifecycle mechanism regulates the experience store by usage frequency, reuse feedback, and temporal decay to curb redundancy and noise. Consistently outperforms prior state of the art on M3-Bench-Robot, M3-Bench-Web, and Video-MME-Long.

### Sigma-Mem: An Online Reliability Memory for LLM-based Multi-Agent Systems
- **arXiv**: 2607.27958 ([link](https://arxiv.org/abs/2607.27958))
- **Date**: 2026-07-30
- **Category**: Optimization
- **Summary**: Notes that agent memory preserves interaction content but never models which peers can be trusted and under what conditions — a gap that bites in multi-agent systems where a central model cannot directly verify plausible or correlated peer responses. Sigma-Mem records per-peer competence evidence and cross-peer relationship evidence as real symmetric states updated from post-decision correctness feedback, with Weyl's inequality bounding the spectral change of each event-level update so online adaptation stays stable without retraining any model. One write-and-read interface then serves residual steering, response-free peer routing, or reliability-weighted voting; across five Qwen-family models it tracks counterfactual reliability shifts, generalizes to unseen peers and task domains, and direct readouts beat both majority voting and the best fixed peer over the full OOD set.

### ChronoMem: Version Control and Semantic Rollback for Large Language Model Agent Memory
- **arXiv**: 2607.27773 ([link](https://arxiv.org/abs/2607.27773))
- **Date**: 2026-07-30
- **Category**: Optimization
- **Summary**: Existing agent memory evolves forward only — accumulating, consolidating, overwriting — with no principled way to inspect, version, or revert, leaving agents brittle under corrections, concept drift, and corruption once later information has already been absorbed. ChronoMem, integrated into Google's open-source Agent Development Kit, commits a whole-memory snapshot at each write, maintains structured version histories, and maps natural-language undo intents onto concrete historical versions through hybrid lexical and semantic retrieval, rank fusion, and reranking. A post-exposure protocol then tests whether the agent can answer and summarize counterfactually as if the later updates never occurred, where ChronoMem substantially beats prompt-only and retrieval-only baselines.

### SKILL-KD: Contrastive Skill Distillation for LLM Agents
- **arXiv**: 2607.28048 ([link](https://arxiv.org/abs/2607.28048))
- **Date**: 2026-07-30
- **Category**: Optimization
- **Summary**: Argues that storing skills as experience summaries or memory entries misfires for weaker student agents — a failed trajectory carries too little evidence of the missing behavior, and the teacher trajectory is too implicit to internalize as reusable guidance. SKILL-KD distills the actionable discrepancy between a student failure and the teacher trajectory on the same task into a textual skill patch, validates it by re-running the student, and refines iteratively; Drift-Aware Skill Consolidation keeps trace-linked edit histories and decides per patch whether to add a rule, delete or modify an existing one, or skip, preventing repeated local updates from degrading the store. Improves frozen student agents over fixed-model adaptation baselines across five benchmarks and two student settings.

### Bridging Inference-Time Scaling and Episodic Memory with Action-Centric Graphs
- **arXiv**: 2607.27415 ([link](https://arxiv.org/abs/2607.27415))
- **Date**: 2026-07-29
- **Category**: Optimization
- **Summary**: Inference-time scaling for language agents is wasteful because each rollout is effectively stateless and redoes work already performed in earlier attempts. GAMER models historical reasoning as a dynamic action-centric graph and decouples this memory from the LLM itself to cut computational overhead, using temporal-difference learning to estimate both positive and negative values for action nodes from past outcomes; at inference the value function guides decisions bidirectionally, proposing beneficial actions and flagging risky ones, for gains of 20.81%/6.17% in success/progress rate over vanilla baselines.

### Retain or Consolidate? Budget-Dependent Operator Selection for Language Agent Memory
- **arXiv**: 2607.17545 ([link](https://arxiv.org/abs/2607.17545))
- **Date**: 2026-07-20 (revised 2026-07-21)
- **Category**: Optimization
- **Summary**: Formalizes the retention-versus-consolidation choice every agent memory system makes implicitly: raw records preserve exact detail but relevant evidence may not fit a tight budget, while compression improves coverage per token at the risk of losing query-critical details, so neither is universally preferable. The paper decomposes each operator's utility (Merge, Abstract, Rewrite) into a coverage effect over evidence retention would omit and a signed replacement effect over evidence that already fits, which explains why the preferred action flips with relative budget pressure, and implements the rule as Offline Abstraction-Safety, a lightweight learner estimating action utilities from pre-generation features with held-out harm calibration. On LongMemEval consolidation gains up to 48% absolute accuracy under tight budgets while retention wins under loose ones, and LoCoMo reproduces the crossover at a smaller budget; cross-note abstraction and merging generally beat local rewriting when compression is required.

### AttriMem: Attribution-Guided Process Feedback for Agent Memory Learning
- **arXiv**: 2607.21106 ([link](https://arxiv.org/abs/2607.21106))
- **Date**: 2026-07-23
- **Category**: Optimization
- **Summary**: A memory-construction policy decides what to extract, store, update, compress, or discard as interactions accumulate, but heuristic methods encode subjective task-specific rules while RL methods see only outcome- or module-level rewards that cannot identify which intermediate memory contents supported the final answer — a fine-grained credit-assignment bottleneck made worse by the absence of ground-truth targets for intermediate decisions. AttriMem supplies the missing process feedback by deriving local rewards from token-level contributions to the final answer and adding them to the global outcome reward, outperforming retrieval-based, heuristic, and RL baselines on long-horizon dialogue QA while generalizing across benchmarks and answer models and stabilizing RL optimization.

### PRO-LONG: Programmatic Memory Enables Long-Horizon Reasoning
- **arXiv**: 2607.20064 ([link](https://arxiv.org/abs/2607.20064))
- **Date**: 2026-07-22 (revised 2026-07-23)
- **Category**: Optimization
- **Summary**: Frames the decisive design choice in long-horizon exploratory agents as what to save from the environment and how to load it back, where preserving more information makes retrieving the relevant detail less tractable. PRO-LONG resolves the tradeoff by keeping a complete structured interaction log and delegating retrieval to coding-agent-style search over that history instead of summarizing it away. On the full ARC-AGI-3 public game set it adds 18.0 percentage points on average over a base coding agent and matches or exceeds specialized harnesses (up to 76.1% pass@1) while using 4.2-5.8x fewer tokens.

### Agentic Context Management: Solving Agent Memory and Cost by Treating Them as Lifecycle and Architecture Problems
- **arXiv**: 2607.21503 ([link](https://arxiv.org/abs/2607.21503))
- **Date**: 2026-07-23
- **Category**: Optimization
- **Summary**: Argues production agents fail on managing what sits in their reasoning context — conversation histories, large prompts, large tool definitions, ballooning tool outputs — rather than on reasoning capability, and that treating this as a storage problem misses the structure. It decomposes context management into five lifecycle activities (deciding what to remember, extracting and structuring, selecting storage, consolidating while preserving provenance, judging current relevance), shows naive accumulation grows token cost quadratically while validated compaction keeps it linear at preserved accuracy, and reports 92% on LongMemEval and 93.2% on LoCoMo for its Maximem Synap reference implementation, while flagging latency, token efficiency, and context-rot resistance as evaluation dimensions current benchmarks underexplore.

### Voice Memory for Agentic Speech Recognition
- **arXiv**: 2607.26410 ([link](https://arxiv.org/abs/2607.26410))
- **Date**: 2026-07-29
- **Category**: Optimization
- **Summary**: An inference-only agent memory scheme that splits an ASR correction agent into a frozen "listener-thinker" corrector, which reads a single per-domain memory file and decides per utterance whether to act or abstain, and an asynchronous score-gated optimizer that revises that file through bounded edits accepted only on strict held-out improvement. Because the two roles are coupled solely through the memory, the learned skill stays auditable, portable across corrector families, and adds zero parameters to the inference path. Restraint is the skill the loop actually discovers: unconstrained generative error correction breaks correct tokens on up to 64% of edits on financial news versus 35% here, and weighted WER drops from 8.36% to 7.52% across ten HyPoradise domains without regressing any dataset below its 1-best baseline.

### Exploratory and Assimilating Reflection: Reflective Recall Cycle for Long-term Memory
- **arXiv**: 2607.17879 ([link](https://arxiv.org/abs/2607.17879))
- **Date**: 2026-07-20
- **Category**: Optimization
- **Summary**: Existing agent memory retrieval lacks adaptability and sample efficiency and struggles to pull the right mixture of memories out of heterogeneous stores. EAR pairs Exploratory Reflection, an iterative search that bootstraps retrieval and harvests useful per-query experiences, with Assimilating Reflection, which replays those experiences from an Experience Buffer to refine a global reranker more efficiently than immediate-reward-only methods. Improves retrieval by up to 17.9% over the baseline retriever on two long-term dialogue benchmarks while staying sample-efficient and robust to noisy feedback.

### RECON: Benchmarking Agent Memory for Compositional Reasoning over Long Contexts
- **arXiv**: 2607.16716 ([link](https://arxiv.org/abs/2607.16716))
- **Date**: 2026-07-18
- **Category**: Optimization
- **Summary**: Prior memory benchmarks test whether agents retrieve scattered facts or notice that a fact changed; RECON evaluates what happens *after* the change — which downstream conclusions are invalidated, which survive through independent support, and how alternative timelines would have unfolded. It spans 24 case files of 50k-100k tokens across criminal, medical, and financial domains over six memory-intensive tasks (multi-hop evidence chains, cascading invalidation, source-conflict resolution, counterfactuals, temporal constraints, temporal fact retrieval). Even the strongest non-Oracle system reaches only 22.4% accuracy, with retrieval and reasoning each surfacing as separate bottlenecks.

### From Memory to Skills: Evidence-Grounded Co-Evolution Governance for Long-Horizon LLM Agents
- **arXiv**: 2607.16621 ([link](https://arxiv.org/abs/2607.16621))
- **Date**: 2026-07-18
- **Category**: Optimization
- **Summary**: MSCE is a training-free framework that converts accumulated agent experience into three coupled stores — grounded step traces, reusable procedural policies, and declarative environmental cognition — and crystallizes only policies with positive expected gain into callable skills, each retaining its evidence links, applicability constraints, and reliability estimates. Reflection-weighted value backfilling propagates sparse terminal feedback through dense local self-reflections to produce calibrated trace values, addressing the credit-assignment problem that makes naive experience accumulation unreliable. Reports substantial gains over baselines on EvoAgentBench and LoCoMo with notable cross-domain transfer and continual-learning behavior.

### AgentBrew: Lifelong Knowledge Brewing from Strong Teachers to Weak LLM Agents
- **arXiv**: 2607.16851 ([link](https://arxiv.org/abs/2607.16851))
- **Date**: 2026-07-18
- **Category**: Optimization
- **Summary**: Targets the deployment reality that a compact student model serves at test time even when a stronger teacher was available during training, and distills the teacher's interactive experience into a persistent external memory instead of weights — requiring no weight updates, expert demonstrations, ground-truth labels, or test-time teacher access. A failure-triggered teacher-Ralph loop turns student failures into environment-validated memory notes to work around sparse binary feedback, while student-aware synthesis calibrates teacher knowledge to the weak executor's operational granularity so the stored guidance is actually executable. Evaluated across coding, math, and tool-use tasks with ablations.

### OpsMem: Dual-Memory Reasoning with Cross-Memory Resonance for Failure Diagnosis
- **arXiv**: 2607.11357 ([link](https://arxiv.org/abs/2607.11357))
- **Date**: 2026-07-13
- **Category**: Optimization
- **Summary**: Existing LLM diagnosis methods improve on agentic reasoning or knowledge augmentation but lack a mechanism to coordinate the evolving diagnostic state with prior operational experience during iterative investigation. OpsMem uses cross-memory resonance to activate only state-relevant long-term memory, conditions multi-agent diagnosis jointly on short-term and activated long-term memory, and consolidates reusable experience from solved incidents back into the long-term store. On a real-world Huawei microservice failure dataset it improves Match and Relevant by up to 46.88% and 18.39% over the strongest baseline.

### AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents
- **arXiv**: 2607.02255 ([link](https://arxiv.org/abs/2607.02255))
- **Date**: 2026-07-02
- **Category**: Optimization
- **Summary**: Proposes a bounded-memory contract in which every decision is made from a fresh user message assembled by typed retrieval, with no raw cross-decision transcript appended, so prompt size stays constant regardless of task duration and individual memory components can be ablated in isolation. Instantiated on Slay the Spire 2, which demands hundreds of sequential choices, the harness wins 6 of 10 games with strategic skills enabled versus 3 without. Releases 298 documented trajectories, frozen memory states, prompt records, and analysis tooling for reproducible study of how memory architecture drives long-horizon performance.

### MemSyco-Bench: Benchmarking Sycophancy in Agent Memory
- **arXiv**: 2607.01071 ([link](https://arxiv.org/abs/2607.01071))
- **Date**: 2026-07-01 (revised 2026-07-02)
- **Category**: Optimization
- **Summary**: Retrieved memory is not uniformly beneficial — it induces sycophancy, pushing agents to over-align with the user at the cost of factual accuracy and objective reasoning, a failure mode existing benchmarks miss because they only check whether memories were stored, retrieved, or updated correctly. MemSyco-Bench instead measures *when* memory should influence a decision and *how* valid memory should be used, across five tasks: rejecting memory as factual evidence, respecting its applicable scope, resolving memory-versus-evidence conflicts, tracking memory updates, and using valid memory for personalization.

### SF-AMS: Strategic Forgetting for Structured Memory in LLM Agent
- **arXiv**: 2607.22562 ([link](https://arxiv.org/abs/2607.22562))
- **Date**: 2026-05-29
- **Category**: Optimization
- **Summary**: Replaces static retrieval and heuristic time decay with a utility-driven survival mechanism that models each memory unit's long-term importance from usage redundancy and temporal signals, inducing a hierarchical structure that prioritizes stable entity-consistent information and filters noise. Composite Importance Scoring adds entity-level signals to semantic ones for retrieval robustness. On LoCoMo and LongMemEval-s it beats LightMem, MemO, and A-Mem, with the largest gain on multi-hop reasoning (+9.65 F1 under Qwen2.5-7B), then temporal reasoning (+6.91 F1) and open-domain tasks (+6.53 F1).

### AgentKVShift: Efficient KV Cache Reuse for Agentic Memory Systems
- **arXiv**: 2607.21604 ([link](https://arxiv.org/abs/2607.21604))
- **Date**: 2026-05-15
- **Category**: Optimization
- **Summary**: Every retrieval in a memory-augmented agent re-encodes structured memory units (summaries, keywords, tags) into KV states, and that prefill dominates inference cost; existing training-free KV reuse methods were built for RAG-style raw passages and degrade on curated agentic memory. AgentKVShift observes that the per-memory KV reuse residual decomposes into a shared memory-level offset plus small token-wise fluctuations, estimates that offset from a small probe set, and corrects *every* reused token rather than leaving un-recomputed tokens stale. Across four models (3B-32B) and two long-horizon agentic memory benchmarks it nears full-recompute quality while refreshing only 10-30% of the cache (up to 5x less recompute than baselines need), giving 2-3.5x prefill speedup on a single A100 and composing with KV quantization.

### Accurate and Efficient Long-Term Memory for LLM Agents
- **arXiv**: 2607.16211 ([link](https://arxiv.org/abs/2607.16211))
- **Date**: 2026-05-15
- **Category**: Optimization
- **Summary**: Attacks two coupled limitations of persistent agent memory — flat unstructured storage that loses the relational context needed for multi-hop and temporal reasoning, and reliance on expensive LLM-based classification that blocks latency-sensitive deployment — while noting such systems silently accumulate contradictions without validation. MOSAIC combines entity-typed graph storage over events, personas, and relationships; hash-accelerated dual-path retrieval that swaps LLM classification for locality-sensitive hashing; and active save-time conflict detection against existing graph neighbors that triggers updates or deletions. Reaches 89.35% on LoCoMo (+27.21 pp over the best baseline), best HaluMem extraction and QA scores, and detects 66% of injected factual conflicts versus 14% for the best baseline at 0.58 s average search latency.

### Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents
- **arXiv**: 2606.27472 ([link](https://arxiv.org/abs/2606.27472))
- **Date**: 2026-06-25
- **Category**: Optimization
- **Summary**: Isolates memory *maintenance* — using current fact values while discarding superseded ones as users relocate, prices shift, and plans change — as a distinct failure mode separate from comprehension. On LongMemEval's knowledge-update subset, replacing full context with bounded self-maintained memory drops gpt-5.4 from 92% to 77%, a gap that persists across model scales and is not recovered by proportionally expanding memory as conversation length grows 24x. Supersede is an open RL environment (verifiers/prime-rl) rewarding use of current values and penalizing outdated ones; GRPO fine-tuning of Qwen2.5-3B nearly doubles held-out performance (9.0% to 16.7%), showing the gap is trainable rather than merely measurable.

### Organize then Retrieve: Hierarchical Memory Navigation for Efficient Agents
- **arXiv**: 2606.11680 ([link](https://arxiv.org/abs/2606.11680))
- **Date**: 2026-06-10
- **Category**: Optimization
- **Summary**: Existing working-memory mechanisms rely on lossy compression or similarity-based retrieval and miss the temporal structure and causal dependencies multi-step agentic tasks need. HORMA organizes experience into a file-system-like hierarchy linking summarized entities to their raw trajectories, splitting working memory into structured construction — which iteratively refines the structure by distinguishing failures caused by missing information from those caused by misleading or overloaded context — and navigation-based retrieval by a lightweight RL-trained agent that traverses the hierarchy to select minimal sufficient context, cutting latency on the critical path. Across ALFWorld, LoCoMo, and LongMemEval it improves task performance under constrained context budgets while using at most 22.17% of baseline tokens on long conversations.

### Rethinking How to Remember: Beyond Atomic Facts in Lifelong LLM Agent Memory
- **arXiv**: 2605.19952 ([link](https://arxiv.org/abs/2605.19952))
- **Date**: 2026-05-19
- **Category**: Optimization
- **Summary**: The dominant extracted-fact paradigm compresses raw dialogue into atomic facts via handcrafted static prompts, discarding fine-grained detail, failing at deep reasoning over scattered isolated facts, and unable to hold extraction granularity constant across dialogue styles. TriMem keeps three coexisting granularities at once — raw dialogue segments anchored by source identifiers for storage fidelity, atomic facts for efficient retrieval, and synthesized profiles aggregating dispersed facts for deep reasoning — and applies TextGrad-based prompt optimization to refine extraction and profiling prompts from response-quality feedback, achieving lifelong evolution with no parameter updates. Consistently beats strong memory baselines on LoCoMo and PerLTQA across multiple backbones.
