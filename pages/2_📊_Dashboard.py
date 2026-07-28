from modules.health_card import HealthCard
from modules.executive_briefing import ExecutiveBriefing
from modules.dashboard import Dashboard
from modules.theme import Theme
from modules.ui import UI
import streamlit as st

st.set_page_config(
    page_title="Pinkal AI Analytics",
    page_icon="📊",
    layout="wide"
)

Theme.load()
UI.show_sidebar()

st.title("📊 Executive Dashboard")

project = st.session_state.get("project")

if project is None:
    st.warning("⚠️ No dataset loaded.")
    st.info("Please upload a dataset from the Home page.")
    st.stop()

df = project["df"]
profile = project["profile"]
insights = project["insights"]
health = project["health"]

briefing = ExecutiveBriefing.generate(project)

# ==================================================
# Business Health
# ==================================================

HealthCard.show(health)

st.divider()

# ==================================================
# Executive Briefing
# ==================================================

st.subheader("🧠 Executive Briefing")

quality = profile["quality_score"]

if quality >= 90:
    status = "🟢 Excellent"
elif quality >= 70:
    status = "🟡 Good"
else:
    status = "🔴 Needs Attention"

st.success(
    f"""
### Dataset: **{project['file_name']}**

Overall Data Quality: **{status} ({quality}%)**
"""
)

st.markdown("### 📋 Key Findings")

for item in briefing["findings"]:
    st.markdown(f"✅ {item}")

st.markdown("### 🎯 Recommended Actions")

for item in briefing["recommendations"]:
    st.markdown(f"• {item}")

st.divider()

# ==================================================
# KPI Cards
# ==================================================

st.subheader("📊 Key Metrics")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Rows", f"{profile['rows']:,}")
c2.metric("Columns", profile["columns"])
c3.metric("Duplicates", profile["duplicates"])
c4.metric("Quality", f"{quality}%")

st.divider()

# ==================================================
# AI Findings
# ==================================================

st.subheader("💡 AI Findings")

for insight in insights:
    st.info(insight)

st.divider()

# ==================================================
# Interactive Dashboard
# ==================================================

st.subheader("📈 Interactive Dashboard")

Dashboard.build(df)