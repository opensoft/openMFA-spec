# Implementation Plan: 001-challenge-receipt-core

**Status**: Draft candidate implementation
**Date**: 2026-11-10
**Spec**: [spec.md](spec.md)
**Governance**: [add-challenge-receipt-core](../../openspec/changes/add-challenge-receipt-core/proposal.md)

## Summary

A file-backed, caller-bound challenge/receipt core with real issuer signatures, default-deny factor verification, cancellation, expiry, binding revocation and idempotent one-use consumption.

## Technical Context

Python 3.12; cryptography 50.0.1; rfc8785 0.1.4. File-backed SQLite and real Ed25519 issuer signatures. No network calls or live credentials in the candidate gate. Tests generate ephemeral keys in memory.

## Constitution and boundaries

No project constitution is present; follow the assembly instructions and shared protocol. Governance/contracts stay in this spec leg; code/tests stay in the paired code leg. No sibling checkout reads in code gates. No unmerged leg pins, release tag, authority vocabulary fork or approval-rule change.

## Project Structure

- Spec leg: `contracts/*-v0.schema.json`, `tests/runtime_contracts/`, this feature and OpenSpec change.
- Code leg: `openmfa_runtime/core.py`, `pyproject.toml`, substantive tests and source CI.
- Assembly root: reproducible OpenSpec/Speckit bootstrap tooling, reviewed separately with unchanged leg pins.

## Research and data model

See [research.md](research.md), [data-model.md](data-model.md) and [quickstart.md](quickstart.md). Fixed algorithms/canonicalization and exact bound contexts are chosen to make independent compatibility vectors possible. The schemas are candidates, not an accepted dependency.

## Sequence and validation

The sole executable list is [tasks.md](tasks.md). Capture governance and schema first, implement candidate math/state second, then run the spec and code gates, reconcile evidence, open paired draft PRs and request Codex review. Keep owner acceptance, merges and root pins pending.

## Analysis

FR subjects map one-to-one to the capability requirements. Code tests cover each subject and critical negative/race paths; schema tests cover structure only. Synthetic state-test factors cannot clear real adapter acceptance. No unresolved clarification is delegated to code; future integration gates are explicit exclusions.
