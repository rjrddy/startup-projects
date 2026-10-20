# Project catalog: 42 portfolio projects mapped to the companies on your list

Each project is small (a weekend or two), uses public or synthetic data, and ends in a README with measured numbers. Company mapping is my inference from what each company does (see the confidence tags in the email file). Wave 1 = highest coverage of the priority 20. Wave 2 = Tier A and strong Tier B/C fits. Wave 3 = long tail.

## Wave 1: build first (13 projects)

### R1. Robot action validator  ·  Robotics  ·  1-2 weekends
**Targets:** Mbodi AI, Physical Turing, Intelligence Factory  
**Build:** Layer between an LLM and a robot: parse model output into a typed action schema, reject invalid or unsafe actions, dry-run in a simulator, log every decision for replay.  
**Done when:** 100 percent of malformed or out-of-bounds actions rejected in a fuzz test; replay reproduces any past run; README shows a before/after failure rate.  
**Stack:** Python, pydantic, MuJoCo or PyBullet

### R2. Humanoid/arm eval regression harness  ·  Robotics  ·  1-2 weekends
**Targets:** Physical Turing, Mbodi AI, Radical AI  
**Build:** Versioned scenarios, fixed seeds, scoring, and a CI gate on an open MuJoCo arm/humanoid task. Fails a PR when success rate drops.  
**Done when:** Same seed gives identical scores; gate demo shows a failing PR; results table across 3 policy versions.  
**Stack:** Python, MuJoCo, GitHub Actions

### P1. Sensor-fusion replay rig  ·  Robotics  ·  2 weekends
**Targets:** Arlo Industries, Mantis, Intelligence Factory, Dataminr, Via  
**Build:** Align 3+ noisy, unsynchronized synthetic streams, tolerate dropped sources, ship a replay tool that re-scores any run.  
**Done when:** Dropout test shows graceful degradation; timeline plot of aligned streams.  
**Stack:** Python + C++ core

### M1. LLM serving TTFT and throughput benchmark  ·  ML infra  ·  1-2 weekends
**Targets:** nCompass, Modal, Beam, Reflection AI  
**Build:** Benchmark an open model on vLLM: time-to-first-token and throughput under load, then test batching and scheduling settings.  
**Done when:** Table of p50/p99 TTFT vs concurrency; one config change that measurably moves p99; reproducible script.  
**Stack:** Python, vLLM, a small open model

### M2. Multi-provider LLM router  ·  ML infra  ·  1 weekend
**Targets:** OpenRouter, Porter, Parea, Wild Moose  
**Build:** Router with fallbacks, timeouts, circuit breaker and p99 tracking across 2+ model backends (can be local mocks plus one real API).  
**Done when:** Chaos test kills a backend and requests still succeed; latency/error dashboard.  
**Stack:** Python, FastAPI, Prometheus

### V1. Streaming ASR latency harness  ·  Voice  ·  1-2 weekends
**Targets:** AssemblyAI, ElevenLabs, Hume AI, ASAPP  
**Build:** Stream audio to an open ASR model; measure per-stage latency (capture, VAD, model, endpointing). CI gate on p99.  
**Done when:** Chart of where the latency budget goes; gate fails on an injected slowdown.  
**Stack:** Python, faster-whisper or similar

### D1. CI failure triage clusterer  ·  Dev tools  ·  1-2 weekends
**Targets:** Silogy, Haystack, Ellipsis, Wild Moose  
**Build:** Cluster CI failures by log signature across an open repo's history and link each cluster to likely changed files.  
**Done when:** Cluster purity measured on labeled sample; report of top 10 failure families; works on a real open-source repo.  
**Stack:** Python, scikit-learn

### D2. Flaky-test detector  ·  Dev tools  ·  1 weekend
**Targets:** Haystack, Mobot, Ellipsis, Hatchet  
**Build:** Detect flaky tests from CI history and rerun evidence, quarantine them with a policy, and report cost saved.  
**Done when:** Precision/recall on injected flakes; GitHub Action that comments on PRs.  
**Stack:** Python, GitHub Actions

### P2. Deploy gate with auto-rollback  ·  Dev tools  ·  1 weekend
**Targets:** Ryvn, Porter, UiPath, Haystack  
**Build:** Containerized service with canary, behavior diff against last good build, and automatic rollback.  
**Done when:** A failing run the gate caught, linked in the README.  
**Stack:** Docker, GitHub Actions

### F1. Ledger with property-based tests  ·  Fintech  ·  1 weekend
**Targets:** Rillet, DualEntry, Tabs, Basis, Ramp  
**Build:** Double-entry ledger with Hypothesis property tests, replayable from an event log.  
**Done when:** At least 10 properties; seeded bug caught; replay matches state.  
**Stack:** Python, Hypothesis

### F2. Real-time decision engine  ·  Fintech  ·  1-2 weekends
**Targets:** Alloy, Taktile, Sixfold, Pagaya, Hadrius  
**Build:** Rules and score engine with a sub-100ms budget, versioned rules, and replay of any past decision.  
**Done when:** p99 latency measured; replay reproduces decisions bit for bit; audit log.  
**Stack:** Python, FastAPI

### H1. Human-review loop  ·  Healthcare  ·  2 weekends
**Targets:** Tennr, Navina, K Health, SmarterDx, Parea, Raycaster  
**Build:** Confidence-routed review queue with PHI-style redaction, audit log and reviewer-feedback scoring.  
**Done when:** Auto-approve rate vs error rate curve; every decision auditable.  
**Stack:** Python, FastAPI, small UI

### P7. Reliable job runner  ·  Platform  ·  1-2 weekends
**Targets:** GUILD, MorphoAI, Photonium, Hatchet, Clay, WorkFusion, Normal Computing  
**Build:** Idempotent jobs, retries, dedupe, backpressure, tracing, chaos test.  
**Done when:** Chaos test proves no loss/duplication; load test table.  
**Stack:** Python, SQLite/Postgres

## Wave 2 (16 projects)

### R3. Demonstration-data validator  ·  Robotics  ·  1-2 weekends
**Targets:** Intelligence Factory, Mbodi AI, Arlo  
**Build:** Ingest video + IMU/pose streams from public egocentric datasets, check time sync and corruption, flag bad episodes before training.  
**Done when:** Detects injected desync and dropped frames with measured precision/recall; per-episode quality report.  
**Stack:** Python, OpenCV, NumPy

### R4. Test-station measurement logger  ·  Hardware  ·  1 weekend
**Targets:** Beyond Reach Labs, Photonium, Nanotronics, Augury  
**Build:** Simulated lab station: run a measurement script on N units, store results by unit ID, flag out-of-spec units, produce a daily yield report.  
**Done when:** Handles instrument timeouts and retries; yield dashboard from 1,000 simulated units; SQL schema documented.  
**Stack:** Python, SQLite, FastAPI

### M3. Mini vector search engine  ·  ML infra  ·  2 weekends
**Targets:** Pinecone, Haystack, Hugging Face  
**Build:** HNSW or IVF index in C++ with a Python binding. Benchmark recall vs latency vs memory against FAISS on a public dataset.  
**Done when:** Recall@10 and QPS curve vs FAISS; honest comparison in the README.  
**Stack:** C++17, pybind11, Python

### M4. Cold-start and checkpoint benchmark  ·  ML infra  ·  2 weekends
**Targets:** Cedana, Beam, Modal  
**Build:** Reproducible benchmark of container and process start/restore times across kernels, with a regression gate. Pair with an upstream PR.  
**Done when:** Numbers across at least 3 configurations; script anyone can rerun; PR link to a target repo.  
**Stack:** Python, Docker, CRIU

### V2. Voice agent with barge-in  ·  Voice  ·  2 weekends
**Targets:** Regal, Prosper, Paratus Health, EliseAI  
**Build:** Voice loop with interruption handling, turn-taking and a hard latency budget. Measures time-to-first-audio.  
**Done when:** Demo recording; measured time-to-first-audio; interruption test results.  
**Stack:** Python, open TTS/ASR, WebRTC or websockets

### D3. Incident timeline builder  ·  Dev tools  ·  1 weekend
**Targets:** Wild Moose, Prepared, OpenReplay  
**Build:** Join deploy events, alerts and logs into one timeline and highlight the change most likely tied to the incident.  
**Done when:** Tested on 3 replayed public postmortems; timeline output readable in under a minute.  
**Stack:** Python

### D4. Infrastructure change risk checker  ·  Dev tools  ·  1 weekend
**Targets:** Brainboard, Ryvn, Porter, Fastgen  
**Build:** Parse a Terraform plan and score blast radius (deletes, IAM changes, data stores) with a PR comment.  
**Done when:** Catches 5 seeded risky changes; false-positive rate reported.  
**Stack:** Python, Terraform JSON plans

### P3. Supply-chain-hardened pipeline  ·  Security  ·  1 weekend
**Targets:** Cyera, Adaptive Security, Noma Security, Frame Security  
**Build:** SBOM, signing, vulnerability gate, shown blocking a bad dependency.  
**Done when:** Blocked-build screenshot or log; verification instructions.  
**Stack:** syft, cosign, grype, Actions

### F3. Document extraction with field-level eval  ·  Fintech  ·  1-2 weekends
**Targets:** Ocrolus, Vic.ai, Extend, Tennr, Hyperscience  
**Build:** Extract fields from synthetic invoices/bank statements; measure accuracy per field and per template, route low confidence to review.  
**Done when:** Per-field accuracy table; review-queue rate vs accuracy tradeoff curve.  
**Stack:** Python, open OCR/LLM

### F4. Reconciliation engine  ·  Fintech  ·  1 weekend
**Targets:** Basis, Tabs, Cedar, Garner Health, Nourish  
**Build:** Match bank transactions to ledger entries with fuzzy rules, explain each match, surface exceptions.  
**Done when:** Match rate and false-match rate on synthetic data with injected noise.  
**Stack:** Python, pandas

### F5. Finance Q&A with citation checker  ·  Fintech  ·  2 weekends
**Targets:** Rogo, AlphaSense, Financial Datasets, Persado  
**Build:** RAG over public SEC filings where every claim is checked against its cited passage; unsupported claims get flagged.  
**Done when:** Citation-support rate on 50 questions; examples of caught hallucinations.  
**Stack:** Python, embeddings, EDGAR

### F6. Market-data freshness monitor  ·  Fintech  ·  1 weekend
**Targets:** Financial Datasets, Spade, Collective[i], Fluid Markets  
**Build:** Ingest public price/filings data, detect stale, missing or anomalous values, alert with context.  
**Done when:** Detects injected gaps and outliers; freshness SLO dashboard.  
**Stack:** Python, SQLite

### H2. Referral/fax document extractor  ·  Healthcare  ·  2 weekends
**Targets:** Tennr, Navina, Cedar, Headway  
**Build:** Extract structured data from messy synthetic referrals and route exceptions to a human.  
**Done when:** Field accuracy table; exception queue demo; zero PHI in logs test.  
**Stack:** Python, OCR

### S2. Prompt-injection test harness  ·  Security  ·  1 weekend
**Targets:** Noma Security, Parea, Wild Moose  
**Build:** Test suite that attacks an LLM agent with injection payloads and reports which tools it misuses.  
**Done when:** Attack success rate before/after a mitigation.  
**Stack:** Python

### X1. High-volume message sender  ·  Platform  ·  1-2 weekends
**Targets:** Attentive, Kustomer, Unthread  
**Build:** Queue-based sender with rate limits, dedupe, retries and delivery-status reconciliation.  
**Done when:** Throughput and duplicate-send rate under chaos; p99 enqueue-to-send.  
**Stack:** Python, Redis or Postgres

### X2. Remote config and staged rollout service  ·  Platform  ·  1-2 weekends
**Targets:** Superwall, Hatchet, Ryvn  
**Build:** Serve config to clients with staged rollout, kill switch and rollback; SDK client with offline cache.  
**Done when:** Rollback tested; client correctness under flaky network.  
**Stack:** Python/TypeScript

## Wave 3 (13 projects)

### M5. Distributed KV store with failure injection  ·  ML infra  ·  2 weekends
**Targets:** VAST Data, Pinecone, Hatchet  
**Build:** Replicated key-value store with a failure-injection test suite (node kill, partition, slow disk) that checks linearizability on small histories.  
**Done when:** Test suite finds a seeded bug; README lists guarantees and what is not guaranteed.  
**Stack:** Python or Go-style design in Python, Jepsen-style tests

### V3. Domain-term accuracy eval  ·  Voice  ·  1 weekend
**Targets:** AssemblyAI, Paratus Health, Prosper  
**Build:** WER plus domain-term accuracy (e.g. medical terms) on public audio. Shows where general WER hides the failures that matter.  
**Done when:** Report comparing 2 models on overall WER vs term accuracy.  
**Stack:** Python, jiwer

### D5. Session capture with PII redaction  ·  Dev tools  ·  1-2 weekends
**Targets:** OpenReplay, Superwall, Unthread  
**Build:** Capture client events cheaply, redact PII at the edge, benchmark overhead.  
**Done when:** Redaction test with seeded PII leaks 0; overhead under 2 percent measured.  
**Stack:** TypeScript or Python, benchmark

### F7. Payment descriptor enrichment API  ·  Fintech  ·  1 weekend
**Targets:** Spade, Ramp, Alloy  
**Build:** Clean messy merchant strings into merchant names/categories via an API with accuracy benchmark and caching.  
**Done when:** Accuracy on a labeled sample; p99 latency.  
**Stack:** Python, FastAPI

### H3. Clinical summary with source checking  ·  Healthcare  ·  2 weekends
**Targets:** Navina, SmarterDx, Hyro, K Health  
**Build:** Summarize synthetic patient notes and verify each statement against its source span.  
**Done when:** Unsupported-claim rate measured; reviewer UI shows evidence.  
**Stack:** Python, LLM, synthetic data

### H4. Eligibility and claims mock pipeline  ·  Healthcare  ·  1 weekend
**Targets:** Headway, Nourish, Grow Therapy, Garner Health  
**Build:** Mock payer API integration with retries, idempotency and reconciliation of claims status.  
**Done when:** Chaos test with payer timeouts; reconciliation report.  
**Stack:** Python

### P9. Permission-check service  ·  Security  ·  2 weekends
**Targets:** authzed, Floracene  
**Build:** Zanzibar-style relationship check service with load test and correctness tests against a reference model.  
**Done when:** p99 check latency; correctness suite; consistency notes.  
**Stack:** Python/C++

### S1. Deepfake detection eval harness  ·  Security  ·  2 weekends
**Targets:** Reality Defender, Intezer, Noma Security  
**Build:** Benchmark open detectors on audio/video/image with adversarial perturbations; report robustness.  
**Done when:** Accuracy under 5 perturbations; honest limitations.  
**Stack:** Python, PyTorch

### S3. Alert triage deduper  ·  Security  ·  1 weekend
**Targets:** Intezer, Cyera, Adaptive Security  
**Build:** Cluster and dedupe security alerts, rank by novelty and risk, cut noise measurably.  
**Done when:** Alert volume reduced by X percent at Y percent recall of true positives.  
**Stack:** Python

### X3. API docs drift detector  ·  Platform  ·  1 weekend
**Targets:** ReadMe, Mito, Trackstar  
**Build:** Diff documentation against a live OpenAPI spec and real traffic, open a PR to fix drift.  
**Done when:** Detects 10 seeded drifts; GitHub Action.  
**Stack:** Python, OpenAPI

### X4. Entity matching quality harness  ·  Platform  ·  1 weekend
**Targets:** Vendelux, Narrative, Collective[i], H1  
**Build:** Match company/person records across messy sources, measure precision/recall, show tradeoffs.  
**Done when:** P/R curve; error-analysis table.  
**Stack:** Python

### X5. Unified-API adapter with contract tests  ·  Platform  ·  1-2 weekends
**Targets:** Trackstar, Trunk Tools, Optimal Dynamics  
**Build:** One API over 3 mock logistics/warehouse systems, with contract tests that catch upstream changes.  
**Done when:** Contract tests fail on a seeded upstream change.  
**Stack:** Python, pytest

### X6. Dispatch simulator  ·  Platform  ·  1-2 weekends
**Targets:** Via, Prepared, Optimal Dynamics  
**Build:** Simulate requests and vehicles/responders, measure wait time under load and failure.  
**Done when:** Wait-time distribution under 3 loads; failure-mode report.  
**Stack:** Python, simpy