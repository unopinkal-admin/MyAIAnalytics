import streamlit as st

from modules.theme import Theme
from modules.ui import UI

from modules.header import Header
from modules.filter_engine import FilterEngine
from modules.business_metrics import BusinessMetrics
from modules.kpi_cards import KPICards
from modules.chart_engine import ChartEngine
from modules.executive_briefing import ExecutiveBriefing
from modules.health_card import HealthCard


# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="Pinkal AI Analytics Pro",
    page_icon="🚀",
    layout="wide",
)

Theme.load()
UI.show_sidebar()


# =====================================================
# Load Project
# =====================================================

project = st.session_state.get("project")

if project is None:
    st.warning("⚠️ No dataset loaded.")
    st.info("Please upload a dataset from the Home page.")
    st.stop()


# =====================================================
# Global Filters
# =====================================================

filtered_df = FilterEngine.apply(project["df"])

filtered_project = project.copy()
filtered_project["df"] = filtered_df

metrics = BusinessMetrics.calculate(filtered_project)

filtered_project["metrics"] = metrics


# =====================================================
# Executive Header
# =====================================================

Header.show(filtered_project)

st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)


# =====================================================
# Business Overview
# =====================================================

KPICards.show(filtered_project)

st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)


# =====================================================
# Analytics Workspace
# =====================================================

ChartEngine.show(filtered_df)

st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)


# =====================================================
# Executive Intelligence
# =====================================================

briefing = ExecutiveBriefing.generate(filtered_project)

st.markdown(
    """
<div style="
background:white;
padding:28px;
border-radius:22px;
border:1px solid #E5E7EB;
box-shadow:0 8px 24px rgba(0,0,0,.06);
margin-bottom:24px;
">

<h2 style="margin-top:0;margin-bottom:25px;color:#1E293B;">
🧠 Executive Intelligence
</h2>

""",
    unsafe_allow_html=True,
)

left, right = st.columns(2)

with left:

    st.markdown("### 📌 Key Findings")

    for finding in briefing["findings"]:
        st.success(finding)

with right:

    st.markdown("### 🎯 Recommended Actions")

    for recommendation in briefing["recommendations"]:
        st.info(recommendation)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)


# =====================================================
# Business Health
# =====================================================

HealthCard.show(filtered_project["health"])

st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)


# =====================================================
# Footer
# =====================================================

st.markdown(
    """
<div style="
text-align:center;
color:#94A3B8;
font-size:13px;
padding:10px 0 20px 0;
">
Pinkal AI Analytics Pro • Executive Dashboard
</div>
""",
    unsafe_allow_html=True,
)