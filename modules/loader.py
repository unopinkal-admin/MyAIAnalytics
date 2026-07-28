import pandas as pd
import streamlit as st


class DataLoader:
    """Handles loading and intelligent type detection."""

    @staticmethod
    def load(uploaded_file):
        """
        Load an uploaded Excel or CSV file and automatically
        detect better data types.
        """

        if uploaded_file is None:
            return None

        try:
            filename = uploaded_file.name.lower()

            if filename.endswith(".csv"):
                df = pd.read_csv(uploaded_file)

            elif filename.endswith((".xlsx", ".xls")):
                df = pd.read_excel(uploaded_file)

            else:
                st.error("Unsupported file type.")
                return None

            # ------------------------------------
            # Intelligent Type Detection
            # ------------------------------------

            for col in df.columns:

                # Skip columns already numeric
                if pd.api.types.is_numeric_dtype(df[col]):
                    continue

                # ---------- Try Date ----------
                try:
                    converted = pd.to_datetime(
                        df[col],
                        format="%d-%m-%Y",
                        errors="coerce"
                    )

                    if converted.notna().sum() >= len(df) * 0.8:
                        df[col] = converted
                        continue

                except Exception:
                    pass

                # ---------- Try Number ----------
                try:
                    cleaned = (
                        df[col]
                        .astype(str)
                        .str.replace(",", "", regex=False)
                        .str.replace("$", "", regex=False)
                        .str.replace("%", "", regex=False)
                        .str.strip()
                    )

                    numeric = pd.to_numeric(
                        cleaned,
                        errors="coerce"
                    )

                    if numeric.notna().sum() >= len(df) * 0.8:
                        df[col] = numeric
                        continue

                except Exception:
                    pass

            return df

        except Exception as e:
            st.error(f"Unable to read file.\n\n{e}")
            return None

if __name__ == "__main__":
    print("Loader.py loaded successfully!")