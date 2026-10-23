# Project Overview

Create this separate document alongside a new passport/guide pair, or when the user requests it for an existing project. Default to `PROJECT_OVERVIEW.md`; reuse an existing canonical equivalent. Use the bundled starter to avoid missing a section, not as a rigid page layout. For focused maintenance, review only sections affected by the task.

## Minimum useful content

- **What the project is:** a brief explanation of the actual target product, its purpose, intended users and the result they receive. Describe that project, not the skill, starter page, documentation process or template. Lead with facts a new PM needs; keep implementation details for the later sections.
- **Participants and roles:** who uses or operates the product, what each role does and how their work connects. Use verified product roles; name people or teams only when current sources establish them.
- **How it works:** one short end-to-end example with a real starting action, key steps and final outcome. Explain participants and system actions in ordinary language; link detailed scenarios to the product guide.
- **Used stack:** actual frontend, backend, data/storage, integrations and delivery technologies where present; their responsibilities and source references. Read manifests, lockfiles and runtime/deploy configuration. Do not invent absent layers or infer a deployed version from a source dependency.
- **Architecture:** actual major components, ownership of logic/state, interactions and important external boundaries. Explain the normal request/data flow in prose or a small source-backed diagram. Link detailed technical passport entries; avoid a copied module inventory or a third detailed function specification.
- **Working context:** agreed environments, access, bug reporting and relevant materials. Keep secrets out; retain environment-specific meanings and clearly identify genuinely shared facts.

## Creation and maintenance

Fill known facts from current sources. Mark the exact missing boundary and next evidence instead of publishing scaffold placeholders as accepted knowledge. Keep the source document in the owning project, with last-review evidence in its existing task/operational records rather than a new changelog at the top of the overview.

Review when purpose, audience, participant roles, the main workflow, stack, services, interfaces, data/storage or integration boundaries change, as well as environment/access/reporting/link changes. Update relevant prose and citations in the same task; record scoped no-change when the document remains accurate. Reuse existing checks and publication mechanisms.

## Start-page link

Bind the existing Project help button to the overview's readable HTML/document view. Add its Markdown source to the project's renderer allowlist, build it, and verify the destination and selected environment. If one overview covers several environments, assign that shared resource explicitly. Treat source creation, local rendering, publication and live navigation as separate verified boundaries; do not claim a deployed view from a local build.
