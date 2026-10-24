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
- [`references/project-overview.md`](references/project-overview.md) and [`assets/project-overview.template.md`](assets/project-overview.template.md) — a short introduction to the actual product, its audience, participants, workflow, stack and architecture, maintained alongside the passport and guide.
- [`references/project-adapter.md`](references/project-adapter.md) — the small set of facts each project must supply so the same skill can create and maintain its passport.
- [`references/behavior-verification.md`](references/behavior-verification.md) — negative scenarios, alternate writers, readback and honest verification boundaries.
- [`references/graph-workflow.md`](references/graph-workflow.md) — tool readiness, query selection, recovery and dual-tool evidence.
- [`references/maintenance-checks.md`](references/maintenance-checks.md) — conditional checks for existing registries and review baselines.
- [`scripts/evidence_snapshot.py`](scripts/evidence_snapshot.py) — optional file/revision snapshot for a reproducible final audit.
- [`agents/openai.yaml`](agents/openai.yaml) — optional Codex display metadata.

The passport itself, project requirements, source code, generated indexes, and project-specific scripts stay in the project repository. The shared skill includes many conditional checks; a project uses only those relevant to its behavior. This repository should not contain credentials or private project evidence.

### One shared installation for all projects

Install the skill once per developer account, from this repository. Every project on that machine uses the same installed version. Codex supports a user-scoped skill directory; see [the official discovery rules](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).

For a new installation:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/alrch/living-system-passport.git ~/.agents/skills/living-system-passport
```

An existing user-level installation already discovered by your Codex client can stay in its current directory. Use that actual directory in the commands below instead of creating a second installation. A shared installation must be its own checkout, not a link into another application's working tree.

Projects keep their own passport, product guide, overview, sources, commands and adapter. They refer to `$living-system-passport`; they do not vendor or modify another copy of this skill. Add a short pointer to the project's existing instructions:

```markdown
Use the user-installed $living-system-passport from https://github.com/alrch/living-system-passport.
The project adapter is [actual adapter path]; it owns the project's document paths, sources and checks.
If the skill is missing, follow its repository README to install it once for this user.
Do not create a project copy. Record the skill revision used in review evidence, not as a separate project pin.
```

Replace the adapter placeholder before committing. The source URL alone does not install the skill. Each developer and each machine needs their own user installation; one update affects all projects on that account, not every teammate automatically. Codex may need a new chat or restart to refresh discovery.

### Update manually, for example once a week

A periodic review is enough; no watcher or scheduler is installed. From the actual shared installation, confirm that the branch is `main`, the origin is this repository, and the working tree is clean. Stop on a wrong source, another branch, or any staged, unstaged or untracked changes before proceeding:

```bash
git -C ~/.agents/skills/living-system-passport remote get-url origin
git -C ~/.agents/skills/living-system-passport branch --show-current
git -C ~/.agents/skills/living-system-passport status --short
```

Fetch the reviewed branch, then check whether the installation has any commits that are absent from it:

```bash
git -C ~/.agents/skills/living-system-passport fetch origin main
git -C ~/.agents/skills/living-system-passport log --oneline origin/main..HEAD
```

If that log prints anything, stop and preserve those local commits in a separate candidate checkout. A clean working tree does not mean its commits are reviewed; `merge --ff-only` alone also succeeds when the installation is locally ahead. Require `HEAD` to be an ancestor of the fetched `origin/main` before adoption; a nonzero result from this command stops the update:

```bash
git -C ~/.agents/skills/living-system-passport merge-base --is-ancestor HEAD origin/main
```

Only after that check succeeds, list the incoming changes:

```bash
git -C ~/.agents/skills/living-system-passport log --oneline HEAD..origin/main
```

Review the listed merged changes and relevant checks, then adopt them once for all projects:

```bash
git -C ~/.agents/skills/living-system-passport merge --ff-only origin/main
```

Stop on local edits, a non-main branch, locally ahead commits or a diverged history. Preserve the work; do not reset or force an update. Use the actual installed directory if it differs from this example. Record the previous and resulting revision in the update result, and confirm the resulting `HEAD` equals the fetched `origin/main`. A clean fast-forward of already reviewed changes is an installation update, not a new project acceptance or deployment.

For a substantial workflow change, compare a small new function entry and an existing-entry update at one project revision before adopting it. Check factual correctness, traceability, relevant verification, uncertainty and unnecessary work; a changed length alone is not a useful result.

### Propose improvements without changing every project's active skill

Keep the shared installation on reviewed `main`. Develop a candidate in a separate checkout or worktree of this repository on a `codex/` branch. A method problem found in an application belongs here; the application's configuration and product findings stay in that application.

1. Search existing [Issues](https://github.com/alrch/living-system-passport/issues) and pull requests for the same problem.
2. Reproduce it with a small sanitized case, improve the shared instructions/helper, and validate the result. An issue is optional when there is already a concrete fix.
3. When publication is authorized, push the candidate branch and open a pull request here. Explain the observable improvement and the checks actually run.
4. Review the candidate and decide whether to merge it. An open PR is a proposal, not an accepted update. Rejected candidates never enter the active shared installation.
5. After merge, update the shared installation with the manual procedure above. Projects on that account then use the same approved version.

If somebody edited the active installation directly, preserve staged and unstaged changes, new untracked files and any local commits in a separate candidate checkout before restoring its reviewed state. A Git diff alone omits new untracked files. Verify that the candidate contains the complete improvement before changing the active installation; do not discard it or distribute it silently. See [feedback.md](references/feedback.md) for the contribution and authorization boundaries.

### Migrate existing project copies

Prepare a reviewable migration and obtain the owner's acceptance before switching consuming projects, unless existing authorization already covers that switch. Preparing or opening a PR is not acceptance. Before removing a copy, compare it with the shared version and inspect its callers. Move actual project parameters into the existing project adapter. Preserve uncommitted changes in a verified backup; do not replace a whole instruction file or lose previous work. Historical local notes are evidence, not another current version of the skill.

Move operational runtime dependencies, such as a documentation renderer used by CI, into the owning project's scripts and update their callers/checks. A clean CI checkout must not depend on an operator's user skill directory. Then remove project skill copies and discovery symlinks, update current instruction/document links, and check that only the user installation supplies this skill. Existing dated audit evidence stays historical.

The skill does not authorize changing product behavior, requirement status, releases, or external systems. Follow the project's normal authorization and review process for those actions.
