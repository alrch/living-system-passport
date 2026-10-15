# Project adapter for the living system passport

The shared skill defines decisions and evidence standards. The owning project supplies locations, commands, and authoritative meanings. A concise section in the project's existing agent instructions or documentation is enough; do not create a second competing rulebook.

## Facts to define for the project

| Question | Project-owned answer |
| --- | --- |
| What is the passport? | Canonical file or linked pages; stable ID convention; finding register location |
| Who owns each fact? | Product rules, requirement wording and status, code, API contracts, data, tests, releases, external evidence |
| What is the repository boundary? | Code repositories and revision identifiers needed to describe one current behavior |
| What triggers review? | Product changes, requirement/status changes, source pulls, screen or API moves, new files, accepted decisions |
| How are affected entries found? | Existing index, graph, changed-file or requirement-ID lookup, or targeted search |
| Which steps are generated? | Inventories and indexes; the build commands and whether regeneration is safe on a mixed working tree |
| How is review accepted? | Structural and scenario checks; source fingerprint or revision baseline procedure, if one exists |
| What must be reported? | Checked scope, evidence, unresolved drift, separate test/CI/deployment results |

Record only commands that exist and the conditions under which they should run. If there is no scenario catalog, graph, fingerprint baseline, or generated view, the shared skill still works from source search and explicit evidence.

## A safe maintenance contract

1. Identify the task's changed paths and requirement IDs. If a helper offers a broad `--changed` mode, use it only when the entire reported change set belongs to this task; otherwise pass exact paths or IDs.
2. Inspect linked entries, direct neighbors, and new source files that are not linked yet. A cited-file fingerprint cannot discover a wholly new file.
3. Update the human explanation and technical links after confirming the current rule and source. Refresh generated views only after their authoritative inputs are current.
4. Run the project's relevant structural check and targeted scenarios. Distinguish a catalog entry from a scenario result and a local result from a released result.
5. If the project tracks reviewed fingerprints or commits, accept only sources actually inspected. Never advance a whole-repository baseline merely to make a check green while unrelated drift remains.
6. Report unrelated drift separately. Do not silently absorb it into the task or imply that the whole passport was reviewed.

This contract applies to creation and editing. On first creation, the baseline records where review starts; it does not prove semantic completeness. On later edits, preserve the previous reviewed boundary until each affected item is checked.
