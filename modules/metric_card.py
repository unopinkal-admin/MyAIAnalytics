import streamlit as st


class MetricCard:

    COLORS = {
        "blue": "#2563EB",
        "green": "#16A34A",
        "orange": "#EA580C",
        "purple": "#7C3AED",
        "red": "#DC2626",
        "teal": "#0F766E",
        "gray": "#475569",
    }

    LIGHT_COLORS = {
        "blue": "#DBEAFE",
        "green": "#DCFCE7",
        "orange": "#FED7AA",
        "purple": "#E9D5FF",
        "red": "#FEE2E2",
        "teal": "#CCFBF1",
        "gray": "#E2E8F0",
    }

    @staticmethod
    def show(
        title,
        value,
        color="blue",
        subtitle=None,
        icon=None,
    ):

        accent = MetricCard.COLORS.get(color, "#2563EB")
        light = MetricCard.LIGHT_COLORS.get(color, "#DBEAFE")

        html = f"""
<style>

.metric-card-v2{{
    background:rgba(255,255,255,.94);
    border-radius:22px;
    border:1px solid rgba(226,232,240,.9);

    padding:24px;

    height:185px;

    display:flex;
    flex-direction:column;
    justify-content:space-between;

    box-shadow:
        0 10px 30px rgba(15,23,42,.08);

    transition:all .25s ease;
}}

.metric-card-v2:hover{{
    transform:translateY(-4px);

    box-shadow:
        0 18px 42px rgba(15,23,42,.15);
}}

.metric-top{{
    display:flex;
    justify-content:space-between;
    align-items:center;
}}

.metric-title{{
    font-size:15px;
    color:#64748B;
    font-weight:600;
}}

.metric-icon{{
    width:54px;
    height:54px;

    border-radius:16px;

    background:{light};

    display:flex;
    align-items:center;
    justify-content:center;

    font-size:26px;
}}

.metric-value{{
    font-size:40px;
    font-weight:700;
    color:#0F172A;

    margin-top:18px;
}}

.metric-subtitle{{
    margin-top:10px;

    color:#64748B;

    font-size:14px;
}}

.metric-footer{{
    margin-top:16px;

    font-size:13px;

    color:{accent};

    font-weight:700;
}}

</style>

<div class="metric-card-v2">

<div class="metric-top">

<div class="metric-title">
{title}
</div>

<div class="metric-icon">
{icon or "📊"}
</div>

</div>

<div>

<div class="metric-value">
{value}
</div>

"""

        if subtitle:

            html += f"""
<div class="metric-subtitle">
{subtitle}
</div>
"""

        html += f"""

<div class="metric-footer">
● Live Business Metric
</div>

</div>

</div>

"""

        st.markdown(
            html,
            unsafe_allow_html=True,
        )