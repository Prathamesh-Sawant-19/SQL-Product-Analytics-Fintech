# Fintech Product Analytics (SQL Project)

## Overview
This project simulates a fintech product dataset and analyses user behaviour across onboarding, activation, revenue, and retention.

The goal is to identify key product bottlenecks and evaluate acquisition channel quality.

## Dataset
- 5,000 users
- 23k+ events
- 43k+ sessions
- 9k+ transactions

Generated using Python with realistic user behaviour patterns.

## Key Analyses

### 1. Onboarding Funnel
- 5000 → 3779 → 2929 users
- Major drop at KYC submission & approval

### 2. Activation Analysis
- Paid Ads: 58% (lowest)
- Referral: 76% (highest)

👉 Key issue: users drop after KYC but before first transaction

### 3. Revenue Analysis
- Referral: €14.80 per user (highest)
- Paid Ads: €9.48 per user (lowest)

### 4. Retention (Month 2)
- ~84–87% across channels (synthetic data bias)
- Organic shows strongest consistency

## Key Insight
The biggest problem is not retention — it is **activation**.

Users are acquired and verified but fail to reach their first transaction.

## Recommendations
- Improve post-KYC onboarding
- Add activation nudges (email/push)
- Optimize paid ads targeting
- Invest in referral & organic channels

## Tech Stack
- SQL (MySQL)
- Python (data generation)
- Excel (analysis)

## Project Structure
- `/data` → dataset
- `/queries` → SQL analysis
- `generate_fintech_data.py` → data generator# SQL-Product-Analytics-Fintech
SQL product analytics project analysing fintech onboarding, activation, revenue, retention, and acquisition channel quality using MySQL and Python-generated synthetic data.
