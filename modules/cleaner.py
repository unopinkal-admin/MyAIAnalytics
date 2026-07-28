import pandas as pd


class DataCleaner:

    @staticmethod
    def clean(df):

        # Remove completely empty rows
        df = df.dropna(how="all")

        # Remove completely empty columns
        df = df.dropna(axis=1, how="all")

        # Remove leading/trailing spaces from column names
        df.columns = [str(col).strip() for col in df.columns]

        # Remove "Unnamed" columns
        df = df.loc[:, ~df.columns.str.contains("^Unnamed", case=False)]

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Reset index
        df = df.reset_index(drop=True)

        return df
