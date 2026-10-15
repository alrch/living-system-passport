---
name: living-system-passport
description: Build or maintain a living system passport that connects product behavior to implementation, requirements, and verification. Use when auditing a function, planning a change, or updating the map after an accepted change.
---

# Living System Passport

A living system passport is a project-owned map of what the system does, where that behavior is implemented, and how it is verified. Keep it navigable for people and agents. It may be one document or several linked pages. Do not copy the authority of requirements, code, tests, or release records into the passport; link to their current sources.

This skill supplies the method, not a universal file layout or a project-specific toolchain. The project's `AGENTS.md` and documentation should identify its passport, sources of truth, IDs, checks, and owners. If these do not exist yet, discover them before choosing a layout. Do not require any particular registry, graph, role model, or service structure.

## Set the scope and evidence

1. Start with the requested function, change, or connected domain. Map the whole platform only when that scope was requested.
2. Find the project's instructions, product rules, requirement and status sources, architecture notes, code, API contracts, data definitions, and scenarios. Record which source owns each claim. Code presence alone does not prove that behavior is accepted, released, or running in production.
3. Reuse established function and scenario IDs. If none exist, create stable passport IDs and distinguish them from tickets and requirement IDs.
4. Trace from an exact route, event, name, ID, or source file. Use a current project graph or index when available, then confirm consequential links in source. If no graph exists, use targeted source search. A graph edge is a lead; a missing edge is not proof that no consumer exists.
5. Record source revisions or evidence dates when they matter to freshness, especially when the passport spans repositories or external requirement snapshots.

## Describe behavior on two levels

- **Meaning for people:** purpose, actors, observable outcome, rules that must survive a change, exceptions, manual or external responsibilities, and open product decisions.
- **Technical realization:** screens or entry points, controls and fields, API contracts, services, stored data, permissions, integrations, state transitions, failure and retry behavior, and direct consumers.

Connect each function to relevant requirements, their authoritative status and evidence, and the scenarios or tests that verify it. Mark a link confirmed or needing verification. Keep planned, implemented, tested, accepted, and deployed claims distinct. A scenario's existence is not a passing result.

Use [the function-entry checklist](references/function-entry.md) when creating an entry or checking one for gaps. Follow an established project format if it covers the same information.

## Plan or assess a change

1. State the proposed observable behavior and the rule it changes or must preserve. Name affected actors and states.
2. Look for the same user outcome in existing functions before proposing a new one.
3. Trace the relevant path from user action or external event through the interface, service, data, and integration boundary. Inspect direct callers, consumers, shared contracts, neighboring functions, and scenarios.
4. Report **confirmed changes**, **places to inspect**, and **missing or uncertain links**, each with evidence. Do not turn a possible dependency into a proven breakage.
5. Choose the smallest useful checks for the affected rule and its direct dependencies: normal path, access boundary, failure or retry, and a relevant edge state. Reuse existing scenarios.
6. For an accepted implementation change, update the affected passport entries in the same task and run the relevant project checks. For a planning request, describe proposed edits and checks without claiming they were completed.

If an accepted rule already determines the outcome, treat a mismatch as an implementation or documentation issue within the user's authorized scope. Investigate missing evidence before asking for a product decision. Ask the owner only when two defensible outcomes remain and the choice changes product behavior, access, retention, or an external obligation. Record a deferred choice with the event that will reopen it.

## Build or review a wider passport

Work in connected domains. Trace consequential actor journeys through visible action, API or service, business rule, stored state, external boundary, and observable result. Prioritize accepted behavior and access or data-loss boundaries. Finish each domain with a clear account of what was checked, what is linked, and what remains uncertain; avoid one platform-wide completeness percentage.

Keep a compact finding register linked from affected functions. Classify each finding as confirmed, candidate, intentional, or resolved. Include evidence on both sides, consequence, next check or decision owner, and review date. Similar code is not automatically a duplicate; static-search absence is not proof of dead code. The [function-entry checklist](references/function-entry.md) includes a finding-note shape.

For detailed cross-layer review, consult only the applicable items in [domain review checks](references/domain-review-checks.md). They are prompts for investigation, not new product rules or a reason to widen a small task into a full audit.

## Keep the passport current

- On an accepted behavior or requirement-status change, inspect the directly affected entries and neighbors. Update human meaning and technical links, then refresh project-owned indexes and run the relevant structural and scenario checks.
- Keep generated inventories separate from reviewed explanations. A route or requirement appearing in a generated table is a discovery lead, not proof that its rule and verification boundary are understood.
- Treat fingerprints, changed files, and graph results as review queues. Inspect the behavior before accepting a new baseline. A changed-file check must also account for new files that were never linked.
- Distinguish local test results, CI results, deployment evidence, and external provider receipts. A prepared workflow or passing mock does not prove the corresponding live stage occurred.
- Keep scripts, commands, analyzers, generated indexes, and baselines in the project that owns the code. Add shared tooling to this skill only when it is genuinely portable and solves a repeated problem.
