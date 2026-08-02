import plotly.express as px
import streamlit as st

from modules.dataset_analyzer import DatasetAnalyzer
from modules.card import Card


class ChartEngine:

    @staticmethod
    def show(df):

        st.subheader("📊 Business Analytics")

        analysis = DatasetAnalyzer.analyze(df)

        metric = analysis["primary_metric"]
        region = analysis["region"]
        category = analysis["category"]
        date_col = analysis["primary_date"]

        if metric is None:
            st.info("No numeric columns available.")
            return

        top_left, top_right = st.columns(2)
        bottom_left, bottom_right = st.columns(2)

        # ==================================================
        # Metric by Region
        # ==================================================

        if region:

            chart = (
                df.groupby(region)[metric]
                .sum()
                .reset_index()
            )

            fig = px.bar(
                chart,
                x=region,
                y=metric,
                color=metric,
                text_auto=".2s",
                title=f"{metric} by {region}"
            )

            fig.update_layout(
                height=420,
                margin=dict(l=20, r=20, t=50, b=20)
            )

            top_left.plotly_chart(
                fig,
                use_container_width=True
            )

        else:
            top_left.info("No geographic column detected.")

        # ==================================================
        # Metric by Category
        # ==================================================

        if category:

            chart = (
                df.groupby(category)[metric]
                .sum()
                .reset_index()
            )

            fig = px.pie(
                chart,
                names=category,
                values=metric,
                hole=.55,
                title=f"{metric} by {category}"
            )

            fig.update_layout(
                height=420,
                margin=dict(l=20, r=20, t=50, b=20)
            )

            top_right.plotly_chart(
                fig,
                use_container_width=True
            )

        else:
            top_right.info("No category column detected.")

        # ==================================================
        # Trend
        # ==================================================

        if date_col:

            trend = (
                df.groupby(date_col)[metric]
                .sum()
                .reset_index()
            )

            fig = px.line(
                trend,
                x=date_col,
                y=metric,
                markers=True,
                title=f"{metric} Trend"
            )

            fig.update_layout(
                height=420,
                margin=dict(l=20, r=20, t=50, b=20)
            )

            bottom_left.plotly_chart(
                fig,
                use_container_width=True
            )

        else:
            bottom_left.info("No date column detected.")

        # ==================================================
        # Distribution
        # ==================================================

        fig = px.histogram(
            df,
            x=metric,
            nbins=25,
            title=f"{metric} Distribution"
        )

        fig.update_layout(
            height=420,
            margin=dict(l=20, r=20, t=50, b=20)
        )

        bottom_right.plotly_chart(
            fig,
            use_container_width=True
        )