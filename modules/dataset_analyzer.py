import pandas as pd


class DatasetAnalyzer:
    """
    Intelligent dataset analyzer used throughout the dashboard.

    Detects important columns automatically so the dashboard
    adapts to almost any dataset.
    """

    METRIC_PRIORITY = [
        "Sales",
        "Revenue",
        "Amount",
        "Profit",
        "Cost",
        "Price",
        "Value",
        "Total",
        "Quantity",
        "Qty",
    ]

    DATE_PRIORITY = [
        "Date",
        "Order Date",
        "Invoice Date",
        "Created",
        "Created Date",
        "Timestamp",
    ]

    REGION_PRIORITY = [
        "Region",
        "Country",
        "State",
        "Province",
        "City",
        "Location",
        "Territory",
    ]

    CATEGORY_PRIORITY = [
        "Category",
        "Department",
        "Segment",
        "Type",
        "Product",
        "Product Category",
        "Brand",
    ]

    STATUS_PRIORITY = [
        "Status",
        "Order Status",
        "Stage",
        "State",
    ]

    @staticmethod
    def _find_column(df, candidates):

        columns = {c.lower(): c for c in df.columns}

        for candidate in candidates:

            if candidate.lower() in columns:
                return columns[candidate.lower()]

        return None

    @staticmethod
    def analyze(df):

        analysis = {}

        # ============================================
        # Numeric Columns
        # ============================================

        analysis["numeric"] = (
            df.select_dtypes(include="number")
            .columns
            .tolist()
        )

        # ============================================
        # Text Columns
        # ============================================

        analysis["categorical"] = (
            df.select_dtypes(
                include=["object", "category"]
            )
            .columns
            .tolist()
        )

        # ============================================
        # Datetime Columns
        # ============================================

        date_columns = (
            df.select_dtypes(
                include=["datetime64", "datetime64[ns]"]
            )
            .columns
            .tolist()
        )

        if not date_columns:

            for column in df.columns:

                if "date" in column.lower():

                    try:
                        pd.to_datetime(df[column])

                        date_columns.append(column)

                    except Exception:
                        pass

        analysis["dates"] = date_columns

        # ============================================
        # Primary Metric
        # ============================================

        metric = DatasetAnalyzer._find_column(
            df,
            DatasetAnalyzer.METRIC_PRIORITY,
        )

        if metric is None and analysis["numeric"]:

            metric = analysis["numeric"][0]

        analysis["primary_metric"] = metric

        # ============================================
        # Primary Date
        # ============================================

        date_col = DatasetAnalyzer._find_column(
            df,
            DatasetAnalyzer.DATE_PRIORITY,
        )

        if date_col is None and date_columns:

            date_col = date_columns[0]

        analysis["primary_date"] = date_col

        # ============================================
        # Region
        # ============================================

        analysis["region"] = DatasetAnalyzer._find_column(
            df,
            DatasetAnalyzer.REGION_PRIORITY,
        )

        # ============================================
        # Category
        # ============================================

        analysis["category"] = DatasetAnalyzer._find_column(
            df,
            DatasetAnalyzer.CATEGORY_PRIORITY,
        )

        # ============================================
        # Status
        # ============================================

        analysis["status"] = DatasetAnalyzer._find_column(
            df,
            DatasetAnalyzer.STATUS_PRIORITY,
        )

        # ============================================
        # Dataset Type
        # ============================================

        lower = [c.lower() for c in df.columns]

        if any(
            x in lower
            for x in [
                "sales",
                "revenue",
                "customer",
                "profit",
            ]
        ):

            dataset_type = "Sales"

        elif any(
            x in lower
            for x in [
                "employee",
                "salary",
                "department",
            ]
        ):

            dataset_type = "HR"

        elif any(
            x in lower
            for x in [
                "expense",
                "budget",
                "income",
                "finance",
            ]
        ):

            dataset_type = "Finance"

        elif any(
            x in lower
            for x in [
                "inventory",
                "stock",
                "warehouse",
            ]
        ):

            dataset_type = "Inventory"

        else:

            dataset_type = "General"

        analysis["dataset_type"] = dataset_type

        # ============================================
        # Summary
        # ============================================

        analysis["rows"] = len(df)
        analysis["columns"] = len(df.columns)
        analysis["missing_values"] = int(df.isna().sum().sum())
        analysis["duplicate_rows"] = int(df.duplicated().sum())

        return analysis