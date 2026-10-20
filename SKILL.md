---
name: living-system-passport
description: Build or maintain a living system passport that connects product behavior to screens, APIs, data, requirements, and tests. Use to map a whole project, audit an existing function, plan a new function, or assess a behavior change; connect findings to project quality checks without making the passport a tool configuration. Create and maintain its linked product guide for PMs, including function interactions and joint lifecycle review.
---

# Living System Passport

A passport helps people and agents understand what a system does and what a proposed change may affect. Keep one navigable, project-owned description of behavior and its evidence. Adapt its file layout to the project; one logical passport can be one file or several linked pages. Preserve existing canonical sources instead of copying their authority into the passport.

The workflow is portable. Discover the project's own sources of truth, repositories, status language, scenario format, indexes, and checks before applying it. The detailed domain checks are optional: select only those matching the behavior under review. No particular architecture, infrastructure, registry, or business domain is required. Verify the actual skill path and revision when user and project installations share this name; do not inherit another project's adapter through a symlink or profile.

Read the project's instructions for its [passport adapter](references/project-adapter.md): where the passport and source evidence live, which changes trigger review, how linked entries are found, and which project commands validate or refresh them. If no adapter exists yet, establish the minimum facts needed for the requested task instead of inventing commands or copying another project's configuration. Project instructions can make this skill mandatory for particular changes without duplicating its full method.

## Keep the passport separate from the change journal

The passport describes the system's current functions, behavior, rules, boundaries and interactions. It is not a changelog, release report, audit diary or task plan.

- Start with the system's purpose, scope, navigation and functions. Do not prepend dated updates, test summaries, deployment history, "what changed", "what to change next", or a findings dashboard.
- Update a changed rule in its existing function entry. Record the resulting behavior, not the sequence of fixes or implementation attempts. A bug fix that restores the documented contract may require no passport prose change.
- Keep change history, decisions and attempts in the project's journal/task history. Keep test runs, screenshots, logs and release details in their existing evidence/operational records. Link to those sources without duplicating their chronology in the passport.
- Put a finding under the affected function, with its current status, consequence and source link. Put genuinely cross-cutting findings in a general findings section at the end. A separate canonical register may retain the details; do not copy its issue history into each entry.
- A function may link to its requirement, scenario and verification evidence and briefly state a material uncertainty. Keep run-by-run results, timestamps, build hashes and deployment receipts outside the narrative; optional version metadata belongs in a separate manifest or compact metadata view.
- Reviewing passport freshness, changing its prose and publishing its reading view are separate actions. Do not require a new entry or publication after every fix or deployment. Publish only within an already authorized documentation workflow or an explicit publication request; do not make optional publication a blocker for the user's implementation task.

## Maintain a technical passport and product guide

Maintain the product guide alongside the technical passport; it replaces the former product passport/editorial summary. Read [product-guide.md](references/product-guide.md) when creating either document, replacing the product view, or reviewing affected behavior. Use the five-part guide, one continuous example, explicit function dependencies and a worked proposed addition. Review affected guide chapters whenever the passport is reviewed, including existing commit/push and environment-specific release boundaries. Record a justified no-change result when appropriate. Keep actual automation, review evidence and publication authorization distinct; a skill instruction is not an installed hook or proof of deployed behavior.

## Establish the boundary

- Find the project's current instructions, product documents, requirement/status source, architecture index, API contracts, schema definitions, and scenario tests. Identify which source owns each fact. Do not infer approval, release, or production behavior from code presence.
- Prefer existing IDs for functions and scenarios. If no function ID exists, create a stable passport ID and distinguish it from requirement or ticket IDs.
- Match the requested scope. For a feature, trace its connected workflow. For a whole-project passport, inventory the project's domains and entry points first, then work through them in bounded batches. A calibration batch does not reduce an explicitly requested whole-project scope; keep working through the remaining domains without asking for renewed permission.

## Create a passport or a new function entry

If the project has no passport, first locate accepted product rules and a few consequential user journeys. Choose a navigable home for one logical passport and define how entries link back to authoritative sources. Choose the first connected domain within the requested scope; draft entries for its visible outcomes and the technical paths that realize them. For whole-project work, keep a coverage map of reviewed, inventory-only, excluded and unresolved areas, including non-UI entry points when present. Do not generate a platform-wide inventory and label it a completed behavioral map.

Before naming a new entry, search the project's existing passport and index for the same user outcome; reuse its function ID if one exists. For each new entry, identify the actor, trigger, precondition, observable result, meaning-level rule, exceptions, owner, and technical path. Link current requirements, code, contracts, data, neighboring functions, and scenarios with evidence. If a narrow decision implements part of a broader requirement, find that parent and any later decision that changes its boundary; link each with its own scope and status. Mark a missing or inferred link explicitly. A function may have no dedicated requirement card; use a distinct passport ID rather than borrowing a neighboring card's status. Apply the [function-entry template](references/function-entry.md) as a completeness check, not a mandatory layout. For a workflow with filters, exports, multiple event sources, or retention, read only the matching [domain review checks](references/domain-review-checks.md) while drafting, not only when auditing a later change.

Before calling the first domain complete, sample traceability in both directions: requirement or user outcome → function → implementation and changed source file → function → scenario. State separately what is structurally linked, described from current sources, checked across layers, and exercised by a scenario. A discovered route or a passing structural check proves only its own layer.

## Use the project graphs

Separate graph purposes from tool names: a code graph navigates implementations and dependencies; a traceability graph connects outcomes, rules, functions, sources and scenarios. Graphify and Codebase Memory can overlap on code navigation; neither automatically proves requirement acceptance. Explicit citations must retain citation semantics.

Use the [graph workflow](references/graph-workflow.md) when connecting tools, tracing dependencies or performing a graph audit. Reuse the project's existing indexes. Prefer Codebase Memory for exact symbols/callers and Graphify for architecture or document relationships when both are usable; choose by actual capability and question. A known text-only edit needs no graph query. An ordinary behavior change needs a focused dependency trace, not duplicate queries to both engines. When the owner requests both, prove readiness and use each for its distinct contribution, recording any unavailable coverage.

Start from an exact ID, symbol, file or entry point; inspect bounded incoming consumers, outgoing dependencies and relevant tests separately when a shared limit hides one direction. Read current sources to confirm consequential edges and cross-boundary contracts. Keep totals, confidence, provenance, truncation and parser exclusions visible. Missing edges do not prove there are no consumers, and a test edge does not mean a test passed.

Keep project identities, commands, graph outputs and runtime settings in the project adapter. A missing tool does not silently reduce requested coverage: diagnose it within scope, use source search for independent work, and report the exact remaining limitation. Do not call an explicit dual-tool audit complete until both were exercised or the limitation was clearly handed back.

## Verify behavior beyond the map

Creating or auditing a passport requires a behavior-verification pass after navigation. Select consequential rules in the requested scope and read the [behavior verification checks](references/behavior-verification.md). Find the actual writers of the same logical data or transition, compare their validation, authority, dependent-state updates and side effects, and follow the result into storage or a real consumer. A setting must reach an enforcing branch; a saved value or permission helper alone does not establish its effect.

For the selected rules, exercise the relevant negative, cross-path, failure or retry scenarios when safe execution is available and authorized. Include an allowed control and inspect readback and side effects, including absence of writes on rejection. Reuse useful tests or make a small isolated probe; do not stop at a suggested test list or a green unrelated suite. Plans need proposed checks only; text-only edits do not trigger a behavioral audit. If execution is unavailable, continue source review and identify the exact unexercised boundary without inventing results or changing product code merely to make the audit complete.

Track mapping, source review and executed checks separately in existing entries/evidence. For a broad passport, apply this pass by domain and keep remaining checks visible; a successful graph lookup does not complete a behavioral review. Record writer paths, expected versus observed behavior, readback and execution limits. Detailed examples in the domain reference are conditional; the decision to verify consequential behavior is not optional.

## Work in domain batches

When building a broad passport, take one connected domain at a time. Start with a few consequential actor journeys and trace each through its actual entry point, rule, state, external boundary and observable result. Include screens and APIs where present; omit nonexistent layers in a library, CLI, batch or document workflow. Prioritize accepted behavior, access or data loss boundaries, and changes that affect several neighboring functions. Keep planned details in the map without requiring every planned field to receive the same depth immediately.

Within the domain, correct source-backed descriptions and links autonomously. Sort findings into a documentation correction, a reproducible implementation gap, or an unresolved product rule. Give implementation gaps an exact scenario and evidence; keep product code changes in their own authorized task. Bundle unresolved product choices into one short decision packet for the domain with the competing rules, options, consequences and a recommended default where the sources support one. Do not request approval for every field or repeat decisions already recorded in authoritative sources.

Before putting an item in an owner decision queue, apply a decision filter. If an accepted rule or basic invariant already fixes the expected outcome, treat the mismatch as a bug and repair it within the user's authorized scope. If evidence is missing, investigate the source or runtime path first. Ask the owner only when at least two defensible outcomes remain after that work and choosing one would change product behavior, access, data retention, or an external obligation. Keep completed fixes and deployment checks out of the active owner-question list. A prior decision packet does not make an obvious technical fix a recurring question.

For a numerical or time-window rule, read the primary source before reducing the choice to a threshold or formula. Name the measured event, numerator and denominator, population, window boundary, and any stated exclusions. If those differ from the available data, surface the difference in one coherent decision packet rather than implementing the chosen number against a convenient proxy.

If a rule compares periods only while a condition remains unchanged, identify the observable fields that define that condition and whether their historical values are retained before offering an implementation choice. When the source does not define the condition, include its proposed meaning in the same decision packet; a choice of strict comparison alone does not define what must be compared.

After the owner selects an outcome, implement the connected finding within the authorized implementation scope before opening another owner question. In an audit-only task, record the accepted correction and its implementation follow-up without changing product code. Resolve ordinary algorithm and data-handling details from the accepted rule and the safest compatible defaults; record behaviorally significant defaults in the affected function entry; keep implementation history in the journal. Do not split one finding into a chain of microdecisions merely because several implementation cases exist. Reopen the owner question only if source review reveals a materially different product outcome.

If the owner explicitly defers a product choice, record the event that will reopen it (for example, a release cutoff), preserve current behavior, and continue independent work. Do not present the same deferred choice as a blocker or ask it again on every domain pass.

Finish the batch when the important journeys and accepted rules have a traceable observable outcome, consequential rights and fields have been checked through their direct dependencies and relevant writer paths, and the selected behavioral checks have observed results or specific execution limitations. A map with only planned scenarios is not a behaviorally verified batch. Report what was checked and what remains open; avoid a single completeness percentage for the whole platform. Use the first batch to calibrate the depth and review cost of later batches.

For an owner-authorized autonomous pass, keep working through independent findings after each local fix and verification. A progress report is not a completion event. Stop the pass only at its agreed time or scope boundary, when no independent work remains, or when the next action genuinely requires the owner's decision or external evidence. Name the unfinished findings and the exact next step when handing the pass back; never imply the whole passport is complete because one batch passed.

## Describe each function on two levels

1. **Meaning for people:** purpose, actors, observable result, business rules that must survive changes, exceptions, responsibility outside the system, and unresolved decisions. Use ordinary language. Explain why a rule matters when that changes implementation decisions.
2. **Technical realization:** entry points and screens, visible controls and fields, API methods and contracts, services, stored data and indexes, integrations, permissions, state transitions, and failure behavior. Link precise sources rather than pasting entire code or specifications.

When an optional recommendation or filtered result appears beside a regular list, trace the condition for each request and the visible fallback when the optional result is empty or fails. Do not describe an absent recommendation as an empty catalog unless the regular list is also empty.

Connect both levels to the relevant requirements, their current statuses, evidence, and scenario tests. Label each link as confirmed or a candidate needing verification. A function may serve several requirements, and a requirement may cross several functions. Keep external or manual obligations visible without portraying them as implemented software.

Use [the function-entry template](references/function-entry.md) when creating a new entry or comparing an existing one for missing information. Follow an established project format if it already provides the same information.

## Analyze a proposed change

For a new function or change in logic:

1. State the proposed behavior and the meaning-level rule it changes or must preserve. Identify the affected actors and states.
2. Search for the same user outcome in existing functions and implementations. Name the best extension point; propose a new module only when its responsibility differs, and explain why the existing one does not fit.
3. Trace the smallest relevant chain in both directions: user action or external event → actual entry point → implementation → state/integration, using only layers the project has; then find direct consumers, shared contracts, nearby functions, and scenario tests. Use existing indexes first, followed by targeted source checks.
4. Return an impact list with **confirmed changes**, **places to inspect**, and **missing/uncertain links**. Give evidence for each. Do not turn a possible dependency into a proven breakage.
5. Choose scenario checks for the changed rule and its direct dependencies: normal path, access boundary, failure or retry, and relevant edge state. Reuse existing scenarios before adding new ones. Run only the checks warranted by the actual change and project gates.
6. Review the affected passport entry in the same task. Update its current description only if the accepted behavior or its links changed; a restored documented contract may need no prose change. If the answer is not yet decided, record the open question and owner of the decision rather than inventing a rule. Record why a reviewed neighboring entry needs no edit when that matters for traceability.

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

- Keep generated inventories separate from authored meaning and reviewed baselines. Structural links, source review, cross-layer checks and scenario execution are different coverage layers; report them separately.
- Start from the task's changed files, rules and statuses, including new unlinked files. Compare current sources with the reviewed boundary; a timestamp or a hash of cited files alone cannot detect every new entry point.
- Record source revisions and relevant working-tree changes for each repository in the evidence record or metadata, not as a passport change narrative. Refresh indexes from current inputs without accepting unreviewed behavior or unrelated drift.
- Review human prose as well as generated status rows. Resolve superseded sources before creating an owner question; preserve historical evidence with its date and scope.
- Bind final audit evidence to the passport text and inspected sources. Freeze them during the final pass or compare before/after hashes; if they change, mark the result stale and recheck the affected scope. An initial fingerprint records a boundary, not semantic approval.
- For the project's actual registry, roles, screen moves, external handoffs or generated views, read the relevant [maintenance checks](references/maintenance-checks.md). Do not load every conditional check for an unrelated task.

## Find contradictions and unnecessary duplication

When filling an entry or changing a connected workflow, inspect its immediate neighbors for these specific signals. A request for full passport coverage justifies a staged inventory across the platform; an ordinary feature change does not authorize a full code audit.

- **Behavioral contradiction:** two accepted rules, or a rule and observable behavior, prescribe different outcomes for the same actor, state, and action. Record both sources, the exact conflicting condition, and who must decide the intended behavior. Distinguish a current implementation defect from an unresolved product decision.
- **Repeated description or function:** several entries, requirements, screens, or endpoints appear to provide the same user outcome. Identify the canonical behavior and why each variant exists before proposing consolidation. Shared logic, role-specific presentation, and historical versions can be intentional.
- **Duplicate implementation or data:** multiple handlers, services, calculations, or stored fields appear to own the same rule. Trace callers and writers, compare contracts and edge cases, and name the likely owner. A text or symbol match alone is only a lead.
- **Dead code candidate:** an entry point, branch, field, or integration appears unused. Check routes, dynamic registration, dependency injection, feature flags, background jobs, migrations, external callers, and tests before concluding it is unreachable. Mark uncertainty when runtime evidence is unavailable; do not remove code as a side effect of documenting it.
- **Missing connection:** a function has no verified requirement, scenario, owner, or downstream link where one is expected. Record the gap rather than inventing the missing relationship.

Keep a compact finding register linked from the passport. Classify each finding as **confirmed**, **candidate**, **intentional**, or **resolved**; include scope, two-sided evidence, consequence, decision owner or next check, and date. Do not label a similarity as a defect or a static-search absence as proof of dead code. Revisit open findings when the adjacent function changes, and close them only with evidence or an explicit product decision.


Keep skill/tool/agent-method observations separately from product findings, using existing lightweight project locations. Preserve finding IDs when splitting an existing register and link each register from the passport or adapter. For a method observation, record the reproducible friction, proposed portable correction and its validation. Mark it adopted only after the shared skill or helper actually changes; do not call it resolved merely because one project has a workaround. Keep unmeasured efficiency claims and untested transfer hypotheses explicit.

For team feedback, use the [shared feedback workflow](references/feedback.md): reusable observations from any project go to this skill repository's Issues or pull requests under the user's submission authorization. Keep project-specific evidence local and link the shared discussion back to the local method finding. The application's push does not publish the skill.
