# TASK-NNNN — <Smallest Useful Delivery>

Record the user's request, beneficiary, relevant knowledge, baseline and current
worktree here. Use one contract block; delete irrelevant prose sections.
New tasks use schema 1. Follow the project's canonical task paths and adjust
relative navigation links when moving the record.

Ownership: workstream `<durable-owner-alias>`; coordinator `<owner-alias>`;
receiver `<shared-integration-owner>`; permitted writes `<explicit-paths>`.
Record another owner's task as a dependency, not as your actionable focus.
Session IDs/settings are observable metadata or unknown, not ownership proof.
For an independent checkout, record repository/task/owner, path, branch and
resolved base, following the applicable project/company policy.

## Release Contract

```json task-release
{
  "schema_version": 1,
  "task_id": "TASK-NNNN",
  "revision": 1,
  "status": "In progress",
  "stage": "frame-and-retrieve",
  "risk": "standard",
  "purpose": "<beneficiary, problem and smallest useful result>",
  "scope": "<included, excluded, invariants and allowed actions>",
  "authority": "<actual user request>",
  "acceptance_policy": {
    "mode": "automatic",
    "owner": "user",
    "authority": "<automatic closure authorization; use owner mode when required>"
  },
  "artifacts": {},
  "criteria": [
    {
      "id": "AC-01",
      "required": true,
      "scenario": "<input, preconditions and baseline>",
      "expected": "<observable expected result or threshold>",
      "method": "<appropriate check and data>",
      "result": "PENDING",
      "validation": null
    }
  ],
  "review": null,
  "acceptance": null,
  "receipt": null
}
```

## Approach And Decisions

At most three current actionable steps. Record meaningful alternatives,
rationale/owner, changes to the original contract and useful failed attempts.
Link a durable decision only when it governs later work.

## Evidence And Closure Instructions

Read the current workflow and relevant tool commands routed by local instructions. Declare delivered
artifact paths in `artifacts`, initially with null hashes; `--snapshot` prints
current hashes/digests. After actual checks, fill each PASS validation with:

- `contract_digest`, `artifact_digest`, UTC `observed_at`, `environment`;
- `evidence`: nonempty array of repository-relative `path` and `sha256`;
- optional UTC `expires_at` for time-limited proof.

Review fields: `result`, `kind` (same-agent/independent/human), `reviewer`,
`findings` array and `validation`. Its proof adds `validation_digest` of the
current check ledger and `receipt_digest` of the closure receipt. Findings own unique `id`, `severity` (blocking/nonblocking),
`state` (open/resolved), `description` and `resolution_evidence` array; resolved
findings require proof.

Automatic `acceptance` stays null and derives from the authorized policy.
Owner mode requires `result`, `accepted_by` matching the owner, and `validation`
adding `review_digest`. Review follows check observations; acceptance follows review.

Receipt fields: `delivered`, `why`, `rollback`, `knowledge`, `next_action`
(meaningful strings, explaining non-applicability); `revalidation_triggers`,
`limitations`, `follow_ups` (arrays of strings; at least one trigger).
Keep the mutable task out of its own artifact/evidence hashes.
Close only after READY and required acceptance; retain exact limitations.
For integrated work, include the target commit/PR and separate worktree/local
branch/remote branch dispositions in the existing receipt fields. Verify squash
integration explicitly; retire after preserving needed local files/runtime data,
or retain with reason, responsible owner and review date. Update inventory/editor
entries after actual removal. Record unauthorized/unsafe cleanup as pending;
schema 1 does not automatically prove or perform cleanup.
For shared handoff, name the receiver and integration/pending disposition in
`receipt.knowledge`/`follow_ups`. The receiver acknowledges the task/revision in
the project handoff register, without rewriting your ledger.

In `receipt.knowledge`, state **Update**, **Add** or **None** (Update and Add can be
combined). None needs no extra explanation or filler entry. For retained learning,
identify existing/new stable keys, canonical source/date, evidence state, limits
and revalidation trigger. The receiving owner updates the shared index; record
pending integration explicitly and preserve historical receipts. This is semantic
closure guidance within schema 1, not a new field or proof that a claim is true.
