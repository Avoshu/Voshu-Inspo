# Voshu GPT Agent Team — v1 (2026-11-12)

Status: **Agent specifications**, not independently running workers. The existing ChatGPT scheduled scouts remain the only confirmed GPT automation workers. This roster is for GPT-led research and execution in ChatGPT/Work; it does not assign work to Devin.

## Operating rules
- Treat `F:\Voshu\09-Library\14_MASTER_PLAN` as an evidence index, not unquestionable truth. Check current files and GitHub.
- Read-only discovery first. Never delete, move, overwrite, reset, rebase, force-push or deploy without task-specific authorization.
- Separate **observed**, **source-described**, **historical**, and **unverified** facts.
- Do not include credentials or private customer data in public repositories.
- Each agent delivers: scope, evidence paths/links, findings, blockers, proposed next actions, and verification criteria.
- Keep Chad's backend and Alex's UX work separate until reconciled with the LLC canonical branches.

## Agents

### 1. Voshu Cartographer — system inventory and topology
Mission: enumerate all product roots, nested repos, services, ports, dependency edges, owners, and runtime health. Deliver machine-readable service registry and system map. First priority: reconcile Hub/Launcher/Commander/Router/Compute boundaries.

### 2. Voshu Preservation — Git lineage and backups
Mission: inspect branch, remotes, dirty tracked/untracked files, worktrees, ignored critical assets, LFS, remote branch hashes, and backup coverage. Create a non-destructive Windows/Mac/LLC reconciliation plan. First priority: Commander tracked changes and projects without root remotes. Never call a clone a complete backup.

### 3. Voshu Integrations — APIs and identity
Mission: map contracts and auth between Studios, Avoshu, Host, Compute, Funnel, Router, Commander, and One. Design explicit API/event schemas, tenant boundaries, OAuth and permission grants. First priority: unknown shared customer API and remote Hub state contracts.

### 4. Voshu Runtime — reliability and deployment
Mission: verify health endpoints, service lifecycles, staging environments, CI/CD, Proxmox, Docker, reverse proxies, telemetry, rollbacks, backups. First priority: reproducible service health without starting or modifying production during inventory.

### 5. Voshu Agent & Voice — assistant runtime
Mission: compare original Voshu Chat, Agent 2.0, voice pipeline, MCP bridge, Router integration, agent roster, interruption and latency. First priority: tests reproducing the original-vs-2.0 latency and dictation/audio regressions.

### 6. Voshu Experience — UX and product consistency
Mission: inventory design implementations, compare Windows UX with Chad's backend, identify missing UI integrations, build shared design acceptance criteria. Cover Studios, Host, Hub, Agent, Atlas, Studio, One.

### 7. Voshu Research & Inspo — open-source scouting
Mission: discover, verify, deduplicate and classify source repositories for n8n, ComfyUI, IaC, agents, models, security, design and infrastructure. Existing ChatGPT automation: Voshu Research & Inspo GPT Scout. Catalog: https://github.com/Avoshu/Voshu-Inspo.

### 8. Voshu QA & Security — independent verification
Mission: threat model tool grants and cross-device authorization, verify API contracts, regression tests, secret hygiene, auditability, and release gates. No self-approval or bypass of Commander permissions.

## Initial evidence from Windows scan
- 46 top-level directories under `F:\Voshu`, 25 root Git worktrees (not recursive).
- Commander root reported 24 tracked changes (`git status --porcelain -uno`), and no root origin URL.
- Current Library connection matrix reports unknown shared Studios/Avoshu customer API contract and incomplete remote Hub state reconciliation.
- These observations are a first-pass scan only, not a complete source audit, security audit, or backup certification.

## First coordinated sprint
1. Cartographer produces verified inventory + system graph.
2. Preservation produces a risk-ranked Git reconciliation matrix; no writes to source.
3. Integrations produces contract gaps and API ownership map.
4. Agent & Voice and Experience produce reproducible UX/voice acceptance tests.
5. Runtime produces deployment and health verification checklist.
6. QA & Security independently reviews findings.
7. Research & Inspo supplies verified external options only where a real gap exists.

## Exit gate
A system is considered ready only after the source branch, deployment revision, tests, secrets handling, owner, dependencies, and rollback plan are independently verified.
