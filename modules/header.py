import streamlit as st
from datetime import datetime


class Header:

    @staticmethod
    def show(project):

        profile = project["profile"]
        health = project["health"]

        quality = profile["quality_score"]

        if quality >= 90:
            color = "#16a34a"
            badge = "🟢 Excellent"
        elif quality >= 70:
            color = "#f59e0b"
            badge = "🟡 Good"
        else:
            color = "#dc2626"
            badge = "🔴 Needs Attention"

        dataset = project.get("file_name", "Unknown Dataset")

        rows = profile.get("rows", 0)
        cols = profile.get("columns", 0)

        now = datetime.now().strftime("%d %b %Y • %I:%M %p")

        st.markdown(
            f"""
<style>

.executive-header{{
background:linear-gradient(135deg,#0f172a,#1e3a8a);
padding:30px;
border-radius:22px;
color:white;
box-shadow:0 10px 30px rgba(0,0,0,.18);
margin-bottom:25px;
}}

.header-grid{{
display:grid;
grid-template-columns:2fr 1fr;
gap:30px;
align-items:center;
}}

.small-title{{
font-size:14px;
opacity:.85;
letter-spacing:.4px;
margin-bottom:8px;
}}

.big-title{{
font-size:38px;
font-weight:700;
margin-bottom:6px;
}}

.subtitle{{
font-size:18px;
opacity:.92;
margin-bottom:25px;
}}

.info-grid{{
display:grid;
grid-template-columns:repeat(4,1fr);
gap:18px;
margin-top:10px;
}}

.info-card{{
background:rgba(255,255,255,.08);
padding:16px;
border-radius:14px;
backdrop-filter:blur(8px);
}}

.info-label{{
font-size:13px;
opacity:.8;
}}

.info-value{{
font-size:18px;
font-weight:600;
margin-top:6px;
}}

.health-card{{
background:white;
border-radius:20px;
padding:28px;
text-align:center;
}}

.health-score{{
font-size:54px;
font-weight:700;
color:{color};
line-height:1;
}}

.health-label{{
font-size:15px;
color:#666;
margin-top:8px;
}}

.health-status{{
margin-top:18px;
display:inline-block;
padding:8px 18px;
background:#f3f4f6;
border-radius:999px;
font-weight:600;
}}

</style>

<div class="executive-header">

<div class="header-grid">

<div>

<div class="small-title">
EXECUTIVE BUSINESS DASHBOARD
</div>

<div class="big-title">
👋 Welcome back, Pinkal
</div>

<div class="subtitle">
AI-powered Business Intelligence Platform
</div>

<div class="info-grid">

<div class="info-card">
<div class="info-label">Dataset</div>
<div class="info-value">{dataset}</div>
</div>

<div class="info-card">
<div class="info-label">Rows</div>
<div class="info-value">{rows:,}</div>
</div>

<div class="info-card">
<div class="info-label">Columns</div>
<div class="info-value">{cols}</div>
</div>

<div class="info-card">
<div class="info-label">Last Updated</div>
<div class="info-value">{now}</div>
</div>

</div>

</div>

<div class="health-card">

<div style="color:#666;font-size:15px;">
Business Health
</div>

<div class="health-score">
{health["score"]}
</div>

<div class="health-label">
out of 100
</div>

<div class="health-status">
{badge}
</div>

</div>

</div>

</div>
""",
            unsafe_allow_html=True,
        )