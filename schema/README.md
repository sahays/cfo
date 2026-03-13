# Enterprise Cashflow Schemas

This directory contains the production-grade JSON schemas for the AI-powered Cashflow Analysis system. These schemas are designed to handle the complexity of large media enterprises (e.g., StreamNova).

## Core Schemas

### 1. [Treasury Ledger](./treasury_ledger.json)
The "Ground Truth" for liquidity. It consolidates transactions from banks, payment gateways (PayFlow), and app stores (AppStore Central).
- **Key Features:** Gross vs. Net amount tracking, platform fee capture, and settlement status (Pending vs. Settled).

### 2. [Accounts Receivable (AR)](./accounts_receivable.json)
Tracks "Inflow Expectations" from advertisers and partners.
- **Key Features:** Contracted vs. historical payment days (Silent Delay detection), revenue stream categorization, and tax (GST/VAT) breakdown.

### 3. [Accounts Payable (AP)](./accounts_payable.json)
Tracks "Outflow Commitments" to vendors and production houses.
- **Key Features:** Project-level linking, spend categorization (VFX, Talent, Marketing), and early-payment discount tracking.

### 4. [Content Metadata](./content_metadata.json)
The dimensional "Secret Sauce" for the conversational interface.
- **Key Features:** Links financial records to creative attributes like Genre, Production Tier (Tentpole vs. Mid-budget), and Release Dates.

## Design Principles
- **Traceability:** Every record includes `source_system` and `version` for audit trails.
- **Reconciliation:** All financial schemas use `reconciliation_ref` and `project_code` as "glue" for cross-system analysis.
- **Global Ready:** Supports multi-currency with built-in `reporting_currency` conversion fields.
