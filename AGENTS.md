# Repository Guidelines

## Public Documentation Hosting

This repository owns the reviewed GitHub Pages hosting workflow and public API
documentation releases. Application source, team guides, credentials and runtime
configuration stay private. Publish only a verified public-consumer artifact.

Run `python3 -B -m unittest discover -s tests -v` for artifact validation.
Hosting consumes an immutable release archive and its SHA256. Never execute code
from that archive. Ordinary source changes use develop-based task worktrees and
human-merged PRs; initial main/develop bootstrap has explicit owner authority.

<!-- guignalabs:begin -->
## GuignaLabs Shared Instructions

Before work, find the nearest checkout ancestor containing both `AGENTS.md` and
`.workspace/company/workflow.md`, then explicitly read both. Grouped worktrees
have a deeper company root; do not assume it is the immediate parent or rely on
automatic instruction discovery across Git roots. When no company root exists
in an isolated clone, read the portable `.workspace/workflow.md` instead.
Repository-local instructions refine the shared defaults; explicit user
instructions authorize task-specific exceptions. Use
`.workspace/templates/task.md` for a bounded task record when appropriate.

Implement ordinary repository tasks in a dedicated worktree and branch from
fetched `origin/develop`, using
`.worktrees/<repository>/task-<id>-<purpose>/` under the company root. Record its
owner/task/base SHA. Declared stack layers may use their recorded predecessor
as base/target, keeping trunk `develop` and one worktree per layer. Task layers
ultimately land by squash on `develop`; release MRs promote
`develop` to `main` with a normal merge. Never push directly to either branch.
Read `.workspace/development.md` for the shared branch catalog, review-size bands,
stack dependencies, primary PR labels, verified owner assignment, human-only
merges, coordinated guide adoption and manual story closure. One issue can span many PRs; do not
require line estimates or fixed PR counts when creating it. Prefer 400 changed
lines, warn with a reason at 401–600, and split larger work. Follow the shared
workflow's MR readiness, current-candidate CI and review duties. Every stack
layer needs its own primary `type:` label and verified owner assignee. Read
back actual PR metadata, CI and auto-merge state before human handover; agents
must not merge, enable auto-merge or schedule a merge. Preserve another
owner's active publication inputs and coordinate portable adoption.
After confirming the MR is merged and dependents no longer need it, preserve
needed local files/data, remove only its owned worktree/local/remote task branch,
and verify/update the inventory; never delete `develop` or `main`. Keep task
resources while the MR is unmerged or cleanup
has a concrete preservation blocker; record owner and review date. The owner's
standing direction covers scoped local worktree/branch setup and post-merge task
cleanup. It does not authorize commits, publication, MR merge, unrelated deletion
or cloud actions.

Keep shared workflow and task records in ordinary Markdown filenames, such as
`.workspace/workflow.md` and `task.md`. Reserve `*.workspace.*` names, such as
`config.workspace.json`, for local configuration ignored by the repository's
managed `.gitignore` block. Never put secrets or private records in portable files.

The portable files are reviewed snapshots. If bootstrap `--check` reports drift,
review the differences and update the affected snapshot, managed blocks and
metadata together manually; bootstrap never overwrites a conflicting version.
<!-- guignalabs:end -->
