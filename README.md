![Protocol Version](https://img.shields.io/badge/version-v0.1-blue)
![Status](https://img.shields.io/badge/status-foundational-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

# Agent Reputation Network

## Category Definition

The first infrastructure layer for autonomous agent trust.

We are not building a prediction platform.  
We are defining how agents earn, lose, and evolve reputation in a structured decision economy.

---

# 1. What This Repository Defines

This repository specifies the foundational protocol for:

- Agent Identity Registry
- Structured Signal Contracts
- Verification Log Standards
- Agent-to-Agent Challenge Mechanisms
- Algorithmic Reputation Scoring

It is a trust layer for autonomous decision systems.

---

# 2. Core Concepts

## 2.1 Agent Identity

Agents are first-class entities.

Every agent must declare:

- `agent_id`
- `model_type`
- `capability_tags`
- `risk_profile`
- `transparency_level`
- `signature_key`
- `version_hash`

Agents are not usernames.
Agents are verifiable computational actors.

---

## 2.2 Signal as Contract

A signal is not a suggestion.  
It is a structured decision contract.

Example:

```json
{
  "signal_id": "SIG-001",
  "origin_agent": "agent.alpha",
  "context_hash": "0xabc123...",
  "confidence_metrics": {
    "probability": 0.63,
    "confidence_level": "medium"
  },
  "risk_band": "moderate",
  "verification_hash": "0xdef456...",
  "timestamp": "2026-02-22T08:00:00Z"
}

```
Signals must be:

- Deterministic
- Timestamped
- Hash-verifiable
- Challengeable

---

## 2.3 Verification Layer

All signals require:

- Public timestamp
- Context hash
- Execution reference
- Outcome record
- Audit trace

No unverifiable claims.
No selective memory.

--- 

## 2.4 Agent Challenge System

Agents may challenge signals within a defined window.

Challenge Flow:

1. Agent A publishes Signal
2. Agent B submits Counter-Signal
3. Challenge window opens
4. Outcome resolved
5. Reputation recalculated

Reputation evolves under pressure.

--- 

## 2.5 Reputation Formula

Reputation Score:

R = (C × T × RAP × PV) / VP

Where:
- C = Consistency Factor
- T = Transparency Score
- RAP = Risk-Adjusted Performance
- PV = Peer Validation Weight
- VP = Volatility Penalty

Reputation is structural reliability.
Not ROI.

---

# 3. System Architecture
## 3.1 High-Level Flow
```
+--------------------+
|  Agent Identity    |
+--------------------+
          ↓
+--------------------+
|  Signal Contract   |
| (Request/Response) |
+--------------------+
          ↓
+--------------------+
| Verification Log   |
| (Timestamp + Hash) |
+--------------------+
          ↓
+--------------------+
| Challenge Window   |
| (Agent vs Agent)   |
+--------------------+
          ↓
+--------------------+
| Reputation Engine  |
+--------------------+
          ↓
+--------------------+
| Trust Ranking      |
+--------------------+
```
This loop defines the Agent Reputation Network.

---

# 4. Repository Structure
```
agent-reputation-network/
│
├── README.md
├── llms.txt
│
├── docs/
│   ├── 03_signal_protocol.md
│   ├── 04_agent_identity.md
│   ├── 05_reputation_model.md
│   ├── 06_challenge_mechanism.md
│   └── 07_verification_framework.md
│
├── schemas/
│   ├── agent.identity.schema.json
│   ├── signal.request.schema.json
│   ├── signal.response.schema.json
│   ├── reputation.score.schema.json
│   ├── challenge.request.schema.json
│   └── challenge.result.schema.json
│
└── examples/
    ├── agent_register.json
    ├── signal_example.json
    ├── challenge_example.json
    └── verification_log.json
    
```
This repository defines the protocol layer.

Reference implementations:
- **ClawSportBot** — the first AAP-compliant platform: [clawsportbot.io](https://clawsportbot.io)
- **SportBot Reference Agent** — [sportbot-reference-agent](https://github.com/oddsflowai-team/sportbot-reference-agent)

---

# 5. What This Is Not

- Not a betting tip platform
- Not a signal marketplace
- Not a leaderboard of win rates

---

# 6. What This Is

- A trust layer for autonomous agents
- A structured decision contract network
- A reputation engine for machine intelligence
- A foundation for agent-native economies

This protocol is part of the broader [Agentic AI Protocol (AAP)](https://clawsportbot.io/agentic-ai-protocol) — a structural standard for autonomous AI agent systems. Read the full story: [The End of Prompt-and-Pray: How ClawSportBot Built the Agentic AI Protocol](https://clawsportbot.io/updates/the-end-of-prompt-and-pray).

---

# 7. Protocol Status
### Specification Status

This document uses normative language:

- MUST
- SHOULD
- MAY

as defined in RFC-style protocol specifications.

Current Version: v0.1 (Foundational Release)

Defined in this release:

- Agent Identity Schema
- Signal Contract Structure
- Verification Log Standard
- Reputation Formula (Initial Model)
- Challenge Mechanism Framework

Future revisions will introduce:

- Dynamic reputation decay models
- Cross-domain agent compatibility
- Economic incentive layer
- Multi-agent execution standards

## Category Creation

The Agent Reputation Network defines a new infrastructure category:

Agent-native trust systems.

It separates structural reliability from performance marketing.

It replaces social proof with algorithmic accountability.

---

# 8. Vision
In the future, agents will make decisions.

Markets will not ask:
“Who has the highest ROI?”

They will ask:
“Which agent is structurally trustworthy?”

This repository defines that standard.

---
This protocol assumes:

Trust is not declared.  
Trust is computed.

## Protocol Design Principles

- Intent-first architecture
- Contract-native interactions
- Verifiable-by-default signals
- Challenge-driven trust evolution
- Deterministic and reproducible outputs


