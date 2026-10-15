# Living System Passport

A reusable Codex skill for keeping a project-owned map of product behavior, implementation, requirements, and verification. The skill describes **how to investigate and maintain the map**. Each project decides where its passport lives, which sources are authoritative, and which checks it runs.

## For people

### What is in this repository

- [`SKILL.md`](SKILL.md) — the reusable workflow Codex loads when the skill applies.
- [`references/function-entry.md`](references/function-entry.md) — a checklist for a function entry, change-impact note, and finding.
- [`references/domain-review-checks.md`](references/domain-review-checks.md) — optional prompts for relevant cross-layer checks.

The passport itself, project requirements, source code, generated indexes, and project-specific scripts stay in the project repository. This repository should not contain credentials or private project evidence.

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
Keep project-specific rules and scripts here, not in the shared skill.
```

Replace all placeholders before committing `AGENTS.md`. A URL in `AGENTS.md` tells people and agents where the source is; **the skill becomes discoverable after its directory is installed**. Codex normally detects new skills, but starting a new Codex task or restarting the app may be needed if it does not appear.

### Update

From the project root:

```bash
git -C .agents/skills/living-system-passport pull --ff-only
```

Review changes to the skill before using an updated workflow on consequential work. Each project and developer chooses when to update; the `AGENTS.md` URL does not automatically pull new commits. Do not edit the local checkout for project-specific rules—put those in the project's `AGENTS.md` or passport. Send reusable corrections to this repository through a pull request.

## For the agent setting up a project

When asked to connect or update this skill:

1. Locate the project root and read its `AGENTS.md`, passport, requirement/status sources, and scenario or test documentation. Do not assume any particular file layout or tooling.
2. Check whether `.agents/skills/living-system-passport` already exists. If it is this repository, update only when requested, using `git pull --ff-only`; inspect local changes before any update. If the path contains something else, stop and report the conflict rather than overwriting it.
3. If absent, clone the source URL above into that path. Ensure the nested checkout is ignored by the project Git repository; preserve unrelated `.gitignore` entries. Do not commit the downloaded checkout as project content.
4. Add or update the short `AGENTS.md` section above with actual project sources, checks, and the source URL. Keep project-specific commands, IDs, and assumptions in that project.
5. Validate that `SKILL.md` and its linked references are present. Start a new Codex task if skill discovery has not refreshed. In a small real project task, check that the skill uses the project's own sources and produces confirmed versus uncertain links correctly.
6. Report the installed commit, changed project files, validation performed, and anything the project owner still needs to define. Do not claim the project's passport is complete merely because the skill is installed.

The skill does not authorize changing product behavior, requirement status, releases, or external systems. Follow the project's normal authorization and review process for those actions.
