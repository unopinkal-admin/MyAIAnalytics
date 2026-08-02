import pandas as pd
import streamlit as st


class FilterEngine:

    @staticmethod
    def apply(df):

        filtered_df = df.copy()

        st.subheader("🔎 Dashboard Filters")

        c1, c2, c3, c4 = st.columns(4)

        # -----------------------------
        # Region
        # -----------------------------
        if "Region" in filtered_df.columns:

            regions = sorted(filtered_df["Region"].dropna().unique())

            selected_regions = c1.multiselect(
                "🌍 Region",
                regions,
                default=regions
            )

            filtered_df = filtered_df[
                filtered_df["Region"].isin(selected_regions)
            ]

        # -----------------------------
        # Category
        # -----------------------------
        if "Category" in filtered_df.columns:

            categories = sorted(filtered_df["Category"].dropna().unique())

            selected_categories = c2.multiselect(
                "📦 Category",
                categories,
                default=categories
            )

            filtered_df = filtered_df[
                filtered_df["Category"].isin(selected_categories)
            ]

        # -----------------------------
        # Status
        # -----------------------------
        if "Status" in filtered_df.columns:

            status = sorted(filtered_df["Status"].dropna().unique())

            selected_status = c3.multiselect(
                "📄 Status",
                status,
                default=status
            )

            filtered_df = filtered_df[
                filtered_df["Status"].isin(selected_status)
            ]

        # -----------------------------
        # Date
        # -----------------------------
        date_columns = filtered_df.select_dtypes(
            include=["datetime64[ns]"]
        ).columns.tolist()

        if len(date_columns):

            date_col = date_columns[0]

            minimum = filtered_df[date_col].min()
            maximum = filtered_df[date_col].max()

            dates = c4.date_input(
                "📅 Date",
                value=(minimum, maximum),
                min_value=minimum,
                max_value=maximum
            )

            if len(dates) == 2:

                filtered_df = filtered_df[
                    (filtered_df[date_col] >= pd.Timestamp(dates[0])) &
                    (filtered_df[date_col] <= pd.Timestamp(dates[1]))
                ]

        st.divider()

        return filtered_df