import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from modules.dataset_analyzer import DatasetAnalyzer
from modules.card import Card


class ChartEngine:

    @staticmethod
    def _style(fig):

        fig.update_layout(
            height=420,
            template="plotly_white",
            margin=dict(l=20, r=20, t=55, b=20),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="white",
            font=dict(
                family="Inter",
                size=13,
                color="#334155"
            ),
            title=dict(
                font=dict(size=18),
                x=0.02
            ),
            legend=dict(
                orientation="h",
                y=1.05
            )
        )

        fig.update_xaxes(
            showgrid=False,
            zeroline=False
        )

        fig.update_yaxes(
            gridcolor="#EEF2F7",
            zeroline=False
        )

        return fig

    @staticmethod
    def show(df):

        analysis = DatasetAnalyzer.analyze(df)

        metric = analysis["primary_metric"]
        region = analysis["region"]
        category = analysis["category"]
        date_col = analysis["primary_date"]

        if metric is None:
            st.info("No numeric columns detected.")
            return

        Card.section(
            title="Analytics Workspace",
            icon="📈"
        )

        left, right = st.columns(2)

        # --------------------------------------------------
        # Revenue by Region
        # --------------------------------------------------

        with left:

            with Card.container(
                title="Regional Performance",
                icon="🌍",
                accent="#2563EB"
            ):

                if region:

                    chart = (
                        df.groupby(region)[metric]
                        .sum()
                        .reset_index()
                        .sort_values(metric, ascending=False)
                    )

                    fig = px.bar(
                        chart,
                        x=region,
                        y=metric,
                        color=metric,
                        text_auto=".2s",
                        color_continuous_scale="Blues"
                    )

                    st.plotly_chart(
                        ChartEngine._style(fig),
                        use_container_width=True
                    )

                else:
                    st.info("No region column detected.")

        # --------------------------------------------------
        # Category Breakdown
        # --------------------------------------------------

        with right:

            with Card.container(
                title="Category Breakdown",
                icon="🥧",
                accent="#7C3AED"
            ):

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
                        hole=.65
                    )

                    st.plotly_chart(
                        ChartEngine._style(fig),
                        use_container_width=True
                    )

                else:
                    st.info("No category column detected.")

        bottom_left, bottom_right = st.columns(2)

        # --------------------------------------------------
        # Trend
        # --------------------------------------------------

        with bottom_left:

            with Card.container(
                title="Business Trend",
                icon="📈",
                accent="#16A34A"
            ):

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
                        markers=True
                    )

                    fig.update_traces(
                        line=dict(width=3)
                    )

                    st.plotly_chart(
                        ChartEngine._style(fig),
                        use_container_width=True
                    )

                else:
                    st.info("No date column detected.")

        # --------------------------------------------------
        # Distribution
        # --------------------------------------------------

        with bottom_right:

            with Card.container(
                title="Distribution",
                icon="📊",
                accent="#EA580C"
            ):

                fig = px.histogram(
                    df,
                    x=metric,
                    nbins=25
                )

                st.plotly_chart(
                    ChartEngine._style(fig),
                    use_container_width=True
                )