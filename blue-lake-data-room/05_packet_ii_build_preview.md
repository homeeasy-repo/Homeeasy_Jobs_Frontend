# 05 - Packet II Build Preview

Packet II is sent by email after Packet I review. The exact prompt may change, but the shape is:

Build a small Revenue Captain service.

## Inputs

- `applications.json`
- `events.json`
- `school_routes.json`

## Required Behavior

The service should:

1. Normalize records into a durable state model.
2. Produce a ranked next-action queue with reason codes.
3. Detect stale candidates, duplicate applicants, missing evidence, bounced routes, and human-review cases.
4. Include one idempotent worker command that can run repeatedly without corrupting state.
5. Include tests for duplicates, stale candidates, missing evidence, bounced route, and rerun/idempotency.
6. Include a short README explaining architecture, tradeoffs, and production hardening.

## Submission

Candidates send:

- GitHub repository link.
- Five to eight minute walkthrough recording.
- Expected monthly compensation in USD.
- Three interview windows overlapping US Central Time.

## Live Follow-Up

Selected candidates will be asked to modify or explain their work live without AI assistance.
