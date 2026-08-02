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
    def card(title, value):

        st.markdown(
            f"""
<div style="
background:#ffffff;
padding:18px;
border-radius:16px;
box-shadow:0 2px 10px rgba(0,0,0,.08);
border:1px solid #ececec;
text-align:center;
height:120px;
display:flex;
flex-direction:column;
justify-content:center;
">

<div style="
font-size:15px;
color:#666;
margin-bottom:10px;
font-weight:600;
">

{title}

</div>

<div style="
font-size:34px;
font-weight:700;
color:#1f77b4;
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
                KPICards.money(metrics["revenue"])
            )

        with c2:
            KPICards.card(
                "💸 Cost",
                KPICards.money(metrics["cost"])
            )

        with c3:
            KPICards.card(
                "📈 Profit",
                KPICards.money(metrics["profit"])
            )

        with c4:
            KPICards.card(
                "📊 Margin",
                KPICards.percent(metrics["margin"])
            )

        with c5:
            KPICards.card(
                "📄 Records",
                KPICards.number(metrics["rows"])
            )

        with c6:
            KPICards.card(
                "⭐ Quality",
                KPICards.percent(metrics["quality"])
            )