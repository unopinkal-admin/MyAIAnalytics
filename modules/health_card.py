import streamlit as st


class HealthCard:

    @staticmethod
    def show(health):

        score = health["score"]
        status = health["status"]

        # Color based on score
        if score >= 90:
            color = "🟢"
        elif score >= 75:
            color = "🟡"
        else:
            color = "🔴"

        st.markdown("## 💚 Business Health")

        c1, c2 = st.columns([1, 2])

        with c1:
            st.metric(
                label="Health Score",
                value=f"{score}/100"
            )

        with c2:
            st.success(f"{color} Status: {status}")

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("✅ Strengths")

            if health["strengths"]:
                for item in health["strengths"]:
                    st.write(f"• {item}")
            else:
                st.write("None")

        with col2:

            st.subheader("⚠ Risks")

            if health["risks"]:
                for item in health["risks"]:
                    st.write(f"• {item}")
            else:
                st.write("None")

        st.markdown("---")

        st.subheader("🎯 Recommendations")

        for item in health["recommendations"]:
            st.write(f"• {item}")
