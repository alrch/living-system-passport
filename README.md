# Living System Passport

A reusable Codex skill for keeping a project-owned map of product behavior, implementation, requirements, and verification. The skill describes **how to investigate and maintain the map**. Each project decides where its passport lives, which sources are authoritative, and which checks it runs.

## One place for improvements from every project

If the skill confused an agent or failed on your project, [send a skill improvement](https://github.com/alrch/living-system-passport/issues/new?template=skill-improvement.yml). Reports from all projects go to [the same issue list](https://github.com/alrch/living-system-passport/issues). Describe the general problem; your application's bugs and settings stay in your application.

Have a fix? Change the skill in its own checkout and send a pull request to this repository. Changes to `main` require a pull request and owner review (`@alrch`); new commits invalidate earlier approvals. The owner can merge their own maintenance pull requests, but direct pushes, force pushes and branch deletion are blocked. Its Git remote is separate from your application's remote; pushing the application does not push the skill. After a fix is merged, installations update separately.

Agents: follow the [feedback workflow](references/feedback.md) for deduplication, publication authorization and a short generic reproduction. No automatic upload or extra service is required.

## For people

### What is in this repository

- [`SKILL.md`](SKILL.md) — the reusable workflow Codex loads when the skill applies.
- [`references/function-entry.md`](references/function-entry.md) — a checklist for a function entry, change-impact note, and finding.
- [`references/domain-review-checks.md`](references/domain-review-checks.md) — detailed, optional checks across forms, analytics, access, workflows, integrations, files, media, and learning.
- [`references/project-adapter.md`](references/project-adapter.md) — the small set of facts each project must supply so the same skill can create and maintain its passport.
- [`references/behavior-verification.md`](references/behavior-verification.md) — negative scenarios, alternate writers, readback and honest verification boundaries.
- [`references/graph-workflow.md`](references/graph-workflow.md) — tool readiness, query selection, recovery and dual-tool evidence.
- [`references/maintenance-checks.md`](references/maintenance-checks.md) — conditional checks for existing registries and review baselines.
- [`scripts/evidence_snapshot.py`](scripts/evidence_snapshot.py) — optional file/revision snapshot for a reproducible final audit.
- [`agents/openai.yaml`](agents/openai.yaml) — optional Codex display metadata.

The passport itself, project requirements, source code, generated indexes, and project-specific scripts stay in the project repository. The shared skill includes many conditional checks; a project uses only those relevant to its behavior. This repository should not contain credentials or private project evidence.

### Connect it to a project

From the **project root**, install the skill into Codex's repository skill location:

```bash
mkdir -p .agents/skills
git clone https://github.com/alrch/living-system-passport.git .agents/skills/living-system-passport
```

If the project tracks `.agents/`, add `.agents/skills/living-system-passport/` to its `.gitignore`. The checkout is local to each developer; the project stores only the source URL and its own rules. Access to a private source repository requires the developer's GitHub credentials.

Add a short section like this to the project's `AGENTS.md`, replacing the bracketed items with real paths and commands:

```markdown
## Living system passport

Skill source: https://github.com/alrch/living-system-passport.git
Use `$living-system-passport` when mapping an existing function, planning a behavior change, or updating the passport after an accepted change.
If the skill is missing, follow the repository README to install it under `.agents/skills/living-system-passport`.
The project passport is [path]. Requirements/status are in [path]. Scenarios and checks are in [path or commands].
The project's passport adapter is in [existing project instruction or documentation path]; it defines source ownership, change triggers, indexes, and review acceptance.
Tested skill revision: [full Git commit SHA, if the project pins one].
Keep project-specific paths and commands there; apply the shared method and only relevant domain checks from the skill.
```

Replace all placeholders before committing `AGENTS.md`; omit the revision line if the project does not pin a version. A URL in `AGENTS.md` tells people and agents where the source is; **the skill becomes discoverable after its directory is installed**. Codex normally detects new skills, but restarting the app may be needed if it does not appear.

If work starts inside several independent Git repositories, a standalone user-level checkout in the skill directory supported by the installed agent can make the skill available to all of them. Clone this source repository directly there; do not symlink to a copy inside a different project. Keep the project instructions pointing to the same source. If user and project copies coexist, inspect the path actually loaded and the project's pinned revision; they are not merged. Keep intentional version pins explicit.

### Keep a team on one tested version

For shared project work, record the full commit SHA tested with that project in its existing instructions. After cloning, each teammate runs `git -C .agents/skills/living-system-passport checkout <tested-commit>`. A detached checkout is expected. When adopting a newer version, review and test it, update the recorded SHA, then each teammate runs:

```bash
git -C .agents/skills/living-system-passport fetch origin main
git -C .agents/skills/living-system-passport checkout <new-tested-commit>
```

Check the active revision with `git -C .agents/skills/living-system-passport rev-parse HEAD`. The project instruction is the team's version choice; the source repository's `main` may be newer.

### See whether a newer version is available

From the project root, fetch the shared repository and list commits added since the installed revision:

```bash
git -C .agents/skills/living-system-passport fetch origin main
git -C .agents/skills/living-system-passport log --oneline HEAD..origin/main
```

An empty list means there is no newer commit on `main`. This check does not change the version Codex uses. Review the listed changes, run the two small comparison cases below, then update the tested commit in the project's instructions and check it out locally. Each teammate repeats the checkout; a URL in `AGENTS.md` does not watch the repository or update a skill automatically.

### Update a project that follows latest

From the project root:

```bash
git -C .agents/skills/living-system-passport pull --ff-only
```

Use `pull --ff-only` only when the checkout still follows `main` and the project intentionally uses the latest reviewed version. Review changes to the skill before using an updated workflow on consequential work. The `AGENTS.md` URL does not automatically pull new commits. Do not edit the local checkout for project-specific rules—put those in the project's `AGENTS.md` or passport. Send reusable corrections to this repository through a pull request.

### Check a new version before replacing an old one

Use two small, source-backed cases from the same project revision: create one new function entry and update one existing entry after a behavior or requirement-status change. Apply the old and new versions to separate copies of those cases. Compare factual correctness, traceability, relevant checks, unresolved uncertainty, and unnecessary work. A shorter result is not automatically better; a longer checklist is not evidence that it found a real issue. Keep the old version active until the new one preserves its useful decisions and adds a clear improvement.

## For the agent setting up a project

When asked to connect or update this skill:

1. Locate the project root and read its `AGENTS.md` or existing instruction source, passport, requirement/status sources, and scenario or test documentation. Do not assume any particular file layout or tooling. Fill the facts in the [project-adapter checklist](references/project-adapter.md) from these sources.
2. Check whether `.agents/skills/living-system-passport` already exists. If it is this repository, inspect local changes and the project's tested revision before any requested update; use the pinned-revision commands above or `git pull --ff-only` for a project following latest. If the path contains something else, stop and report the conflict rather than overwriting it.
3. If absent, clone the source URL above into that path and check out the project's tested revision, if recorded. Ensure the nested checkout is ignored by the project Git repository; preserve unrelated `.gitignore` entries. Do not commit the downloaded checkout as project content.
4. Add or update the project's existing instruction source with the source URL and actual project sources, checks, and adapter path. Keep the adapter and operational graph rules directly in the owning project's instructions; do not route setup through another project or private configuration workspace. Preserve existing project rules when replacing a bootstrap pointer. Keep project-specific commands, IDs, and assumptions in that project.
5. Prove graph readiness with the [graph workflow](references/graph-workflow.md) when graphs are in scope: installed is not indexed or queryable. Validate that `SKILL.md` and its linked references are present and that `HEAD` matches the project's tested revision, if pinned. Restart Codex if skill discovery has not refreshed. In a small real project task, check that the skill uses the project's own sources and produces confirmed versus uncertain links correctly.
6. Report the installed commit, changed project files, validation performed, and anything the project owner still needs to define. Do not claim the project's passport is complete merely because the skill is installed.

The skill does not authorize changing product behavior, requirement status, releases, or external systems. Follow the project's normal authorization and review process for those actions.
