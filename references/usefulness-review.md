# Autonomous usefulness review

Use for creation, substantial expansion and audits of the technical passport/product guide. For routine maintenance apply the questions only to the changed behavior and direct neighbors. The goal is a usable explanation with honest evidence, not maximum length or a documentation score.

## Establish what “ready” means for this request

Identify the reader's work, decisions and requested scope. If the owner supplied a good reference, inspect representative passages and extract the capabilities that make it useful: action granularity, concrete rules, field/state consequences, navigation and change analysis. Do not copy its domain, size, infrastructure or requirement registry into another project.

Inventory the actual entry points before a whole-project rewrite, including role-specific UI, public/API-only actions, imports/bulk operations and background jobs where present. Use the existing domain map to track authored/source-reviewed/exercised/remaining coverage separately. Work through the requested domains; one calibration batch is not a completed broad assignment.

## Turn evidence into current knowledge

For each domain read its current reports, relevant accepted decisions, implementation and consequential tests. Extract current rules and negative/retry behavior. Put those facts in the function entry and explain their practical consequence in the guide; keep commands, timestamps, raw test results and deployment history in evidence. A reader should not have to reconstruct an order lifecycle from a migration report.

Distinguish three different facts: what the implementation does, what execution has demonstrated, and what the owner has accepted. Reuse historical execution evidence only with its source/revision/scope; do not present it as a new run or as current runtime proof. Compare changed sources before carrying its claim forward.

For a consequential calculation or transition, explain actual branch/default selection and its result rather than naming a calculator or fallback. For retry/correction, recover the exact request identity, compared/preserved values and rejected versus reused outcome. If linked records are grouped or matched, state the identity and cardinality that determine the result. Scope this precision to rules a reader needs to reason about; do not transcribe every implementation line.

## Read the result without filling gaps from memory

Select realistic tasks across the consequential branches in scope. Include correction or reversal and one proposed change. Answer using only the authored pair, following its links when needed. For each answer cite the actual passage; if the answer relies on knowledge from investigation that is absent from the text, the document fails that question.

| Reader question | Sufficient answer |
| --- | --- |
| Who can start and what must already exist? | Actor, object/scope, concrete inputs and their origins; distinguish viewing from changing |
| Where does the person act and when is the result ready? | Screen/command, significant fields and actions, visible result and the downstream consumer |
| What changes automatically and what remains a historical fact? | Exact dependent fields/states, snapshots/invalidation, manual next actions; no blanket “check dependencies” |
| What happens on failure, partial data, repetition or correction? | Actual boundary, rejection or partial result, recovery/retry semantics and any known defect |
| What would a proposed change affect? | Existing extension point, upstream input, direct consumers, shared contracts, preserved invariant and relevant scenario |
| What supports this answer? | Precise current source and applicable scenario/evidence; observed/planned/accepted status kept separate |

Follow partial results to their terminal state: what remains outstanding, which
promise/reservation survives or is released, and whether the same document can be
completed later. Compare the actual public entry point with a shared service or
wrapper before describing them as equivalent. When a summary groups records,
check which identity links are retained in the original records and lost in the
projection; neither invent a per-person link from an aggregate nor call an
existing partial link wholly unknown.

For the guide, check that the same teaching example carries actual outputs into later steps and works backward through a correction before continuing. Include branches such as insufficient stock, incomplete configuration, another responsible role, and an already completed result where they materially change work. Technical identifiers may be linked, but must not replace the user's explanation.

## Check the working loop as well as the text

For a substantial rewrite intended to support later implementation, retain the original explanation and a source-bound intermediate document revision before the main fixes. Use the improved passport to select a real extension point, trace consequences and choose checks; after the change, reconcile the explanation and rerun affected reader questions. Record what was learned from the passport versus rediscovered in source. Do not impose a whole-project rewrite or intermediate commit on routine maintenance; a fingerprint or existing evidence record can preserve the boundary without granting Git authorization.

During broad acceptance, add a fresh question about a consequential exception or proposed change that was not used to draft the answer. Answer from the final documents and links first, then verify against source. Capture the actual answer location, gap and correction. Another agent is useful when authorized, but is not necessary for every review. An analyzer inventory, green gate or working graph cannot fill a missing explanation from the reviewer's memory.

When a quality-tool rollout is in scope, verify its separate [control proofs and enforcement boundary](quality-controls.md#accept-both-explanations-and-controls). Documentation can explain a rule even when a static tool cannot cover it; a static result does not establish that the rule was exercised. Keep semantic, behavioral, structural and enforcement conclusions distinct.

## Criticize and repair before handoff

Look specifically for these failure modes:

- A domain label or a few source links stand in for several different actions.
- The text says a test passed but omits the rule it established.
- “Nothing changed” preserves an incomplete explanation even though new knowledge was obtained.
- The guide repeats migration status, tooling or server configuration instead of helping the reader do or assess work.
- Generic cautions (“check”, “may affect”, “not verified”) replace an available answer.
- The change example is an idea checklist without actual inputs, consequences, boundaries and acceptance cases.
- A collection of route/model names is described as full behavioral coverage, or an absent customer registry prevents documenting source-established behavior.
- Two sections describe incompatible current topology or policy because historical evidence was copied into the present tense.

Check that navigation/coverage labels, function entries and the guide describe
the same knowledge boundary. For consequential findings extracted from the
selected reports, verify their presence in the current explanation; a link to
the report alone does not pass this check.

For every material gap: locate the owning source, investigate within scope, rewrite the affected explanation, and rerun the failed reader question. Continue with independent gaps until the scoped questions are answerable or the remaining boundary genuinely needs external evidence, a product choice, or additional authorization. Do not ask permission for ordinary further reading or editing already requested. Do not finish merely because a planned number of passes was reached.

A legitimate unknown is local: name the actor/action/state, sources already checked, observable consequence and exact missing evidence. Lack of runtime access does not prevent explaining code-established behavior. Unknown legal/customer intent does not erase observed behavior. Never silently choose a new product rule to fill a gap.

## Record and deliver

Keep the review in the project's task/evidence record, outside the passport narrative. Record the reader questions and answer locations, material gaps found and repaired, genuinely remaining limitations, source/document fingerprints and the actual checks run. An existing suitable record is preferable to a new tracking system. An independent review can strengthen this pass when authorized and warranted; another agent and repeated green structural checks are not required for every edit.

Check navigation and source links, preserve existing anchors, build the configured reading view, and inspect it if rendering/layout changed or the project requires browser QA. Recheck affected claims if their sources change during review. Report authored coverage, reused evidence, new execution and publication separately. A completed documentation pass may retain precisely bounded product uncertainties; it cannot retain source-answerable omissions and call the result complete.
