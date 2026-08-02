import plotly.express as px
import streamlit as st


class ChartEngine:

    @staticmethod
    def show(df):

        st.subheader("📊 Business Analytics")

        numeric = df.select_dtypes(include="number").columns.tolist()

        if len(numeric) == 0:
            st.info("No numeric columns available.")
            return

        c1, c2 = st.columns(2)

        # ======================================
        # Revenue by Region
        # ======================================

        if "Region" in df.columns:

            revenue = numeric[0]

            chart = (
                df.groupby("Region")[revenue]
                .sum()
                .reset_index()
            )

            fig = px.bar(
                chart,
                x="Region",
                y=revenue,
                title=f"{revenue} by Region",
                color=revenue,
                text_auto=".2s"
            )

            fig.update_layout(height=400)

            c1.plotly_chart(
                fig,
                use_container_width=True
            )

        # ======================================
        # Revenue by Category
        # ======================================

        if "Category" in df.columns:

            revenue = numeric[0]

            chart = (
                df.groupby("Category")[revenue]
                .sum()
                .reset_index()
            )

            fig = px.pie(
                chart,
                names="Category",
                values=revenue,
                hole=.55
            )

            fig.update_layout(height=400)

            c2.plotly_chart(
                fig,
                use_container_width=True
            )

        # ======================================
        # Trend
        # ======================================

        date_columns = df.select_dtypes(
            include="datetime"
        ).columns.tolist()

        if len(date_columns):

            st.divider()

            date_col = date_columns[0]

            revenue = numeric[0]

            trend = (
                df.groupby(date_col)[revenue]
                .sum()
                .reset_index()
            )

            fig = px.line(
                trend,
                x=date_col,
                y=revenue,
                markers=True,
                title=f"{revenue} Trend"
            )

            fig.update_layout(height=450)

            st.plotly_chart(
                fig,
                use_container_width=True
            )