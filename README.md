# FINAUDIT-KSA
### Intelligent Financial Audit Intelligence Platform — Kingdom of Saudi Arabia

> **Built for KSA auditors, finance professionals, and Big4/mid-tier candidates seeking to stand out in the competitive Saudi market.**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![SOCPA](https://img.shields.io/badge/SOCPA-Aligned-gold)
![IFRS](https://img.shields.io/badge/IFRS-Compliant-orange)

---

## What Makes This Unique

Most audit tools are generic. FINAUDIT-KSA is built specifically for the **Saudi regulatory and business environment**:

| Feature | What it does | Why it matters in KSA |
|---|---|---|
| **Benford's Law Engine** | Detects statistical fraud signals in GL data | Required by ISA 240 — rarely automated in KSA firms |
| **SOCPA/IFRS Checklist** | Sector-specific compliance per Saudi standards | Aligned with SOCPA pronouncements + IFRS as adopted in KSA |
| **GAZT / Zakat Notes** | Flags Zakat base and VAT reconciliation issues | Critical for all Saudi entities; often missed in generic tools |
| **Vision 2030 Sector Tags** | Tailored risk flags per sector (Giga-projects, Oil & Gas, etc.) | Directly relevant to NEOM, ROSHN, Aramco supply chain audits |
| **Anomaly Detection** | Multi-factor risk scoring: after-hours entries, round numbers, reversals | Addresses ISA 330 substantive testing requirements |
| **Auto Audit Memo** | Generates structured audit memo in seconds | Saves 2–4 hours per engagement; demo-able in interviews |
| **Preparer Risk Analysis** | Identifies which staff post anomalous entries | Supports segregation of duties review |
| **CSV Upload** | Works with real GL / Trial Balance data | Practical for live demos with real client data |

---

## Tech Stack

```
Python 3.12
Streamlit       — Web app framework
Pandas          — Data wrangling
NumPy           — Statistical computations
Plotly          — Interactive charts (Benford, radar, timeline, histogram)
```

Zero heavy ML dependencies. Runs instantly on Streamlit Cloud free tier.

---

## Audit Methodology

### 1. Composite Risk Score (0–100)
Weighted across five factors:

```
Score = Σ(
    Transaction Anomalies    × 0.40,
    After-Hours Entries      × 0.20,
    Round Number Concentration × 0.15,
    Reversal Frequency       × 0.15,
    Benford Law Deviation    × 0.10
)
```

### 2. Benford's Law Analysis
Tests the leading-digit distribution of all transaction amounts against the expected Benford distribution using Chi-squared statistic. Significant deviation (χ² > 5) triggers a fraud risk flag per **ISA 240**.

### 3. IFRS / SOCPA Compliance Checklist
Sector-aware checklist covering:
- **SOCPA 1, 3, 7, 9, 15** — Core Saudi accounting standards
- **IFRS 9, 15, 16** — Expected Credit Loss, Revenue, Leases
- **IAS 36, 37, 39** — Impairment, Provisions, Financial Instruments
- **Basel III** — For Banking & Finance sector
- **GAZT** — Zakat base, VAT, Transfer Pricing rules

### 4. After-Hours Entry Detection
Flags journal entries posted between 20:00–07:00, a key indicator of management override per **ISA 240.A3**.

### 5. Auto Audit Memo
Structured memo output aligned with ISA memo format, including:
- Risk rating and findings
- Zakat/tax considerations
- Vision 2030 alignment flags
- Management recommendations

---

## Quick Start

### Local
```bash
git clone https://github.com/YOUR_USERNAME/finaudit-ksa.git
cd finaudit-ksa
pip install -r requirements.txt
streamlit run app.py
```

### Streamlit Cloud (Free)
1. Fork this repo
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Deploy → select `app.py`
4. Live in 2 minutes

---

## How to Use

1. **Enter entity name and sector** in the left sidebar
2. **Upload your own GL / Trial Balance CSV** (optional) or use synthetic data
3. **Select modules** to run (Benford, Anomaly, Compliance, Memo)
4. Hit **RUN AUDIT** — results appear instantly across 5 tabs:
   - `Risk Overview` — Radar chart + risk factor breakdown
   - `Anomaly Detection` — Benford chart + flagged entries
   - `IFRS/SOCPA Compliance` — Full checklist with pass/fail
   - `GL Analytics` — Monthly trends, account breakdown, distribution
   - `Audit Memo` — Auto-generated memo ready to download

### CSV Upload Format
Your file should have at minimum:
```csv
Date,Amount_SAR,Account_Name,Description,Debit_Credit,Preparer
2024-01-15,125000.00,Revenue,Contract revenue,Cr,Ahmad Al-Harbi
```

---

## Sectors Supported

- Oil & Gas
- Banking & Finance
- Real Estate
- Construction
- Retail & FMCG
- Healthcare
- Telecom
- Manufacturing
- **Vision 2030 Giga-Projects** (NEOM, ROSHN, Qiddiya)
- Government Entities

---

## KSA Regulatory Coverage

| Regulation | Coverage |
|---|---|
| SOCPA Standards | Full checklist for all 10 core standards |
| IFRS (as adopted in KSA) | IFRS 9, 15, 16 + IAS 36, 37 |
| GAZT Zakat Rules | Zakat base flags, VAT reconciliation, Transfer Pricing |
| ISA 240 / 315 / 330 | Fraud risk, internal control, substantive testing alignment |
| Nitaqat (Saudization) | Payroll compliance flag |
| CMA ESG Circular | Disclosure readiness flag |

---

## Why This Beats Generic Audit Tools

**Generic tools**: CSV → pivot table → export. No intelligence.

**FINAUDIT-KSA**:
- Statistical fraud detection (Benford) — not just filters
- KSA-specific regulatory flags (GAZT, SOCPA, Zakat)
- Sector intelligence (Giga-projects ≠ Banking ≠ Oil & Gas)
- AI-ready architecture (plug in Claude/GPT for narrative generation)
- Interview-ready: live demo in 30 seconds, zero setup

---

## Roadmap

- [ ] LLM-powered audit narrative (Claude API integration)
- [ ] Arabic language UI (`ar` locale)
- [ ] SAP / Oracle GL direct connector
- [ ] GAZT e-invoice reconciliation module
- [ ] CAAT (Computer Assisted Audit Techniques) full suite
- [ ] Streamlit multi-page with user authentication

---

## Author

Built as a portfolio project for KSA audit / finance roles.
Demonstrates: Python, financial audit methodology, IFRS/SOCPA knowledge, data analytics, and KSA regulatory awareness.

**Stack:** Python · Streamlit · Pandas · NumPy · Plotly · Statistical Methods

---

## License

MIT — free to use, fork, and extend.

---

*FINAUDIT-KSA is a portfolio/analytical tool. Outputs are for indicative purposes and must be validated by a licensed SOCPA Chartered Accountant before use as an official audit opinion.*
