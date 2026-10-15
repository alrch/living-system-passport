# Shared feedback from many projects

The shared inbox is [Issues in the skill source repository](https://github.com/alrch/living-system-passport/issues). This is the same inbox for every project. The [issue form](https://github.com/alrch/living-system-passport/issues/new?template=skill-improvement.yml) and pull request template live in this repository, not in a separate coordination service.

## Collect a useful observation

Keep product defects, business decisions and project configuration in the owning project. A skill observation is different: an instruction was ambiguous, a navigation step failed, the agent made an unsupported claim, or a reusable helper behaved incorrectly. Record it briefly in the project's method findings while investigating. A local workaround does not mean the shared skill was fixed.

For sharing, reduce the observation to the skill revision/local edits, relevant tool versions, expected versus observed behavior, and a small generic reproduction. Add a proposed general correction and its check if known. Do not copy the project's passport, absolute paths, private source links, user data or raw logs into the shared repository. A report must be understandable without access to its originating project. An upstream tool defect can be linked to that tool's official issue; explain separately whether the skill needs a better workaround.

## Submit to the shared inbox

When the user asks to send feedback or existing explicit authorization covers it, use the installed GitHub connector or CLI. Select `alrch/living-system-passport` explicitly; the application's `origin` is not the destination. Search open and closed issues for the same failure first. Reuse an existing issue when it is the same problem, adding only new evidence. Do not create one issue per local finding ID. A concrete code/doc fix may go straight to a pull request; an issue is not a mandatory extra step.

Create the issue with the form or equivalent structured content. For CLI submission, write the exact sanitized body to a temporary UTF-8 file, then use `gh issue create --repo alrch/living-system-passport --title "..." --body-file <file>`. Record the returned URL beside the originating local method finding, so later work can find the shared discussion. If submission is not authorized or access is unavailable, keep a ready-to-send local draft and report that it has not been submitted. Never claim a local note is visible to the team.

## Contribute a change from an installed checkout

The skill checkout has its own `.git` and `origin`. Confirm they belong to this source repository, inspect local edits and fetch the current default branch. Keep the application's Git repository untouched. In the skill checkout, create a `codex/` branch from the appropriate source revision; reconcile newer upstream changes without discarding the installed edits. Commit only portable changes and validate the skill and any changed helpers. Push that branch to the skill repository and open a pull request there, or use a fork when direct write access is unavailable. Follow the user's publication authorization; do not silently merge or change a project's pinned version.

Use the pull request template to explain the resulting agent behavior, actual tests and portability boundary. Link the shared issue when relevant. The maintainer reviews and merges; an issue or published branch alone does not change the installed skill. After merge, update installations deliberately and record the tested revision in project instructions. A push of the application never pushes this nested skill repository. User-level and project-level copies do not update one another automatically.

## Keep the process light

No extra database, scheduled collector, automatic upload of local findings or central copy of project settings is needed. GitHub issue/PR state is the shared status. The local method register needs only a short observation and the shared URL once submitted. A fixed local installation is not a published fix; a merged fix is not proof that every project has upgraded.
