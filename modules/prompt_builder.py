import pandas as pd


class PromptBuilder:

    @staticmethod
    def build(df):

        prompt = []

        prompt.append("# Dataset Overview")

        prompt.append(f"Rows: {len(df):,}")
        prompt.append(f"Columns: {len(df.columns)}")

        prompt.append("")

        # -------------------------
        # Column Types
        # -------------------------

        numeric = df.select_dtypes(include="number").columns.tolist()
        text = df.select_dtypes(include=["object", "string"]).columns.tolist()

        prompt.append("Numeric Columns:")
        prompt.append(", ".join(numeric) if numeric else "None")

        prompt.append("")
        prompt.append("Text Columns:")
        prompt.append(", ".join(text) if text else "None")

        prompt.append("")

        # -------------------------
        # Missing Values
        # -------------------------

        missing = df.isna().sum()

        prompt.append("Missing Values:")

        for col, value in missing.items():

            if value > 0:

                prompt.append(f"- {col}: {value}")

        if missing.sum() == 0:
            prompt.append("None")

        prompt.append("")

        # -------------------------
        # Numeric Statistics
        # -------------------------

        if numeric:

            prompt.append("Key Statistics:")

            for col in numeric:

                prompt.append(
                    f"""
{col}

Average : {round(df[col].mean(),2)}

Minimum : {df[col].min()}

Maximum : {df[col].max()}

Total : {round(df[col].sum(),2)}
"""
                )

        prompt.append("")

        # -------------------------
        # Top Categories
        # -------------------------

        for col in text[:3]:

            prompt.append(f"Top values in {col}:")

            values = (
                df[col]
                .value_counts()
                .head(5)
            )

            for item, count in values.items():

                prompt.append(f"- {item}: {count}")

            prompt.append("")

        return "\n".join(prompt)
