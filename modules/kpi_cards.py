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
    def _metric(label, value, subtitle, color):

        st.markdown(
            f"""
        <div style="
            padding:18px 10px;
            border-radius:14px;
            background:white;
            border-bottom:4px solid {color};
            text-align:center;
            height:135px;
        ">

            <div style="
                color:#64748B;
                font-size:14px;
                font-weight:600;
            ">
                {label}
            </div>

            <div style="
                margin-top:12px;
                font-size:34px;
                font-weight:700;
                color:#0F172A;
            ">
                {value}
            </div>

            <div style="
                margin-top:10px;
                color:#94A3B8;
                font-size:13px;
            ">
                {subtitle}
            </div>

        </div>
        """,
            unsafe_allow_html=True,
        )

    @staticmethod
    def show(project):

        metrics = BusinessMetrics.calculate(project)

        st.markdown(
            """
            <div style="
                background:white;
                padding:24px;
                border-radius:22px;
                border:1px solid #E5E7EB;
                box-shadow:0 8px 24px rgba(0,0,0,.06);
                margin-bottom:25px;
            ">
            <div style="
                font-size:24px;
                font-weight:700;
                color:#1E293B;
                margin-bottom:25px;
            ">
                💼 Business Overview
            </div>
            """,
            unsafe_allow_html=True,
        )

        r1 = st.columns(3)

        with r1[0]:
            KPICards._metric(
                "Revenue",
                KPICards.money(metrics["revenue"]),
                "Total Sales",
                "#2563EB",
            )

        with r1[1]:
            KPICards._metric(
                "Profit",
                KPICards.money(metrics["profit"]),
                "Net Profit",
                "#16A34A",
            )

        with r1[2]:
            KPICards._metric(
                "Margin",
                KPICards.percent(metrics["margin"]),
                "Profit Margin",
                "#7C3AED",
            )

        st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

        r2 = st.columns(3)

        with r2[0]:
            KPICards._metric(
                "Cost",
                KPICards.money(metrics["cost"]),
                "Total Cost",
                "#EA580C",
            )

        with r2[1]:
            KPICards._metric(
                "Records",
                KPICards.number(metrics["rows"]),
                "Rows Loaded",
                "#0F766E",
            )

        with r2[2]:
            quality = KPICards.percent(metrics["quality"])

            subtitle = (
                "Excellent"
                if metrics["quality"] >= 90
                else "Good"
                if metrics["quality"] >= 70
                else "Needs Attention"
            )

            KPICards._metric(
                "Data Quality",
                quality,
                subtitle,
                "#DC2626",
            )

        st.markdown("</div>", unsafe_allow_html=True)