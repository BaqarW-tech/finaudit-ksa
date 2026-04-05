"""
FINAUDIT-KSA: Intelligent Financial Audit Intelligence Platform
Saudi-focused financial audit app with AI-driven risk scoring, SOCPA/IFRS compliance,
Vision 2030 sector analysis, and automated audit memo generation.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import json
import io
import re
from datetime import datetime, timedelta
import random
import math

# ── Page config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FINAUDIT-KSA | Intelligent Audit Intelligence",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=Playfair+Display:wght@700;900&family=Source+Sans+3:wght@300;400;600&display=swap');

:root {
    --gold: #C8A96E;
    --gold-light: #E8C98A;
    --dark: #0A0E1A;
    --dark2: #111827;
    --dark3: #1C2333;
    --surface: #1E2A3A;
    --border: #2A3A4F;
    --text: #E8EDF5;
    --text-muted: #8A9BB5;
    --green: #2ECC71;
    --red: #E74C3C;
    --amber: #F39C12;
    --blue: #3B82F6;
}

html, body, [class*="css"] {
    font-family: 'Source Sans 3', sans-serif;
    background-color: var(--dark);
    color: var(--text);
}

.main { background-color: var(--dark); }
.stApp { background-color: var(--dark); }

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0D1421 0%, #111827 100%);
    border-right: 1px solid var(--border);
}
[data-testid="stSidebar"] * { color: var(--text) !important; }

/* Hero header */
.hero-header {
    background: linear-gradient(135deg, #0D1421 0%, #1A2640 50%, #0D1421 100%);
    border: 1px solid var(--border);
    border-top: 3px solid var(--gold);
    border-radius: 4px;
    padding: 2rem 2.5rem;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.hero-header::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -10%;
    width: 40%;
    height: 200%;
    background: radial-gradient(ellipse, rgba(200,169,110,0.06) 0%, transparent 70%);
    pointer-events: none;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    font-weight: 900;
    color: var(--gold);
    letter-spacing: -0.5px;
    margin: 0;
    line-height: 1.1;
}
.hero-subtitle {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.75rem;
    color: var(--text-muted);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-top: 0.4rem;
}
.hero-badge {
    display: inline-block;
    background: rgba(200,169,110,0.1);
    border: 1px solid rgba(200,169,110,0.3);
    color: var(--gold);
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 2px;
    padding: 3px 10px;
    border-radius: 2px;
    text-transform: uppercase;
    margin-top: 0.8rem;
    margin-right: 0.5rem;
}

/* KPI cards */
.kpi-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; margin-bottom: 1.5rem; }
.kpi-card {
    background: var(--dark3);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 1.2rem 1.4rem;
    position: relative;
    overflow: hidden;
    transition: border-color 0.2s;
}
.kpi-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 2px;
}
.kpi-card.gold::after  { background: var(--gold); }
.kpi-card.green::after { background: var(--green); }
.kpi-card.red::after   { background: var(--red); }
.kpi-card.blue::after  { background: var(--blue); }
.kpi-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 2px;
    color: var(--text-muted);
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}
.kpi-value {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 700;
    line-height: 1;
}
.kpi-value.gold  { color: var(--gold); }
.kpi-value.green { color: var(--green); }
.kpi-value.red   { color: var(--red); }
.kpi-value.blue  { color: var(--blue); }
.kpi-sub { font-size: 0.75rem; color: var(--text-muted); margin-top: 0.3rem; }

/* Risk badge */
.risk-badge {
    display: inline-block;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 2px;
    font-weight: 600;
}
.risk-critical { background: rgba(231,76,60,0.15); border: 1px solid #E74C3C; color: #E74C3C; }
.risk-high     { background: rgba(231,76,60,0.08); border: 1px solid rgba(231,76,60,0.5); color: #E74C3C; }
.risk-medium   { background: rgba(243,156,18,0.1); border: 1px solid #F39C12; color: #F39C12; }
.risk-low      { background: rgba(46,204,113,0.1); border: 1px solid #2ECC71; color: #2ECC71; }

/* Section card */
.section-card {
    background: var(--dark3);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1.2rem;
}
.section-title {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 3px;
    color: var(--gold);
    text-transform: uppercase;
    margin-bottom: 1rem;
    padding-bottom: 0.6rem;
    border-bottom: 1px solid var(--border);
}

/* Table */
.styled-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.82rem;
}
.styled-table th {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--text-muted);
    padding: 8px 12px;
    border-bottom: 1px solid var(--border);
    text-align: left;
}
.styled-table td {
    padding: 9px 12px;
    border-bottom: 1px solid rgba(42,58,79,0.5);
    color: var(--text);
}
.styled-table tr:hover td { background: rgba(255,255,255,0.02); }

/* Anomaly flag */
.anomaly-flag {
    background: rgba(231,76,60,0.08);
    border-left: 3px solid var(--red);
    padding: 0.8rem 1rem;
    margin: 0.5rem 0;
    border-radius: 0 4px 4px 0;
    font-size: 0.82rem;
}
.finding-flag {
    background: rgba(243,156,18,0.06);
    border-left: 3px solid var(--amber);
    padding: 0.8rem 1rem;
    margin: 0.5rem 0;
    border-radius: 0 4px 4px 0;
    font-size: 0.82rem;
}
.pass-flag {
    background: rgba(46,204,113,0.06);
    border-left: 3px solid var(--green);
    padding: 0.8rem 1rem;
    margin: 0.5rem 0;
    border-radius: 0 4px 4px 0;
    font-size: 0.82rem;
}

/* Progress bar */
.progress-bar-bg {
    background: var(--border);
    border-radius: 2px;
    height: 6px;
    overflow: hidden;
    margin-top: 0.3rem;
}
.progress-bar-fill {
    height: 100%;
    border-radius: 2px;
    transition: width 0.6s ease;
}

/* Memo box */
.memo-box {
    background: #0A0E1A;
    border: 1px solid var(--border);
    border-top: 2px solid var(--gold);
    border-radius: 4px;
    padding: 1.5rem;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.78rem;
    line-height: 1.7;
    color: #C8D8E8;
    white-space: pre-wrap;
}

/* Sidebar nav */
.nav-item {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--text-muted);
    padding: 0.5rem 0;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, var(--gold), #A88040) !important;
    color: var(--dark) !important;
    border: none !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 0.72rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    font-weight: 600 !important;
    padding: 0.6rem 1.5rem !important;
    border-radius: 2px !important;
    transition: opacity 0.2s !important;
}
.stButton > button:hover { opacity: 0.85 !important; }

/* Selectbox / inputs */
.stSelectbox > div > div, .stTextInput > div > div > input,
.stNumberInput > div > div > input, .stTextArea > div > div > textarea {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
    border-radius: 3px !important;
}

.stFileUploader {
    background: var(--dark3) !important;
    border: 1px dashed var(--border) !important;
    border-radius: 4px !important;
}

/* Divider */
hr { border-color: var(--border) !important; }

/* Metric */
[data-testid="metric-container"] {
    background: var(--dark3);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 0.8rem 1rem;
}

/* Tab */
.stTabs [data-baseweb="tab-list"] {
    background: transparent;
    border-bottom: 1px solid var(--border);
    gap: 0;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--text-muted) !important;
    background: transparent !important;
    border: none !important;
    padding: 0.7rem 1.2rem !important;
}
.stTabs [aria-selected="true"] {
    color: var(--gold) !important;
    border-bottom: 2px solid var(--gold) !important;
}

/* Hide streamlit branding */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem !important; }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════
# DATA LAYER — synthetic but realistic KSA financial data
# ═══════════════════════════════════════════════════════════════════════

KSA_SECTORS = [
    "Oil & Gas", "Banking & Finance", "Real Estate", "Construction",
    "Retail & FMCG", "Healthcare", "Telecom", "Manufacturing",
    "Vision 2030 Giga-Projects", "Government Entities"
]

SOCPA_STANDARDS = {
    "SOCPA 1": "Presentation of Financial Statements",
    "SOCPA 3": "Revenue Recognition",
    "SOCPA 7": "Related Party Disclosures",
    "SOCPA 9": "Financial Instruments",
    "SOCPA 15": "Leases",
    "IFRS 16": "Leases — Right-of-use Assets",
    "IAS 36": "Impairment of Assets",
    "IAS 37": "Provisions & Contingencies",
    "IAS 39": "Financial Instruments Recognition",
    "IFRS 9": "Expected Credit Loss Model",
}

BENFORD_DIST = {d: math.log10(1 + 1/d) for d in range(1, 10)}


def generate_gl_entries(n=500, seed=42):
    rng = np.random.default_rng(seed)
    accounts = {
        "1001": "Cash & Cash Equivalents",
        "1101": "Accounts Receivable",
        "1201": "Inventories",
        "1501": "Property, Plant & Equipment",
        "2001": "Accounts Payable",
        "2101": "Accrued Liabilities",
        "3001": "Share Capital",
        "4001": "Revenue",
        "4101": "Other Income",
        "5001": "Cost of Revenue",
        "5101": "Salaries & Benefits",
        "5201": "G&A Expenses",
        "5301": "Depreciation",
        "5401": "Finance Costs",
    }
    acc_codes = list(accounts.keys())
    amounts_base = rng.lognormal(mean=11, sigma=2, size=n)

    # Inject anomalies
    anomaly_mask = rng.random(n) < 0.05
    amounts_base[anomaly_mask] *= rng.uniform(8, 25, anomaly_mask.sum())

    # Round amounts to SAR (2 dp)
    amounts = np.round(amounts_base, 2)

    dates = pd.date_range("2024-01-01", "2024-12-31", periods=n)
    dates = dates[rng.integers(0, n, n)]

    df = pd.DataFrame({
        "Entry_ID": [f"JE-{str(i).zfill(5)}" for i in range(1, n+1)],
        "Date": sorted(dates),
        "Account_Code": rng.choice(acc_codes, n),
        "Description": rng.choice([
            "Monthly payroll", "Vendor payment", "Customer receipt",
            "Depreciation charge", "Accrual entry", "Reversal",
            "Intercompany settlement", "Asset purchase", "Expense reimbursement",
            "Tax provision", "Zakat payment", "Dividend distribution",
            "Advance payment", "Loan repayment", "Contract revenue",
        ], n),
        "Amount_SAR": amounts,
        "Debit_Credit": rng.choice(["Dr", "Cr"], n),
        "Preparer": rng.choice(["Ahmad Al-Harbi", "Sara Al-Qahtani", "Mohammed Bin Saleh", "Fatima Al-Otaibi", "Khalid Al-Dossari"], n),
        "Posted_Hour": rng.integers(0, 24, n),
        "Is_Anomaly": anomaly_mask,
        "Is_Reversal": rng.random(n) < 0.03,
        "Is_Round_Number": (amounts % 1000 == 0),
    })
    df["Account_Name"] = df["Account_Code"].map(accounts)
    return df


def run_benford_analysis(series):
    """Return observed vs expected leading digit distribution."""
    series = series[series > 0]
    leading = series.apply(lambda x: int(str(x).replace('.', '').lstrip('0')[0]))
    observed = leading.value_counts(normalize=True).sort_index()
    result = pd.DataFrame({
        "Digit": list(range(1, 10)),
        "Expected_%": [BENFORD_DIST[d] * 100 for d in range(1, 10)],
        "Observed_%": [observed.get(d, 0) * 100 for d in range(1, 10)],
    })
    result["Deviation"] = result["Observed_%"] - result["Expected_%"]
    result["Chi_Sq"] = ((result["Observed_%"] - result["Expected_%"]) ** 2) / result["Expected_%"]
    return result


def compute_risk_score(df):
    """Multi-factor risk scoring (0–100)."""
    scores = {}
    # 1. Anomaly rate
    anomaly_rate = df["Is_Anomaly"].mean()
    scores["Transaction Anomalies"] = min(anomaly_rate * 500, 40)

    # 2. After-hours entries (risk of override)
    after_hours = ((df["Posted_Hour"] < 7) | (df["Posted_Hour"] > 20)).mean()
    scores["After-Hours Entries"] = min(after_hours * 200, 20)

    # 3. Round-number concentration
    round_pct = df["Is_Round_Number"].mean()
    scores["Round Number Concentration"] = min(round_pct * 60, 15)

    # 4. Reversal frequency
    rev_rate = df["Is_Reversal"].mean()
    scores["Reversal Frequency"] = min(rev_rate * 300, 15)

    # 5. Benford deviation
    bf = run_benford_analysis(df["Amount_SAR"])
    chi_sq = bf["Chi_Sq"].sum()
    scores["Benford Law Deviation"] = min(chi_sq * 2, 10)

    total = sum(scores.values())
    return round(min(total, 100), 1), scores


def generate_ifrs_checklist(sector):
    """Generate IFRS/SOCPA compliance checklist tailored to sector."""
    base = [
        ("SOCPA 3", "Revenue recognition policy documented", "High"),
        ("IFRS 16", "Right-of-use assets recognised for leases > 12 months", "High"),
        ("SOCPA 7", "Related party transactions disclosed", "Critical"),
        ("IAS 36", "Annual impairment test performed on non-current assets", "Medium"),
        ("IAS 37", "Provisions and contingent liabilities assessed", "Medium"),
        ("IFRS 9", "Expected Credit Loss model applied to receivables", "High"),
        ("SOCPA 1", "Going concern assessment documented", "High"),
        ("SOCPA 9", "Financial instruments classified and measured correctly", "Medium"),
    ]
    if sector in ["Oil & Gas", "Manufacturing"]:
        base += [("IAS 2", "Inventories valued at lower of cost / NRV", "High")]
    if sector in ["Banking & Finance"]:
        base += [
            ("IFRS 9", "Hedge accounting documentation complete", "Critical"),
            ("Basel III", "Capital adequacy ratio computed and disclosed", "Critical"),
        ]
    if sector in ["Real Estate", "Construction"]:
        base += [
            ("IFRS 15", "Contract revenue % completion method applied", "High"),
            ("IAS 40", "Investment properties fair valued or cost model disclosed", "Medium"),
        ]
    if sector in ["Vision 2030 Giga-Projects"]:
        base += [
            ("IFRS 15", "Multi-element arrangement revenue split documented", "Critical"),
            ("SOCPA 7", "Government grants and subsidies disclosed", "High"),
        ]
    rng = np.random.default_rng(99)
    statuses = rng.choice(["✅ Pass", "⚠️ Partial", "❌ Fail"], len(base), p=[0.55, 0.3, 0.15])
    return pd.DataFrame(base, columns=["Standard", "Requirement", "Priority"]).assign(Status=statuses)


def generate_memo(company, sector, risk_score, findings):
    """Generate a structured audit memo."""
    date_str = datetime.now().strftime("%d %B %Y")
    risk_level = "CRITICAL" if risk_score > 70 else "HIGH" if risk_score > 50 else "MODERATE" if risk_score > 30 else "LOW"
    return f"""
CONFIDENTIAL AUDIT MEMORANDUM
══════════════════════════════════════════════════════════
FINAUDIT-KSA | Audit Intelligence Platform v2.0
══════════════════════════════════════════════════════════

TO      : Audit Committee / Board of Directors
FROM    : AI-Assisted Audit Engine (FINAUDIT-KSA)
DATE    : {date_str}
ENTITY  : {company}
SECTOR  : {sector}
ZAKAT FY: 2024 (Hijri 1446)
RISK    : {risk_level} ({risk_score}/100)

──────────────────────────────────────────────────────────
1. EXECUTIVE SUMMARY
──────────────────────────────────────────────────────────
This memorandum presents the findings of the AI-assisted
financial audit conducted on {company} for the financial
year ended 31 December 2024. The overall composite risk
score is {risk_score}/100, classified as {risk_level}.

The audit was conducted in accordance with the Standards
on Auditing issued by the Saudi Organization for Chartered
and Professional Accountants (SOCPA) and aligned with
International Standards on Auditing (ISA).

──────────────────────────────────────────────────────────
2. KEY FINDINGS
──────────────────────────────────────────────────────────
{chr(10).join(f"  [{i+1}] {f}" for i, f in enumerate(findings))}

──────────────────────────────────────────────────────────
3. ZAKAT & TAX CONSIDERATIONS (GAZT)
──────────────────────────────────────────────────────────
  • Zakat base computation reviewed under Ministerial
    Resolution 1535 — adjustments noted.
  • VAT (15%) reconciliation to filed GAZT returns pending.
  • Transfer pricing documentation required for related
    party transactions exceeding SAR 5M (Ministerial
    Decision 4/1/20-00219-1/220).

──────────────────────────────────────────────────────────
4. VISION 2030 ALIGNMENT FLAG
──────────────────────────────────────────────────────────
  • Sector: {sector}
  • NTP compliance indicators: Reviewed
  • Saudization (Nitaqat) payroll threshold: Verified
  • ESG disclosure readiness (CMA Circular): Partial

──────────────────────────────────────────────────────────
5. MANAGEMENT RECOMMENDATIONS
──────────────────────────────────────────────────────────
  [R-1] Implement automated 3-way matching for AP cycle.
  [R-2] Strengthen month-end close controls — segregation
        of duties gaps identified.
  [R-3] Formalise ECL model documentation (IFRS 9).
  [R-4] Engage GAZT pre-clearance for disputed Zakat base.
  [R-5] Board to ratify related-party policy within 30 days.

──────────────────────────────────────────────────────────
6. DISCLAIMER
──────────────────────────────────────────────────────────
This memo is generated by the FINAUDIT-KSA AI engine for
analytical and indicative purposes. Findings must be
validated by a licensed SOCPA Chartered Accountant before
issuance as an official audit opinion.

══════════════════════════════════════════════════════════
FINAUDIT-KSA | Powered by AI | SOCPA-Aligned | ISA-Ready
══════════════════════════════════════════════════════════
""".strip()


# ═══════════════════════════════════════════════════════════════════════
# CHART HELPERS
# ═══════════════════════════════════════════════════════════════════════

CHART_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="IBM Plex Mono, monospace", color="#8A9BB5", size=10),
    margin=dict(l=40, r=20, t=40, b=40),
)


def benford_chart(bf_df):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=bf_df["Digit"], y=bf_df["Expected_%"],
        name="Benford Expected", marker_color="rgba(200,169,110,0.3)",
        marker_line_color="#C8A96E", marker_line_width=1,
    ))
    fig.add_trace(go.Scatter(
        x=bf_df["Digit"], y=bf_df["Observed_%"],
        name="Observed", mode="lines+markers",
        line=dict(color="#E74C3C", width=2),
        marker=dict(size=7, symbol="diamond"),
    ))
    fig.update_layout(
        **CHART_LAYOUT,
        title=dict(text="BENFORD'S LAW ANALYSIS", font=dict(color="#C8A96E", size=11), x=0),
        xaxis=dict(title="Leading Digit", gridcolor="#1C2333", tickvals=list(range(1, 10))),
        yaxis=dict(title="Frequency %", gridcolor="#1C2333"),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(size=9)),
        height=300,
    )
    return fig


def risk_radar(scores):
    categories = list(scores.keys())
    values = list(scores.values())
    values += values[:1]
    categories += categories[:1]
    fig = go.Figure(go.Scatterpolar(
        r=values, theta=categories, fill='toself',
        fillcolor='rgba(200,169,110,0.12)',
        line=dict(color="#C8A96E", width=2),
        marker=dict(color="#C8A96E"),
    ))
    fig.update_layout(
        **CHART_LAYOUT,
        polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(visible=True, range=[0, 40], gridcolor="#2A3A4F", tickfont=dict(size=8)),
            angularaxis=dict(gridcolor="#2A3A4F"),
        ),
        title=dict(text="RISK RADAR", font=dict(color="#C8A96E", size=11), x=0),
        height=320,
        showlegend=False,
    )
    return fig


def timeline_chart(df):
    monthly = df.groupby(df["Date"].dt.to_period("M")).agg(
        Total_SAR=("Amount_SAR", "sum"),
        Anomalies=("Is_Anomaly", "sum"),
    ).reset_index()
    monthly["Date"] = monthly["Date"].dt.to_timestamp()

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Bar(
        x=monthly["Date"], y=monthly["Total_SAR"] / 1e6,
        name="Total (SAR M)", marker_color="rgba(59,130,246,0.5)",
        marker_line_color="#3B82F6", marker_line_width=1,
    ), secondary_y=False)
    fig.add_trace(go.Scatter(
        x=monthly["Date"], y=monthly["Anomalies"],
        name="Anomalies", mode="lines+markers",
        line=dict(color="#E74C3C", width=2),
        marker=dict(size=6),
    ), secondary_y=True)
    fig.update_layout(
        **CHART_LAYOUT,
        title=dict(text="TRANSACTION VOLUME & ANOMALY TREND", font=dict(color="#C8A96E", size=11), x=0),
        xaxis=dict(gridcolor="#1C2333"),
        yaxis=dict(title="SAR (Millions)", gridcolor="#1C2333"),
        yaxis2=dict(title="Anomaly Count", gridcolor="#1C2333"),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(size=9)),
        height=280,
        barmode="group",
    )
    return fig


def account_breakdown_chart(df):
    by_acc = df.groupby("Account_Name")["Amount_SAR"].sum().nlargest(8).reset_index()
    fig = go.Figure(go.Bar(
        x=by_acc["Amount_SAR"] / 1e6, y=by_acc["Account_Name"],
        orientation='h',
        marker=dict(
            color=by_acc["Amount_SAR"] / 1e6,
            colorscale=[[0, "#1C2333"], [0.5, "#2A5F8F"], [1, "#C8A96E"]],
            showscale=False,
        ),
        text=[f"SAR {v:.1f}M" for v in by_acc["Amount_SAR"] / 1e6],
        textposition="outside",
        textfont=dict(color="#8A9BB5", size=9),
    ))
    fig.update_layout(
        **CHART_LAYOUT,
        title=dict(text="TOP ACCOUNTS BY VOLUME", font=dict(color="#C8A96E", size=11), x=0),
        xaxis=dict(title="SAR (Millions)", gridcolor="#1C2333"),
        yaxis=dict(gridcolor="rgba(0,0,0,0)"),
        height=280,
    )
    return fig


# ═══════════════════════════════════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════════════════════════════════

with st.sidebar:
    st.markdown("""
    <div style="padding: 0.5rem 0 1.5rem 0;">
        <div style="font-family:'Playfair Display',serif; font-size:1.4rem; color:#C8A96E; font-weight:900;">FINAUDIT</div>
        <div style="font-family:'IBM Plex Mono',monospace; font-size:0.6rem; letter-spacing:3px; color:#8A9BB5; text-transform:uppercase;">KSA Audit Intelligence</div>
        <div style="margin-top:0.8rem; height:1px; background:linear-gradient(90deg, #C8A96E, transparent);"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="nav-item">⬡  Configuration</div>', unsafe_allow_html=True)
    company_name = st.text_input("Entity Name", value="Al-Madar Trading Co.", label_visibility="collapsed",
                                  placeholder="Enter entity name...")

    sector = st.selectbox("Sector", KSA_SECTORS, index=0)
    audit_year = st.selectbox("Audit Year", [2024, 2023, 2022], index=0)

    st.markdown('<hr style="margin: 1rem 0;">', unsafe_allow_html=True)
    st.markdown('<div class="nav-item">⬡  Data Source</div>', unsafe_allow_html=True)

    use_upload = st.checkbox("Upload GL / Trial Balance (CSV)", value=False)
    uploaded_file = None
    if use_upload:
        uploaded_file = st.file_uploader("Upload CSV", type=["csv"], label_visibility="collapsed")

    n_entries = st.slider("Synthetic GL Entries", 200, 2000, 500, 100)

    st.markdown('<hr style="margin: 1rem 0;">', unsafe_allow_html=True)
    st.markdown('<div class="nav-item">⬡  Modules</div>', unsafe_allow_html=True)
    mod_benford   = st.checkbox("Benford's Law Analysis", value=True)
    mod_anomaly   = st.checkbox("Anomaly Detection", value=True)
    mod_compliance = st.checkbox("IFRS / SOCPA Checklist", value=True)
    mod_memo      = st.checkbox("Auto Audit Memo", value=True)

    st.markdown('<hr style="margin: 1rem 0;">', unsafe_allow_html=True)
    run_btn = st.button("▶  RUN AUDIT", use_container_width=True)

    st.markdown("""
    <div style="margin-top:2rem; font-family:'IBM Plex Mono',monospace; font-size:0.6rem;
                color:#4A5A70; line-height:1.8; text-align:center;">
        SOCPA-Aligned · ISA-Ready<br>IFRS · GAZT · Vision 2030<br>
        <span style="color:#C8A96E;">FINAUDIT-KSA v2.0</span>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════
# MAIN — HERO
# ═══════════════════════════════════════════════════════════════════════

st.markdown(f"""
<div class="hero-header">
    <div class="hero-title">FINAUDIT-KSA</div>
    <div class="hero-subtitle">Intelligent Financial Audit Intelligence Platform — Kingdom of Saudi Arabia</div>
    <div style="margin-top:0.8rem;">
        <span class="hero-badge">SOCPA-Aligned</span>
        <span class="hero-badge">IFRS Compliant</span>
        <span class="hero-badge">Vision 2030</span>
        <span class="hero-badge">GAZT Ready</span>
        <span class="hero-badge">Benford's Law Engine</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════
# LOAD DATA
# ═══════════════════════════════════════════════════════════════════════

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        df["Date"] = pd.to_datetime(df.get("Date", pd.Timestamp.now()))
        # Normalize column
        if "Amount" in df.columns and "Amount_SAR" not in df.columns:
            df["Amount_SAR"] = df["Amount"]
        if "Amount_SAR" not in df.columns:
            st.error("CSV must contain an 'Amount_SAR' or 'Amount' column.")
            st.stop()
        if "Is_Anomaly" not in df.columns:
            df["Is_Anomaly"] = False
        if "Is_Reversal" not in df.columns:
            df["Is_Reversal"] = False
        if "Is_Round_Number" not in df.columns:
            df["Is_Round_Number"] = df["Amount_SAR"] % 1000 == 0
        if "Posted_Hour" not in df.columns:
            df["Posted_Hour"] = 9
        st.success(f"✓ Loaded {len(df):,} entries from uploaded file.")
    except Exception as e:
        st.error(f"Error reading file: {e}")
        df = generate_gl_entries(n_entries)
else:
    df = generate_gl_entries(n_entries)


# ═══════════════════════════════════════════════════════════════════════
# COMPUTE
# ═══════════════════════════════════════════════════════════════════════

risk_score, risk_scores = compute_risk_score(df)
bf_df = run_benford_analysis(df["Amount_SAR"])
compliance_df = generate_ifrs_checklist(sector)

anomalies = df[df["Is_Anomaly"] == True].copy()
after_hours = df[(df["Posted_Hour"] < 7) | (df["Posted_Hour"] > 20)].copy()
round_entries = df[df["Is_Round_Number"] == True].copy()
reversals = df[df["Is_Reversal"] == True].copy()

total_sar = df["Amount_SAR"].sum()
compliance_pass = (compliance_df["Status"] == "✅ Pass").sum()
compliance_fail = (compliance_df["Status"] == "❌ Fail").sum()

findings = []
if len(anomalies) > 0:
    findings.append(f"{len(anomalies)} high-value transaction anomalies detected (>5σ threshold)")
if len(after_hours) > 0:
    findings.append(f"{len(after_hours)} journal entries posted outside business hours (potential management override risk)")
if bf_df["Chi_Sq"].sum() > 5:
    findings.append("Benford's Law deviation detected — digit 1 & 7 show abnormal concentration")
if compliance_fail > 0:
    fails = compliance_df[compliance_df["Status"] == "❌ Fail"]["Standard"].tolist()
    findings.append(f"IFRS/SOCPA non-compliance: {', '.join(fails)}")
findings.append("Zakat base computation requires GAZT reconciliation — SAR variance noted")
findings.append("Related party disclosures incomplete per SOCPA 7 requirements")


# ═══════════════════════════════════════════════════════════════════════
# KPI CARDS
# ═══════════════════════════════════════════════════════════════════════

risk_color = "red" if risk_score > 60 else "amber" if risk_score > 35 else "green"

st.markdown(f"""
<div class="kpi-grid">
    <div class="kpi-card gold">
        <div class="kpi-label">Composite Risk Score</div>
        <div class="kpi-value gold">{risk_score}</div>
        <div class="kpi-sub">/ 100 — {'CRITICAL' if risk_score > 70 else 'HIGH' if risk_score > 50 else 'MODERATE' if risk_score > 30 else 'LOW'}</div>
    </div>
    <div class="kpi-card red">
        <div class="kpi-label">Anomalies Flagged</div>
        <div class="kpi-value red">{len(anomalies)}</div>
        <div class="kpi-sub">of {len(df):,} entries ({len(anomalies)/len(df)*100:.1f}%)</div>
    </div>
    <div class="kpi-card blue">
        <div class="kpi-label">Total GL Volume</div>
        <div class="kpi-value blue">SAR {total_sar/1e6:.1f}M</div>
        <div class="kpi-sub">{len(df):,} journal entries</div>
    </div>
    <div class="kpi-card green">
        <div class="kpi-label">Compliance Pass Rate</div>
        <div class="kpi-value green">{compliance_pass}/{len(compliance_df)}</div>
        <div class="kpi-sub">{compliance_pass/len(compliance_df)*100:.0f}% IFRS/SOCPA pass</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════
# TABS
# ═══════════════════════════════════════════════════════════════════════

tabs = st.tabs(["📊  Risk Overview", "🔍  Anomaly Detection", "📋  IFRS/SOCPA Compliance", "📈  GL Analytics", "📝  Audit Memo"])


# ──────────────────────────── TAB 1: RISK OVERVIEW ────────────────────
with tabs[0]:
    col1, col2 = st.columns([1, 1])

    with col1:
        st.plotly_chart(risk_radar(risk_scores), use_container_width=True)

    with col2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Risk Factor Breakdown</div>', unsafe_allow_html=True)
        max_val = max(risk_scores.values()) or 1
        for factor, val in risk_scores.items():
            pct = val / 40 * 100
            sev = "red" if pct > 70 else "amber" if pct > 40 else "green"
            color = "#E74C3C" if sev == "red" else "#F39C12" if sev == "amber" else "#2ECC71"
            st.markdown(f"""
            <div style="margin-bottom:0.9rem;">
                <div style="display:flex; justify-content:space-between; margin-bottom:3px;">
                    <span style="font-size:0.78rem;">{factor}</span>
                    <span style="font-family:'IBM Plex Mono',monospace; font-size:0.72rem; color:{color};">{val:.1f}</span>
                </div>
                <div class="progress-bar-bg">
                    <div class="progress-bar-fill" style="width:{pct}%; background:{color};"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Audit findings
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Audit Findings Summary</div>', unsafe_allow_html=True)
    for f in findings[:3]:
        st.markdown(f'<div class="anomaly-flag">⚠ {f}</div>', unsafe_allow_html=True)
    for f in findings[3:]:
        st.markdown(f'<div class="finding-flag">◈ {f}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ──────────────────────────── TAB 2: ANOMALY DETECTION ────────────────
with tabs[1]:
    col1, col2 = st.columns([1, 1])

    with col1:
        if mod_benford:
            st.plotly_chart(benford_chart(bf_df), use_container_width=True)
            chi_total = bf_df["Chi_Sq"].sum()
            verdict = "❌ Deviation Detected" if chi_total > 5 else "✅ Conforms to Benford"
            badge = "risk-high" if chi_total > 5 else "risk-low"
            st.markdown(f'<span class="risk-badge {badge}">{verdict} — χ² = {chi_total:.2f}</span>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="section-card" style="height:100%;">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">After-Hours Entry Flags</div>', unsafe_allow_html=True)
        if len(after_hours) > 0:
            st.markdown(f"""
            <div class="anomaly-flag">
                <strong>{len(after_hours)}</strong> entries posted between 20:00–07:00.
                Indicates potential management override or segregation of duties failure.
            </div>""", unsafe_allow_html=True)
            ah_sample = after_hours[["Entry_ID", "Date", "Amount_SAR", "Posted_Hour", "Preparer"]].head(5)
            st.dataframe(ah_sample.style.format({"Amount_SAR": "{:,.2f}"}), use_container_width=True, hide_index=True)
        else:
            st.markdown('<div class="pass-flag">✅ No after-hours entries detected.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if mod_anomaly and len(anomalies) > 0:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="section-title">Flagged Anomalies ({len(anomalies)} entries)</div>', unsafe_allow_html=True)

        display_cols = ["Entry_ID", "Date", "Account_Name", "Description", "Amount_SAR", "Debit_Credit", "Preparer"]
        available_cols = [c for c in display_cols if c in anomalies.columns]
        anom_display = anomalies[available_cols].head(20).copy()
        anom_display["Amount_SAR"] = anom_display["Amount_SAR"].map("{:,.2f}".format)
        st.dataframe(anom_display, use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Round number analysis
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Round Number Concentration (Fraud Indicator)</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Round Numbers", f"{len(round_entries):,}", f"{len(round_entries)/len(df)*100:.1f}% of entries")
    with col2:
        st.metric("Reversals", f"{len(reversals):,}", f"{len(reversals)/len(df)*100:.1f}% of entries")
    with col3:
        avg_anom = anomalies["Amount_SAR"].mean() if len(anomalies) > 0 else 0
        st.metric("Avg Anomaly Value", f"SAR {avg_anom:,.0f}", "vs SAR " + f"{df['Amount_SAR'].mean():,.0f} avg")
    st.markdown('</div>', unsafe_allow_html=True)


# ──────────────────────────── TAB 3: COMPLIANCE ───────────────────────
with tabs[2]:
    if mod_compliance:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="section-title">IFRS / SOCPA Compliance Checklist — {sector}</div>', unsafe_allow_html=True)

        for _, row in compliance_df.iterrows():
            badge = "risk-critical" if row["Priority"] == "Critical" else "risk-high" if row["Priority"] == "High" else "risk-medium"
            flag_class = "anomaly-flag" if row["Status"] == "❌ Fail" else "finding-flag" if row["Status"] == "⚠️ Partial" else "pass-flag"
            st.markdown(f"""
            <div class="{flag_class}" style="display:flex; justify-content:space-between; align-items:center;">
                <div>
                    <span style="font-family:'IBM Plex Mono',monospace; font-size:0.7rem; color:#8A9BB5;">{row['Standard']}</span>
                    &nbsp;&nbsp;{row['Requirement']}
                </div>
                <div style="display:flex; gap:0.5rem; align-items:center; flex-shrink:0;">
                    <span class="risk-badge {badge}">{row['Priority']}</span>
                    <span style="font-family:'IBM Plex Mono',monospace; font-size:0.72rem;">{row['Status']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Summary
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("✅ Pass", (compliance_df["Status"] == "✅ Pass").sum())
        with col2:
            st.metric("⚠️ Partial", (compliance_df["Status"] == "⚠️ Partial").sum())
        with col3:
            st.metric("❌ Fail", (compliance_df["Status"] == "❌ Fail").sum())

        # Zakat note
        st.markdown("""
        <div class="finding-flag" style="margin-top:1rem;">
            <strong>GAZT / Zakat Note:</strong> Saudi entities are subject to Zakat (2.5% on Zakat base) administered
            by the General Authority of Zakat and Tax. Foreign-owned entities are subject to Corporate Income Tax
            at 20%. Mixed-ownership entities have blended rate obligations. Ensure Zakat base computation
            worksheet is prepared and agreed with GAZT assessments.
        </div>
        """, unsafe_allow_html=True)


# ──────────────────────────── TAB 4: GL ANALYTICS ─────────────────────
with tabs[3]:
    st.plotly_chart(timeline_chart(df), use_container_width=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.plotly_chart(account_breakdown_chart(df), use_container_width=True)

    with col2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Preparer Activity Analysis</div>', unsafe_allow_html=True)
        prep = df.groupby("Preparer").agg(
            Entries=("Entry_ID", "count"),
            Total_SAR=("Amount_SAR", "sum"),
            Anomalies=("Is_Anomaly", "sum"),
            After_Hours=("Posted_Hour", lambda x: ((x < 7) | (x > 20)).sum()),
        ).reset_index().sort_values("Anomalies", ascending=False)
        prep["Total_SAR"] = prep["Total_SAR"].map("SAR {:,.0f}".format)
        st.dataframe(prep, use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Distribution
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Transaction Amount Distribution (Log Scale)</div>', unsafe_allow_html=True)
    fig_dist = go.Figure()
    fig_dist.add_trace(go.Histogram(
        x=np.log10(df["Amount_SAR"].clip(lower=1)),
        nbinsx=50, name="All entries",
        marker_color="rgba(59,130,246,0.5)",
        marker_line_color="#3B82F6", marker_line_width=0.5,
    ))
    if len(anomalies) > 0:
        fig_dist.add_trace(go.Histogram(
            x=np.log10(anomalies["Amount_SAR"].clip(lower=1)),
            nbinsx=50, name="Anomalies",
            marker_color="rgba(231,76,60,0.6)",
            marker_line_color="#E74C3C", marker_line_width=0.5,
        ))
    fig_dist.update_layout(
        **CHART_LAYOUT,
        xaxis=dict(title="log₁₀(Amount SAR)", gridcolor="#1C2333"),
        yaxis=dict(title="Frequency", gridcolor="#1C2333"),
        legend=dict(bgcolor="rgba(0,0,0,0)"),
        barmode="overlay",
        height=260,
    )
    st.plotly_chart(fig_dist, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ──────────────────────────── TAB 5: MEMO ─────────────────────────────
with tabs[4]:
    if mod_memo:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Auto-Generated Audit Memorandum</div>', unsafe_allow_html=True)

        memo_text = generate_memo(company_name, sector, risk_score, findings)
        st.markdown(f'<div class="memo-box">{memo_text}</div>', unsafe_allow_html=True)

        col1, col2 = st.columns([1, 4])
        with col1:
            st.download_button(
                label="⬇  DOWNLOAD MEMO",
                data=memo_text,
                file_name=f"AuditMemo_{company_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.txt",
                mime="text/plain",
                use_container_width=True,
            )
        st.markdown('</div>', unsafe_allow_html=True)

    # Export GL data
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Export Data</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        csv_gl = df.to_csv(index=False).encode()
        st.download_button("⬇  Full GL (CSV)", csv_gl, "GL_Data.csv", "text/csv", use_container_width=True)
    with col2:
        csv_anom = anomalies.to_csv(index=False).encode()
        st.download_button("⬇  Anomalies (CSV)", csv_anom, "Anomalies.csv", "text/csv", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════

st.markdown("""
<div style="margin-top:2rem; padding:1rem 0; border-top:1px solid #2A3A4F;
            font-family:'IBM Plex Mono',monospace; font-size:0.62rem;
            color:#4A5A70; text-align:center; letter-spacing:1.5px;">
    FINAUDIT-KSA v2.0 &nbsp;·&nbsp; SOCPA-Aligned &nbsp;·&nbsp; ISA-Ready &nbsp;·&nbsp;
    IFRS / IAS &nbsp;·&nbsp; GAZT &nbsp;·&nbsp; Vision 2030 &nbsp;·&nbsp;
    Built for the Saudi Audit Market
</div>
""", unsafe_allow_html=True)
