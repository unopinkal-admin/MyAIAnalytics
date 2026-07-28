import streamlit as st
from services.project_service import ProjectService

st.set_page_config(
    page_title="MyAIAnalytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 MyAIAnalytics")
st.caption("Your Personal AI Data Analyst")

st.markdown("---")

st.markdown("""
## 👋 Hello!

I'm ready to analyze your data.

After you upload an Excel or CSV file, I'll automatically:

- ✅ Clean your data
- ✅ Detect data quality issues
- ✅ Build interactive dashboards
- ✅ Find trends and anomalies
- ✅ Generate executive insights
- ✅ Answer questions about your data
""")

st.markdown("---")

uploaded_file = st.file_uploader(
    "📂 Upload your dataset",
    type=["csv", "xlsx", "xls"]
)

st.markdown("---")

st.subheader("💡 Try asking me")

st.info("📈 Summarize this dataset")
st.info("📊 Which products perform best?")
st.info("🚨 Detect anomalies")
st.info("💰 Explain my sales")
st.info("📄 Create an executive report")

if uploaded_file:

    with st.spinner("🤖 AI is analyzing your dataset..."):
        project = ProjectService.create(uploaded_file)

    if project:

        st.success(f"✅ {project['file_name']} analyzed successfully!")

        st.balloons()

        # Verify Business Health exists
        st.subheader("💚 Business Health")

        st.metric(
            "Health Score",
            f"{project['health']['score']}/100"
        )

        st.success(
            f"Status: {project['health']['status']}"
        )

        st.subheader("🧠 Executive Summary")

        st.info(
            f"""
Dataset contains **{project['profile']['rows']:,} rows**
and **{project['profile']['columns']} columns**.

Quality Score: **{project['profile']['quality_score']}%**
"""
        )

        st.success("🎉 Your AI project is ready!")

        st.write("Open **📊 Dashboard** from the sidebar to explore your data.")
