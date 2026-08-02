import streamlit as st


class Theme:

    @staticmethod
    def load():

        st.markdown("""
<style>

/* ==========================
   Main App
========================== */

.main .block-container{
    max-width:1400px;
    padding-top:1.5rem;
    padding-bottom:2rem;
}

/* ==========================
   Headers
========================== */

h1{
    font-weight:700;
    margin-bottom:0.25rem;
}

h2,h3{
    font-weight:600;
}

/* ==========================
   Sections
========================== */

.section-title{
    font-size:22px;
    font-weight:700;
    margin-top:25px;
    margin-bottom:12px;
}

/* ==========================
   Divider
========================== */

hr{
    margin-top:25px;
    margin-bottom:25px;
}

/* ==========================
   Streamlit Metrics
========================== */

[data-testid="metric-container"]{
    border-radius:16px;
    padding:18px;
    border:1px solid #ECECEC;
    box-shadow:0 2px 8px rgba(0,0,0,.05);
}

/* ==========================
   Sidebar
========================== */

[data-testid="stSidebar"]{
    border-right:1px solid #ECECEC;
}

/* ==========================
   Plotly Charts
========================== */

.js-plotly-plot{
    border-radius:16px;
}

/* ==========================
   Tables
========================== */

[data-testid="stDataFrame"]{
    border-radius:16px;
}

</style>
""", unsafe_allow_html=True)