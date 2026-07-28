import pandas as pd


class InsightEngine:

    @staticmethod
    def generate(df, context):

        insights = []

        # Dataset Summary
        insights.append(
            f"Dataset contains {context['rows']} rows and {context['columns']} columns."
        )

        # Data Quality
        total_missing = sum(context["missing_values"].values())

        if total_missing == 0:
            insights.append("✅ No missing values detected.")
        else:
            insights.append(
                f"⚠️ Dataset contains {total_missing} missing values."
            )

        if context["duplicates"] == 0:
            insights.append("✅ No duplicate records found.")
        else:
            insights.append(
                f"⚠️ {context['duplicates']} duplicate rows detected."
            )

        # Numeric Insights
        for col, stats in context["numeric_statistics"].items():

            insights.append(
                f"{col}: Average = {stats['mean']}, "
                f"Minimum = {stats['min']}, "
                f"Maximum = {stats['max']}"
            )

        return insights
