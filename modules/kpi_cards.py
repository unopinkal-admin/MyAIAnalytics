import streamlit as st

from modules.business_metrics import BusinessMetrics
from modules.metric_card import MetricCard


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
    def show(project):

        metrics = BusinessMetrics.calculate(project)

        c1, c2, c3 = st.columns(3)

        with c1:

            MetricCard.show(
                title="Revenue",
                value=KPICards.money(metrics["revenue"]),
                icon="💰",
                color="blue",
                subtitle="Total Sales"
            )

        with c2:

            MetricCard.show(
                title="Cost",
                value=KPICards.money(metrics["cost"]),
                icon="💸",
                color="orange",
                subtitle="Total Cost"
            )

        with c3:

            MetricCard.show(
                title="Profit",
                value=KPICards.money(metrics["profit"]),
                icon="📈",
                color="green",
                subtitle="Net Profit"
            )

        st.write("")

        c4, c5, c6 = st.columns(3)

        with c4:

            MetricCard.show(
                title="Margin",
                value=KPICards.percent(metrics["margin"]),
                icon="📊",
                color="purple",
                subtitle="Profit Margin"
            )

        with c5:

            MetricCard.show(
                title="Records",
                value=KPICards.number(metrics["rows"]),
                icon="📄",
                color="teal",
                subtitle="Rows Loaded"
            )

        with c6:

            MetricCard.show(
                title="Quality",
                value=KPICards.percent(metrics["quality"]),
                icon="⭐",
                color="red",
                subtitle="Data Quality"
            )