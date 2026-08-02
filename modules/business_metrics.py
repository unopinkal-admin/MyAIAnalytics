from modules.dataset_analyzer import DatasetAnalyzer


class BusinessMetrics:
    """
    Calculates reusable business metrics for the application.
    """

    @staticmethod
    def _sum_column(df, column):

        if column and column in df.columns:
            return float(df[column].fillna(0).sum())

        return None

    @staticmethod
    def calculate(project):

        df = project["df"]
        profile = project["profile"]

        analysis = DatasetAnalyzer.analyze(df)

        metrics = {}

        # ==================================================
        # Dataset Metrics
        # ==================================================

        metrics["rows"] = len(df)
        metrics["columns"] = len(df.columns)
        metrics["quality"] = profile.get("quality_score", 0)

        # ==================================================
        # Primary Metric
        # ==================================================

        revenue_column = analysis["primary_metric"]

        revenue = BusinessMetrics._sum_column(
            df,
            revenue_column,
        )

        metrics["revenue"] = revenue

        # ==================================================
        # Cost
        # ==================================================

        cost_column = None

        for column in [
            "Cost",
            "Costs",
            "Expense",
            "Expenses",
            "Total Cost",
        ]:

            if column in df.columns:

                cost_column = column
                break

        cost = BusinessMetrics._sum_column(
            df,
            cost_column,
        )

        metrics["cost"] = cost

        # ==================================================
        # Profit
        # ==================================================

        profit = None

        if revenue is not None:

            if "Profit" in df.columns:

                profit = float(
                    df["Profit"].fillna(0).sum()
                )

            elif cost is not None:

                profit = revenue - cost

        metrics["profit"] = profit

        # ==================================================
        # Margin
        # ==================================================

        margin = None

        if (
            revenue is not None
            and revenue != 0
            and profit is not None
        ):

            margin = (profit / revenue) * 100

        metrics["margin"] = margin

        # ==================================================
        # Average Transaction
        # ==================================================

        average_sale = None

        if revenue is not None and len(df):

            average_sale = revenue / len(df)

        metrics["average_sale"] = average_sale

        # ==================================================
        # Record Statistics
        # ==================================================

        metrics["transactions"] = len(df)

        metrics["missing"] = int(
            df.isna().sum().sum()
        )

        metrics["duplicates"] = int(
            df.duplicated().sum()
        )

        metrics["numeric_columns"] = len(
            analysis["numeric"]
        )

        metrics["categorical_columns"] = len(
            analysis["categorical"]
        )

        metrics["dataset_type"] = analysis[
            "dataset_type"
        ]

        metrics["primary_metric"] = revenue_column

        return metrics