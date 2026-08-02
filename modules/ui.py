import streamlit as st


class UI:

    @staticmethod
    def show_sidebar():

        with st.sidebar:

            st.title("📊 Pinkal AI Analytics")
            st.caption("Your Personal Data Analyst")

            st.markdown("---")

            project = st.session_state.get("project")

            if project:

                profile = project["profile"]

                st.subheader("📁 Current Project")

                st.success(project["file_name"])

                st.write(f"**Rows:** {profile['rows']:,}")
                st.write(f"**Columns:** {profile['columns']}")
                st.write(f"**Quality:** {profile['quality_score']}%")

                st.success("🟢 AI Ready")

            else:

                st.info("No dataset loaded")

            st.markdown("---")

            st.caption("Version 0.3")
