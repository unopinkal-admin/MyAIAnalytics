import streamlit as st
from modules.business_metrics import BusinessMetrics


class KPIWorkspace:

    @staticmethod
    def money(value):
        if value is None:
            return "-"
        return f"${value:,.0f}"

    @staticmethod
    def percent(value):
        if value is None:
            return "-"
        return f"{value:.1f}%"

    @staticmethod
    def number(value):
        if value is None:
            return "-"
        return f"{value:,}"

    @staticmethod
    def card(title, value, icon, color):

        st.markdown(
            f"""
<div style="
background:rgba(255,255,255,.92);
border-radius:22px;
padding:22px;
border:1px solid rgba(226,232,240,.8);
box-shadow:0 10px 25px rgba(15,23,42,.08);
transition:.3s;
height:170px;
">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
">

<div style="
font-size:16px;
font-weight:600;
color:#64748B;
">
{title}
</div>

<div style="
width:48px;
height:48px;
border-radius:14px;
background:{color};
display:flex;
justify-content:center;
align-items:center;
font-size:24px;
">
{icon}
</div>

</div>

<div style="
margin-top:28px;
font-size:38px;
font-weight:700;
color:#0F172A;
">
{value}
</div>

<div style="
margin-top:12px;
font-size:14px;
color:#22C55E;
font-weight:600;
">
▲ Executive Metric
</div>

</div>
""",
            unsafe_allow_html=True,
        )

    @staticmethod
    def show(project):

        metrics = BusinessMetrics.calculate(project)

        st.markdown("## 💼 Business Overview")

        c1, c2, c3 = st.columns(3)

        with c1:
            KPIWorkspace.card(
                "Revenue",
                KPIWorkspace.money(metrics["revenue"]),
                "💰",
                "#DBEAFE",
            )

        with c2:
            KPIWorkspace.card(
                "Profit",
                KPIWorkspace.money(metrics["profit"]),
                "📈",
                "#DCFCE7",
            )

        with c3:
            KPIWorkspace.card(
                "Margin",
                KPIWorkspace.percent(metrics["margin"]),
                "📊",
                "#F3E8FF",
            )

        st.write("")

        c4, c5, c6 = st.columns(3)

        with c4:
            KPIWorkspace.card(
                "Cost",
                KPIWorkspace.money(metrics["cost"]),
                "💸",
                "#FEF3C7",
            )

        with c5:
            KPIWorkspace.card(
                "Records",
                KPIWorkspace.number(metrics["rows"]),
                "📄",
                "#E0F2FE",
            )

        with c6:
            KPIWorkspace.card(
                "Quality",
                KPIWorkspace.percent(metrics["quality"]),
                "⭐",
                "#FEE2E2",
            )