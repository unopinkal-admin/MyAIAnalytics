from modules.theme import Theme
from modules.ui import UI
import streamlit as st

st.set_page_config(page_title="Pinkal AI Analytics", page_icon="🏠")
Theme.load()
UI.show_sidebar()

st.title("📊 Pinkal AI Analytics")

st.subheader("AI Data Analyst")

st.markdown("---")

st.markdown("""
### 👋 Welcome!

Upload an Excel or CSV file and I'll automatically:

- ✅ Clean your data
- ✅ Analyze quality
- ✅ Build dashboards
- ✅ Detect trends
- ✅ Find anomalies
- ✅ Answer business questions
""")

st.markdown("---")

st.info("👈 Use the sidebar to navigate through the application.")
