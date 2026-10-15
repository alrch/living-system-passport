# Verify behavior beyond navigation

Use this when creating or auditing a passport, or reviewing a behavior change. Graph queries and source inventories select what to inspect; this pass checks the rules those links are supposed to enforce. It applies to the project's actual entry points, including libraries, command lines, batch jobs or documents. It does not require a UI, HTTP API, database or external provider.

## Select consequential rules, not a test quota

Identify the accepted invariant and its source before choosing an input. Prioritize access boundaries, irreversible or costly writes, state invalidation, shared calculations, configurable limits and retries with side effects. For a whole-project passport, select representative consequential transitions in each domain under review and show where only mapping was completed. For a local change, stay with the changed rule and its direct consumers. Do not pick only easy happy paths or expand a label correction into a system audit.

Choose the smallest useful set of checks that can distinguish the accepted outcome from a plausible implementation error. Reuse tests that assert that rule; a green nearby suite or a test with a relevant name is not sufficient. Where safe execution is available within the task's authorization, actually run the selected negative or cross-path check rather than only proposing it. A small disposable probe is suitable for diagnosis; do not turn every observation into a permanent test or product fix.

For planning, record proposed scenarios and their expected evidence without running them or claiming verification. For an audit with unavailable execution, continue source review and record exactly which claims remain unexercised. Do not manufacture a product requirement merely to obtain a failing test.

## Compare writers of the same logical state

Start from a consequential field, rule or state transition. Find the actual code that writes it, not only its displayed screen or model declaration. Check alternative paths present in this project: another role's editor, direct service call, import, bulk operation, background task, clone/restore or retry. Trace the shared storage/value and its immediate consumers to discover writers a graph may miss.

Compare the paths under equivalent preconditions: actor and scope, input normalization, validation, dependent-field invalidation, state writes, side effects, retry identity and returned/read-back result. Different roles or workflows can intentionally have different contracts; establish the accepted reason before labeling the difference a defect. A deliberate exception should have a scope and source, not be inferred from missing validation.

For a displayed setting, trace the value from editor to storage, policy reader, enforcing branch and observable allowed/denied outcome. Exercise a changed setting when safe. An editable/saved setting or an unused permission helper does not prove enforcement; a missing graph caller alone does not prove the setting is unused.

## Challenge the selected boundary

Apply only the cases relevant to the rule:

- **Access or scope:** compare an allowed actor/resource with a disallowed one through the actual callable boundary. Confirm rejection leaves state and side effects unchanged.
- **Values:** compare a valid control with an invalid or boundary input. Consider omitted versus explicit empty/false/zero, units, rounding and finite-number requirements where meaningful. Match the real parser/schema contract; direct language objects and transport payloads can accept different values.
- **Transitions and failures:** inspect the write order and exercise an eligible failure point using disposable state. Read back both primary and dependent state after rejection or partial failure; a status/error alone does not prove rollback.
- **Retry and repetition:** when the operation can be retried or repeated, apply the same logical request again and inspect records, totals and side effects. Check concurrent claims only when concurrency is relevant and can be isolated. Do not infer idempotency from the presence of a request ID.
- **Result consumption:** read through a real consumer or inspect stored state independently of the mutation response. Include related output such as a derived value, report, event or file when it is part of the accepted outcome. A response that echoes the request is not readback evidence.

Use isolated fixtures, temporary files, mocked external boundaries or an existing safe test target. An audit does not authorize real payments, production writes, destructive cleanup, sending messages or changing access. When those effects cannot be safely substituted within scope, preserve the boundary as unverified and give the specific next check. A mock can prove control flow or argument propagation while hiding real validation, transactions, serialization or delivery; inspect the relevant real contract and label the remaining limit.

## Record the evidence and finish honestly

Keep a compact note in the existing function entry or task evidence; no new tracking system is needed. For each selected rule, record:

| Rule and source | Writer paths compared | Check and expected result | Actual observation/readback | Evidence and boundary |
| --- | --- | --- | --- | --- |
| Accepted invariant or explicitly unresolved rule | Actual entry points and their scope | Allowed control and relevant negative, cross-path or failure case | State/output/side effects observed, or not exercised | Command/result/revision; source-reviewed, executed, proposed or blocked, with mock/transport limits |

Link a confirmed mismatch or candidate finding to the affected function. Source inspection can establish a source-level contradiction without runtime execution; name that level rather than implying live harm. Preserve failed probes as findings/evidence and distinguish a probe setup error from a product failure. Do not rewrite the expected result to match the implementation or call an existing green suite proof of an untested boundary.

Before closing a domain batch, check that consequential selected rules have both a writer-path comparison and the relevant adversarial evidence, or a specific recorded limitation. Do not label a mapped or merely source-reviewed domain as behaviorally verified. In a broad audit, continue the independent checks that remain within scope; do not stop because a graph counter is green or a desired number of findings was reached. Completion is about coverage of the requested questions, not a bug count. Return unresolved checks explicitly when the scope or safe execution boundary is reached.
