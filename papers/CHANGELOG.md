# Changelog

Log of paper additions from each scheduled run. Newest first.

---

## 2026-08-04 (scheduled scan)

8 new papers (3 Security, 5 Optimization).

**A new arXiv announcement batch finally landed.** The 08-02 and 08-03 runs were
both pure backfills because 2026-07-30 was still the newest submission date and
nothing above 2607.28551 existed. That is no longer true: `cs.CR/recent`,
`cs.CL/recent`, `cs.AI/recent`, `cs.LG/recent` and `cs.MA/recent` now cover
announcements through Mon 2026-08-03, exposing the 2026-07-31 submission batch up
to 2607.29600. Five of the eight additions come from that batch and are genuinely
fresh rather than backfill. Note `arxiv.org/list/<cat>/2026-08` still returns "no
updates for this time period" and no 2608 ID exists yet.

Retrieval note: `export.arxiv.org/api/query` returned HTTP 429/503 for most of
this run after the first two calls, so category `/recent?show=250` listing pages
were used as the primary sweep instead. Every entry below was still verified
individually against its arXiv abstract page.

**Security:**

- **Memory Provenance Laundering in LLM Agents: A Non-Amplification Firewall for
  Persistent Memory** (2607.29167) — submitted 2026-07-31. Names memory
  provenance laundering: LLM-based consolidation rewrites an untrusted
  observation as apparent user history, keeping the action trigger while erasing
  the low-trust source that should cap its authority. Vulnerable consolidated
  memories reach 1.000 ASR; the PPMF middleware gates tool calls on
  action-risk-versus-memory-authority and blocks every evaluated unauthorized
  high-risk action.
- **Visual Inception: Compromising Long-term Planning in Agentic Recommenders via
  Multimodal Memory Poisoning** (2604.16966) — submitted 2026-04-18. Triggers in
  user-uploaded lifestyle photos sit dormant in an agentic recommender's
  long-term memory and hijack the reasoning chain when retrieved during later
  planning, with no prompt injection; ~85% Goal-Hit Rate, reduced to ~10% by the
  proposed CognitiveGuard dual-process defense.
- **MemoryGraft: Persistent Compromise of LLM Agents via Poisoned Experience
  Retrieval** (2512.16962) — submitted 2025-12-18. Poisons remembered
  *successful procedures* rather than facts, exploiting agents' semantic
  imitation heuristic; validated on MetaGPT DataInterpreter with GPT-4o, where a
  few grafted records dominate retrieved experiences on benign workloads and
  cause cross-session behavioral drift.

**Optimization:**

- **Zero-Mem: Zero-Token Memory Operations for LLM Agents** (2607.29377) —
  submitted 2026-07-31. No step outside final QA invokes an LLM or consumes LLM
  tokens; an entity-context graph plus a temporal hierarchy over preserved raw
  traces are weighed per query, cutting memory-operation time cost 57.6% versus
  the fastest baseline at equal reader and context budget.
- **Beyond Retrieval: Analytic Memory for Multimodal Agents** (2607.29440) —
  submitted 2026-07-31. Formulates analytic memory (filtering, aggregation,
  ranking, temporal comparison over accumulated observations) as complementary
  to retrieval memory; AdaMM discovers recurring field structures without an
  application-defined schema, +11.3% on MemEye and +7.3% on MemGallery.
- **TransMem: Transforming Hidden States into Memory for Large Language Models**
  (2607.29032) — submitted 2026-07-31. Inference-time parametric memory turning
  sparse historical hidden states of a frozen backbone into reusable
  representations via a gating network, trained by evidence-conditioned
  self-distillation; MemoryAgentBench average accuracy 29.54% to 40.00%.
- **HAM-VLN: Harnessing Hierarchical Agentic Memory for Zero-Shot
  Vision-and-Language Navigation** (2607.29600) — submitted 2026-07-31. Writes
  the memory inside the same model call that picks the next action, so
  maintenance costs no extra LLM calls; bounded verbatim window plus
  relevance/recency/salience retrieval over a depth-grounded world graph cuts
  context length by more than 65% while improving success rate.
- **Know It, Act on It: Investigating Memory Utilization in LLM Personalization**
  (2607.29433) — submitted 2026-07-31. Paired Know/Act tests over 1,000
  preferences, 16 systems and five memory architectures separate "failed to
  remember" from "remembered but failed to use"; agents routinely pass recall and
  fail the paired behavioral scenario, worst for health and therapy preferences.

**Checked and deliberately skipped:**

- *Co-Evolving Graph and Text Memory for Training-Free Multi-Hop QA* (2607.23278)
  — synchronized graph-text *working* memory within a reasoning chain, no
  persistent cross-session store; same boundary that keeps graph-RAG systems out.
- *When Unlearning Fails: Reliable Data Deletion under Post-Training in Agent
  Networks* (2607.28829) — deletion of training trajectories and model-side
  influence in federated agent networks, not an agent memory store; same
  boundary as the CACHE-UK exclusion on 08-03.
- *Memory Decoder at Scale* (2607.27919), *Understanding Is Done Early ...
  Unbounded-Context Memory* (2607.28263), *Recall Before You Rank* (2607.27692) —
  LLM-level parametric/long-context memory with no agent-memory framing. TransMem
  was included by contrast because it is evaluated on agent memory benchmarks
  (LoCoMo, MemoryAgentBench) and framed for long-context LLM agents.
- *ViSAGE* (2607.28678) — self-correcting memory for long-form video
  understanding, not an agent's persistent memory.
- Agent-security work with no memory component: *Piggybacking on Perception*
  (2607.28165), *Agent Harness Distillation* (2607.28147), *Early Detection of
  Distributed Backdoors in Multi-Agent LLM Systems* (2607.24893).
- Keyword collision: *Dimension Reduction for Quantum Adaptive Agents*
  (2607.19156) — quantum memory dimension, nothing to do with LLM agents.

Known remaining backlog carried over from 08-03 and still unrecorded (not a
claim of full coverage): 2606.30005, 2606.22844, 2606.08151, 2606.06090,
2606.04536, 2606.03463, 2605.20833, 2605.12260.

## 2026-08-03 [Conference scan]

2 new conference papers added (both Security), plus one venue backfill.

**USENIX Security 2026** — the Cycle 2 acceptances have now landed in the
technical-sessions program (~230+ papers, up from the 50 Cycle 1 papers that
were all this edition showed in the 07-13 and 07-20 scans). The dedicated
`cycle2-accepted-papers` URL is still a 404, so the program page is the
authoritative list. Direct WebFetch again returned HTTP 403; retrieved via the
`r.jina.ai` reader proxy. Each addition was verified against its official USENIX
presentation page.

- **HijackKV: New Threat in Position-Independent KV Cache Reuse** — USENIX
  Security 2026 (arXiv 2607.19957) — Security. Poisons a reused position-
  independent KV cache so a benign-looking chunk carries an attacker-controlled
  prefix into later victim queries; ~94% single-attempt success, persists across
  multi-turn interactions and transfers black-box.
- **When Memory Becomes a Vulnerability: Towards Multi-turn Jailbreak Attacks
  against Text-to-Image Generation Systems** — USENIX Security 2026 (arXiv
  2504.20376) — Security. "Inception" plants intent in the session memory of a
  T2I system and assembles prohibited semantics across turns via segmentation
  and recursion, so no single prompt trips the filter; +20.0pp ASR over prior
  work on commercial systems.

**Venue backfill (not a new entry):** *FragFuse: Bypassing Access Control of
Large Language Model Agents via Memory-Based Query Fragmentation and Fusion* was
already tracked from its arXiv preprint (2606.15609) and appears in the USENIX
Security '26 program. Added a `**Venue**` line to the existing entry and
recorded it in `conf_seen.json` so future conference scans skip it.

**IEEE S&P 2026 (Oakland)** — accepted-papers.html fetched directly (252 papers).
Unchanged from prior scans; no agent-memory papers. IEEE S&P 2027 Cycle 1
notifications are not due until March 2027, so there is no 2027 list to scan yet.
USENIX Security '27 pages do not exist yet (404).

**Scope note on the two additions.** Both sit just outside the usual
"LLM-agent memory store" framing and were judged in-scope deliberately:
HijackKV attacks a serving-layer KV cache, but that cache is a persistent
cross-session memory substrate and the tracker already covers KV-cache-as-memory
on both sides (*When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM
Collaboration*, *MemDecay*, *AgentKVShift*); excluding it would leave the
tracker covering KV-cache efficiency but not KV-cache poisoning. Inception
targets a T2I service rather than an LLM agent, but the vulnerability *is* the
system's multi-turn memory mechanism, and the fragment-across-memory-writes
pattern is the same one FragFuse uses against agent access control.

**Reviewed and excluded (USENIX Security 2026, Cycle 2 additions):**
- RAG-corpus security — *Confundo* (robust RAG poison), *BadGraph* (GraphRAG
  structural knowledge isolation), *Securing Retrieval-Augmented Code Generation
  via Contextual Knowledge Injection*. Static retrieval corpus, not an agent's
  persistent memory — same boundary that keeps PoisonedRAG/AgentPoison out.
- Prompt-injection work with no memory component — *MUZZLE* (agentic web-agent
  red-teaming), *AttriGuard* (IPI defense via tool-invocation attribution),
  *Overcoming the Retrieval Barrier*, *When AIOps Become "AI Oops"*.
- *Context Contamination in LLM Analysis of Network Security Logs* — single-
  context contamination, no persistent memory store.
- *Autonomy Comes with Costs* (resource-abuse DoS in LLM agents) — agent
  security, not memory.
- *Attacks on Approximate Caches in Text-to-Image Diffusion Models* — inference
  cache, no cross-session memory semantics.
- OS/hardware "memory" keyword collisions: *Download More RAM*, *Memclave*,
  *KernelRCA*, *SoK: On the Fragility of Memory Error Exploit Mitigations*,
  *Fence2Pwn*, *DMGuard*.

## 2026-08-03 (scheduled scan)

15 new papers (12 Security, 3 Optimization). Still no new arXiv announcement
batch: 2026-07-30 remains the newest submission date, the highest ID visible on
`cs.CR/recent` is 2607.28551, and nothing in the 2608 range exists yet. As on
2026-08-02, this run is therefore a backfill — but a targeted one. The previous
run added zero Security papers, so this run swept the memory-security literature
specifically (poisoning, injection, privacy leakage, membership inference,
provenance/lineage defenses) and found a substantial unrecorded backlog. Every
entry below was verified individually against its arXiv abstract page.

Known remaining backlog (identified, verified as unrecorded, deliberately
deferred to keep this run bounded — **not** a claim of full coverage): on the
Optimization side 2606.30005, 2606.22844, 2606.08151, 2606.06090, 2606.04536,
2606.03463, 2605.20833, 2605.12260 and others surfaced by the
"memory compression LLM agent" sweep. Future runs should continue this backfill.

Checked and deliberately skipped: MIRROR (2606.26793, memory-guided MCTS
red-teaming for agentic RAG — the "memory" is the attacker's search memory, not
agent memory as the asset), Inference Cost Attacks for Retrieval-Augmented LLMs
(2606.02643, RAG-level not agent-memory), Agent-Native Immune System (2606.28270,
broad agent-safety architecture, memory not central), Cyber-Capable AI Agents
(2607.25379) and Rethinking Penetration Testing for AI-Enabled Systems
(2607.14006, both agent security but not memory), CACHE-UK (2607.28292, model
editing for quantized LLMs rather than agent memory).

**Security:**

- **MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents**
  (2606.10742) — submitted 2026-06-09. Black-box trigger-conditioned retrieval
  attack plus post-retrieval induction via adversarial perturbation and stealthy
  OCR injection against graph-structured multimodal memory; up to 99.15% success
  on GPT-5-family web agents, transferring across architectures and scales.
- **SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM
  Agent Systems** (2606.12703) — submitted 2026-06-10. Names Multi-Session
  Memory Poisoning and gives the first certified bound for it: HMAC-SHA256 write
  provenance plus randomised memory ablation with verdict-based voting. Unsigned
  attack success 93-100% to 0%; end-to-end query-only attack 65.3% to 5.3%.
- **When Does Belief-Based Agent Memory Help? Reliability-Conditional Updating
  and Provenance-Capped Poisoning Defense** (2606.22030) — submitted 2026-06-20,
  revised 2026-07-16. Bayesian belief updating alone barely beats last-write-wins
  because benchmarks lack conflicting evidence; reliability-conditioned and
  provenance-capped updating is what turns it into a poisoning defense.
- **Manufactured Confidence: How Memory Consolidation Turns Hearsay into
  Confident Facts** (2606.29279) — submitted 2026-06-28. Memory products rewrite
  hedged remarks into confident dated assertions the agent then obeys, with no
  attacker needed; the agent responds to phrasing confidence rather than source,
  and one redundant source is the constructive fix.
- **Membrane: A Self-Evolving Contrastive Safety Memory for LLM Agent Defense**
  (2606.05743) — submitted 2026-06-04. Contrastive Safety Memory cells pair
  block-conditions with permit-conditions for superficially similar benign
  requests; best F1 on all six jailbreak attacks with benign refusal at 7-14%
  versus prior guards' 28-85%, stable under memory poisoning.
- **Hijacking Agent Memory: Stealthy Trojan Attacks Through Conversational
  Interaction** (2605.29960) — submitted 2026-05-28. MemPoison defeats the
  selective extraction and rewriting stages prior attacks ignore, via semantic
  relational bridging, entity masquerading, and joint embedding optimization;
  ASR up to 0.95, with evaluated defenses shown fundamentally limited.
- **MRMMIA: Membership Inference Attacks on Memory in Chat Agents** (2605.27825)
  — submitted 2026-05-27. Extends MIA from training corpora and retrieval
  databases to agent memory, using multiple recall probes to extract a membership
  signal across black-, gray-, and white-box settings.
- **The Misattribution Gap: When Memory Poisoning Looks Like Model Failure in
  Agentic AI Systems** (2605.22842) — submitted 2026-05-12. Formalizes Semantic
  Norm Drift and the Trust Laundering Chain; four safety classifiers produced
  zero detections across 510 checkpoints. Counterfactual Composition Testing hits
  87.5% attribution accuracy; releases the SND Corpus.
- **OEP: Poisoning Self-Evolving LLM Agents via Locally Correct but
  Non-Transferable Experiences** (2605.18930) — submitted 2026-05-18.
  Low-privilege black-box attack seeding clean, plausible edge-cases that bias
  reflection into over-generalized high-priority rules; >50% ASR on GPT-4o agents
  and survives LLM auditing defense.
- **MemLineage: Lineage-Guided Enforcement for LLM Agent Memory** (2605.14421) —
  submitted 2026-05-14. Chain-of-custody rather than filtering: Merkle log over
  Ed25519-signed entries, a weighted derivation DAG, and a sensitive-action gate
  that refuses dispatches descending from an external ancestor. Only configuration
  reaching zero ASR on all three workloads at sub-millisecond overhead.
- **ShadowMerge: A Novel Poisoning Attack on Graph-Based Agent Memory via
  Relation-Channel Conflicts** (2605.09033) — submitted 2026-05-09, revised
  2026-05-15. Poisoned relation shares the query-activated anchor and
  canonicalized relation channel with benign evidence while carrying a conflicting
  value; 93.8% ASR on Mem0 (+50.3 points), responsibly disclosed to vendors.
- **Observable Channels, Not Just Storage: Evaluating Privacy Leakage in LLM
  Agent Pipelines** (2603.22751) — submitted 2026-03-24, revised 2026-03-30.
  CIPL gives one channel-oriented protocol spanning memory-, retrieval-, and
  tool-mediated targets; memory is a near-saturated high-risk special case while
  leakage overall is governed by channel conditions, not a dominant attack recipe.

**Optimization:**

- **Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents**
  (2606.27472) — submitted 2026-06-25. Bounded self-maintained memory drops
  gpt-5.4 from 92% to 77% on LongMemEval's knowledge-update subset; the released
  RL environment nearly doubles held-out performance for Qwen2.5-3B under GRPO,
  showing the maintenance gap is trainable, not just measurable.
- **Organize then Retrieve: Hierarchical Memory Navigation for Efficient Agents**
  (2606.11680) — submitted 2026-06-10. HORMA builds a file-system-like hierarchy
  linking summaries to raw trajectories and navigates it with a lightweight
  RL-trained retriever; matches or beats baselines on ALFWorld, LoCoMo, and
  LongMemEval using at most 22.17% of baseline tokens on long conversations.
- **Rethinking How to Remember: Beyond Atomic Facts in Lifelong LLM Agent
  Memory** (2605.19952) — submitted 2026-05-19. TriMem keeps raw segments,
  atomic facts, and synthesized profiles coexisting at three granularities and
  refines its extraction prompts with TextGrad, evolving without parameter
  updates; beats strong baselines on LoCoMo and PerLTQA.

---

## 2026-08-02 (scheduled scan)

11 new papers (0 Security, 11 Optimization). No new announcement batch since the
previous run: 2026-07-30 is still the newest submission date on arXiv (2026-07-31
is a Friday whose submissions are announced Sunday evening ET, and 2026-08-01 /
2026-08-02 fall on the weekend). This run is therefore entirely a backfill of
clearly on-topic papers earlier runs missed, verified one by one against their
abstract pages. Three of them (2607.22562, 2607.21604, 2607.16211) carry 2607
identifiers but May 2026 submission timestamps on arXiv — the date recorded is
the one arXiv reports. A targeted sweep of the memory-security literature turned
up no unrecorded papers, hence zero Security additions.

Checked and deliberately skipped as off-topic or not memory-central:
Isolation as a First-Class Principle for LLM-Agent System Safety (2607.12406,
isolation-boundary survey, memory only one attack type among many), MemVLN
(2607.23504, visual-token resolution in a VLN architecture rather than an agent
memory system), SemPIC (2607.28069, KV-cache method with no agent-memory
framing), Dimension Reduction for Quantum Adaptive Agents (2607.19156, keyword
collision on "memory").

**Optimization:**

- **Voice Memory for Agentic Speech Recognition** (2607.26410) — submitted
  2026-07-29. Frozen corrector reads a per-domain memory file and abstains when
  unsure while an asynchronous score-gated optimizer edits that file; cuts
  over-correction from 64% to 35% of edits and weighted WER from 8.36% to 7.52%
  across ten HyPoradise domains, adding zero inference-path parameters.
- **Exploratory and Assimilating Reflection: Reflective Recall Cycle for
  Long-term Memory** (2607.17879) — submitted 2026-07-20. Iterative exploratory
  search bootstraps retrieval and fills an Experience Buffer that is replayed to
  refine a global reranker; up to 17.9% retrieval improvement on two long-term
  dialogue benchmarks, sample-efficient and robust to noisy feedback.
- **RECON: Benchmarking Agent Memory for Compositional Reasoning over Long
  Contexts** (2607.16716) — submitted 2026-07-18. 24 case files of 50k-100k
  tokens testing what happens after a fact changes (cascading invalidation,
  surviving independent support, counterfactual timelines); best non-Oracle
  system reaches only 22.4% accuracy.
- **From Memory to Skills: Evidence-Grounded Co-Evolution Governance for
  Long-Horizon LLM Agents** (2607.16621) — submitted 2026-07-18. Training-free
  MSCE crystallizes positive-expected-gain policies into callable skills with
  evidence links, applicability constraints, and reliability estimates, using
  reflection-weighted value backfilling to densify sparse terminal feedback.
- **AgentBrew: Lifelong Knowledge Brewing from Strong Teachers to Weak LLM
  Agents** (2607.16851) — submitted 2026-07-18. Distills teacher interactive
  experience into persistent external memory for a compact student with no
  weight updates, demonstrations, labels, or test-time teacher access.
- **OpsMem: Dual-Memory Reasoning with Cross-Memory Resonance for Failure
  Diagnosis** (2607.11357) — submitted 2026-07-13. Activates only state-relevant
  long-term memory, conditions multi-agent diagnosis on short-term plus activated
  long-term memory, and consolidates solved incidents back; +46.88% Match and
  +18.39% Relevant over the strongest baseline on a Huawei microservice dataset.
- **AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents**
  (2607.02255) — submitted 2026-07-02. Bounded-memory contract keeps prompt size
  constant regardless of task duration via typed retrieval with no appended
  transcript; 6/10 wins with strategic skills versus 3/10 without on Slay the
  Spire 2, with 298 trajectories and frozen memory states released.
- **MemSyco-Bench: Benchmarking Sycophancy in Agent Memory** (2607.01071) —
  submitted 2026-07-01, revised 2026-07-02. Five tasks measuring when memory
  should influence a decision and how valid memory should be used, covering a
  failure mode storage/retrieval-correctness benchmarks miss entirely.
- **SF-AMS: Strategic Forgetting for Structured Memory in LLM Agent**
  (2607.22562) — submitted 2026-05-29. Utility-driven survival mechanism
  replacing static retrieval and heuristic decay; beats LightMem, MemO, and
  A-Mem with +9.65 F1 on multi-hop reasoning under Qwen2.5-7B.
- **AgentKVShift: Efficient KV Cache Reuse for Agentic Memory Systems**
  (2607.21604) — submitted 2026-05-15. Decomposes the per-memory KV reuse
  residual into a shared offset plus token-wise fluctuations and corrects even
  un-recomputed tokens; near full-recompute quality at 10-30% refresh, 2-3.5x
  prefill speedup on an A100.
- **Accurate and Efficient Long-Term Memory for LLM Agents** (2607.16211) —
  submitted 2026-05-15. MOSAIC pairs entity-typed graph storage with
  LSH-accelerated retrieval and save-time conflict detection: 89.35% on LoCoMo
  (+27.21 pp), 66% of injected conflicts detected versus 14%, 0.58 s per query.

---

## 2026-08-01 (scheduled scan)

14 new papers (4 Security, 10 Optimization). The 2026-07-30 announcement batch
supplied seven of them; the other seven are a backfill of clearly on-topic
2026-07-20 to 2026-07-23 submissions that earlier runs missed. No 2026-07-31
submissions were available — 2026-08-01 is a Saturday and arXiv does not
announce over the weekend, so 2026-07-30 is the newest announced batch.

**Security:**

- **MIND: Lightweight and Effective Memory Injection Defense for LLM Agents via
  Intent-Aware Information Bottleneck** (2607.28103) — submitted 2026-07-30.
  Intent-aware information bottleneck plus a lightweight detector; cuts mean
  ASR-r/ASR-a by 55.4%/55.3% on ReAct-StrategyQA at undefended accuracy and
  latency, avoiding repeated LLM auditing.
- **MemTxn: A Transaction Boundary for Source-Supported Updates and
  Complete-State Recovery in Agent Memory** (2607.27834) — submitted
  2026-07-30. Governance layer validating writes against cited sources; accepts
  60/60 supported originals, rejects 179/179 hard negatives, and restores the
  complete declared active map under persistent multi-key faults.
- **Auditing Provenance Sensitivity in LLM Agent Action Selection** (2607.20827)
  — submitted 2026-07-23. Holds evidence content fixed and varies only
  provenance: unauthorized evidence changes the selected action in ~2.4% of
  comparisons, and trusted/untrusted variants diverge in 5.4% of competing cases.
- **Self-State Attacks on Self-Hosted AI Agents: How Far Can OS Defenses Go?**
  (2607.17986) — submitted 2026-07-20. 43 concrete operations corrupting an
  agent's own memory and config files via ordinary OS syscalls; a residual
  surface stays structurally indistinguishable from legitimate writes.

**Optimization:**

- **MemHarness: Memory Is Reconstructed, Not Replayed** (2607.28272) —
  submitted 2026-07-30. GRPO-trained policy reconstructs retrieved experience
  against the current state instead of replaying it verbatim, removing negative
  transfer on ALFWorld/WebShop.
- **RRM: Experience-Driven Reflective Retrieval Memory for Long-Horizon
  Multimodal Reasoning** (2607.28156) — submitted 2026-07-30. Reflective
  experience memory distilling reusable retrieval strategies, regulated by usage
  frequency, reuse feedback, and temporal decay.
- **Sigma-Mem: An Online Reliability Memory for LLM-based Multi-Agent Systems**
  (2607.27958) — submitted 2026-07-30. Stores per-peer competence and peer
  relationship evidence as symmetric states with Weyl-bounded online updates.
- **ChronoMem: Version Control and Semantic Rollback for Large Language Model
  Agent Memory** (2607.27773) — submitted 2026-07-30. Snapshot-per-write
  version history in Google's ADK with natural-language rollback and a
  post-exposure counterfactual evaluation protocol.
- **SKILL-KD: Contrastive Skill Distillation for LLM Agents** (2607.28048) —
  submitted 2026-07-30. Distills student/teacher trajectory discrepancies into
  skill patches, with Drift-Aware Skill Consolidation deciding add/delete/modify
  or skip per patch.
- **Bridging Inference-Time Scaling and Episodic Memory with Action-Centric
  Graphs** (2607.27415) — submitted 2026-07-29. GAMER decouples episodic memory
  from the LLM as an action-centric graph with TD-learned action values;
  +20.81%/+6.17% success/progress rate.
- **Retain or Consolidate? Budget-Dependent Operator Selection for Language
  Agent Memory** (2607.17545) — submitted 2026-07-20, revised 2026-07-21.
  Decomposes Merge/Abstract/Rewrite utility into coverage and replacement
  effects; consolidation gains up to 48% absolute accuracy under tight budgets
  while retention wins under loose ones.
- **AttriMem: Attribution-Guided Process Feedback for Agent Memory Learning**
  (2607.21106) — submitted 2026-07-23. Adds local rewards from token-level
  contributions to the final answer, resolving the credit-assignment bottleneck
  in RL-learned memory-construction policies.
- **PRO-LONG: Programmatic Memory Enables Long-Horizon Reasoning** (2607.20064)
  — submitted 2026-07-22, revised 2026-07-23. Keeps a complete structured
  interaction log and searches it programmatically: +18.0 points on ARC-AGI-3
  with 4.2-5.8x fewer tokens.
- **Agentic Context Management: Solving Agent Memory and Cost by Treating Them
  as Lifecycle and Architecture Problems** (2607.21503) — submitted 2026-07-23.
  Five-activity context lifecycle; naive accumulation is quadratic in token cost
  while validated compaction stays linear at preserved accuracy. Distinct from
  the similarly named ACM paper (2607.23809) already tracked.

Checked and deliberately excluded: 2607.28069 (SemPIC, position-independent KV
caching — an inference-serving cache system, not an agent memory system),
2607.19156 (quantum adaptive agents — keyword collision on "memory").

---

## 2026-07-31 (scheduled scan)

12 new papers (3 Security, 9 Optimization). Two entries (RSMeM, IFCMemoryBench)
carry older submission dates but were only announced in the 2026-07-29 batch, so
no prior run could have seen them.

**Security:**

- **Isolated but Exposed: Persistence-Based Memory Extraction Attack on LLM
  Agents** (2607.23444) — submitted 2026-07-26. SPORE exfiltrates private
  long-term memory through malicious tool-invocation parameters without
  violating per-user isolation; 80.0% record extraction, and extracted records
  can be re-attributed to specific users in multi-user deployments.
- **ContainmentBench: Trace-Based Evaluation of Post-Injection Containment in
  Tool-Using LLM Agents** (2607.23999) — submitted 2026-07-27, revised
  2026-07-28. Shows identical "no committed harm" endpoints hide very different
  memory-contamination traces; 73.5% of matched tainted pairs diverge in
  trajectory or utility.
- **MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence
  and Repair** (2607.27080) — submitted 2026-07-29. Write-Execute-Forget
  protocol over 310 cases: poisoned content persists in 84.2% of cases, and
  repair capability varies 41.3 points across 24 memory-system configurations.

**Optimization:**

- **RSMeM: Knowledge-Enhanced Memory Evolution for Remote Sensing Agents**
  (2607.24772) — submitted 2026-06-11, announced late July. Distills
  failure-annotated tool traces into reusable constraints; +6% accuracy for
  under 1% extra experience tokens.
- **IFCMemoryBench: Evaluating Long-Term Memory of LLM-Based Agents in BIM
  Information Retrieval** (2607.26072) — submitted 2026-07-13, announced
  2026-07-29. 143 multi-session tasks over 4,016 seeded prior sessions; best
  system reaches only 32.4% accuracy under realistic ingestion scope.
- **ACM: Agentic Context Management for Long Horizon Tasks** (2607.23809) —
  submitted 2026-07-26. Exposes compression/offload/retrieve as agent-invoked
  tools instead of fixed triggers, cutting peak token pressure losslessly.
- **MemLens: A Value-Aware Memory Management System with Interactive Analytics**
  (2607.25992) — submitted 2026-07-28. Shapley-style memory valuation plus a
  lifecycle dashboard comparing strategies on quality, latency, and tokens.
- **A Graph-Native Bitemporal Memory Store for Conversational AI Agents**
  (2607.26520) — submitted 2026-07-29. Neo4j identity/content versioning with
  valid time and transaction time; 46.7% R@10 on LongMemEval, 80% on
  knowledge-update questions.
- **Living-Harness Is an Interactive-Agent Evolver** (2607.26598) — submitted
  2026-07-29. Turns trajectories into bounded harness updates written as
  episodic memory plus a repair state graph; +10.07/+9.91 points, transferable
  across backbones.
- **Filesystem-Based Memory for LLM Agents: Organization, Evolution, and
  Sustainability** (2607.26637) — submitted 2026-07-29. Organized markdown
  stores roughly halve retrieval cost at scale, but agents cannot sustain the
  organization, and tooling shapes structure as much as the model does.
- **Metis: Memory Foundation Model** (2607.26760) — submitted 2026-07-29. Native
  memory state inside the backbone accessed via memory attention, evolving
  through the forward pass with frozen weights.
- **Setoka: A Benchmark for Hierarchical User Understanding in Personalized
  Agents over Heterogeneous Data** (2607.27056) — submitted 2026-07-29. Four
  levels (semantic, episodic, behavior pattern, personality); five memory
  systems degrade sharply above the semantic level.

---

## 2026-07-30 (scheduled scan)

14 new papers (4 Security, 10 Optimization). Large batch because the previous
recorded run was 2026-07-21, leaving a nine-day backlog (the local cron only
fires while this machine is on).

**Security:**

- **ChannelGuard: Safe Models Do Not Compose into Safe Multi-Agent Systems**
  (2607.19430) — submitted 2026-07-20. Information-bottleneck gates on every
  inter-agent channel; shows an "apparently safe" undefended pipeline owed its
  0.000 tool-/memory-poisoning success almost entirely to the cloud provider's
  server-side filter.
- **The Chronos Vulnerability: A Taxonomy of Temporal Persistence and
  Memory-Based Deception in Agentic AI** (2607.19433) — submitted 2026-07-20.
  Formalizes memory-based attacks that decouple compromise from effect in time
  (memory injection, sleeper agents, "Dynamics Blindness").
- **ConsistencyGate: Preventing Memory Contamination in LLM Agents via
  Self-Consistency Admission Control** (2607.22962) — submitted 2026-07-25.
  Write-time admission gate that blocks hallucinated facts from persisting as
  false premises; three new contamination benchmarks.
- **MemTX: Transactional Belief Commit for Stateful Agent Memory** (2607.23929)
  — submitted 2026-07-27 (v2 2026-07-28). Snapshot-isolated memory
  transactions with provenance/validity, tool calls gated on belief state, and
  cascading repair on retraction.

**Optimization:**

- **Profile-Graph Memory for LLM Agents** (2607.19359) — abstract page lists
  v1 as 2026-06-01 despite the 2607 identifier; recorded as listed. MemHop
  multi-hop benchmark plus ProGraph two-layer profile/residual memory.
- **LazyMem: Retrieve Broadly, Construct Selectively** (2607.22690) —
  submitted 2026-07-17 (v2 2026-07-28). Query-time memory construction;
  0.85 LongMemEval accuracy at 213 context tokens, 21x fewer than baseline.
- **Beyond Memory Leaderboards: Evaluating Scientific Memory as Budgeted
  Context Restoration** (2607.16848) — submitted 2026-07-18. Shows a leading
  system's win vanishes once retrieval budget is controlled.
- **Mechanistic Attention Guidance for Agent Memory Refinement** (2607.17621)
  — submitted 2026-07-20. Retrieval-head attention as a utilization signal for
  segment-level memory updates (AGMR).
- **Supra Cognitive Modes: A Routed Architecture for Agent Memory**
  (2607.19096) — submitted 2026-07-21. Per-query mode routing over a shared
  substrate; note the paper itself states token ledgers and timing are
  unavailable, so efficiency claims are unverified.
- **MemTools: A Unified Research Framework for Interoperable Agent Memory**
  (2607.21404) — submitted 2026-07-23. Declarative lifecycle contracts for
  swapping memory components across systems.
- **Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory**
  (2607.21962) — submitted 2026-07-24. Ground-truth-first corpus construction;
  memory-architecture rankings invert as interaction history lengthens.
- **Keep It InMind: Benchmarking the Implicit-Association Blind Spot in Agent
  Memory** (2607.24368) — submitted 2026-07-27. 84.0% in-context vs at most
  14.4% retrieved on indirect queries needing a world-knowledge bridge.
- **MemChain: Learning Interpretable Memory Traces** (2607.24097) — submitted
  2026-07-27. Trainable post-retrieval policy producing compact grounded
  evidence contexts (TMPO objective).
- **UniMem: Complementary Episodic-to-Parametric Memory** (2607.26017) —
  submitted 2026-07-28. Routing tokens consolidate recurring patterns into
  expandable parametric memory without task boundaries.

All fourteen verified against their arXiv abstract pages before inclusion.
Surfaced via date-sorted `export.arxiv.org` API queries on agent-memory,
memory-poisoning/injection, and long-term-memory/compression term sets across
cs.AI, cs.CL, cs.CR, cs.LG, cs.MA, cross-checked with web search. Note:
`export.arxiv.org` began returning HTTP 429 partway through, so verification
was completed against `arxiv.org/abs/<id>` pages instead.

**Near-misses considered and excluded:**

- 2607.19292 (hidden safety-critical challenges perspective) and 2607.12406
  (isolation as a first-class principle for LLM-agent safety) — broad agent
  safety taxonomies where memory is one of several layers/boundaries, not
  agent-memory-specific.
- 2607.19156 (dimension reduction for quantum adaptive agents) — keyword
  collision on "memory"; quantum information, unrelated to LLM agents.
- 2607.25415 (learnable agent harness / control system), 2607.14275 (context
  quality metrics), 2607.18886 (traceability-driven multi-agent development) —
  agentic but not memory systems.
- 2607.11787 (forgetting and conceptual alignment in a coordination game),
  2607.11377 (long-term physical coexistence with robots), 2607.09322
  (LongMedBench) — memory-adjacent but not agent-memory security or
  optimization contributions.
- 2607.11357 (OpsMem) and 2607.05577 (narrative writer memory) — plausible
  Optimization entries but well outside the current window (2026-07-13 and
  2026-07-06); left unrecorded rather than back-filled.
- Several June-dated agent-memory papers surfaced by the same queries
  (2606.29914, 2606.29774, 2606.28270, 2606.27499, 2606.25206) — far outside
  the scan window.

---

## 2026-07-21 (scheduled scan)

1 new paper (Security):

- **Do Agents Dream of False Memories? Black-box Visual Attacks on Long-term
  Memory in Multimodal AI Agents** (2607.15657) — verified against its abstract
  page; submitted 2026-07-17. Introduces Lucid, a black-box framework that
  attacks the long-term memory of multimodal AI agents via imperceptible image
  perturbations (memory poisoning and memory injection modes), extending
  memory-poisoning threats from text to the visual channel; reports 61.6% /
  58.4% success across multiple memory architectures.

Surfaced via the cs.CR date-sorted API query (highest ID in the July 16-17
batch). Cross-checked cs.AI, cs.CL, cs.LG, and cs.MA listings plus
"long-term memory / memory compression / memory management" term searches for
the July 16-21 window; nothing announced from July 18-21 (weekend gap — arXiv's
newest on-topic listings top out at July 17).

**Near-misses considered and excluded:**
- MemDefrag: Latent Memory Defragmentation for Large Language Models
  (2607.05969, submitted 2026-07-07, revised 2026-07-15) — training-free
  ranking/reordering/forgetting over stored "memories," but those memories are
  the model's own per-layer hidden states (an internal latent-representation
  store), not an agent's external/episodic/RAG memory system. Out of scope
  (model-internal memory, not agent memory). Excluded.
- Stigmergic Graph Memory (2607.15182) — shared environment map for classical
  multi-agent pickup/delivery (MAPF), not an LLM/RAG agent memory system.
  Keyword collision. Excluded.
- VTM-Nav (2607.14514), ReflectWorld-MM (2607.09759), LightMem-Ego (2607.11487)
  — memory systems for embodied navigation / multimodal video / personal-life
  logging; not security- or optimization-focused on the memory subsystem in the
  senses this tracker follows. Excluded.

## 2026-07-20 (Conference scan)

No new conference papers found.

Checked the official accepted-papers lists for both tracked venues:
- **USENIX Security 2026** — Cycle 1 accepted papers (50 papers). Direct WebFetch
  returned HTTP 403; retrieved successfully via the `r.jina.ai` reader proxy.
  No agent-memory papers. The Cycle 2 accepted-papers page does not yet exist
  (404), so Cycle 1 is the full published coverage for this edition so far.
- **IEEE S&P 2026 (Oakland)** — accepted-papers.html (254 papers), fetched
  directly. No agent-memory papers.

`conf_seen.json` is still empty; nothing added this run.

**Near-misses considered and excluded (IEEE S&P 2026):**
- GraphRAG under Fire (arXiv 2501.14050) — poisoning of GraphRAG's static
  external knowledge-graph corpus for QA (GragPoison). General RAG-corpus
  security, not persistent agent memory. Excluded.
- Who Taught the Lie? Responsibility Attribution for Poisoned Knowledge in
  Retrieval-Augmented Generation (RAGOrigin, arXiv 2509.13772) — attributes
  which knowledge-database texts caused a RAG misgeneration. General RAG
  corpus, not agent memory. Excluded.
- AttnTrace: Contextual Attribution of Prompt Injection and Knowledge
  Corruption (arXiv 2508.03793) — general prompt-injection/context attribution,
  not agent memory. Excluded.
- Recovering and Rehosting Mobile Local LLM Conversations and Contexts via
  Memory Forensics — device/RAM memory forensics, a keyword collision on
  "memory", not an agent-memory system. Excluded.
- Also noted but out of scope for this scan: ShadowMerge (arXiv 2605.09033), a
  genuine graph-based agent-memory poisoning attack, is an arXiv-only preprint
  not on either venue's accepted list; left to the daily arXiv scan.

## 2026-07-20 (scheduled scan)

1 new paper (Security):

- **Bad Memory: Evaluating Prompt Injection Risks from Memory in Agentic Systems**
  (2607.14611) — verified against its abstract page; submitted 2026-07-16.
  Empirically evaluates prompt-injection risk from the persistent state (memory
  files, preferences, knowledge bases) agentic systems carry across sessions:
  agents resist overwriting their own memory, but payloads already resident in
  memory files are effective attack vectors for current and future sessions.

Surfaced via the cs.MA / cs.CR "recent" listings — the arXiv abstract-search
index still lags to ~2026-07-14, so date-sorted API queries did not return it.
Cross-checked cs.AI, cs.CL, cs.LG, and cs.MA "recent" listings plus multiple
web/API searches for the July 15-20 window.

**Near-misses considered and excluded:**
- PReM: Learning What to Preserve and When to Refresh for Context Compression
  (2607.14327, 2026-07-15) — re-verified against its abstract page; a generic
  long-context KV-cache/context-compression method for single-shot LLM inference
  (32K-token QA). Makes no mention of agents, tool use, multi-turn tasks, or
  agent memory, unlike the agent-framed compaction papers already tracked
  (2607.08032, 2607.10582). Out of scope (agent memory) — excluded.
- Forgetting Our Way to Shared Meaning (2607.11787) — a human coordination-game
  study on conceptual forgetting; keyword collision on "forgetting", not agent
  memory. Excluded.

## 2026-07-19 (scheduled scan)

No new papers found.

Searched arXiv (cs.AI, cs.CL, cs.CR, cs.LG, cs.MA) and the web for new
agent-memory security/optimization papers, focusing on the July 16-19 window.
The arXiv full-text search index still lags to ~2026-07-14, and seen_ids already
covers through 2026-07-16 (added by the 2026-07-18 run); today is a Sunday, when
arXiv does not announce new submissions, so no fresh on-topic papers had appeared.
Queried the arXiv API by "agent memory" plus security terms (memory
poisoning/injection/extraction) and optimization terms
(compression/retrieval/forgetting/consolidation/efficiency); every result was
already in seen_ids or off-topic.

**Near-misses considered and excluded:**
- Isolation as a First-Class Principle for LLM-Agent System Safety (2607.12406) —
  re-verified against its abstract page; a five-boundary agent-safety taxonomy
  where memory poisoning is only one failure type, not a memory-focused
  contribution. Already excluded on prior runs; kept excluded.
- MemSyco-Bench: Benchmarking Sycophancy in Agent Memory (2607.01071) and MemDelta:
  Controlled Baselines and Hidden Confounds in Agent Memory Evaluation (2606.29914)
  — evaluation/benchmark methodology for agent memory, not a security
  (poisoning/privacy/access) or optimization (compression/retrieval/forgetting)
  technique; also both well outside the recent window.

## 2026-07-18 (scheduled scan)

Searched arXiv (cs.AI, cs.CL, cs.CR, cs.LG, cs.MA) and the web for new
agent-memory papers, focusing on the July 14-18 window (the 2026-07-17 run
covered through July 15). arXiv has now indexed submissions through 2026-07-16
(newest on-topic IDs 2607.146xx). Found 5 new, verified, on-topic papers (each
checked against its arXiv abstract page).

**Security (2):**
- MemPoison: Uncovering Persistent Memory Threats and Structural Blind Spots in LLM Agents (2607.14651) — 2026-07-16
- Token-Flow Firewall: Semantic Runtime Auditing for Persistent AI Agents (2607.08395) — 2026-07-09

**Optimization (3):**
- Track, Rank, Crack: Epistemic Working Memory Scales Multi-Hop Reasoning in Language Agents (2607.12267) — 2026-07-14
- MemoHarness: Agent Harnesses That Learn from Experience (2607.14159) — 2026-07-14
- MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations (2607.12893) — 2026-07-14

**Near-misses considered and excluded:**
- Isolation as a First-Class Principle (2607.12406), Critic Experience Bank
  (2607.12397), and PM-Bench (2607.12385) — all previously logged as near-misses
  on the 2026-07-16/07-17 runs and unchanged; kept excluded for consistency.
  Isolation is a five-boundary agent-safety taxonomy where memory poisoning is
  only one failure type, not a memory-focused contribution.
- Out of Sight: Compression-Aware Content Protection against Agentic Crawlers
  (2607.08180) — content-watermarking defense against crawlers, not an
  agent-memory security or optimization technique.
- RetroAgent (2607.14512), Forgetting Our Way to Shared Meaning (2607.11787) —
  a domain-specific retrosynthesis planner and a coordination-game study of
  forgetting; neither a memory security nor a compression/efficiency technique.

Token-Flow Firewall (2607.08395) is dated 2026-07-09, just outside the recent
window, but was not previously tracked and treats persistent memory updates as a
core attack surface, so it is included per the "clearly relevant, not yet seen"
allowance.

## 2026-07-17 (scheduled scan)

Searched arXiv (cs.AI, cs.CL, cs.CR, cs.LG, cs.MA) and the web for new
agent-memory papers, focusing on the July 14-17 window (the 2026-07-16 run
covered through July 14). arXiv has now indexed submissions through 2026-07-15
(newest IDs 2607.138xx). Found 3 new, verified, on-topic papers (each checked
against its arXiv abstract page). No new Security papers this run — the security
search surfaced only already-tracked entries.

**Optimization (3):**
- Oracle Agent Memory as an Enterprise Memory Substrate for Long-Horizon AI Agents (2607.13157) — 2026-07-14
- Memory as a Controlled Process: Learned Adaptive Memory Management for LLM Agents (2607.13591) — 2026-07-15
- Experience Memory Graph: One-Shot Error Correction for Agents (2607.13884) — 2026-07-15

**Near-misses considered and excluded:**
- Critic Experience Bank (2607.12397), PM-Bench (2607.12385), Isolation as a
  First-Class Principle (2607.12406), PalmClaw (2607.13027), and the
  self-improving-agents architecture (2607.12254) — all previously logged as
  near-misses on the 2026-07-16 run and unchanged.
- Forgetting Our Way to Shared Meaning (2607.11787) and LongMedBench (2607.09322) —
  a coordination-game study of forgetting and a medical long-horizon benchmark;
  neither a memory security nor a compression/efficiency technique.

The late-June/May backlog flagged on prior runs (Memory Contagion, MemVenom,
RaMem, Hijacking agent memory 2605.29960, MRMS 2607.04617, etc.) remains
available for a deliberate backfill if wanted.

## 2026-07-16 (scheduled scan)

Searched arXiv (cs.AI, cs.CL, cs.CR, cs.LG, cs.MA) and the web for new
agent-memory papers, focusing on the July 13-15 window (the 2026-07-15 run
covered through July 13). arXiv has now indexed submissions through 2026-07-14
(newest ID 2607.13027); nothing dated July 15 is announced yet. Found 2 new,
verified, on-topic papers (each checked against its arXiv abstract page). No new
Security papers this run.

**Optimization (2):**
- ToolAtlas: Learning Once, Reusing Everywhere with Tool-Side Memory (2607.11126) — 2026-07-13
- Speculate with Memory: Lossless Acceleration for LLM Agents (2607.12236) — 2026-07-14

**Near-misses considered and excluded:**
- Isolation as a First-Class Principle for LLM-Agent System Safety (2607.12406) —
  a boundary/isolation safety taxonomy across five agent interfaces; touches
  memory poisoning as one vector but is a system-safety survey, not a memory
  mechanism.
- Critic Experience Bank (2607.12397) — a self-evolving memory bank of past
  judgments, but the contribution is step-level confidence calibration, not a
  memory security or compression/efficiency method.
- PM-Bench: Evaluating Prospective Memory in LLM Agents (2607.12385) — benchmarks
  the cognitive capability of executing delayed intentions; a memory-evaluation
  benchmark, neither a security nor optimization technique.
- A Formal Hierarchical Architecture for Agentic Orchestration with Stack-Based
  Execution and Lazy Discovery (2607.11138) — tool-registry routing/orchestration
  efficiency where lazy memory and branch isolation are byproducts, not an
  agent-memory contribution.
- PalmClaw (2607.13027) and "How to Realize Recursively Self-Improving Agents"
  (2607.12254) — an on-device mobile agent framework and a multi-agent
  self-improvement architecture; memory is an incidental component in both.

The late-June/May backlog flagged on prior runs (Memory Contagion, MemVenom,
RaMem, Hijacking agent memory 2605.29960, MRMS 2607.04617, etc.) remains
available for a deliberate backfill if wanted.

## 2026-07-15 (scheduled scan)

Searched arXiv (cs.AI, cs.CL, cs.CR, cs.LG, cs.MA) and the web for new
agent-memory papers, focusing on the July 11-14 window (the 2026-07-14 run
covered through July 10). arXiv has now indexed submissions through 2026-07-13
(newest IDs 2607.117xx). Found 4 new, verified, on-topic papers (each checked
against its arXiv abstract page).

**Security (2):**
- The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory (2607.10608) — 2026-07-12
- Agents Don't Just Agree, They Remember: Benchmarking Persistent Sycophancy in Stateful Personal Agents (2607.10526) — 2026-07-12

**Optimization (2):**
- MemDecay: Region-Aware KV Cache Eviction for Efficient LLM Agent Inference (2607.10582) — 2026-07-12
- AAFLOW+: Stateful Operator Abstraction with Zero-Copy Distributed KV Cache Orchestration for Multi-Agent Workflows (2607.10987) — 2026-07-13

**Near-misses considered and excluded:**
- Forgetting Our Way to Shared Meaning (2607.11787) — a coordination-game /
  cognitive-science study of how forgetting affects conceptual alignment among
  players, not an engineered LLM-agent memory system for security/optimization.
- OpsMem: Dual-Memory Reasoning with Cross-Memory Resonance for Failure
  Diagnosis (2607.11357) — memory is the central mechanism, but the contribution
  targets diagnostic reasoning quality in a narrow AIOps domain rather than the
  security or optimization axes this tracker follows.
- Vinci2 (2607.11523) and A Glimpse into Long-term Physical Coexistence with
  Intelligent Robots (2607.11377) — egocentric-video / robotics application
  papers that use persistent memory incidentally.

The late-June/May backlog flagged on prior runs (Memory Contagion, MemVenom,
RaMem, Hijacking agent memory 2605.29960, MRMS 2607.04617, etc.) remains
available for a deliberate backfill if wanted.

## 2026-07-14 (scheduled scan)

Searched arXiv (cs.AI, cs.CL, cs.CR, cs.LG, cs.MA) and the web for new
agent-memory papers published/revised in roughly the last 3 days. arXiv has now
indexed submissions through 2026-07-10 (newest ID 2607.09xxx); nothing past
July 10 is announced yet (July 11-13 was the weekend/Monday, July 14 announces
later this ET evening). Found 2 new, verified, on-topic papers (each checked
against its arXiv abstract page). No new Security papers this run.

**Optimization (2):**
- Shared Selective Persistent Memory for Agentic LLM Systems (2607.09493) — 2026-07-10
- Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents (2607.08716) — 2026-07-09

**Near-misses considered and excluded:**
- Mosaic: Runtime-Efficient Multi-Agent Embodied Planning (2607.09603) — core
  contribution is ILP-based coordination; agent-centric semantic memory is a
  supporting mechanism, not a memory compression/efficiency contribution.
- Harness VLA: Steering Frozen VLAs via Memory-Guided Agents (2607.08448) —
  robotic-manipulation VLA composition; memory is an operational enabler, not
  the contribution.
- Seeing and Reflecting / MMEACR (2607.07108) — multimodal recommendation
  application that uses a dual-track memory architecture; memory serves the
  downstream recommendation task rather than being the research focus.
- Danus (2607.06447), End-to-End LLM Flight Planning with RAG-based Memory
  (2607.06964) — application papers that use memory incidentally.
- Token-Flow Firewall (2607.08395) and Out of Sight (2607.08180) — general agent
  runtime auditing / crawler content protection, already/again excluded as not
  memory-centric.

The late-June/May backlog flagged on prior runs (Memory Contagion, MemVenom,
RaMem, Hijacking agent memory 2605.29960, etc.) remains available for a
deliberate backfill if wanted.

## 2026-07-13 [Conference scan]

No new conference papers found.

First run of the weekly conference scan (USENIX Security, IEEE S&P). Read the
official accepted-papers lists as the source of truth:
- **USENIX Security '26 Cycle 1** (50 papers, via the technical-sessions program):
  reviewed all titles; none concern LLM-agent memory. Cycle 2's accepted-papers
  page is not yet published (404), so nothing to scan there yet.
- **IEEE S&P 2026** (251 papers across both cycles): reviewed every title
  containing memory/agent/RAG/retrieval; none concern agent memory systems.

**Reviewed and excluded (out of scope):**
- IEEE S&P "memory" hits are all hardware/OS memory or memory forensics
  (Leafblower, GHost in the SHELL, Battering RAM, SeqAss, Heap Localization,
  Recovering Mobile LLM Conversations via Memory Forensics) — keyword collisions,
  not agent memory.
- RAG-corpus security papers at both venues (USENIX "Overcoming the Retrieval
  Barrier" IPI-into-corpora, USENIX "Five Queries Are Enough" membership
  inference on RAG datastores, IEEE "Who Taught the Lie?" RAG poisoning
  attribution, IEEE "GraphRAG under Fire") target the static retrieval corpus,
  not an agent's persistent memory store — same boundary that keeps PoisonedRAG/
  AgentPoison out of this tracker.
- Web/browser-agent security (WebCloak, Dark Patterns on LLM web agents, Site
  Isolation in Agentic Browsers, AI-agent data-access permissions) is agent
  security but not memory.

conf_seen.json remains empty; nothing added to paper_list.md.

## 2026-07-13 (scheduled scan)

No new papers found.

Searched arXiv (cs.AI, cs.CL, cs.CR, cs.LG, cs.MA) and the web for new
agent-memory papers in the last ~3 days. Sorting by both submittedDate and
lastUpdatedDate, no on-topic paper carries a July 10-13 date — arXiv has still
not announced any submissions past 2026-07-09 (today is Monday; weekend
submissions are announced later in the ET evening). Every on-topic July paper
surfaced (2607.08032, 2607.06595, 2607.05029, 2607.04391, 2607.04089,
2607.03726, 2607.01935, 2607.01919, 2607.01916, 2607.02579) is already
recorded in seen_ids.json.

**Untracked July items reviewed and excluded:** Narrative World Model
(2607.05577, fiction-writing memory) and COMFYCLAW (2607.01709, self-evolving
image-generation skill harnesses) are near-misses, not security/optimization of
agent interaction-memory. MemSyco-Bench (2607.01071, sycophancy in retrieved
memory) and Multi-Head Recurrent Memory Agents (2607.01523) are on-topic but
~12 days old, well outside the daily window. The late-June backlog flagged on
2026-07-12 (Memory Contagion, MemVenom, RaMem, etc.) remains available for a
deliberate backfill if wanted.

## 2026-07-12 (scheduled scan)

No new papers found.

Searched arXiv (cs.AI, cs.CL, cs.CR, cs.LG, cs.MA) and the web for new
agent-memory papers in the last ~3 days. The most recent arXiv ID currently
indexed is 2607.08666 (2026-07-09); arXiv has not yet announced any July 10-12
submissions (July 12 is a Sunday). All on-topic July 9 papers are already
handled: 2607.08032 was recorded on 2026-07-11, and the July 9 memory-adjacent
security papers (TRACE 2607.08400, Token-Flow Firewall 2607.08395, Multi-Agent
Firewall 2607.08282) were already evaluated and excluded as near-misses that
same run. Nothing in the July 6-9 "just outside the window" zone is both
on-topic and untracked.

**Untracked older candidates noted (out of window, not added):** a sweep
surfaced several clearly on-topic June papers that were never recorded by prior
curated runs — e.g. Memory Contagion (2606.23195), Manufactured Confidence
(2606.29279), Agent-Native Immune System (2606.28270), SMSR certified defence
(2606.12703), MemVenom (2606.10742), GateMem (2606.18829), TRUSTMEM
(2606.25161), Supersede (2606.27472), RaMem (2606.22844). These are 2-3 weeks
old, so they were left out of a daily scan; flagged here in case a deliberate
late-June backfill is wanted later.

## 2026-07-11 (scheduled scan)

Searched arXiv (cs.AI, cs.CL, cs.CR, cs.LG, cs.MA) and the web for new agent-memory papers published/revised in roughly the last 3 days. Found 5 new, verified, on-topic papers (each checked against its arXiv abstract page).

**Security (1):**
- StateFuse: Deterministic Conflict-Preserving Memory for Multi-Agent Systems (2607.05844) — 2026-07-07

**Optimization (4):**
- What to Keep, What to Forget: A Rate-Distortion View of Memory Compaction in LLMs and Agents (2607.08032) — 2026-07-09
- A Hierarchical Memory Architecture Overcomes Context Limits in Long-Horizon Multi-Agent Computational Modeling (2607.07666) — 2026-07-08
- Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation (2607.07608) — 2026-07-08
- NativeMEM: Native Memory Compression for Long-Horizon Robotic Manipulation (2607.06678) — 2026-07-07

**Near-misses considered and excluded:**
- MemDefrag (2607.05969) and TF-Engram (2607.07388) — latent/external memory for general LLM inference (hidden-state retention, offline knowledge injection), not agent interaction-memory systems.
- Token-Flow Firewall / TokenWall (2607.08395) — general agent runtime auditing across state, skills, and tool calls; memory is only one propagation vector, not a memory-centric defense.
- TRACE (2607.08400) — trajectory-attribution watermarking against reseller model-substitution/rebranding (IP protection), not a memory poisoning/privacy/access contribution.
- Multi-Agent Firewall for Privacy (2607.08282) — I/O-level privacy filtering of LLM interactions, not agent-memory-specific.

## 2026-07-10 (scheduled scan)

Searched arXiv (cs.AI, cs.CL, cs.CR, cs.LG, cs.MA) and the web for new agent-memory papers published/revised in roughly the last 3 days. Found 3 new, verified, on-topic papers (each checked against its arXiv abstract page).

**Security (1):**
- When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents (2607.06595) — 2026-07-06

**Optimization (2):**
- Akashic: A Low-Overhead LLM Inference Service with MemAttention (2607.05708) — 2026-07-07
- Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory (2607.05511) — 2026-07-06

**Near-misses considered and excluded:**
- AgentTether (2607.06273) — graph-guided diagnosis and runtime intervention for agent reliability/repair, not an agent-memory security or optimization method.
- Narrative World Model (2607.05577) — narratology-grounded retrieval for fiction-writing quality (already excluded 2026-07-09); not a security or compression/efficiency contribution.
- LogicHunter (2607.06195) and CurateEvo (2607.06140) — LLM-agent framework testing and agentic post-training data curation respectively; touch "agent" but are not about agent memory.

## 2026-07-09 (scheduled scan)

Searched arXiv (cs.AI, cs.CL, cs.CR, cs.LG, cs.MA) and the web for new agent-memory papers published/revised in roughly the last 3 days. Found 3 new, verified, on-topic papers (each checked against its arXiv abstract page).

**Security (1):**
- When Claws Remember but Do Not Tell: Stealthy Memory Injection in Persistent Personal Agents (2607.05189) — 2026-07-06

**Optimization (2):**
- Memory in the Loop: In-Process Retrieval as Extended Working Memory for Language Agents (2607.05690) — 2026-07-06
- From Passive Retrieval to Active Memory Navigation: Learning to Use Memory as a Structured Action Space / NapMem (2607.05794) — 2026-07-07

**Near-misses considered and excluded:**
- Agent Data Injection Attacks are Realistic Threats to AI Agents (2607.05120) — indirect prompt injection across trusted/untrusted data broadly, not specifically an agent-memory attack.
- Narrative World Model (2607.05577) — narratology-grounded retrieval for fiction writing quality, not a security or compression/efficiency contribution.
- DepthWeave-KV (2607.06523) and FreqDepthKV (2607.06519) — KV-cache compression for long-context LLM inference generally, not agent long-term memory systems.

## 2026-07-08 (scheduled scan)

Searched arXiv (cs.AI, cs.CL, cs.CR, cs.LG, cs.MA) and the web for new agent-memory papers. The strict last-3-days window (2026-07-05 to 2026-07-08) contained no untracked papers — the July 5-6 papers are already in seen_ids.json and nothing from July 7-8 has been indexed yet. Widened slightly per policy and added 7 clearly on-topic, previously-untracked papers from late June (each verified against its arXiv abstract page).

**Security (4):**
- MemLeak: Diagnosing Information Leaks in Multimodal Agent Memory (2606.29788) — 2026-06-29
- When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration (2606.28958) — 2026-06-27
- MEMPROBE: Probing Long-Term Agent Memory via Hidden User-State Recovery (2606.24595) — 2026-06-23
- Governed Shared Memory for Multi-Agent LLM Systems (2606.24535) — 2026-06-23

**Optimization (3):**
- When Not to Write Memory: Governing False Promotion from Correlated Agent Traces / GovMem (2607.02579) — 2026-06-30
- Selective Memory Retention for Long-Horizon LLM Agents / TraceRetain (2606.29178) — 2026-06-28
- Forget to Improve: On-Device LLM-Agent Continual Learning via Budget-Curated Memory (2606.25115) — 2026-06-23

**Near-misses considered and excluded:**
- MemDelta (2606.29914) and AgenticSTS (2607.02255) — memory-evaluation protocol/testbed methodology, not a security attack/defense or a concrete compression/efficiency technique.
- Manufactured Confidence (2606.29279), TRUSTMEM (2606.25161), Supersede (2606.27472) — memory-consolidation quality/robustness studies, on the edge of scope; deferred to keep this run focused on the strongest security/optimization matches.

## 2026-07-07 (scheduled scan)

Searched arXiv (cs.AI, cs.CL, cs.CR, cs.LG, cs.MA) and the web for new agent-memory papers published/revised in roughly the last 3 days. Found 6 new, verified, on-topic papers (each checked against its arXiv abstract page). One (A-TMA, 2026-07-02) fell just outside the strict window but was clearly on-topic and missed by prior runs, so it was included.

**Security (2):**
- Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses / FARMA + SENTINEL (2607.05029) — 2026-07-06
- PiSAs: Benchmarking Contextual Integrity in Multi-User Agentic Systems (2607.05318) — 2026-07-06

**Optimization (4):**
- Memory-Orchestrated Semantic System (MOSS): An Auditable Agentic Memory Architecture (2607.04391) — 2026-07-05
- PLACEMEM: Toward a Compute-Aware Memory Plane for Lifelong Agents (2607.04089) — 2026-07-05
- SelfMem: Self-Optimizing Memory for AI Agents (2607.03726) — 2026-07-04
- A-TMA: Decoupling State-Aware Memory Failures in Long-Term Agent Memory (2607.01935) — 2026-07-02

**Near-misses considered and excluded:**
- MemSyco-Bench: Benchmarking Sycophancy in Agent Memory (2607.01071, 2026-07-01) — memory-induced sycophancy benchmark, neither an adversarial security attack nor a compression/efficiency technique.
- ArchEval (2607.03601) and Object-Centric Environment Modeling for Agentic Tasks (2607.02846) — agent benchmarks/experience-modeling that touch "memory" incidentally, not agent memory security or optimization methods.

## 2026-07-06 (scheduled scan)

Searched arXiv (cs.AI, cs.CL, cs.CR, cs.LG, cs.MA) and the web for new agent-memory papers published/revised in roughly the last 3-5 days. Found 2 new, verified, on-topic papers (both Optimization — no new Security papers found this run).

**Optimization (2):**
- Self-GC: Self-Governing Context for Long-Horizon LLM Agents (2607.00692) — 2026-07-01
- AutoMem: Automated Learning of Memory as a Cognitive Skill (2607.01224) — 2026-07-01

## 2026-07-05 (scheduled scan)

Searched arXiv (cs.AI, cs.CL, cs.CR, cs.LG, cs.MA) and the web for new agent-memory papers published/revised in roughly the last 3-5 days, widened slightly to catch anything just outside that window. Found 3 new, verified, on-topic papers.

**Security (1):**
- Forensic Trajectory Signatures for Agent Memory Poisoning Detection (2606.30566) — 2026-06-29

**Optimization (2):**
- Imprint: Online Memory Compression for Long-Horizon Egocentric QA (2607.00696) — 2026-07-01
- Memory Depth, Not Memory Access: Selective Parametric Consolidation for Long-Running Language Agents (2606.26806) — 2026-06-25

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
