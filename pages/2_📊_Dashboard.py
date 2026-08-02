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


# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Pinkal AI Analytics",
    page_icon="📊",
    layout="wide"
)

Theme.load()
UI.show_sidebar()

# ---------------------------------------------------
# Load Project
# ---------------------------------------------------

project = st.session_state.get("project")

if project is None:
    st.warning("⚠️ No dataset loaded.")
    st.info("Upload a dataset from the Home page.")
    st.stop()

# ---------------------------------------------------
# Executive Header
# ---------------------------------------------------

Header.show(project)

# ---------------------------------------------------
# Global Filters
# ---------------------------------------------------

filtered_df = FilterEngine.apply(project["df"])

# Create a filtered project so every module
# uses the same filtered data.
filtered_project = project.copy()
filtered_project["df"] = filtered_df

# ---------------------------------------------------
# Business Metrics
# ---------------------------------------------------

BusinessMetrics.calculate(filtered_project)

KPICards.show(filtered_project)

# ---------------------------------------------------
# Charts
# ---------------------------------------------------

ChartEngine.show(filtered_df)

st.divider()

# ---------------------------------------------------
# Executive Briefing
# ---------------------------------------------------

st.subheader("🧠 Executive Briefing")

briefing = ExecutiveBriefing.generate(filtered_project)

for item in briefing["findings"]:
    st.success(item)

st.markdown("### Recommended Actions")

for item in briefing["recommendations"]:
    st.markdown(f"• {item}")

st.divider()

# ---------------------------------------------------
# Business Health
# ---------------------------------------------------

st.subheader("❤️ Business Health")

HealthCard.show(filtered_project["health"])