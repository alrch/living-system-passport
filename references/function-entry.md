# Function entry and change-impact note

Use this as a checklist, not a mandatory document layout. Omit inapplicable fields with a reason; never fill gaps with guesses.

| Field | Record |
| --- | --- |
| Stable ID and name | Existing function ID, or a distinct passport ID |
| Scope and state | Included behavior; planned, observed, accepted, or externally gated, with status source |
| Meaning for people | Purpose, actors, outcome, and the rule a future solution must preserve |
| Exceptions | Negative cases, failures, manual or external duties, open decisions |
| Interface | Screens or entry points, roles, visible controls, fields, and states |
| Services and API | Method or event, request and response, errors, authorization, implementation source |
| Data | Models, fields, relationships, indexes, lifecycle, and unverified physical names |
| Field path | For consequential values: input and default → validation → transformation → storage → read or export |
| Transition path | Precondition, ordered writes and side effects, failure point, retry, observable result |
| Connections | Upstream triggers, direct consumers, neighboring functions, shared contracts |
| Traceability | Requirement or ticket IDs, scenarios, test result and date, evidence, source revision |
| Findings | Linked contradictions, duplicate candidates, unused-code candidates, missing connections |

Write the human meaning as prose a nontechnical colleague can read. Technical identifiers support that explanation; they do not replace it.

## Change-impact note

State the proposed observable change and the rule to preserve or change. Then record:

| Class | Affected item | Evidence | Action or question |
| --- | --- | --- | --- |
| Confirmed change | Rule, screen, API, data, or scenario | Current source or accepted decision | Concrete edit and targeted check |
| Inspect | Possible consumer or neighbor | Graph lead, search result, or shared contract | Exact relationship to verify |
| Gap | Missing link, evidence, test, or owner | What was checked | Next check or decision |

Finish with the smallest useful scenario set and the passport entries to update. Separate proposed checks from checks actually run and passed.

## Finding note

Use one note per concrete issue, linked from affected entries. Record its ID, class, status (confirmed, candidate, intentional, or resolved), affected actor or component, evidence on both sides, consequence, owner or next check, and review date. A dead-code or duplicate candidate does not authorize deletion or consolidation.
