# Graph workflow for a living passport

Read this when connecting graph tools, checking dependencies or auditing a passport with graphs. Discover the installed tools and their live schemas; command options and index modes can change. No engine version, repository count, framework or deployment topology is prescribed here.

## Connect a new project

1. Confirm the actual skill path, source and revision. Inspect existing project instructions and indexes before installing anything. Keep the adapter in this project; link directly to authoritative sources, not another project's copy or private profile. A global skill installation must stand alone.
2. Identify repositories and other source roots, relevant domains and entry points, requirements/status ownership and scenarios. Use the project's real equivalents; a CLI, library, worker or document workflow need not have screens or HTTP routes.
3. Separate graph purposes: **code dependencies** for symbols/callers/contracts and **traceability** for outcomes, rules, functions, source citations and scenarios. Graphify and Codebase Memory are engines, not those two purposes. Do not treat their output as two independent proofs of the same behavior.
4. Reuse usable indexes. For a demonstrated gap, build the smallest justified source scope with an installed tool. Keep output, cache and generated indexes separate from canonical passport text. Record actual build/status/query commands in the adapter; do not copy another project's script and assume it generalizes.
5. Define exclusions from the project, protecting secrets and avoiding generated/dependency output. Include tests or scripts when the requested trace requires them; inspect mode behavior instead of assuming that a mode called `full` parses everything. Record unsupported and partial files. Do not exclude test source as build output by default.

## Prove readiness

These are separate states: installed → callable → indexed for the correct repository → sufficiently fresh and covered → usable for the requested lookup and dependency trace.

For each selected repository, obtain index status, verify the indexed root/identity and mode, then look up one real source anchor by file and symbol and query a real relationship. Inspect parse/coverage warnings and compare relevant source changes with the index. An empty result can be a wrong identity, spelling, exclusion or parser limit before it is a product finding. A version string or a successful process start is not a readiness check. Do not index all repositories for a local question merely to satisfy this checklist.

Read current tool schemas through the available tool-discovery surface or CLI help. Keyword search and graph query languages are different interfaces; do not pass one to the other. Distinguish a JSON transport envelope from JSON payload formatting. Treat tool-level errors inside an otherwise successful response as failed queries.

### Codebase Memory recovery, only when needed

Use the installed release's help and the upstream [configuration reference](https://github.com/DeusData/codebase-memory-mcp/blob/main/docs/CONFIGURATION.md). The [source repository](https://github.com/DeusData/codebase-memory-mcp) owns supported versions and installation guidance. Do not copy a command from a secondary project as installation authority.

Cache storage and IPC/runtime coordination are different boundaries. For releases supporting `CBM_CACHE_DIR` and `CBM_RUNTIME_DIR`, isolating the cache alone need not isolate the runtime. If isolation addresses the observed conflict, create a private runtime directory under a location allowed by that release and use the same environment in CLI and MCP sessions. Preserve the project's existing settings; do not force private runtimes for every installation or change global watchers as a side effect.

Separate socket permission/sandbox failure, stale coordination metadata, wrong repository and actual version incompatibility. A generic coordination/version message does not identify the cause. Do not kill shared processes, delete sockets or reset other indexes to repair a project. Use a project-owned runtime or the environment's supported permission route when justified, then repeat status, exact lookup and trace. If still unavailable, record the observed failure and continue independent source review; do not claim the tool worked.

### Graphify recovery, only when needed

Use the installed package's own metadata to locate its interpreter and upstream; the [Graphify source](https://github.com/Graphify-Labs/graphify) is the primary reference. A CLI installed in a managed environment need not be importable by system Python. Use that environment rather than installing a duplicate package into another interpreter. Preserve EXTRACTED/INFERRED/AMBIGUOUS or equivalent provenance; deterministic citations prove references, not `implements` or `accepted` relations.

## Choose and bound the query

| Question | Starting route when available | Verify next |
| --- | --- | --- |
| Known text-only correction | Exact file read/search | That the affected claim/link is current |
| Symbol, caller, dependency or behavior change | Codebase Memory, scoped to one repository | Current implementation, direct callers and relevant tests |
| Architecture, domain or document/rule relationships | Existing Graphify graph of that purpose | Current authoritative documents and exact implementations |
| Explicit dual-tool passport audit | Both engines, with distinct recorded contributions | Exact source anchors, dependency evidence and passport citations |

Start from an exact name, ID or path with a small neighborhood. Inspect incoming consumers and outgoing dependencies separately if a shared limit can hide one direction. Explicitly include test definitions when needed and supported. Preserve total count, returned count, truncation/cursor, depth and relevant confidence; expand for a concrete unresolved link, not to traverse a central node's entire graph. Omitted or unsupported metadata stays unknown rather than becoming zero or complete.

Confirm important edges against source, including runtime registration and cross-repository contracts when relevant. No callers in a static graph is not proof of dead code. Neither matching node counts between engines nor the presence of a TESTS edge proves behavioral correctness or a scenario pass. Conflicting graph results require source inspection; two engines can share the same blind spot.

## Whole-project and dual-tool evidence

For whole-project requests, discover the project's actual domains and entry points before selecting anchors. Keep reviewed, inventory-only, excluded and unresolved areas visible, including non-interactive/background surfaces where present. Work domain by domain until the requested scope is covered; a first sample is calibration. A route count alone cannot establish meaningful coverage.

For a dual-tool audit, derive cases from the current passport's canonical IDs rather than a stale hardcoded count. Validate the exact expected-ID set against results, including missing, unexpected and duplicate IDs. Verify each selected anchor by repository, file and symbol; an unresolved anchor or failed tool response must remain visible even if most cases pass. Use code relationships from the appropriate engines and explicit passport/source/scenario citations for traceability; these contributions need not be identical. Save bounded evidence rather than whole graphs.

Record passport hash or immutable revision, inspected source hashes/revisions including relevant local changes, graph input revision/freshness, engine versions and query scope. Keep the passport stable during the final pass or compare inputs before and after. If inputs changed, label the affected evidence stale and recheck; do not attach an old green result to new prose. Regenerating navigation afterward does not renew behavioral evidence. An optional [snapshot helper](../scripts/evidence_snapshot.py) captures exact files and repository revisions; it does not discover new files, validate graph semantics or accept a review baseline. Use source discovery separately for new unlinked paths.

Finish with separate statements for structural links, source-reviewed meaning, cross-layer checks, scenarios actually executed and remaining runtime/external uncertainty. Keep tool/skill/method friction in the method findings; product behavior belongs in the product findings. A local successful workaround is not yet a portable skill correction.

Run the helper with Python 3.10 or newer. `python3 scripts/evidence_snapshot.py --help` describes capture/check arguments. Pass each inspected document/source with repeated `--file`, and exact Git roots with optional repeated `--repository`, under an explicit common `--root`. Use a new `--snapshot` file for each capture. Check returns 0 for unchanged recorded inputs, 1 for drift and 2 for invalid input or an execution error. Capture never overwrites old evidence or advances a reviewed baseline. The helper does not inventory new files or detect source edits outside its explicit file scope.
