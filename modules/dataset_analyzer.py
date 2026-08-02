import pandas as pd


class DatasetAnalyzer:
    """
    Intelligent dataset analyzer.

    This module inspects a dataframe and returns useful
    metadata that every dashboard component can reuse.
    """

    @staticmethod
    def analyze(df):

        analysis = {}

        # ----------------------------------
        # Column Types
        # ----------------------------------

        analysis["numeric"] = (
            df.select_dtypes(include="number")
            .columns
            .tolist()
        )

        analysis["categorical"] = (
            df.select_dtypes(
                include=["object", "category"]
            )
            .columns
            .tolist()
        )

        analysis["dates"] = (
            df.select_dtypes(
                include="datetime"
            )
            .columns
            .tolist()
        )

        # ----------------------------------
        # Primary Metric
        # ----------------------------------

        preferred_metrics = [
            "Sales",
            "Revenue",
            "Amount",
            "Profit",
            "Cost",
            "Price",
            "Value",
        ]

        metric = None

        for col in preferred_metrics:
            if col in df.columns:
                metric = col
                break

        if metric is None and analysis["numeric"]:
            metric = analysis["numeric"][0]

        analysis["primary_metric"] = metric

        # ----------------------------------
        # Primary Date
        # ----------------------------------

        analysis["primary_date"] = (
            analysis["dates"][0]
            if analysis["dates"]
            else None
        )

        # ----------------------------------
        # Region
        # ----------------------------------

        region_names = [
            "Region",
            "Country",
            "State",
            "City",
            "Location",
        ]

        region = None

        for col in region_names:
            if col in df.columns:
                region = col
                break

        analysis["region"] = region

        # ----------------------------------
        # Category
        # ----------------------------------

        category_names = [
            "Category",
            "Department",
            "Segment",
            "Type",
            "Product",
        ]

        category = None

        for col in category_names:
            if col in df.columns:
                category = col
                break

        analysis["category"] = category

        # ----------------------------------
        # Dataset Type
        # ----------------------------------

        dataset_type = "General"

        cols = [c.lower() for c in df.columns]

        if any(x in cols for x in [
            "sales",
            "revenue",
            "profit",
            "customer"
        ]):
            dataset_type = "Sales"

        elif any(x in cols for x in [
            "employee",
            "salary",
            "department"
        ]):
            dataset_type = "HR"

        elif any(x in cols for x in [
            "expense",
            "income",
            "budget"
        ]):
            dataset_type = "Finance"

        analysis["dataset_type"] = dataset_type

        return analysis