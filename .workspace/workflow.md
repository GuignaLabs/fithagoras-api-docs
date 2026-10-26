# Repository Workflow

Framework version: 0.3.0. Generated from the current method and reviewed project policy. This document does not install the tools: use the coordination root containing scripts, and report unavailable checks accurately.

## GuignaLabs Policy

Apply the current framework together with these company choices. Explicit owner
requests and host constraints govern task-specific authority. Product domain,
runtime and budget choices stay in their owning repositories.

### Communication And Ownership

Communicate with the owner in Spanish. Preserve repository code/documentation
language; public brand material stays in English. Do not invent customers,
contacts, domains, licenses, delivered capabilities or approval. The company root
stays outside Git; repositories own independent histories and remotes. The central
`.workspace` is local-only coordination. Read root/project/nested AGENTS rules.
Find the company root among checkout ancestors using root AGENTS.md and
`.workspace/company/workflow.md`; an isolated clone uses its portable snapshot.

### Git, Worktrees And External Authority

For every ordinary product or organization repository task, fetch `origin/develop`
and create a task-specific worktree and branch from that exact commit. Use the
shared ordinary prefixes: `feature/`, `fix/`, `docs/`, `refactor/`, `test/`, `ci/`,
`build/`, `perf/` or `chore/`. Name it `<type>/<issue-or-task-id>-<description>`;
one issue may identify several branches with distinct descriptions. Existing
shorter local naming examples do not narrow this owner-adopted company catalog.
Reserve `release/` and `hotfix/` for separately defined, explicitly authorized
special flows; neither grants a different base or destination by its name.
Record the resolved base, task and owner. Implement and validate in that worktree,
never in the primary checkout. If `develop` or its remote is unavailable, resolve
that prerequisite with the owner instead of silently choosing another base.
The owner's standing direction covers this local branch/worktree setup for an
authorized repository task; commits and remote publication retain their own scope.
The canonical private company coordination checkout remains local; do not invent
a remote or publish its records to satisfy a product delivery rule. This exception
does not exempt a product repository because it contains a `.workspace/` folder.

Every integration requires a merge request (MR; pull request/PR on GitHub).
Push only the task branch, open an ordinary MR against `develop`, and attach the actual
scope, validation and limitations. Merge through the MR after required review
and checks; the owner performs every merge manually. Agents must not merge,
enable auto-merge or schedule a merge. Squash task branches into `develop`.
Promote `develop` to `main`
through a release MR with a normal merge preserving history. Never push directly
or force-push to `develop` or `main`, including from a temporary integration
branch. Permission to publish a task does not waive the MR route.

Worktrees use `.worktrees/<repository>/task-<id>-<purpose>/` under the company
root and are registered centrally; permanent editor entries are optional.
An open, closed-unmerged or failed MR keeps its task branch and worktree.
Before retiring a merged stack layer, confirm its dependents have been updated
and no longer need that branch/worktree. Otherwise retain it with the concrete
dependency, responsible owner and review date. After confirming the MR is merged,
retain its URL, source/target SHAs and actual
merge/squash result; then preserve required tracked, untracked and ignored files,
credentials and runtime data. The owner's standing cleanup instruction covers
removing only that task's worktree, local branch and remote branch after this
verification. Confirm each removal or that the hosting service already removed
the remote branch, and update inventory/editor entries after actual retirement.
If preservation or ownership is unresolved, record the concrete blocker, owner
and review date instead of forcing removal. Existing sibling role checkouts and
unrelated branches require separately scoped disposition.
Never delete the persistent `develop`/`main` branches during task cleanup.

Commits, pushes, Git initialization, branch/worktree creation/move/removal,
remote/visibility changes, deployment, cloud/data mutation and external messages
require corresponding explicit authority. The standing post-merge cleanup
instruction above grants no commit, push, MR publication/merge, deployment or
unrelated deletion authority.
Request approval before every `bq query`, including read-only and dry-run.
Preserve global profiles, credentials,
required local files and runtime data. No task workflow grants spending authority.

### Merge Request Readiness

Treat local validation, branch publication, an open MR, merge, target-branch CI
and cleanup as separate observed states. An MR can be opened as a draft while
validation or review remains incomplete; a draft is not ready to merge.

#### Before Opening

Prepare one coherent change and review the complete committed diff against its
intended target, plus staged, unstaged and new files in the task worktree.
Unrelated primary-checkout work is not an implicit dependency or publication grant.

| Check | Required evidence |
| --- | --- |
| Identity and target | Repository, task/owner, task worktree, source branch, exact base SHA and intended target. Ordinary task MRs target `develop`; declared stack layers record the predecessor SHA/branch and trunk `develop`; release MRs promote `develop` to `main`. |
| Authority and scope | Existing authorization covers the exact commit/push/MR actions being taken. Agents do not merge, enable auto-merge or schedule a merge; the owner performs merges manually. Do not ask again for publication actions already covered. |
| PR metadata | Plan one primary `type:` label matching the main branch purpose and assignment to the verified owner. Read back each published PR's actual labels, assignee, source/head, target/base, state and auto-merge field before handover; preserve stack dependencies. |
| Complete candidate | Intended files and dependencies are included. Generated source and controlled guidance/metadata match their inputs. No unrelated staged files, conflicts or local-only files enter the candidate. |
| Behavioral evidence | Relevant repository checks pass on the actual candidate, including meaningful regression/boundary coverage for changed behavior. State skipped or unavailable checks and their impact; a narrower check does not establish full acceptance. |
| API and documentation | Public behavior changes include the contract, synthetic examples, generated clients/types and affected guides in the same MR. Internal changes require prose only when reader instructions or external behavior change. Run the repository documentation/API gate. |
| Privacy and review | Review source and the MR body for credentials, private profiles/logs, data and private coordination records. Resolve blocking findings; label same-agent review honestly. Include screenshots only when useful and safe. |
| Description | Explain the concrete problem, resulting behavior, task/issue if available, exact validation/results, material risks/compatibility/migration implications and practical rollback. Do not invent issue links or claim unobserved publication/deployment. |

Before an authorized commit, use the exact staged-candidate gate in the actual
task worktree with the resolved base, explicit path scope and correct hygiene
profile. Recheck its snapshot immediately before committing, then verify the
committed candidate against the same bindings. A working-tree test or gate PASS
alone does not authorize publication. Keep private evidence in its owning
coordination location; publish only an appropriate summary in the MR.

#### Before Merging

Reconfirm the MR source/head SHA, target/base SHA, intended diff and configured
merge method. If the base advances or the candidate changes, resolve conflicts
in the task worktree and refresh affected checks and review. Do not rewrite a
published/shared branch without explicit authority. Check the current MR's
applicable CI, including the test merge candidate when the platform uses one;
an earlier green push run is not sufficient evidence for a changed integration.
Critical acceptance skipped by a green job remains unverified.

Require the repository's applicable approvals and resolve blocking discussions.
Name the responsible reviewer and verified human owner; follow the task's
risk-based review/acceptance policy. An agent's review note is not a GitHub
approval unless that approval was actually submitted and observed.
Select squash for each task layer ultimately landing on `develop`, and a normal
history-preserving merge for a release MR from `develop` to `main`. Leave the
PR open for the owner to merge manually after applicable checks and review.
Neither a green pipeline, owner assignment nor the final stack layer grants
an agent merge authority; never substitute a local integration push.

#### After Merging

Confirm the hosting service reports the MR as merged and record its URL, source
SHA and resulting target commit. A closed MR is not proof of merge. Squash
changes commit identity: verify the actual delivered result instead of treating
source-commit ancestry as the only integration test. Observe applicable
target-branch CI and documentation output/change decisions; report failures and
their next owner before claiming a verified delivery.

Before cleanup, confirm that local/remote task refs still belong to that MR and
contain no later unmerged work. Preserve required local files/data, retire only
the owned worktree/local/remote task branch and update the inventory/editor.
GitHub's automatic head-branch deletion, when enabled, removes the remote branch;
local worktree/branch cleanup still requires the agent's verified local action.

#### Hosting Enforcement

Read the actual hosting configuration instead of inferring protection from a
workflow file. Required MRs, applicable CI contexts, review requirements and
push/bypass restrictions must be configured to enforce the policy remotely.
Require only checks that actually run for that repository and target branch.
Remote branch auto-deletion is a separate setting; keep persistent branches
protected. Changing these settings needs the corresponding owner authority.

GitHub semantics checked 2026-10-25: [current head and test-merge checks](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks),
[MR/review rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)
and [automatic head-branch deletion](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-the-automatic-deletion-of-branches).

### PR Classification, Assignment And Guide Adoption

Apply one primary `type:` label to every PR and each stack layer: `type:feature`,
`type:bug`, `type:docs`, `type:refactor`, `type:test`, `type:ci`, `type:build`,
`type:perf` or `type:chore`. The development guide maps each ordinary prefix.
Retain useful unrelated labels; missing-label creation and legacy-label
deletion require separately scoped repository authority. A guide update grants
no remote catalog or hosting-configuration authority.

Assign each PR to the verified owner account. The current GuignaLabs owner is
`jbasualdo`, verified on 2026-10-25; revalidate when the owner or authenticated
account changes. Do not infer an account from the OS username. Assignment
does not replace review approval. Leave each PR open for human review/merge.

Inspect recorded task owners and pinned publication inputs before changing
shared guides or portable versions. Coordinate adoption; do not rewrite
another owner's active snapshots, metadata or historical proofs. Prepare the
next candidate separately when necessary, then adopt its reviewed snapshots,
managed blocks and metadata together. Report prepared, adopted, published
and remotely enforced states separately.

### Development, Review Size And Story Acceptance

These agreements apply to every GuignaLabs project/repository. The
[development guide](development.md) explains them with synthetic examples and
is distributed with the portable workflow; product domain details stay local.

An issue describes an outcome and acceptance criteria without requiring a line
estimate or a fixed PR count. One story may have many PRs. Discover and revise
the decomposition while implementing; subissues are optional for separately
useful outcomes/owners, not required for each size-budget chunk. Keep issue IDs
stable. PR numbers identify changes; `[n/N]` is only a mutable display position.

Prefer at most 400 added plus deleted lines per work PR. From 401 to 600, show
a warning and explain why the change is useful to review together. Above 600,
split into coherent PRs before merge. Measure the effective diff against each
PR's immediate base, including only that layer in a stack. Retain relevant tests
and documentation; do not split arbitrarily to meet the number. Count textual
generated/lockfile changes and disclose binaries separately, without silently
hiding review burden. The exact same-repository `develop` to `main` release
promotion is exempt from the line budget and ordinary prefix requirement because
it aggregates reviewed PRs; enumerate them and validate the integrated result.

Independent PRs target `develop`. For a declared dependent stack, the bottom
layer starts from fetched `origin/develop`; subsequent layers may start from
the recorded predecessor SHA and target that predecessor branch. Every layer
has its own worktree/task scope and identifies the story, predecessor/successor
PRs and trunk `develop`. This is the explicit ordinary-base/target exception.
Review the incremental layers and land them bottom-up, with one squash result
per PR on `develop`. Verify actual host/CI stack support, update dependent history
and bases after lower-layer squash, and rerun affected checks. Retargeting alone
is not proof of a clean diff. Publication/history rewriting keeps its own authority.

No linked PR merge, including the last, automatically closes the story issue.
Manually close only after every necessary PR is merged and the complete criteria
have revision/environment-specific acceptance evidence; cancellation states its
reason. Keep execution and validation independent. Preserve issue/branch/PR links,
use non-closing references and avoid closing directives in story-related PR/commit
text. Under the corresponding configuration authority, disable native linked-PR
auto-close and conflicting bots/Project workflows; these are separate controls.

Each hosted repository must adopt a required branch-policy check and report size
bands against the correct PR layer. Check every relevant PR, including invalid
prefixes and stack layers; filters must not skip the cases being rejected. Prefixes
express intent and can select additional jobs, but changed files determine minimum
checks: naming code changes `docs/` cannot bypass their tests. On GitHub, source
prefix routing uses `github.head_ref`; `pull_request.branches` filters the target.
Record actual per-repository check/protection/manual-close adoption and a tested
multi-PR example. Documentation alone does not install or verify remote enforcement.

### Local Records And Tools

The receiving coordinator owns shared navigation/knowledge and actual handoff
acknowledgements. Keep private product research/evidence in its owning location;
do not copy it into portable repositories. Use ordinary shared filenames and
reserve `*.workspace.*` for ignored local configuration. Adopt generated snapshots
and their metadata together, preserving project-owned AGENTS content.

Company checks are scripts/check_workflow.py and scripts/check_workspace.py;
schema1 release checks remain required for substantive changes. Git-candidate,
knowledge-retrieval, native-agent and product-runtime tools are optional adapters
used for relevant work. A local source check is not hosted CI or agent compliance.
For process diagrams, use the existing draw-simple-flows skill when available
under the company root; no global skill installation is implied.

## Working Method

Every substantive task has a bounded outcome: working behavior, a supported
answer, a decision or an enabling capability. Scale the work record and checks
to risk while preserving acceptance and authority. Project/company policy
supplies local choices; owner requests and host constraints govern execution.

## Frame And Retrieve

Inspect applicable instructions, Git state/remotes and relevant documentation.
Search existing project knowledge before repeating research; read the canonical
source with its date, scope and limits. Historical observations do not establish
current validity. Preserve unrelated/concurrent work and private configuration.

Use one task record with a stable ID and responsible owner. Before execution,
record beneficiary, purpose, actual authority, included/excluded paths, original
acceptance criteria, validation plan, approach and recovery. Name receiving
owners and dependencies. Keep at most three current actionable steps. A routine
task can use one criterion; retain a single canonical state instead of duplicate
hand-maintained result tables. Use the schema-1 task template routed by the local
entrypoint; fill examples with actual values before validation.

## Implement And Validate

Choose the smallest useful change. Follow detected repository commands and
conventions; do not invent stacks, licenses, numeric coverage or capabilities.
Define observable expectations before implementing. Test relevant successful,
failure, boundary and regression cases proportionally. Preserve original
criteria; explain material decisions and skipped/unavailable checks.

Bind a passing observation to the actual contract, delivered file hashes, UTC
time, environment and nonempty evidence. A hash does not prove semantic truth or
actual execution. Changing scope/criteria requires a new task revision with the
old contract, reason and authority retained. Changed artifacts invalidate affected
proofs. Revalidate; do not refresh approvals by replacing hashes alone.

Perform a distinct review against the original outcome, actual diff and evidence.
Record reviewer/kind and resolve blocking findings. Same-agent review is not
independent review. High-impact releases require the configured owner acceptance
and independent/human review. Local tests do not establish hosted CI or deployment.

## Integrate And Manage Worktrees

Use an independent checkout when parallel implementation or revision-specific
testing needs isolation. Follow the workspace's worktree location and branch
strategy. Assign one task/write owner per checkout; record repository, path,
branch and resolved base. Keep one index writer; shared refs and runtime resources
still need coordination. New worktrees do not inherit uncommitted source or ignored
configuration automatically. Set up explicit, separate runtime selectors as needed.

Verify the actual integration result against the current target, including merged
dependencies and conflicts. Earlier task acceptance does not validate a new merge
result. For squash integration retain the target commit/PR binding; branch
reachability alone does not prove the task's changes landed.

Before an authorized commit, validate the exact staged scope against its intended
resolved base using the applicable candidate checker. Bind scope/policy/candidate
digests, recheck immediately before committing and verify the actual commit.
Working-tree tests cannot prove the index contains required files. Missing
dependencies remain a delivery gap; never import another owner's bytes or waive
checks to force a pass. Check-to-commit is not atomic.

After integration resolve worktree, local-branch and remote-branch disposition
separately. Preserve needed tracked, untracked and ignored files, credentials and
runtime data before authorized retirement. Retire the temporary checkout using
Git, or record retention reason, responsible owner and review date. Update
inventory/editor entries after actual removal. Missing authority or unsafe cleanup
stays explicitly pending. Age, merge and task closure never authorize deletion.

## Deliver, Accept And Retain

Retain delivered behavior/paths, purpose, acceptance evidence, review, limitations,
recovery, useful knowledge, follow-ups and next owner/action. Distinguish local
completion, integration, commit, push, publication, deployment and customer
validation. Perform external actions only within corresponding actual authority.
Do not silently leave a contracted delivery unfinished; record its exact blocker
and pending step. Do not treat a prior owner's approval as authority for new work.

Use READY from the release gate and the required semantic/owner acceptance before
closing. Schema 1 fingerprints contract and artifacts; review also binds current
check/receipt digests, and owner acceptance binds review. Automatic acceptance is
derived only from an authorized policy. Tool readiness verifies recorded structure
and integrity; it cannot authenticate actors or prove claims, execution or cleanup.

Before closure record Update, Add or None for reusable knowledge. Reuse existing
keys. Retain findings that change a future decision with canonical source/date,
evidence state, scope/limits and revalidation trigger. None needs no filler record.
The receiving owner alone integrates shared navigation and acknowledges actual
handoff; keep it pending until observed. Preserve historical receipts and original
task ownership. A task may be closed locally while separately scoped integration
or publication remains pending, with explicit receiver/action.

## Maintain Instructions

Current rules live in this versioned core and the applicable project policy.
Record superseded rules and migration in CHANGELOG.md; keep outdated proposals
and dated evidence outside mandatory reading. Version tools, templates and
instructions together. Update only reviewed adopted copies and their metadata;
preserve local instructions and detect drift. Never infer installation, global
settings, permissions or agent compliance from the existence of a document.
