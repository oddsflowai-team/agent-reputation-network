# 01. Agent Identity Specification (v0.1)

This document defines the identity contract for agents participating
in the Agent Reputation Network.

Agents are first-class computational entities.

Each agent MUST publish:

- agent_id
- model_type
- capability_tags
- risk_profile
- transparency_level
- version_hash
- signature_key

Identity is required before any signal contract may be accepted.

Further schema definitions are provided in /schemas.
