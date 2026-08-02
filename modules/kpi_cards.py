import streamlit as st
from modules.business_metrics import BusinessMetrics


class KPICards:

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
    def card(title, value, color="#1f77b4"):

        st.markdown(
            f"""
<div style="
background:linear-gradient(135deg,#ffffff,#f8fbff);
padding:22px;
border-radius:18px;
border-left:6px solid {color};
box-shadow:0 4px 12px rgba(0,0,0,.08);
border:1px solid #ececec;
height:140px;
display:flex;
flex-direction:column;
justify-content:center;
">

<div style="
font-size:16px;
font-weight:600;
color:#666;
margin-bottom:14px;
">

{title}

</div>

<div style="
font-size:36px;
font-weight:700;
color:{color};
line-height:1;
">

{value}

</div>

</div>
""",
            unsafe_allow_html=True,
        )

    @staticmethod
    def show(project):

        metrics = BusinessMetrics.calculate(project)

        c1, c2, c3, c4, c5, c6 = st.columns(6)

        with c1:
            KPICards.card(
                "💰 Revenue",
                KPICards.money(metrics["revenue"]),
                "#2E86DE",
            )

        with c2:
            KPICards.card(
                "💸 Cost",
                KPICards.money(metrics["cost"]),
                "#E67E22",
            )

        with c3:
            KPICards.card(
                "📈 Profit",
                KPICards.money(metrics["profit"]),
                "#27AE60",
            )

        with c4:
            KPICards.card(
                "📊 Margin",
                KPICards.percent(metrics["margin"]),
                "#8E44AD",
            )

        with c5:
            KPICards.card(
                "📄 Records",
                KPICards.number(metrics["rows"]),
                "#16A085",
            )

        with c6:
            KPICards.card(
                "⭐ Quality",
                KPICards.percent(metrics["quality"]),
                "#C0392B",
            )