import pandas as pd


class ContextBuilder:

    @staticmethod
    def build(df, profile):

        context = {
            "rows": profile["rows"],
            "columns": profile["columns"],
            "column_names": profile["column_names"],
            "numeric_columns": profile["numeric_columns"],
            "text_columns": profile["text_columns"],
            "date_columns": profile["date_columns"],
            "duplicates": profile["duplicates"],
            "missing_values": profile["missing_values"],
            "quality_score": profile["quality_score"],
        }

        numeric_stats = {}

        for col in profile["numeric_columns"]:

            numeric_stats[col] = {
                "min": float(df[col].min()),
                "max": float(df[col].max()),
                "mean": round(float(df[col].mean()), 2),
                "median": round(float(df[col].median()), 2),
                "sum": round(float(df[col].sum()), 2),
            }

        context["numeric_statistics"] = numeric_stats

        return context
