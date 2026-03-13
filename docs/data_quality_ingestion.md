# Intelligent Ingestion & Data Quality

Enterprise data is rarely "clean." This system employs a Gemini-powered ingestion layer to detect, cross-reference, and remediate quality issues before they reach the analysis engine.

## 1. Common Data "Pollutants"
*   **Missing Join Keys:** Bank statements missing Invoice IDs (reconciliation refs).
*   **Semantic Inconsistency:** "CloudProvider X" in AP vs. "CPX" in Treasury.
*   **Format Drift:** Inconsistent date formats (DD/MM vs MM/DD) or currency symbols.
*   **Truncated Metadata:** Payment memos that cut off the project code.

## 2. Gemini-Powered Remediation Logic

### A. The "Cross-Reference Glue"
*   **Scenario:** A treasury entry has no `reconciliation_ref`, but the `amount` and `counterparty` match an open invoice in the AR ledger.
*   **Gemini Action:** Perform fuzzy matching and temporal correlation (Date of payment vs. Date of invoice) to "stitch" the record.
*   **Output:** Flag as "Auto-Reconciled (95% Confidence)" and request human confirmation for the remaining 5%.

### B. Semantic Entity Resolution
*   **Scenario:** Multiple variations of vendor or project names across systems.
*   **Gemini Action:** Use LLM reasoning to map "StreamNova Originals - Season 2" and "SN_ORIG_S2_PROD" to the same `project_code` in `content_metadata.json`.

### C. Pattern-Based Imputation
*   **Scenario:** Missing `tax_amount` in an legacy AR system record.
*   **Gemini Action:** Calculate the missing value based on the `legal_entity` region, `base_amount`, and historical GST/VAT rates for that specific `revenue_stream`.

## 3. The Ingestion Pipeline Workflow

1.  **Scan & Profile:** Ingest raw data; identify nulls, outliers, and schema mismatches.
2.  **Reasoning Phase:** Gemini analyzes "Broken" records. It looks for clues in the `memo`, `counterparty`, and `historical_patterns`.
3.  **Remediation:** 
    *   **Success:** Records are auto-fixed and enriched with missing IDs.
    *   **Ambiguity:** Records are sent to a "Quality Quarantine" with a Gemini-generated explanation of *why* it can't be fixed (e.g., "Amount matches two separate invoices; please select").
4.  **Feedback Loop:** Once a human fixes a record, Gemini learns the mapping for future ingestion cycles.

## 4. Actionable Quality Metrics
*   **Match Rate:** % of treasury entries successfully linked to AR/AP.
*   **Imputation Accuracy:** % of auto-filled fields that pass secondary validation.
*   **Time-to-Clean:** Speed of moving data from "Raw" to "Analysis-Ready."
