import pandas as pd
import streamlit as st


class FilterEngine:

    @staticmethod
    def _multiselect(column, label, df):

        values = (
            df[column]
            .dropna()
            .astype(str)
            .sort_values()
            .unique()
            .tolist()
        )

        return st.multiselect(
            label,
            options=values,
            default=values,
        )

    @staticmethod
    def apply(df):

        filtered_df = df.copy()

        st.markdown("""
<div style="
background:white;
padding:22px;
border-radius:22px;
border:1px solid #E5E7EB;
box-shadow:0 8px 24px rgba(0,0,0,.06);
margin-bottom:24px;
">
<h2 style="
margin-top:0;
margin-bottom:20px;
color:#1E293B;
">
🎛 Executive Filters
</h2>
""", unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns(4)

        # ==================================================
        # Region
        # ==================================================

        if "Region" in filtered_df.columns:

            with c1:

                selected = FilterEngine._multiselect(
                    "Region",
                    "🌍 Region",
                    filtered_df,
                )

            filtered_df = filtered_df[
                filtered_df["Region"].astype(str).isin(selected)
            ]

        # ==================================================
        # Category
        # ==================================================

        if "Category" in filtered_df.columns:

            with c2:

                selected = FilterEngine._multiselect(
                    "Category",
                    "📦 Category",
                    filtered_df,
                )

            filtered_df = filtered_df[
                filtered_df["Category"].astype(str).isin(selected)
            ]

        # ==================================================
        # Status
        # ==================================================

        if "Status" in filtered_df.columns:

            with c3:

                selected = FilterEngine._multiselect(
                    "Status",
                    "📄 Status",
                    filtered_df,
                )

            filtered_df = filtered_df[
                filtered_df["Status"].astype(str).isin(selected)
            ]

        # ==================================================
        # Date
        # ==================================================

        date_columns = filtered_df.select_dtypes(
            include=["datetime64[ns]", "datetime64"]
        ).columns.tolist()

        if date_columns:

            with c4:

                date_col = date_columns[0]

                start = filtered_df[date_col].min()
                end = filtered_df[date_col].max()

                selected_dates = st.date_input(
                    "📅 Date Range",
                    value=(start, end),
                    min_value=start,
                    max_value=end,
                )

            if isinstance(selected_dates, tuple) and len(selected_dates) == 2:

                filtered_df = filtered_df[
                    (
                        filtered_df[date_col]
                        >= pd.Timestamp(selected_dates[0])
                    )
                    &
                    (
                        filtered_df[date_col]
                        <= pd.Timestamp(selected_dates[1])
                    )
                ]

        st.markdown(
            f"""
<div style="
margin-top:18px;
padding-top:18px;
border-top:1px solid #E5E7EB;
display:flex;
justify-content:space-between;
align-items:center;
">

<div style="
font-size:15px;
color:#64748B;
">
Showing
<b>{len(filtered_df):,}</b>
of
<b>{len(df):,}</b>
records
</div>

<div style="
background:#2563EB;
color:white;
padding:8px 16px;
border-radius:999px;
font-size:13px;
font-weight:600;
">
Active Dashboard Filters
</div>

</div>

</div>
""",
            unsafe_allow_html=True,
        )

        return filtered_df