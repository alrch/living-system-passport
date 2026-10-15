---
name: living-system-passport
description: Build or maintain a living system passport that connects product behavior to screens, APIs, data, requirements, and tests. Use to audit an existing function, plan a new function, or assess a behavior change; connect findings to project quality checks without making the passport a tool configuration.
---

# Living System Passport

A passport helps people and agents understand what a system does and what a proposed change may affect. Keep one navigable, project-owned description of behavior and its evidence. Adapt its file layout to the project; one logical passport can be one file or several linked pages. Preserve existing canonical sources instead of copying their authority into the passport.

The workflow is portable. Discover the project's own sources of truth, repositories, status language, scenario format, indexes, and checks before applying it. The detailed domain checks are optional: select only those matching the behavior under review. No particular technology, registry, graph, or business domain is required.

Read the project's instructions for its [passport adapter](references/project-adapter.md): where the passport and source evidence live, which changes trigger review, how linked entries are found, and which project commands validate or refresh them. If no adapter exists yet, establish the minimum facts needed for the requested task instead of inventing commands or copying another project's configuration. Project instructions can make this skill mandatory for particular changes without duplicating its full method.

## Establish the boundary

- Find the project's current instructions, product documents, requirement/status source, architecture index, API contracts, schema definitions, and scenario tests. Identify which source owns each fact. Do not infer approval, release, or production behavior from code presence.
- Prefer existing IDs for functions and scenarios. If no function ID exists, create a stable passport ID and distinguish it from requirement or ticket IDs.
- Start with the requested feature or a small connected workflow. Do not claim platform-wide completeness from one sample or run a full-project audit without a concrete need.

## Create a passport or a new function entry

If the project has no passport, first locate accepted product rules and a few consequential user journeys. Choose a navigable home for one logical passport and define how entries link back to authoritative sources. Start with one connected domain; draft entries for its visible outcomes and the technical paths that realize them. Do not generate a platform-wide inventory and label it a completed behavioral map.

Before naming a new entry, search the project's existing passport and index for the same user outcome; reuse its function ID if one exists. For each new entry, identify the actor, trigger, precondition, observable result, meaning-level rule, exceptions, owner, and technical path. Link current requirements, code, contracts, data, neighboring functions, and scenarios with evidence. Mark a missing or inferred link explicitly. A function may have no dedicated requirement card; use a distinct passport ID rather than borrowing a neighboring card's status. Apply the [function-entry template](references/function-entry.md) as a completeness check, not a mandatory layout. For a workflow with filters, exports, multiple event sources, or retention, read only the matching [domain review checks](references/domain-review-checks.md) while drafting, not only when auditing a later change.

Before calling the first domain complete, sample traceability in both directions: requirement or user outcome → function → implementation and changed source file → function → scenario. State separately what is structurally linked, described from current sources, checked across layers, and exercised by a scenario. A discovered route or a passing structural check proves only its own layer.

## Use the project graphs

Find the project's graph index or graph tooling before tracing a function. Select the smallest graph that covers the question: code dependencies for implementation impact, requirements and scenarios for product traceability, or UI/documentation links for visible behavior. Reuse an existing graph; building a new one requires a demonstrated gap.

For an existing function or a proposed change, start from one exact name, ID, route, or entry point. Make a bounded query for its implementation, then follow only the relevant incoming callers, outgoing dependencies, and neighboring functions or scenarios. If a query returns many unrelated nodes, narrow it to a symbol or file instead of increasing the output limit. Open the relevant current source files and confirm each consequential edge, including cross-service API calls. Check when the graph was produced and whether the affected sources changed afterward; refresh the affected graph only when needed for the task. A graph edge is a lead, and an absent edge does not prove there is no consumer.

Carry confirmed links and unresolved gaps into the impact list and passport entry. Keep graph files and tool-specific commands in the owning project. If the project has no usable graph, trace the same narrow path from source search and record the missing navigation aid; do not block the passport task merely because a graph tool is unavailable.

## Work in domain batches

When building a broad passport, take one connected domain at a time. Start with a few consequential actor journeys and trace each through the visible screen, API, rule, persisted state, external boundary and observable result. Prioritize accepted behavior, access or data loss boundaries, and changes that affect several neighboring functions. Keep planned details in the map without requiring every planned field to receive the same depth immediately.

Within the domain, correct source-backed descriptions and links autonomously. Sort findings into a documentation correction, a reproducible implementation gap, or an unresolved product rule. Give implementation gaps an exact scenario and evidence; keep product code changes in their own authorized task. Bundle unresolved product choices into one short decision packet for the domain with the competing rules, options, consequences and a recommended default where the sources support one. Do not request approval for every field or repeat decisions already recorded in authoritative sources.

Before putting an item in an owner decision queue, apply a decision filter. If an accepted rule or basic invariant already fixes the expected outcome, treat the mismatch as a bug and repair it within the user's authorized scope. If evidence is missing, investigate the source or runtime path first. Ask the owner only when at least two defensible outcomes remain after that work and choosing one would change product behavior, access, data retention, or an external obligation. Keep completed fixes and deployment checks out of the active owner-question list. A prior decision packet does not make an obvious technical fix a recurring question.

For a numerical or time-window rule, read the primary source before reducing the choice to a threshold or formula. Name the measured event, numerator and denominator, population, window boundary, and any stated exclusions. If those differ from the available data, surface the difference in one coherent decision packet rather than implementing the chosen number against a convenient proxy.

If a rule compares periods only while a condition remains unchanged, identify the observable fields that define that condition and whether their historical values are retained before offering an implementation choice. When the source does not define the condition, include its proposed meaning in the same decision packet; a choice of strict comparison alone does not define what must be compared.

After the owner selects an outcome, implement the connected finding before opening another owner question. Resolve ordinary algorithm and data-handling details from the accepted rule and the safest compatible defaults; record those defaults in the passport. Do not split one finding into a chain of microdecisions merely because several implementation cases exist. Reopen the owner question only if source review reveals a materially different product outcome.

If the owner explicitly defers a product choice, record the event that will reopen it (for example, a release cutoff), preserve current behavior, and continue independent work. Do not present the same deferred choice as a blocker or ask it again on every domain pass.

Finish the batch when the important journeys and accepted rules have a traceable observable outcome, consequential rights and fields have been checked through their direct dependencies, and remaining uncertainty is explicitly recorded. Report what was checked and what remains open; avoid a single completeness percentage for the whole platform. Use the first batch to calibrate the depth and review cost of later batches.

For an owner-authorized autonomous pass, keep working through independent findings after each local fix and verification. A progress report is not a completion event. Stop the pass only at its agreed time or scope boundary, when no independent work remains, or when the next action genuinely requires the owner's decision or external evidence. Name the unfinished findings and the exact next step when handing the pass back; never imply the whole passport is complete because one batch passed.

## Describe each function on two levels

1. **Meaning for people:** purpose, actors, observable result, business rules that must survive changes, exceptions, responsibility outside the system, and unresolved decisions. Use ordinary language. Explain why a rule matters when that changes implementation decisions.
2. **Technical realization:** entry points and screens, visible controls and fields, API methods and contracts, services, stored data and indexes, integrations, permissions, state transitions, and failure behavior. Link precise sources rather than pasting entire code or specifications.

Connect both levels to the relevant requirements, their current statuses, evidence, and scenario tests. Label each link as confirmed or a candidate needing verification. A function may serve several requirements, and a requirement may cross several functions. Keep external or manual obligations visible without portraying them as implemented software.

Use [the function-entry template](references/function-entry.md) when creating a new entry or comparing an existing one for missing information. Follow an established project format if it already provides the same information.

## Analyze a proposed change

For a new function or change in logic:

1. State the proposed behavior and the meaning-level rule it changes or must preserve. Identify the affected actors and states.
2. Search for the same user outcome in existing functions and implementations. Name the best extension point; propose a new module only when its responsibility differs, and explain why the existing one does not fit.
3. Trace the smallest relevant chain in both directions: user action or external event → screen/client → API/service → data/integration; then find direct consumers, shared contracts, nearby functions, and scenario tests. Use existing indexes first, followed by targeted source checks.
4. Return an impact list with **confirmed changes**, **places to inspect**, and **missing/uncertain links**. Give evidence for each. Do not turn a possible dependency into a proven breakage.
5. Choose scenario checks for the changed rule and its direct dependencies: normal path, access boundary, failure or retry, and relevant edge state. Reuse existing scenarios before adding new ones. Run only the checks warranted by the actual change and project gates.
6. Update the passport in the same task as the accepted behavior change. If the answer is not yet decided, record the open question and owner of the decision rather than inventing a rule. Record why a reviewed neighboring entry needs no edit when that matters for traceability.

For a request to plan rather than implement, produce the impact list and proposed passport changes without claiming that code, tests, requirements, or acceptance statuses were updated.

When maintaining an existing passport, start with the task's exact changed files, cards, or behavior, not every unrelated change in a shared working tree. After a pull or source-revision change, compare against the last reviewed revision before treating the passport as current. If a change is internal and does not alter the documented meaning or links, record that scoped conclusion. See the [project adapter](references/project-adapter.md) for how to map these steps to local commands.

## Connect the passport to quality checks

Use two distinct modes:

- **Audit what already exists:** when the owner requests a review, inspect the selected function or domain; cover the whole project only when that scope was requested. Start with current reports and project checks, run missing or stale checks justified by the scope, and connect confirmed behavior gaps, duplicated implementations, and unused-code candidates to the affected passport functions. A static finding is a lead, not proof that behavior is wrong or code may be deleted. Record scope, evidence, unresolved findings, and what was actually checked.
- **Check a change:** trace only the affected function and its direct consumers using the passport, then run the relevant local quality commands and scenario tests for an implemented change. Compare results with the accepted baseline; investigate new findings before updating the passport. For a plan without code changes, identify the checks to run later without claiming that they passed. Do not repeat a whole-project audit for an ordinary change.

For a destructive workflow or external handoff, prove the local state transition with disposable, isolated data and a bounded test endpoint before claiming it works. Make integration tests refuse production targets and clean up only resources they created. Distinguish a local protocol stand-in from a receipt issued by the real provider; record the remaining external check without turning it into an owner decision.

When introducing missing quality checks, take one check at a time: scan the agreed scope, inspect and classify existing findings, configure it, demonstrate that a new violation fails, then proceed to the next check. Keep executable commands, analyzer configuration, and baselines in the project that owns the code; link to them from project documentation. Do not copy project-specific configuration into this portable skill or treat an updated baseline as a fix.

When committed changes and an active working tree differ, evaluate a newly introduced baseline against a clean copy of that commit before attributing new analyzer findings to it. Report that result separately from checks on the working tree; a clean committed baseline does not clear new local findings.

For a check of hardcoded external URLs, distinguish real navigation or request targets from input placeholders and generated string fragments. Record the purpose of each allowed literal; do not make a failing scanner green by adding examples or unclassified hosts to its allowlist.

For a release, use the same check at successive boundaries: run the relevant commands locally before publication; let CI check the proposed revision and the project's integration branch; check the revision proposed for production before deployment; after deployment, run targeted runtime smoke or scenario checks against the deployed service. Static source analysis in CI and runtime checks on production prove different things. Distinguish a locally prepared CI workflow from one published and actually run; record each result and any stage not yet automated. This skill does not authorize a push, merge, or deployment.

## Keep it current without false automation

- Deterministic checks may validate IDs, links, source paths, declared routes, and missing scenario references. Generate indexes and reading views from canonical sources where possible.
- Keep the mechanical inventory and the meaning-level map separate. A route, schema, or requirement ID in a generated table is a discovery lead; count a requirement as connected only when a named function/process explains its rule, source, and verification boundary. If a card spans several functions, link all of them.
- When a generated inventory changes after adding or removing a source file, recalculate any human-readable structural totals that quote that inventory. Keep this count refresh mechanical and separate from accepting source fingerprints or claiming that the new behavior was reviewed.
- When an implemented action moves between screens, update contract tests to assert the live route, guard, and rendered action. Preserve the behavior check rather than keeping a stale source-file assertion or deleting the scenario.
- For a scoped audit or implementation change, read the relevant checks in [domain review checks](references/domain-review-checks.md) for the affected kind of workflow (forms, analytics, exports, access, learning, integration, or media). Apply only the pertinent checks; do not expand a small change into a platform audit.

- On every accepted change, start from the changed file or requirement ID, inspect direct passport entries and their neighbors, update human meaning and technical links in the same task, then refresh generated indexes and run structural checks. Include compact ID ranges only if the lookup tool expands every member, including lettered subitems, back to the right entry.
- Before refreshing a passport assembled from separate repositories or requirement snapshots, record which revisions its code, cards, and generated indexes read. If one local checkout lags or diverges from the revision being described, do not regenerate an authoritative status view from that checkout; reconcile the source first or label the mismatched view as stale until it can be rebuilt. Preserve unrelated working-tree changes during that reconciliation.
- When a screen, endpoint, capability, or role changes, reconcile its actual server permission and UI visibility with the maintained role-rights register. Record the register version and an allowed/denied scenario for affected roles; a new route must not inherit an unreviewed permission by default.
- For authentication requirements, distinguish account classes and initial MFA from step-up on a named sensitive operation. For failed-login lockout, follow the route through the account state, consecutive-attempt counter, successful-login reset, blocked response, and unlock rule. Trace each relevant failure, including an unknown account, through the service error and controller catch before deciding whether it increments the counter; status code alone does not determine that. A failure journal by itself does not enforce a lock. A login scenario cannot prove that a later sensitive action was blocked until fresh confirmation.
- For an inactivity timeout, compare the last accepted action, browser timer, API authorization and refresh path. Absolute JWT expiry and a background activity timestamp do not prove that a still-valid token is rejected after the idle window; test the boundary with another browser tab and a direct API call.
- For a handoff to an external service, distinguish opening a guest link from an authenticated session tied to the user's platform identity. Compare every scenario step with its stated success result; if one asks for SSO but another accepts a guest route, keep both claims visible and request one coherent criterion before declaring acceptance.
- Treat a requirement card moving to a closed or accepted state as a change even if no product file changed. Refresh its status view, compare the acceptance/evidence and scenario result with the linked function, and revisit neighboring rules before considering the passport current. A generated status row may update automatically; the human explanation and finding register still require review.
- If the project derives a scenario catalog or other index from requirement cards, rebuild it after a card edit and before running passport consistency checks. A source baseline may continue to report drift while generated views refresh; review the affected meaning and neighbors, accept the new fingerprint separately, then rerun the check.
- Audit repeated acceptance locations and routes at the level of a related requirement family. Compare each stated role, screen and external provider with the files cited as evidence; a passing test in an internal UI cannot prove a scenario that explicitly occurs in an external service. Record a wrong route or mixed evidence without changing the requirement's authoritative status on inference.
- When a function moves from one screen or context to another, check the requirement's acceptance location, demo route, scenario steps, fixture keys and evidence together. Keep old checks explicitly labeled as historical; rerun the new route before calling its browser evidence current. Separate the route and roles that passed from adjacent screens or databases that were not exercised.
- Do not compare a requirement's software-coverage class with its implementation percentage as if both measured readiness. Coverage says how much of the obligation software can fulfill; the percentage and demo state describe progress and evidence. Escalate only a real mismatch after reading both field contracts.
- In each acceptance route, identify who creates the source event and who observes its result. Check that the observing screen requests the API variant containing that result and that its counters use the same kind of record; a directly callable API variant is not a visible user flow.
- When a status row is refreshed, search the authored explanation for older status claims about that card. Resolve a stale phrase in the human-readable function entry; the generated row alone cannot correct prose.
- If the project keeps fingerprints of files cited by authored passport entries or screen tables, treat a changed fingerprint as a review queue: inspect the affected behavior and neighbors, then accept the new fingerprint explicitly. Do not silently refresh the fingerprint in the same command that generates route or schema inventories. An initial snapshot is a drift baseline, not proof that every cited file was fully reviewed.
- A cited-file fingerprint cannot detect a new source file that has not yet been linked. Also compare working-tree paths and commits since the last reviewed source revision; send unmatched additions through domain review before accepting a newer revision. Keep acceptance of reviewed committed paths separate from cited-file fingerprints; advance a repository revision only after every changed committed path in that revision has been reviewed.
- If the project has a change-trace helper, use it for changed files or requirement IDs (or its working-tree mode, if available) to find directly linked entries, open findings, and candidate scenarios. Confirm that a generated scenario catalog is current with its registry, then inspect each candidate and neighboring behavior before choosing a test; an indexed scenario is not a passed test.
- When filling a whole passport, work by bounded domains. At the end of each domain, report the remaining unlinked cards, confirm statuses from the canonical registry, and sample traceability in both directions: file → function and requirement → function. Do not treat a mention count as a completeness score.
- Track coverage in separate layers: structurally linked cards, source-backed behavior descriptions, checked cross-layer fields and transitions, and executable scenarios. Never turn the first layer's percentage into a claim that the passport is semantically complete.
- Separate a scenario's presence in a catalog from its execution state. A requirement can carry an accepted status and dated evidence while its structured demo contract is still marked planned; report that metadata gap, inspect the evidence, and avoid changing the authoritative status from the demo flag alone.
- Semantic checks must compare the proposed change with the meaning-level rules and adjacent workflows. An agent may draft a conflict report; a reviewer resolves policy choices and acceptance.
- Surface stale sources, conflicting evidence, and unknown physical or external contracts explicitly. Do not silently prefer an old diagram, generated page, implementation comment, or inferred graph relationship over current authoritative evidence.
- Add a new tool or publishing layer only when it solves a demonstrated navigation, freshness, or review problem. A renderer, graph, or skill does not replace the project-owned behavioral description.

## Find contradictions and unnecessary duplication

When filling an entry or changing a connected workflow, inspect its immediate neighbors for these specific signals. A request for full passport coverage justifies a staged inventory across the platform; an ordinary feature change does not authorize a full code audit.

- **Behavioral contradiction:** two accepted rules, or a rule and observable behavior, prescribe different outcomes for the same actor, state, and action. Record both sources, the exact conflicting condition, and who must decide the intended behavior. Distinguish a current implementation defect from an unresolved product decision.
- **Repeated description or function:** several entries, requirements, screens, or endpoints appear to provide the same user outcome. Identify the canonical behavior and why each variant exists before proposing consolidation. Shared logic, role-specific presentation, and historical versions can be intentional.
- **Duplicate implementation or data:** multiple handlers, services, calculations, or stored fields appear to own the same rule. Trace callers and writers, compare contracts and edge cases, and name the likely owner. A text or symbol match alone is only a lead.
- **Dead code candidate:** an entry point, branch, field, or integration appears unused. Check routes, dynamic registration, dependency injection, feature flags, background jobs, migrations, external callers, and tests before concluding it is unreachable. Mark uncertainty when runtime evidence is unavailable; do not remove code as a side effect of documenting it.
- **Missing connection:** a function has no verified requirement, scenario, owner, or downstream link where one is expected. Record the gap rather than inventing the missing relationship.

Keep a compact finding register linked from the passport. Classify each finding as **confirmed**, **candidate**, **intentional**, or **resolved**; include scope, two-sided evidence, consequence, decision owner or next check, and date. Do not label a similarity as a defect or a static-search absence as proof of dead code. Revisit open findings when the adjacent function changes, and close them only with evidence or an explicit product decision.
