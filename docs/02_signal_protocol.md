# 02. Signal Protocol Specification (v0.1)

This document defines the structure of a signal contract.

A signal is a structured, deterministic decision object.

Minimum required fields:

- signal_id
- origin_agent
- context_hash
- confidence_metrics
- risk_band
- verification_hash
- timestamp

Signals MUST pass JSON schema validation before reputation calculation.

Signals MUST be challengeable within a defined window.
