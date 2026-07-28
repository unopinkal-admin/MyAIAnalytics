import pandas as pd
import plotly.express as px
import streamlit as st


class Dashboard:

    @staticmethod
    def build(df):

        st.header("📊 Dashboard")

        Dashboard.show_kpis(df)

        Dashboard.show_charts(df)

    @staticmethod
    def show_kpis(df):

        numeric = df.select_dtypes(include="number")

        if numeric.empty:
            return

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Rows",
            len(df)
        )

        c2.metric(
            "Columns",
            len(df.columns)
        )

        c3.metric(
            "Numeric Columns",
            len(numeric.columns)
        )

        c4.metric(
            "Total Missing",
            int(df.isna().sum().sum())
        )

    @staticmethod
    def show_charts(df):

        numeric = df.select_dtypes(include="number").columns.tolist()

        category = df.select_dtypes(
            include=["object", "string", "category"]
        ).columns.tolist()

        if len(numeric) == 0:
            st.info("No numeric columns found.")
            return

        # Histogram

        st.subheader("Distribution")

        fig = px.histogram(
            df,
            x=numeric[0]
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

        if len(category) > 0:

            grouped = (
                df.groupby(category[0])[numeric[0]]
                .sum()
                .reset_index()
                .sort_values(
                    numeric[0],
                    ascending=False
                )
            )

            st.subheader(f"{numeric[0]} by {category[0]}")

            fig = px.bar(
                grouped,
                x=category[0],
                y=numeric[0]
            )

            st.plotly_chart(
                fig,
                width="stretch"
            )

        if len(numeric) >= 2:

            st.subheader("Correlation")

            fig = px.scatter(
                df,
                x=numeric[0],
                y=numeric[1]
            )

            st.plotly_chart(
                fig,
                width="stretch"
            )
