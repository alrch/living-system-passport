# Function entry and change-impact note

Use this as a checklist, not a fixed document layout. Omit inapplicable fields with a reason; do not fill gaps with guesses.

## Function entry

| Field | Record |
| --- | --- |
| Stable function ID and name | Existing ID if available; otherwise a passport ID |
| Scope and state | What behavior is included; observed, planned, accepted, or externally gated, with status source |
| Meaning for people | Why this exists, who acts, what they receive, and the rule a future solution must preserve |
| Exceptions and boundaries | Negative cases, failures, manual/external duties, decisions still open |
| Screens | Routes, roles, fields, table columns, controls, visible states |
| API and services | Method/path, request/response/errors, authorization, implementation source |
| Data | Model or collection, fields, relationships, indexes, lifecycle; mark unverified physical names |
| Selection and completeness, when relevant | Applied filters and identity keys across sources; row limit, sorting, retention versus deletion, and whether UI and direct export reveal truncation |
| Field path | For consequential fields: UI input/default → client payload → API validation → service value → stored field → read/export; note any value lost or changed |
| Alternate write paths | Other entry points writing the same consequential field/state; compare policy, validation, dependent-state updates and intentional exceptions |
| Behavioral evidence | Selected rule/source, allowed control and relevant negative/cross-path/failure/retry check, expected versus observed readback/side effects; executed versus source-reviewed/proposed/blocked, with mock and environment limits |
| Transition path | Actor, precondition, ordered state writes and side effects, failure point, retry/idempotency, observable result |
| Connections | Upstream triggers, downstream consumers, neighboring functions, shared contracts |
| Traceability | Requirement/ticket IDs, scenario IDs, demo contract state, test execution/result/date, evidence and source revision; keep acceptance status separate from scenario metadata |
| Findings | Linked contradiction, repeated behavior, duplicate implementation/data, dead code candidate, or missing connection; status and evidence |

Write the human meaning as prose that a nontechnical colleague can read. Technical identifiers belong in the reference rows, not as substitutes for that prose.

## Change-impact note

**Proposed change:** observable behavior and reason.

**Meaning-level rule:** what must remain true, what is being changed, and any unresolved decision.

| Classification | Affected item | Evidence | Action or question |
| --- | --- | --- | --- |
| Confirmed change | Screen/API/data/rule/scenario | Current source or accepted decision | Concrete edit and targeted check |
| Inspect | Possible consumer or neighboring workflow | Graph lead, search result, or shared contract | Verify the exact relationship |
| Gap | Missing link, evidence, test, or owner | What was checked | Record the missing fact or decision |

Finish with the smallest useful scenario set and a list of passport entries to update. For implemented behavior or an audit, include actual scoped behavioral evidence or specific unexercised boundaries using the [behavior verification checks](behavior-verification.md); a test plan alone does not prove behavior. Separate a proposed test from a test actually run and passed.

## Finding note

Use one note per concrete issue, linked from all affected entries. Record: finding ID; class (behavioral contradiction, repeated function, duplicate implementation/data, dead code candidate, missing connection); status (confirmed, candidate, intentional, resolved); affected actor/state/action or code/data owners; evidence on each side; observed consequence; decision owner or targeted next check; and review date. A dead code or duplication candidate does not authorize deletion or consolidation.
