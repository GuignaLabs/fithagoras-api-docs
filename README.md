# Fithagoras API Documentation

Public API-consumer documentation for Fithagoras, hosted with GitHub Pages.
Application source and team documentation remain private.

The hosting workflow accepts an immutable `docs-<source-commit>` release with
`public-api-docs.tar.gz` and an `Artifact SHA256:` line in its release notes.
It validates every file hash, public audience, contract hash and output path
before deploying. Archives cannot contain source code, team routes or symlinks.

Run `python3 -B -m unittest discover -s tests -v` before changing validation.
Use a task worktree from fetched develop for source changes and leave merging
to the verified owner. Source guidance is in [.workspace/development.md](.workspace/development.md).

The published documentation describes the current API contract and synthetic
examples. It does not provision a public API service or advertise production
access.
