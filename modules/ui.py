import streamlit as st


class UI:

    @staticmethod
    def show_sidebar():

        with st.sidebar:

            st.markdown("""
<div style="
text-align:center;
padding:10px 0 20px 0;
">

<div style="
font-size:28px;
font-weight:700;
color:white;
">
🚀 Pinkal AI
</div>

<div style="
font-size:15px;
color:#CBD5E1;
margin-top:6px;
">
Analytics Pro
</div>

</div>
""", unsafe_allow_html=True)

            st.markdown("---")

            project = st.session_state.get("project")

            if project:

                profile = project["profile"]

                st.markdown("""
<div style="
font-size:18px;
font-weight:700;
margin-bottom:12px;
">
📁 Current Project
</div>
""", unsafe_allow_html=True)

                st.success(project.get("file_name", "Unknown Dataset"))

                c1, c2 = st.columns(2)

                c1.metric(
                    "Rows",
                    f"{profile['rows']:,}"
                )

                c2.metric(
                    "Columns",
                    profile["columns"]
                )

                quality = profile["quality_score"]

                if quality >= 90:
                    status = "🟢 Excellent"
                elif quality >= 75:
                    status = "🔵 Good"
                elif quality >= 60:
                    status = "🟡 Fair"
                else:
                    status = "🔴 Poor"

                st.metric(
                    "Data Quality",
                    f"{quality:.1f}%"
                )

                st.info(status)

                st.markdown("---")

                st.markdown("### 📈 Dashboard")

                st.caption("Executive Dashboard")

                st.caption("AI Analyst")

                st.caption("Business Intelligence")

                st.markdown("---")

                st.markdown("### ⚡ Quick Stats")

                st.metric(
                    "Dataset Size",
                    f"{profile['rows']:,}"
                )

                st.metric(
                    "Quality Score",
                    f"{quality:.1f}%"
                )

                st.success("✅ AI Ready")

            else:

                st.info("📂 No dataset loaded.")

                st.caption(
                    "Upload a dataset from the Home page to begin."
                )

            st.markdown("---")

            st.markdown(
                """
<div style="
text-align:center;
font-size:12px;
color:#94A3B8;
padding-top:8px;
">
Pinkal AI Analytics Pro<br>
Version 1.0
</div>
""",
                unsafe_allow_html=True,
            )