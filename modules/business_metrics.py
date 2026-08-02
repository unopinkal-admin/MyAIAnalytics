from modules.dataset_analyzer import DatasetAnalyzer


class BusinessMetrics:
    """
    Calculates reusable business metrics for the application.
    """

    @staticmethod
    def calculate(project):

        df = project["df"]
        profile = project["profile"]

        analysis = DatasetAnalyzer.analyze(df)

        metrics = {}

        metrics["rows"] = profile["rows"]
        metrics["columns"] = profile["columns"]
        metrics["quality"] = profile["quality_score"]

        metric = analysis["primary_metric"]

        revenue = None

        if metric:
            revenue = df[metric].sum(skipna=True)

        metrics["revenue"] = revenue

        cost = None

        if "Cost" in df.columns:
            cost = df["Cost"].sum(skipna=True)

        metrics["cost"] = cost

        profit = None

        if revenue is not None and cost is not None:
            profit = revenue - cost

        metrics["profit"] = profit

        margin = None

        if revenue not in (None, 0) and profit is not None:
            margin = (profit / revenue) * 100

        metrics["margin"] = margin

        metrics["transactions"] = len(df)
        metrics["missing"] = int(df.isna().sum().sum())

        return metrics