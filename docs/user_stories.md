# User Stories: CFO Office (Advanced)

These stories represent the complex, "hard-problem" requirements for the AI-powered Cashflow Analysis app.

## 1. The CFO (Integrity & Anomaly Detection)
*   **Story:** "As the CFO, I want to ask, 'Have we made any duplicate payments to vendors in the last 6 months?' and have Gemini cross-reference multiple bank accounts and AP ledgers to find identical amounts paid to the same vendor twice, even if the invoice IDs were slightly different."
*   **Hard Problem:** Duplicate payment detection across fragmented systems.

## 2. VP of Finance (Operational Leakage)
*   **Story:** "As the VP of Finance, I want to ask, 'Show me all 'Mystery Leakage'—treasury outflows that don't map to any approved bill or project code' and receive a grouped list of bank fees, short-payments, and un-reconciled adjustments with suggested remediation."
*   **Hard Problem:** Identifying unmapped outflows and "ghost" fees.

## 3. Controller (Data Quality & Intelligent Ingestion)
*   **Story:** "As the Controller, I want to ask, 'How much of our data from the legacy ERP was automatically cleaned during ingestion?' and see a report of how Gemini mapped inconsistent vendor names (e.g., 'CPX' vs 'CloudProvider') and 'stitched' bank transactions to invoices that were missing reference numbers."
*   **Hard Problem:** Semantic entity resolution and missing-key reconciliation.

## 4. FP&A Lead (Predictive Burn & Overruns)
*   **Story:** "As the FP&A Lead, I want to ask, 'Which Tentpole productions are trending toward a 15% budget overrun based on their current weekly cash burn?' and get a breakdown of which specific spend categories (e.g., VFX vs. Talent) are driving the variance."
*   **Hard Problem:** Proactive budget overrun prediction in complex production environments.

## 5. Treasury Manager (Revenue Integrity)
*   **Story:** "As the Treasury Manager, I want to ask, 'Compare our contracted terms vs. actual collection dates for our top 5 ad agencies' and identify 'Silent Delays' where agencies are slowly drifting their payment windows to keep the float."
*   **Hard Problem:** Detecting subtle, non-notified shifts in payment behavior.

## 6. Global Tax Director (Liquidity Reserve)
*   **Story:** "As the Tax Director, I want to ask, 'What is our actual 'Net Spendable Cash' globally after subtracting GST/VAT liabilities due in the next 30 days?' and have Gemini verify the tax amounts extracted from inconsistent invoice formats."
*   **Hard Problem:** Real-time tax liability triangulation from gross cashflows.
