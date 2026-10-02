# Verification Report

This report is generated from the repository checks. Run `pytest -q` and `python verification/readiness_audit.py` to refresh the observed results.

## Scope
Manifest structure, documentation, tool contract, dynamic discovery, adapters, security validation, and deterministic domain behavior are covered by the test suite.

## OpenGAP
The project targets OpenGAP specification 0.1.0. The local test validates `agent.yaml` against the published OpenGAP JSON schema when network access is available.

## CLI
The OpenGAP CLI result must be reported from the actual environment and is not inferred from schema validation.
