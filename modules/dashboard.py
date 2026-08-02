import streamlit as st

from modules.business_metrics import BusinessMetrics
from modules.chart_engine import ChartEngine
from modules.executive_briefing import ExecutiveBriefing
from modules.health_card import HealthCard
from modules.header import Header
from modules.kpi_cards import KPICards


class Dashboard:

    @staticmethod
    def build(project):

        metrics = BusinessMetrics.calculate(project)
        project["metrics"] = metrics

        Header.show(project)

        st.markdown(
            "<div style='height:24px'></div>",
            unsafe_allow_html=True,
        )

        KPICards.show(project)

        st.markdown(
            "<div style='height:24px'></div>",
            unsafe_allow_html=True,
        )

        ChartEngine.show(project["df"])

        st.markdown(
            "<div style='height:24px'></div>",
            unsafe_allow_html=True,
        )

        Dashboard.show_ai_summary(project)

        st.markdown(
            "<div style='height:24px'></div>",
            unsafe_allow_html=True,
        )

        HealthCard.show(project["health"])

    @staticmethod
    def show_ai_summary(project):

        briefing = ExecutiveBriefing.generate(project)

        st.markdown(
            """
<div style="
background:white;
border-radius:22px;
padding:26px;
border:1px solid #E5E7EB;
box-shadow:0 8px 24px rgba(0,0,0,.06);
margin-bottom:24px;
">

<h2 style="
margin-top:0;
margin-bottom:24px;
color:#1E293B;
">
🧠 AI Executive Summary
</h2>

""",
            unsafe_allow_html=True,
        )

        left, right = st.columns(2)

        with left:

            st.markdown("#### 📌 Key Findings")

            for finding in briefing["findings"]:
                st.success(finding)

        with right:

            st.markdown("#### 🎯 Recommendations")

            for recommendation in briefing["recommendations"]:
                st.info(recommendation)

        st.markdown(
            "</div>",
            unsafe_allow_html=True,
        )