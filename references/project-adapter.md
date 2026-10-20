# Project adapter for the living system passport

The shared skill defines decisions and evidence standards. The owning project supplies locations, commands, and authoritative meanings. A concise section in the project's existing agent instructions or documentation is enough; do not create a second competing rulebook.

## Facts to define for the project

| Question | Project-owned answer |
| --- | --- |
| What is the passport? | Current functional description and stable IDs; findings under functions or cross-cutting findings at the end; canonical journal, task history and evidence locations kept separate |
| Who owns each fact? | Product rules, requirement wording and status, code, API contracts, data, tests, releases, external evidence |
| Where are selection and lifecycle rules? | Identity keys across sources, visibility and retention policy, cleanup mechanism, if the project has filterable records or exports |
| What is the repository boundary? | Code repositories and revision identifiers needed to describe one current behavior |
| What triggers review? | Product changes, requirement/status changes, source pulls, screen or API moves, new files, accepted decisions |
| Which graph serves which purpose? | Code dependencies versus outcome/rule/scenario citations; engines, actual index identities, build/status/query commands, exclusions and readiness evidence |
| How are affected entries found? | Existing index, graph, changed-file or requirement-ID lookup, or targeted search |
| Which steps are generated? | Inventories and indexes; the build commands and whether regeneration is safe on a mixed working tree |
| How is behavior exercised safely? | Existing test/probe commands, disposable data or supported isolated target, callable boundaries and readback paths; identify external effects that remain unverified |
| How is review accepted? | Structural and behavioral/scenario evidence, writer-path comparison and explicit execution limits; source fingerprint or revision baseline procedure, if one exists |
| How is the skill installed? | Actual source repository, installed path and revision; no dependency on another project checkout or private profile |
| Where does reusable feedback go? | Shared skill Issues/PRs; local method finding links back to its submitted URL; submission authorization and actual access remain explicit |
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


## Graph integration and direct project rules

Read [graph-workflow.md](graph-workflow.md) when adding Graphify or Codebase Memory. Put the operational rules below directly in the project's existing agent instructions, adapted to real installed commands and paths. A reference to another project's instructions is not an adapter. Do not invent a service layout, add a daemon, require both tools on every edit or install a tool solely to fill a template.

```markdown
### Passport and graph maintenance

- The passport describes behavior; code graphs navigate dependencies and traceability graphs preserve explicit outcome/rule/source/scenario links. A citation is not implementation or acceptance.
- For behavior changes, check the affected repository index and trace the implementation, direct consumers, dependencies and relevant tests before editing. Use bounded queries and verify consequential links against current source. Known text-only edits can use direct search.
- Use Codebase Memory for exact code impact and Graphify for architecture/document relationships when available and appropriate. Do not duplicate ordinary queries; exercise both when a dual-tool audit is requested.
- Name the repository/index explicitly. Check status, source freshness, exclusions and partial parsing; separately discover new unlinked files. Retain confidence, truncation and test-inclusion limits. A test relationship is not a passing test.
- Missing or stale tooling requires a concrete diagnosis and scoped source fallback; do not silently mark a requested dual-tool check complete. Do not restart or delete another session's runtime to repair a local index.
- Update the authored passport and links with an accepted behavior change, refresh affected generated views, and accept reviewed baselines separately. Record revisions/document hashes for final audit evidence; invalidate affected evidence if its inputs change.
- Keep product findings and skill/tool/method findings separate in the project's existing documentation. Findings do not authorize unrelated implementation or publication.
```

Alongside these rules, record actual local commands and locations from the table above. Keep executable project adapters parameterized by local repositories and IDs; the shared skill must not import a previous project's route parser, source catalog, shell environment or infrastructure assumptions.

## Editorial and publication boundary

The adapter must preserve the distinction between current functional description, change journal and execution evidence. Do not add mandatory dated passport entries or republishing to every code fix/release. Review the affected entry and record a no-change conclusion in the task record when the documented contract remains correct. Put hosting/version-binding mechanics in operational metadata; publishing remains a separately authorized workflow.

## Product guide binding

Record the canonical product-guide path, its chapter links to passport function IDs, the old product-view replacement/redirect, actual commit/push review rules and deployed-environment/version bindings. Follow [product-guide.md](product-guide.md) for content and joint review. Update active navigation, reading-view source allowlists and manifests to the guide; do not create a third current product summary. State whether each lifecycle check is agent-run or actually enforced by hooks/CI.
