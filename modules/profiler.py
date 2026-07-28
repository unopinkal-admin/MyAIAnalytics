import pandas as pd


class DataProfiler:

    @staticmethod
    def profile(df):

        profile = {}

        profile["rows"] = len(df)
        profile["columns"] = len(df.columns)

        profile["column_names"] = list(df.columns)

        profile["numeric_columns"] = (
            df.select_dtypes(include="number")
            .columns.tolist()
        )

        profile["text_columns"] = (
            df.select_dtypes(include=["object", "string"])
            .columns.tolist()
        )

        profile["date_columns"] = (
            df.select_dtypes(include=["datetime64"])
            .columns.tolist()
        )

        profile["missing_values"] = (
            df.isna()
            .sum()
            .to_dict()
        )

        profile["duplicates"] = int(df.duplicated().sum())

        profile["memory_mb"] = round(
            df.memory_usage(deep=True).sum() / 1024 / 1024,
            2
        )

        profile["quality_score"] = int(
            DataProfiler.quality_score(df)
        )


        return profile


    @staticmethod
    def quality_score(df):

        score = 100

        missing = df.isna().sum().sum()

        duplicates = df.duplicated().sum()

        score -= min(30, missing)

        score -= min(20, duplicates)

        unnamed = sum(
            "unnamed" in str(c).lower()
            for c in df.columns
        )

        score -= unnamed * 5

        return max(score, 0)
