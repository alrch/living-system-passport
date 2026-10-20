# Product guide and joint passport review

## Purpose and canonical pair

Maintain two linked, authored documents: the technical passport explains behavior, rules, implementation links and verification boundaries; the product guide explains the product to a PM/owner and supports reasoning about changes. The guide replaces the former product passport/editorial summary. Do not keep a third competing current product description. Preserve historical material through the project's archive convention or a short forwarding document; update active navigation, source allowlists and reading views to the canonical guide. Stable public URLs may remain unchanged.

Title the guide “Product guide: <product>” in the reader's language; honor a user-supplied title. Choose its project-owned path alongside the technical passport and link them in both directions. Keep a mapping from guide chapters to existing passport function IDs, through ordinary links or the existing traceability mechanism. Do not invent a second function-ID system.

## Five parts

Use these five parts, adapting headings to the project:

1. Product meaning: users and their real work, intended result, success and scope boundaries. Distinguish known roles from assumed personas.
2. Main scenarios and functions: a connected journey with named capabilities, their inputs, outputs and interactions, including returns and corrections.
3. Important rules and constraints: consequences of changes, readiness, manual versus derived values, and exceptional states that affect product decisions.
4. Current state and grounds: practical user consequences of known problems, what is established, what remains uncertain and which evidence supports it. Link run history instead of pasting audit logs.
5. Development directions: desired outcomes, open questions, meaningful measures and a fully worked example of assessing a proposed function. Proposed behavior must remain visibly separate from current capability.

Length follows explanation needs; do not collapse a substantial product to a one-page inventory. Conversely, do not pad chapters to hit a size target. Keep API paths, database structures, commits, test listings and tool instructions in the technical passport or evidence; link when useful. Use concrete user language and explain domain terms needed to understand decisions.

## One continuous example

Use one object, person and starting situation throughout the guide. Show initial information, preparation, calculation/action, completed result and a subsequent correction that travels backward through the workflow and then forward again. Carry outputs from one episode into the next; unrelated mini-examples do not satisfy this purpose.

Prefer an available representative scenario. A fictional teaching example is acceptable when clearly labeled; it is neither a user finding nor an executed test. Do not invent numerical calculation results or customer acceptance. Include incomplete inputs, manual work and the point where the user decides the result is ready.

## Explain function connections

For each significant function or coherent group, explain:

- what the user needs before starting and where those inputs come from;
- what the function produces, where it is saved conceptually and which functions use it;
- what changes automatically, what becomes obsolete or is reset, and what remains unchanged;
- what the person must inspect, choose, save, apply or repeat;
- what happens with incomplete data, failure or retry where consequential;
- the precise unknown behavior if a relevant connection has not been established.

Separate descriptive current behavior, recommended working precautions and proposed rules. A recommendation to check an output must not imply an implemented warning or automatic update. “Check dependencies” alone is insufficient when the sources already establish the consequence. If the answer is genuinely unknown, localize the gap and its decision impact rather than guessing.

Cover branching and shared capabilities as well as the main forward sequence: libraries/defaults, roles and handoff, copies/history, document outputs and optional assistants where present. Distinguish similar concepts with different consequences, such as save/apply, copy/template and generated suggestion/accepted change.

## Work one proposed addition end to end

Choose a relevant proposal; retain a real owner-provided idea when available. Explain the user situation and useful result, today's way of doing the work, the smallest useful addition and why existing functions can or cannot support it. Trace upstream inputs and downstream results.

Show common versus independent information, changes to existing functions, invariants to preserve, manual work, failures/retries, changes after a completed result, decisions requiring agreement, boundaries deferred from the first version, acceptance scenarios and how to assess user benefit. Recommendations are proposals, not silently accepted requirements. A feature checklist or six unanswered questions is not a worked analysis.

Keep the guide's proposed behavior distinct from implementation work: guide authoring alone does not authorize changing product code, requirements status, payment/access rules or deployment.

## Joint review at existing lifecycle boundaries

Whenever the technical passport is reviewed, review affected guide chapters and direct neighbors in the same task. Correct inputs/outputs, user actions, dependencies, limitations, the continuous example and development analysis where necessary. Record a justified no-change result in the existing task/evidence record if the guide remains correct; do not add a dated update entry to its narrative for every review.

- Before an agent-run commit, review relevant changes since the last reviewed boundary, including new unlinked files, against the pair. Before push, cover additional outgoing changes; do not repeat an unchanged review just to produce a receipt. After a merge, assess the combined behavior.
- At CI/release/deployment boundaries, follow the project's actual workflow and compare the exact candidate/deployed revision and all relevant services. Bind each published pair to its actual environment. Local review does not establish pilot/staging/production behavior. Do not invent environments or mark runtime behavior verified from a source check.
- Keep revision/hashes, environment binding and review evidence in the existing manifest or task metadata. Build date, behavior review date, runtime version and acceptance remain separate.
- Deterministic checks can detect stale hashes, missing links and wrong version bindings. They cannot author or approve changed product meaning. Never claim a commit hook, CI semantic audit or automatic synchronization exists because the skill instructs agents to review it. Verify actual wiring; report absent automation explicitly.
- Preserve known mismatches as visible debt in the existing handoff if an update is deferred or blocked. Never advance an unreviewed baseline merely to make a check green.
- Publication remains within an explicitly authorized existing documentation workflow. A passport review does not by itself authorize commit, push or deploy, and optional publishing must not block product implementation.

## Review before handoff

Read the result as a PM unfamiliar with implementation. Use the worked addition to test whether the guide helps identify existing capabilities, common data, affected results and unresolved choices. Replace inventories with explanations where this fails. Check internal links, function anchors, active navigation and configured reading-view inputs. If the renderer changes, build and check its output; verify UI changes in a browser when the project requires it. Report content review, build/link checks and runtime/publication verification separately.

When updating installed skills, discover actual user-level and project-level paths, resolve symlinks, inspect differences and preserve unrelated local rules. Apply this contract to each installation in the requested scope; verify the new reference and entrypoint routing agree. Report the inspected paths and any installation or published upstream version not updated. Local synchronized edits are not a merged or distributed upstream release.
