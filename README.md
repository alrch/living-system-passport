# Living System Passport

A reusable Codex skill for keeping a project-owned map of product behavior, implementation, requirements, and verification. The skill describes **how to investigate and maintain the map**. Each project decides where its passport lives, which sources are authoritative, and which checks it runs.

## For people

### What is in this repository

- [`SKILL.md`](SKILL.md) — the reusable workflow Codex loads when the skill applies.
- [`references/function-entry.md`](references/function-entry.md) — a checklist for a function entry, change-impact note, and finding.
- [`references/domain-review-checks.md`](references/domain-review-checks.md) — detailed, optional checks across forms, analytics, access, workflows, integrations, files, media, and learning.
- [`references/project-adapter.md`](references/project-adapter.md) — the small set of facts each project must supply so the same skill can create and maintain its passport.
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
Keep project-specific paths and commands there; apply the shared method and only relevant domain checks from the skill.
```

Replace all placeholders before committing `AGENTS.md`. A URL in `AGENTS.md` tells people and agents where the source is; **the skill becomes discoverable after its directory is installed**. Codex normally detects new skills, but starting a new Codex task or restarting the app may be needed if it does not appear.

If work starts inside several independent Git repositories, a single checkout in `~/.agents/skills/living-system-passport` can make the skill available to all of them. Keep the project instructions pointing to the same source. Avoid simultaneous copies with the same skill name in user and project locations; Codex can list both instead of merging them.

### Update

From the project root:

```bash
git -C .agents/skills/living-system-passport pull --ff-only
```

Review changes to the skill before using an updated workflow on consequential work. Each project and developer chooses when to update; the `AGENTS.md` URL does not automatically pull new commits. Do not edit the local checkout for project-specific rules—put those in the project's `AGENTS.md` or passport. Send reusable corrections to this repository through a pull request.

### Check a new version before replacing an old one

Use two small, source-backed cases from the same project revision: create one new function entry and update one existing entry after a behavior or requirement-status change. Apply the old and new versions to separate copies of those cases. Compare factual correctness, traceability, relevant checks, unresolved uncertainty, and unnecessary work. A shorter result is not automatically better; a longer checklist is not evidence that it found a real issue. Keep the old version active until the new one preserves its useful decisions and adds a clear improvement.

## For the agent setting up a project

When asked to connect or update this skill:

1. Locate the project root and read its `AGENTS.md` or existing instruction source, passport, requirement/status sources, and scenario or test documentation. Do not assume any particular file layout or tooling. Fill the facts in the [project-adapter checklist](references/project-adapter.md) from these sources.
2. Check whether `.agents/skills/living-system-passport` already exists. If it is this repository, update only when requested, using `git pull --ff-only`; inspect local changes before any update. If the path contains something else, stop and report the conflict rather than overwriting it.
3. If absent, clone the source URL above into that path. Ensure the nested checkout is ignored by the project Git repository; preserve unrelated `.gitignore` entries. Do not commit the downloaded checkout as project content.
4. Add or update the project's existing instruction source with the source URL and actual project sources, checks, and adapter path. If `AGENTS.md` is only a pointer to another maintained profile, update that profile according to its rules instead of creating a competing set of instructions. Keep project-specific commands, IDs, and assumptions in that project.
5. Validate that `SKILL.md` and its linked references are present. Start a new Codex task if skill discovery has not refreshed. In a small real project task, check that the skill uses the project's own sources and produces confirmed versus uncertain links correctly.
6. Report the installed commit, changed project files, validation performed, and anything the project owner still needs to define. Do not claim the project's passport is complete merely because the skill is installed.

The skill does not authorize changing product behavior, requirement status, releases, or external systems. Follow the project's normal authorization and review process for those actions.
