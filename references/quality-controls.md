# Persistent quality controls linked to the passport

Read for project onboarding, an authorized quality-tool rollout, a broad technical audit, or repair of a suspect check. For routine changes use the established profile and read only the relevant failure/maintenance section. The shared skill specifies evidence and decisions; executable configuration stays in the project. A project need not use a particular language, CI provider or tool collection.

## Select capabilities and record the profile

Inspect existing instructions, manifests, entry points, analyzers and CI before adding tools. During broad setup/audit, assess each applicable capability below. Reuse an existing solution that demonstrably covers it; record a missing or unsupported capability with its consequence and next action. Do not silently omit it or install every example to fill a list. A documentation-only task does not authorize this rollout.

| Capability | Evidence of useful coverage | Possible tools; verify the selected release |
| --- | --- | --- |
| Code navigation and repository map | Actual definitions, consumers and a compact generated map; change/delete freshness and parser limits known | Existing graph/IDE index; [Codebase Memory](https://github.com/DeusData/codebase-memory-mcp), [Graphify](https://github.com/Graphify-Labs/graphify); see [graph workflow](graph-workflow.md) |
| Structural search and reuse | An AST query finds a representative construct in real source; agent can locate an existing implementation before adding another | Existing language tools, [ast-grep](https://ast-grep.github.io/guide/) |
| Architecture boundaries and cycles | Real resolved imports, forbidden directions and complete cycle paths under the project's module conventions | [dependency-cruiser](https://github.com/sverweij/dependency-cruiser) for JS/TS, [Import Linter](https://github.com/seddonym/import-linter) for Python, suitable native equivalents |
| Duplicate fragments | A new real clone is distinguished from reviewed existing debt; semantic duplication is additionally reviewed by responsibility | Existing native duplicate detector, [jscpd](https://github.com/kucherenko/jscpd) |
| Unused-code candidates | Real entry points, plugins, public APIs and dynamic registration accounted for; confidence and exclusions recorded | [Knip](https://knip.dev/) for JS/TS, [Vulture](https://github.com/jendrikseipp/vulture) for Python, native equivalents |
| Function/capability index integrity | Unique existing function IDs, valid implementation/consumer/scenario links and resolvable referenced symbols | Existing passport index/registry and its validator; a new competing catalog is unnecessary |
| Decisions and verification | Contract/ownership decisions have a reason and scope; lint/types/build and meaningful scenarios run where applicable | Existing ADR/journal and project test/build commands |

Check current official documentation, installed help, language/OS/runtime compatibility and native baseline/report support before choosing versions or writing glue. Prefer the tool's own parser and identifiers; write minimal adapters only for demonstrated gaps. Do not introduce a second parser, generic graph store or all-language quality runner into the shared skill.

Record the following in the existing project adapter or quality configuration. One concise table is sufficient; no fixed filename or second registry is required:

- Capability, chosen tool/version, purpose and owner; required versus advisory status and explicit exclusions.
- Analyzed roots/languages, real package names/aliases, public/dynamic entry points and expected inventory/coverage checks.
- Reproducible installation and local command, working directory, runtime/dependencies, configuration and output paths. Keep tool runtimes separate from application requirements where needed; pin compatible project dependencies rather than changing a shared/global runtime.
- Existing-debt baseline location, finding identity/multiplicity rules, approval policy and trusted CI source.
- Positive/negative proof, relevant source/config revision and when it becomes stale.
- Local/CI trigger, the real enforcing entry point and last observed execution boundary; for advisory checks, who investigates their findings.

Source maps, indexes and raw reports belong in ignored output locations; configuration, reviewed baselines and reproducible commands belong in the project. Reuse passport function IDs for capability ownership and links to implementation, consumers, contracts and checks. Validate referenced symbols through the project's actual language tooling, not merely file existence. A missing dedicated test is a coverage gap, not an invented link. Keep decision rationale in the existing ADR/journal.

## Establish controls without concealing the starting debt

1. Preserve the worktree and establish the inspected source revision and any relevant local changes. Run available baseline behavior/build/quality checks with their actual prerequisites; retain original failures.
2. Configure one applicable capability at a time. Match actual module/import roots rather than a filesystem prefix; account for workspaces, aliases, framework entry points and dynamic/public consumers. Inspect unexpected volume or emptiness before accepting findings. An incomplete dependency installation is a setup error, not hundreds of new dead files.
3. Classify existing findings and inspect representative paths against current source. A clone/dead-code result is a lead, not authorization to delete or combine code. Link confirmed responsibility/behavior problems to passport functions; cross-cutting structural debt can have one shared finding.
4. Use native baseline support where suitable. Record specific reviewed findings, not just totals. Prove that the command detects a new violation even when other old findings are removed, and still identifies old findings after harmless line/path-format changes.
5. Validate the real local entry point and relevant integration prerequisites. Put commands and invocation rules in existing project instructions. Wire the same supported checks into the existing CI within the task's authority; record remote execution separately. Do not combine setup with a broad product refactor.

Optional hooks may shorten feedback, but record whether they are actually installed. A shared skill, configuration file, available CLI or MCP endpoint is not a background monitor. Continuous protection comes from verified project/CI triggers, not from keeping every analyzer process running. Do not add a daemon, scheduler or global hook silently.

## Prove the check through its real entry point

For each required control, test an allowed control and a small genuine violation in a disposable copy/fixture under its real scan scope. Exercise the actual analyzer and wrapper command that developers/CI use, not a fabricated report or only a unit stub. Confirm the expected finding and final failure status; remove only owned specimens and rerun the affected clean control. Add targeted regression coverage when a real integration failure would otherwise recur; do not rerun every proof for every source edit.

Choose proofs appropriate to the capability:

| Control | Meaningful challenge |
| --- | --- |
| Imports/cycles | Add an actual forbidden import or cycle between resolved modules, including aliases/package conventions used by the application; prove the complete relevant path is reported |
| Clones | Add a sufficiently sized real clone within configured formats/roots; the final command rejects the new finding, even if it accepts reviewed existing clones |
| Unused candidates | Add a reportable unreferenced symbol/file that the chosen tool supports; distinguish this from a real public/dynamic entry point. Assert the configured advisory/required policy, not automatic deletion |
| Registry | Duplicate an ID, break a path and reference a nonexistent symbol in an existing file; a valid control still passes |
| Wrapper/coverage | Exercise a missing executable, tool error, malformed/missing report or unexpectedly empty scan; none may produce a successful required check |
| Trusted baseline | Add the specimen to the evaluated checkout's baseline too; CI must still reject it against the separately selected trusted baseline. Missing/unresolvable trust input must fail the required CI mode |

Inspect the selected release's exit semantics and machine output. Some tools return a documented findings status separately from execution failure. A wrapper may compare legitimate reported findings with reviewed debt, but must not blanket-ignore nonzero exits, accept partial output from a crashed process, or turn an unknown status into success. A zero exit alone is insufficient: inspect report validity, analyzed-file inventory and uncovered languages/roots. An intentionally empty/not-applicable scope must be explicit and justified, never inferred from an empty report.

Record command/cwd, tool/config version, source revision, scanned scope, expected finding, observed native and wrapper statuses and report/evidence path. Results obtained with stubs demonstrate wrapper logic only; they cannot certify that a real analyzer recognizes application syntax. Reprove affected controls after changes to tool versions, wrappers, import roots, filters, fingerprints or baseline policy. Renew graph freshness checks for changed/deleted input; no duplicate full scan is needed when unchanged evidence remains applicable.

## Keep baseline identity and CI trust distinct

Prefer tool-native identities. If normalization is necessary, use repository-relative normalized paths and qualified enclosing symbol/content identity, with a multiplicity strategy. Line numbers alone, unqualified names and total counts are insufficient. Preserve occurrence counts: a second indistinguishable violation must not disappear through set deduplication. Cycle identity must preserve the actual directed path, accounting for equivalent rotations without collapsing different cycles into one edge/count. Verify harmless line movement and same-named symbols in different scopes using the chosen format. Compare results afresh after analyzer/config changes; do not pretend an incompatible report has the old meaning.

A policy/baseline change needs its reason, reviewed before/after findings and retained behavior checks. Do not automatically regenerate it, broaden exclusions, weaken thresholds or remove tests to pass a change. Legitimate policy changes are possible, but must not self-authorize the new debt under review.

Separate local baseline convenience from enforced CI trust. CI obtains a reviewed baseline/configuration from an immutable revision chosen outside the evaluated change, or an equivalent existing protected mechanism. The change's baseline file or self-selected environment variable is not evidence of that trust. Verify how CI obtains the trusted input, including Git/history/dependency prerequisites and failure when it is unavailable.

A trusted baseline alone cannot stop an evaluated change from replacing the checker, CI command or exclusions. Name the protection for those paths/required jobs, such as protected runner policy and required review. If it is not installed, report the limit; a local run with a supplied SHA is a simulation, not independent tamper resistance. YAML parsing proves syntax only. Distinguish configured locally, executed locally, wired in CI, executed remotely on an exact revision and enforced by branch/runner policy. No step implies publication or authority to change server access.

## Use the profile on subsequent work

| Trigger | Work to perform |
| --- | --- |
| Ordinary behavior change | Read affected passport rules, find the shared implementation/consumers, choose scenario checks, then run relevant established structural controls; preserve mandatory project gates |
| New shared module or public contract | Search by behavior/index/AST before adding it, state the extension decision, inspect direct consumers and update existing index/decision records |
| Tool/config/wrapper/baseline-policy change | Review coverage and trust implications, rerun affected positive/negative proofs and compare findings before/after |
| Source move/deletion | Update relevant graph/map/registry links; confirm consumers and registrations, then run affected controls/scenarios |
| Documentation-only change | Check current meaning, links and applicable registry integrity; no unrelated tool rollout or whole-project behavioral scan |
| Agent-run commit/push or CI | Execute the owning project's required commands at that boundary; the skill does not authorize the Git operation or install enforcement itself |

Keep task context small: relevant function IDs, code/writers/consumers, contracts, decisions and checks. Findings should identify the affected function or architectural owner, condition and consequence. Repair confirmed defects within authorization, review the resulting diff independently of the implementation explanation, rerun affected checks and reconcile current passport/guide meaning. A restored contract may justify no prose change; it cannot justify retaining a known explanatory gap.

Before presenting an implemented change as verified, account for each applicable required control in the existing task result: passed with valid evidence, failed, or unexecuted with the exact reason. Reuse prior evidence only while its source/config/scope remains applicable; do not relabel a skipped command as passed. Honor project-defined exemptions rather than inventing a narrower scope to obtain green. When wiring automatic triggers, challenge their path filters and working directories with a representative change: a required job that never starts cannot protect it.

## Accept both explanations and controls

Accept broad setup/audit on separate evidence axes:

- **Meaning:** a reader can recover concrete rules, failure/correction behavior and change consequences from the authored passport/guide using their links; run the [usefulness review](usefulness-review.md).
- **Behavior:** consequential selected scenarios have source/writer comparison and actual readback or a precise execution limit; use [behavior verification](behavior-verification.md).
- **Structure:** applicable controls have real coverage and meaningful positive/negative proofs; list advisory, missing and unsupported areas explicitly.
- **Enforcement:** report actual local/CI/branch boundaries, versions and stale or unexecuted parts. Prepared automation is not operating automation.

An unavailable analyzer must not stop independent source explanation, and a green analyzer must not close a missing explanation or a behavior defect. Known failing scenario IDs and observed limits remain visible. Do not claim a whole-project audit complete because representative controls passed or no new static findings appeared.
