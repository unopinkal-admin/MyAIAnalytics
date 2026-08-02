import pandas as pd


class BusinessMetrics:
    """
    Calculates reusable business metrics for the entire application.

    This module contains NO Streamlit code.

    It simply returns numbers that can be used by:
        • Dashboard
        • AI Analyst
        • Reports
        • Exports
    """

    @staticmethod
    def calculate(project):

        df = project["df"]
        profile = project["profile"]

        metrics = {}

        # --------------------------------------------------
        # Basic Metrics
        # --------------------------------------------------

        metrics["rows"] = profile["rows"]
        metrics["columns"] = profile["columns"]
        metrics["quality"] = profile["quality_score"]

        # --------------------------------------------------
        # Revenue
        # --------------------------------------------------

        revenue = None

        if "Sales" in df.columns:
            revenue = df["Sales"].sum(skipna=True)

        metrics["revenue"] = revenue

        # --------------------------------------------------
        # Cost
        # --------------------------------------------------

        cost = None

        if "Cost" in df.columns:
            cost = df["Cost"].sum(skipna=True)

        metrics["cost"] = cost

        # --------------------------------------------------
        # Profit
        # --------------------------------------------------

        profit = None

        if revenue is not None and cost is not None:
            profit = revenue - cost

        metrics["profit"] = profit

        # --------------------------------------------------
        # Margin %
        # --------------------------------------------------

        margin = None

        if revenue not in (None, 0) and profit is not None:
            margin = (profit / revenue) * 100

        metrics["margin"] = margin

        # --------------------------------------------------
        # Transactions
        # --------------------------------------------------

        metrics["transactions"] = len(df)

        # --------------------------------------------------
        # Missing Values
        # --------------------------------------------------

        metrics["missing"] = int(df.isna().sum().sum())

        return metrics