# GuignaLabs Development Guide

Owner-adopted company development agreements, 2026-10-25. Apply them to every
GuignaLabs project and repository, with checks appropriate to its actual stack.
Apply the [shared workflow](workflow.md) together with the owner-adopted delivery
rules below. The current requirement for human-only merges takes precedence over
earlier snapshot wording that allowed an agent to merge with authorization.
This guide does not install hosting controls.

## Stories, tasks and pull requests

An issue can describe a complete user story, defect or other useful outcome.
Define its objective, scope and observable acceptance without predicting lines
of code. A story may need one or many merge requests (MRs; PRs on GitHub).
Discover and revise that decomposition while inspecting and implementing it.

One focused PR is a review unit. Several PRs may reference the same issue;
subissues are optional when a part needs its own outcome, owner or tracking.
Do not manufacture an issue for every line-budget chunk. A small PR still needs
a coherent change, its relevant tests and documentation.

## Branch catalog

Use the main purpose of the task to choose one ordinary prefix:

| Prefix | Primary PR label | Purpose |
| --- | --- | --- |
| `feature/` | `type:feature` | Add or extend a capability. |
| `fix/` | `type:bug` | Correct defective behavior. |
| `docs/` | `type:docs` | Change documentation only. |
| `refactor/` | `type:refactor` | Restructure code while preserving behavior. |
| `test/` | `type:test` | Add or improve tests as the main outcome. |
| `ci/` | `type:ci` | Change integration pipelines or checks. |
| `build/` | `type:build` | Change compilation, packaging or build tooling. |
| `perf/` | `type:perf` | Improve performance with verification. |
| `chore/` | `type:chore` | Other maintenance that does not fit a more precise category. |

Use `<type>/<issue-or-task-id>-<short-description>` in lowercase with hyphens.
Synthetic examples: `feature/123-booking-rules`, `fix/123-session-recovery`,
`docs/task-0123-development-guide`. Several branches may share an issue number;
their distinct descriptions and PR numbers identify their separate changes.
Use Bug to classify an issue and `fix/` for its correction branch; do not add
`bug/` or `bugfix/` aliases. Including tests/docs in a feature does not change
its primary prefix. Commit types remain separate: `feature/` commonly uses
`feat(scope): ...` for a feature commit; a branch can contain several commit types.

`main` and `develop` are persistent branches. Ordinary task branches originate
from the exact fetched `origin/develop` SHA and integrate by squash PR into
`develop`. A release promotion is a normal, history-preserving PR from the same
repository's `develop` to `main`; this exact pair is a branch-prefix exception.

Reserve `release/<version>` for a separately defined stabilization process;
a release PR does not require such a branch. Reserve `hotfix/<id>-<description>`
for an explicitly authorized production-repair process, including its correct
released base and return of the fix to development. Neither prefix silently
changes the ordinary base, target, authority or merge rules. No Gitflow extension
or global tool installation is required by this naming convention.

## Worktrees and delivery

Implement and validate every product/organization task in its own registered
worktree at `.worktrees/<repository>/task-<id>-<purpose>/` under the company root.
Record its owner, task, branch and exact base SHA. Keep the primary checkout and
other tasks intact. The canonical private company coordination checkout alone
stays local; a product's own `.workspace/` directory does not grant an exemption.

Publish only an authorized task branch, open its PR with the issue reference,
scope, actual checks/evidence, limitations and relevant recovery information,
then obtain the required review and hand it to the owner for a manual merge.
Agents must not merge, enable auto-merge or schedule a merge. Never push directly
or force-push to `develop` or `main`. A passing check grants no publication
authority. A merged PR alone does not establish acceptance of the whole story.

## PR metadata and human handover

Apply one primary `type:` label from the branch catalog to every PR, including
each layer of a stack. Choose the main purpose; a feature containing tests and
documentation still uses `type:feature`. For a release promotion, describe the
aggregate purpose and choose the corresponding agreed type; do not invent a
new label merely because `develop` is the source branch. Labels do not establish
test results or approval. Retain useful unrelated labels. Creating missing labels
or deleting legacy labels requires separately scoped repository authority;
guide adoption does not authorize a catalog cleanup.

Assign every PR to the verified owner's GitHub account. For the current
GuignaLabs owner this is `jbasualdo`, verified on 2026-10-25; revalidate if the
owner or authenticated account changes. Never infer the account from an OS
username. Assignment identifies the recipient and does not substitute for review.

Before handing a PR to the owner, read back its actual repository, source/head
SHA, target/base, primary label, assignee, state and auto-merge field. Verify the
immediate base, trunk and predecessor/successor links for each stack layer.
Distinguish local checks from current hosted CI, report outstanding checks or
blocking discussions, and leave the PR open for the owner's review and merge.
Commits, pushes and PR creation/updates retain their own explicit authorization.

The owner performs every merge manually. Neither authorization to publish,
assignment, a green pipeline nor the final stack layer permits agent merging,
auto-merge or scheduling. Keep worktrees and branches until the owner's merge
is observed and the retention requirements below are satisfied.

## Review size

Count additions plus deletions in the PR's effective diff against its immediate
base, rather than net file growth, commit count or total branch history.

| Changed lines | Treatment |
| --- | --- |
| 0–400 | Normal review-size target. |
| 401–600 | Visible warning and an explanation of why reviewing the change together is useful. |
| More than 600 | Reorganize into several coherent PRs before merge. |

The purpose is readable, understandable and verifiable changes. Do not remove
tests, move necessary explanations elsewhere or divide code at arbitrary line
boundaries merely to make the number smaller. Count textual generated files and
lockfile changes and identify them separately; disclose binary changes because
line counts do not measure their review burden. Do not silently hide exclusions.

These bands apply to work PRs. A `develop` to `main` release promotion may
aggregate many already reviewed work PRs and is exempt from this line budget;
list its included PRs and validate the integrated release. Source-generating
changes remain subject to the ordinary work-PR policy.

## Multiple PRs and dependent stacks

Split independent changes into separate PRs against `develop`. Use a stack when
a later change depends on one that is not merged yet. Every layer has its own
worktree, focused scope and checks. This is the explicit base/target exception:

1. Start the bottom layer from fetched `origin/develop`; its PR targets `develop`.
2. Start the next layer from its recorded predecessor SHA; its PR targets that
   predecessor branch. Record both the predecessor and the stack trunk `develop`.
3. Link every PR to the same story and to its predecessor/successor PRs. Each
   PR number is stable; a display position such as `[2/3]` can change as work is
   discovered. Do not require a known total when creating the issue.
4. Review only each layer's incremental diff. The owner integrates bottom-up, with one
   squash result per PR ultimately landing on `develop`.
5. After a lower-layer squash, update dependent history/bases and revalidate the
   resulting diffs before merging them. Merely retargeting can retain old commits.

Synthetic example: story `#123` can have PR `#201` for state, `#202` for the API
and `#203` for the interface. Those PRs do not require three new issues. The
story lists the necessary PRs and their remaining acceptance work.

Verify the selected host's actual stack support, CI events and merge behavior;
GitHub's native stacks and manually chained PRs are not interchangeable setups.
Rewriting or publishing task-branch history retains its explicit authority
requirements. No stack permits direct pushes to persistent branches.

## Acceptance and manual issue closure

Merging any linked PR, including the last one, must not automatically close the
story issue. All required PRs being merged is a prerequisite; explicitly verify
the full acceptance criteria and retain revision/environment-specific evidence
before manually closing it. A cancelled story records a reason instead.

Use non-closing references such as `Refs #123`; do not issue `Closes`, `Fixes`
or `Resolves` directives for the story in PR bodies or commit messages. Preserve
issue/branch/PR associations. Disable the hosting provider's linked-PR auto-close
setting and any conflicting bot/Project workflow when configuring that repository
under the corresponding owner authority. Project automation and native provider
auto-close are separate controls; disabling one does not prove the other is off.
Keep execution status and acceptance/validation status independent.

## Automation and enforcement

Each hosted repository must adopt a required policy check for ordinary prefixes
and approved base/target routes, including the exact release-promotion exception.
Run it for every relevant PR, including unknown prefixes and stack layers; a
filter that skips invalid names cannot reject them. Report review-size bands
against the correct layer, references and the need to split oversized work.

The prefix communicates intent and can select additional jobs. Changed content
determines mandatory checks: a `docs/` branch changing code still needs its code
tests. With GitHub Actions, `pull_request.branches` filters the target branch;
use `github.head_ref` for the source prefix and verify stack-trunk handling.

Document the host-specific adoption per repository: installed policy check,
required checks/protection, prefix routing, size reporting, manual-close setting
and a tested issue/multiple-PR example. Until actually configured and exercised,
these are required controls with pending enforcement, not claims of active CI.
This documentation rollout changes no remote settings or workflow code.

## Coordinated guide adoption

Before changing a shared guide, portable snapshot or adapter version, inspect
the canonical task assignments and affected publication inputs. Record the
execution identity, allowed paths, exact source version and downstream owners.
Another owner's active candidate is a dependency, not writable scope. Coordinate
the adoption or prepare the next candidate separately; do not rewrite snapshots,
metadata or historical proofs during an active publication.

Adopt a reviewed portable workflow, development guide, managed AGENTS block,
task template and version/hash metadata together. Preserve project-owned AGENTS
content and unrelated local work. Validate the exact candidate using its recorded
policy inputs, then use the repository's ordinary worktree/MR route for publication.
Report prepared, adopted, published and remotely enforced states separately.

## Retention and cleanup

Confirm the MR is merged and retain its URL, source/target SHAs and actual squash
result. Preserve needed tracked, untracked and ignored files, credentials and
runtime data. Confirm dependent stack layers no longer need the predecessor
before retiring only that task's worktree and local/remote branch, then update
the inventory. Keep unmerged resources, or record a concrete preservation/dependency
blocker with responsible owner and review date. Never delete `develop` or `main`.

## Primary references

Checked 2026-10-25. The company policy is an adaptation, including squash task
integration; the original Gitflow article does not prescribe this entire guide.

- [Original Gitflow model](https://nvie.com/posts/a-successful-git-branching-model/)
- [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)
- [GitHub stacked PR requirements](https://docs.github.com/en/pull-requests/reference/stacked-pull-requests)
- [GitHub Actions pull request events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request)
- [GitHub issue auto-close setting](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-auto-closing-issues)
