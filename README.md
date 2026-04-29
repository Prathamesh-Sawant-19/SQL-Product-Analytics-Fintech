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

| Table | Purpose |
|---|---|
| `users` | User profile, signup date, acquisition channel, country, device, KYC status |
| `events` | Product actions such as app open, onboarding started, KYC submitted, KYC approved, bank added, and first transaction |
| `sessions` | App usage sessions and engagement behaviour |
| `transactions` | Transaction amounts, transaction status, and fee revenue |
| `support_tickets` | Customer issues such as KYC, payment failure, and account access |

---

## Key Analyses

### 1. Onboarding Funnel

Funnel analysed:

app_open → onboarding_started → kyc_submitted → kyc_approved → bank_added

| Funnel Step | Users |
|---|---:|
| App opened | 5,000 |
| Onboarding started | 5,000 |
| KYC submitted | 3,779 |
| KYC approved | 2,929 |
| Bank added | 2,929 |

Main finding:

The largest drop occurred before KYC submission, suggesting friction, trust concerns, or lower user intent at the KYC stage.

There was also a meaningful drop between KYC submission and KYC approval, which may indicate document quality issues, failed verification, or eligibility-related problems.

---

### 2. Acquisition Channel Quality

| Channel | KYC Submission Rate | KYC Approval Rate |
|---|---:|---:|
| Referral | 78.57% | 81.24% |
| Affiliate | 75.73% | 78.11% |
| Organic | 74.81% | 77.44% |
| Paid Ads | 73.77% | 73.97% |

Main finding:

Referral users showed the strongest intent and trust, while paid ads generated volume but lower-quality conversion.

This suggests paid ads users may need better targeting or stronger trust-building before entering the KYC flow.

---

### 3. Activation Analysis

Activation was defined as users who completed a first successful transaction after KYC approval.

| Channel | KYC Approved Users | Activated Users | Activation Rate |
|---|---:|---:|---:|
| Referral | 801 | 615 | 76.78% |
| Organic | 858 | 628 | 73.19% |
| Affiliate | 446 | 301 | 67.49% |
| Paid Ads | 824 | 478 | 58.01% |

Main finding:

Paid ads had the largest post-KYC activation gap. Out of 824 KYC-approved paid ads users, only 478 completed a first successful transaction.

That means **346 paid ads users passed KYC but did not activate**, making this the strongest opportunity for product improvement.

---

### 4. Revenue Analysis

| Channel | Transacting Users | Total Revenue | Revenue per User |
|---|---:|---:|---:|
| Referral | 615 | €18,578.51 | €14.80 |
| Organic | 628 | €18,439.36 | €12.45 |
| Paid Ads | 478 | €14,310.21 | €9.48 |
| Affiliate | 301 | €8,277.23 | €10.98 |

Main finding:

Referral produced the highest revenue per user, while paid ads produced the lowest revenue per user.

This confirms that acquisition volume alone is not enough. Channel quality matters more than raw user count.

---

### 5. Month-2 Retention

Retention was measured as whether users had a session between day 30 and day 60 after signup.

| Channel | Total Users | Month-2 Retained Users | Month-2 Retention Rate |
|---|---:|---:|---:|
| Organic | 1,481 | 1,284 | 86.70% |
| Referral | 1,255 | 1,086 | 86.53% |
| Paid Ads | 1,510 | 1,303 | 86.29% |
| Affiliate | 754 | 636 | 84.35% |

Main finding:

Retention was relatively similar across channels, meaning the main performance gap was not retention.

The bigger issue was activation and revenue conversion before users reached long-term engagement.

Note: Because this is synthetic data, retention rates are higher than expected real-world fintech benchmarks. This limitation is acknowledged in the analysis.

---

## Final Business Insight

The product’s biggest issue is **activation leakage after KYC**, not user retention.

Paid ads generated high user volume, but those users had the weakest activation rate and lowest revenue per user. This suggests paid ads users were either lower intent or needed stronger post-KYC guidance before making their first transaction.

Referral was the strongest channel overall, performing best across activation and revenue per user.

Organic was also strong, showing high activated user volume and the strongest Month-2 retention.

---

## Recommendations

### 1. Improve post-KYC activation

- Add guided first-transaction flows
- Send push/email nudges within 24–72 hours after KYC approval
- Test first-transaction incentives such as fee waivers or cashback

### 2. Improve paid ads targeting

- Shift from broad targeting to higher-intent segments
- Retarget users who already showed fintech interest
- Align ad messaging with the product’s actual value proposition

### 3. Scale referral and organic growth

- Build a structured referral programme
- Invest in SEO, content, and app store optimisation
- Use trust-led messaging to attract higher-intent users

---

## Tech Stack

- MySQL
- SQL
- Python
- VS Code
- CSV
- GitHub

---

## Skills Demonstrated

- SQL joins
- CTEs
- Aggregations
- CASE WHEN logic
- Funnel analysis
- Activation analysis
- Revenue analysis
- Retention analysis
- Acquisition channel segmentation
- Synthetic data generation
- Data validation
- Business insight generation

---

## Project Structure

```text
.
├── README.md
├── generate_fintech_data.py
├── generate_users_insert_sql.py
├── insert_users.sql
├── users.csv
├── events.csv
├── sessions.csv
├── transactions.csv
└── support_tickets.csv
```

---

## Summary

This project demonstrates how SQL can be used to move beyond basic reporting and support product decision-making.

The key takeaway is that acquisition volume alone is not enough — the real value comes from identifying which users activate, transact, retain, and generate revenue.