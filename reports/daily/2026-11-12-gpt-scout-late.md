# Voshu GPT Scout — follow-up research, 2026-11-12 (late pass)

## Scope and preservation
Cross-referenced existing README.md, CATALOG.md, data/repositories.json, data/organizations.json, and LOCAL-INVENTORY.md in Avoshu/Voshu-Inspo. Existing local-inventory claims were read from GitHub; **no new F: drive inspection**. Canonical GitHub URLs were deduplicated case-insensitively. No third-party code executed. Existing catalog entries and manual notes retained.

**New repository origins: 9; previous catalog count: 246; revised count: 255.** GitHub repository identities, default-branch README files, license files or README licensing notices, and recent commit URLs were checked on 2026-11-12. A recent commit link proves accessible history, **not** a precise last-push timestamp; `last_push` is null pending verification. No dependency or security audit was performed.

## Verified research shortlist

| Upstream | Category | License evidence | Concrete Voshu relevance | Activity evidence |
|---|---|---|---|---|
| [kestra-io/kestra](https://github.com/kestra-io/kestra) | Workflow Orchestration | Apache-2.0 | YAML/event-driven orchestration with visual editor and MCP execution attribution; evaluate for Studios onboarding and Commander job auditability. | [Commit 30473aa1](https://github.com/kestra-io/kestra/commit/30473aa195dc6c6fb7ce266a83864b76f2162258) |
| [activepieces/activepieces](https://github.com/activepieces/activepieces) | Visual Workflow Automation | MIT community / commercial enterprise | Visual automation and integration pieces; benchmark against n8n for Avoshu social DM funnels and client onboarding. | [Commit b3c2e8d0](https://github.com/activepieces/activepieces/commit/b3c2e8d009e4b0247c02a6fa7725e0bc179f99cf) |
| [hatchet-dev/hatchet](https://github.com/hatchet-dev/hatchet) | Durable Agent Orchestration | MIT | Durable queues, DAGs, rate limits and concurrency; candidate for Commander long-running tasks and GPU job scheduling. | [Commit a749e252](https://github.com/hatchet-dev/hatchet/commit/a749e252c7692c1187f8033e336f93d19d1158d1) |
| [powersync-ja/powersync-service](https://github.com/powersync-ja/powersync-service) | Local-First Databases & Sync | Apache-2.0 | Postgres-to-client SQLite synchronization; assess for Voshu One desktop/offline workspaces and client portal. | [Commit 8b2d252c](https://github.com/powersync-ja/powersync-service/commit/8b2d252c18bee555385a6ee7f3cfb08862f57307) |
| [automerge/automerge](https://github.com/automerge/automerge) | Realtime Collaboration & CRDT | MIT | CRDT persistence and sync for offline-first collaborative Atlas panes, notes and shared workspaces. | [Commit d09a2ffa](https://github.com/automerge/automerge/commit/d09a2ffafb775a2bfabb3fc64f0532d26e38c76b) |
| [ansible/ansible](https://github.com/ansible/ansible) | Infrastructure as Code | GPL-3.0 (README; license file path unresolved) | Configuration management and repeatable provisioning for Voshu Compute/Proxmox nodes and Windows/Linux services. | [Commit b4b2b1e8](https://github.com/ansible/ansible/commit/b4b2b1e82a535d27f902a71fc8396c3af138fca2) |
| [dagger/dagger](https://github.com/dagger/dagger) | Developer Tools & CI | Apache-2.0 | Containerized reproducible build/test pipeline for Voshu repositories and agent worktrees. | [Commit 3991a28b](https://github.com/dagger/dagger/commit/3991a28b9dbcfb6e9badbf35fa3b54e9419d07f2) |
| [triggerdotdev/trigger.dev](https://github.com/triggerdotdev/trigger.dev) | Durable Agent Orchestration | Apache-2.0 | Long-running TypeScript jobs with self-hosting; benchmark against Hatchet and Inngest for onboarding. | [Commit 2fbd5c7c](https://github.com/triggerdotdev/trigger.dev/commit/2fbd5c7cf4e9c8e19b88e2b72a7133795611e33d) |
| [yjs/yjs](https://github.com/yjs/yjs) | Realtime Collaboration & CRDT | MIT | Network-agnostic shared data and collaborative cursors for Atlas split panes and multi-agent editing. | [Commit 52396473](https://github.com/yjs/yjs/commit/52396473094be82868fe098f1f8d01d737478dbb) |

## Architectural implications

**Commander / Agent 2.0:** Hatchet, Trigger.dev and the already cataloged Temporal/Inngest are competing durable-execution designs. Compare retry/idempotency semantics, cancellation, audit trails, tenancy, per-job approval propagation, deployment footprint and worker scheduling before selecting one. Kestra's recent [caller-attribution commit](https://github.com/kestra-io/kestra/commit/30473aa195dc6c6fb7ce266a83864b76f2162258) is directly relevant to authenticated MCP action logs.

**Voshu Studios:** Activepieces and Kestra should be compared against existing n8n on visual authoring, external integrations, self-hosting, and commercial licensing. Do not treat Activepieces' enterprise code as MIT licensed.

**Voshu One / Atlas:** PowerSync is server-authoritative Postgres-to-SQLite sync; Yjs and Automerge solve collaborative CRDT data merging. These are **different layers**, not interchangeable products. Prototype a single offline workspace and explicit conflict/reconnect behavior before adopting.

**Voshu Compute / Host:** Ansible is appropriate for repeatable configuration, Dagger for reproducible build/test pipelines. OpenTofu, Flux and Proxmox Backup remain separate research tracks; Kubernetes GitOps should not be imposed on a Proxmox/Docker-only deployment without a demonstrated need.

## Verification and blockers

- GitHub connector confirmed canonical repository identities and non-archived status; read READMEs and license evidence. Ansible's root LICENSE path returned 404; its README identifies GPL v3, so license file verification is incomplete.
- No exact last-push timestamps, full license-compatibility opinions, CVE checks, build tests or deployments are asserted.
- Local `F:\PROJECTS\INSPO` and `F:\Voshu` were **not** accessed.
- No existing manual notes, source folders or repository entries were removed or overwritten in content.
- Follow-up priority: compare Hatchet vs Trigger.dev vs Inngest on one Commander job lifecycle, then evaluate PowerSync vs CRDT sync on Atlas.
