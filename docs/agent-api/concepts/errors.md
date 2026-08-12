---
description: "DeGov Agent API validation, payment, rate-limit, quota, and server error behavior."
---

# Errors

Do not assume every failure has one envelope. The API currently exposes several response families.

## Validation and resource errors

Business errors identify a stable code and message when available. Common cases include invalid parameters, missing resources, oversized query windows, invalid cursors, stale cursors, and candidate-budget limits. Fix the query or restart pagination as directed.

## Payment challenges

An unpaid paid-route request returns HTTP 402 with a `payment-required` header and a JSON payment description. This is an x402 offer, not the normal business-error envelope. Inspect the current offer and delegate authorization and settlement to an x402-capable wallet.

## Authentication behavior

An invalid or insufficient partner token may currently fall through to a 402 challenge. Clients should branch on the observed response rather than hardcoding 401/403 assumptions.

## Rate limits and quotas

HTTP 429 can represent a short-window rate limit or monthly quota exhaustion. Back off for rate limits; wait for quota renewal or change the partner plan for exhausted quotas.

## Server errors

Retry transient 5xx responses with bounded exponential backoff. Include `requestId` when reporting a persistent problem. Never automatically replay a payment without the wallet capability's retry and settlement checks.
