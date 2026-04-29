# Fintech Product Analytics — SQL Project

## Overview

This project analyses a synthetic fintech product dataset to identify onboarding drop-offs, activation gaps, revenue differences, retention behaviour, and acquisition channel quality.

The main business question:

**Are acquired users actually reaching activation and generating value?**

The key finding was that the product’s biggest issue was not retention. It was **post-KYC activation**, especially among paid ads users.

---

## Dataset

The dataset was generated using Python to simulate realistic fintech user behaviour across acquisition, onboarding, KYC, transactions, sessions, and support interactions.

Dataset size:

- 5,000 users
- 23,681 events
- 43,134 sessions
- 9,026 transactions
- 1,310 support tickets

---

## Tables

The project uses five relational tables:

| Table | Purpose |
|---|---|
| `users` | User profile, signup date, acquisition channel, country, device, KYC status |
| `events` | Product actions such as app open, onboarding started, KYC submitted, bank added, first transaction |
| `sessions` | App usage sessions and engagement behaviour |
| `transactions` | Transaction amounts, status, and fee revenue |
| `support_tickets` | Customer issues such as KYC, payment failure, and account access |

---

## Key Analyses

### 1. Onboarding Funnel

Funnel analysed:

```text
app_open → onboarding_started → kyc_submitted → kyc_approved → bank_added