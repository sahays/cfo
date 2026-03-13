# Use Cases: Gemini-Powered Cashflow Analysis

This app uses Gemini's reasoning capabilities to move beyond static charts into deep-dive anomaly detection and proactive remediation.

## Use Case 1: Real-Time Liquidity "Triangulation"
*   **The Problem:** Cash is fragmented across Banks, PayFlow, AppStore Central, and AR.
*   **Gemini Analysis:** Correlates `treasury_ledger` with `accounts_receivable` to find "Ghost Cash."
*   **Question Answered:** "How much of our 'Earned Revenue' is currently stuck in the App Store vs. Payment Gateways?"
*   **Remediation:** Gemini identifies the specific settlement delays and suggests moving high-volume regions to a direct-to-bank payment provider.

## Use Case 2: Content Production "Burn Variance"
*   **The Problem:** Original content often goes over budget, but finance only finds out 30 days later.
*   **Gemini Analysis:** Monitors `accounts_payable` and `content_metadata` to find spikes in vendor spending (CDN, Talent) that don't match the project's timeline.
*   **Question Answered:** "Which 'Original Series' are currently burning cash 20% faster than their estimated budget?"
*   **Remediation:** Gemini flags the specific vendor (e.g., a VFX house) causing the overrun and drafts a query for the Production Head.

## Use Case 3: "Silent Delay" Detection in Revenue
*   **The Problem:** Major ad agencies slowly drift their payment dates from Net-30 to Net-45 without notice.
*   **Gemini Analysis:** Compares `invoice_date` and `settlement_date` across the `accounts_receivable` history.
*   **Question Answered:** "Which agencies have increased their payment cycle over the last 6 months, and what is the impact on our monthly liquidity?"
*   **Remediation:** Gemini calculates the $ value of the float they are keeping and drafts a "Strict Net-30" enforcement notice for the Sales team.

## Use Case 4: Tax & Compliance Liability Forecasting
*   **The Problem:** CFOs often mistake "Cash in Bank" for "Spendable Cash," forgetting upcoming GST/VAT obligations.
*   **Gemini Analysis:** Aggregates `tax_amount` from all AR/AP records and matches them to regulatory payment dates.
*   **Question Answered:** "What is our net 'Spendable Cash' for next month after accounting for our quarterly tax liabilities?"
*   **Remediation:** Gemini suggests reserving a specific amount in a separate liquidity pool to ensure zero-day compliance.

## Use Case 5: Anomaly Deep-Dive (The "Why" Question)
*   **The Problem:** A sudden $500k dip in daily subscription revenue.
*   **Gemini Analysis:** Scans Gateway logs (`treasury_ledger`) for `FAILED` status codes or `FEE_ADJUSTMENT` spikes.
*   **Question Answered:** "Why did our cash inflow from South India drop by 15% yesterday?"
*   **Remediation:** Gemini identifies a technical failure in a specific bank's UPI gateway and suggests temporarily routing those transactions through an alternative provider.
