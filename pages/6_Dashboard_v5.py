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


st.set_page_config(
    page_title="Pinkal AI Analytics Pro",
    page_icon="🚀",
    layout="wide"
)

Theme.load()
UI.show_sidebar()

project = st.session_state.get("project")

if project is None:
    st.warning("⚠️ No dataset loaded.")
    st.info("Please upload a dataset from the Home page.")
    st.stop()


# ====================================================
# Executive Header
# ====================================================

Header.show(project)

st.markdown("<br>", unsafe_allow_html=True)


# ====================================================
# Global Filters
# ====================================================

st.markdown("## 📊 Executive Workspace")

filtered_df = FilterEngine.apply(project["df"])

filtered_project = project.copy()
filtered_project["df"] = filtered_df

BusinessMetrics.calculate(filtered_project)


# ====================================================
# Business Overview
# ====================================================

st.markdown("### 💼 Business Overview")

KPICards.show(filtered_project)

st.markdown("---")


# ====================================================
# Analytics Workspace
# ====================================================

st.markdown("### 📈 Analytics Workspace")

ChartEngine.show(filtered_df)

st.markdown("---")


# ====================================================
# Executive Intelligence
# ====================================================

st.markdown("### 🧠 Executive Intelligence")

briefing = ExecutiveBriefing.generate(filtered_project)

for finding in briefing["findings"]:
    st.success(finding)

st.markdown("#### 🎯 Recommended Actions")

for recommendation in briefing["recommendations"]:
    st.markdown(f"- {recommendation}")

st.markdown("---")


# ====================================================
# Business Health
# ====================================================

st.markdown("### ❤️ Business Health")

HealthCard.show(filtered_project["health"])