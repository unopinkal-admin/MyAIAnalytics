import pandas as pd

from modules.dataset_analyzer import DatasetAnalyzer


class PromptBuilder:

    @staticmethod
    def build(df):

        analysis = DatasetAnalyzer.analyze(df)

        lines = []

        # ==================================================
        # DATASET OVERVIEW
        # ==================================================

        lines.append("# DATASET OVERVIEW")
        lines.append(f"Rows: {analysis['rows']:,}")
        lines.append(f"Columns: {analysis['columns']}")
        lines.append(f"Dataset Type: {analysis['dataset_type']}")
        lines.append("")

        # ==================================================
        # IMPORTANT COLUMNS
        # ==================================================

        lines.append("# IMPORTANT COLUMNS")
        lines.append(f"Primary Metric: {analysis['primary_metric']}")
        lines.append(f"Primary Date: {analysis['primary_date']}")
        lines.append(f"Region: {analysis['region']}")
        lines.append(f"Category: {analysis['category']}")
        lines.append(f"Status: {analysis['status']}")
        lines.append("")

        # ==================================================
        # DATA QUALITY
        # ==================================================

        lines.append("# DATA QUALITY")
        lines.append(f"Missing Values: {analysis['missing_values']:,}")
        lines.append(f"Duplicate Rows: {analysis['duplicate_rows']:,}")
        lines.append("")

        # ==================================================
        # NUMERIC SUMMARY
        # ==================================================

        numeric = analysis["numeric"]

        if numeric:

            lines.append("# NUMERIC SUMMARY")

            for column in numeric:

                series = df[column].dropna()

                if series.empty:
                    continue

                lines.append(f"## {column}")

                lines.append(f"Total: {series.sum():,.2f}")
                lines.append(f"Average: {series.mean():,.2f}")
                lines.append(f"Minimum: {series.min():,.2f}")
                lines.append(f"Maximum: {series.max():,.2f}")
                lines.append(f"Median: {series.median():,.2f}")

                lines.append("")

        # ==================================================
        # TOP CATEGORIES
        # ==================================================

        categorical = analysis["categorical"][:3]

        if categorical:

            lines.append("# TOP CATEGORIES")

            for column in categorical:

                lines.append(f"## {column}")

                values = (
                    df[column]
                    .fillna("Unknown")
                    .astype(str)
                    .value_counts()
                    .head(10)
                )

                for value, count in values.items():

                    lines.append(f"- {value}: {count:,}")

                lines.append("")

        # ==================================================
        # SAMPLE RECORDS
        # ==================================================

        lines.append("# SAMPLE DATA")

        preview = df.head(5)

        lines.append(
            preview.to_markdown(index=False)
        )

        lines.append("")

        lines.append(
            "Answer all business questions ONLY using the information above."
        )

        return "\n".join(lines)