import streamlit as st


class Theme:

    @staticmethod
    def load():

        st.markdown("""
<style>

/* -------------------------------------------------
   Google Font
-------------------------------------------------- */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Inter',sans-serif;
}

/* -------------------------------------------------
   Main App
-------------------------------------------------- */

.stApp{
    background:#F3F6FB;
}

/* -------------------------------------------------
   Sidebar
-------------------------------------------------- */

section[data-testid="stSidebar"]{
    background:#111827;
    border-right:1px solid #1F2937;
}

section[data-testid="stSidebar"] *{
    color:white;
}

/* -------------------------------------------------
   Headers
-------------------------------------------------- */

h1{
    color:#1E3A8A;
    font-weight:700;
}

h2{
    color:#1E293B;
    font-weight:700;
}

h3{
    color:#334155;
}

/* -------------------------------------------------
   Metric Cards
-------------------------------------------------- */

.metric-card{
    background:white;
    border-radius:18px;
    padding:18px;
    border:1px solid #E5E7EB;
    box-shadow:0 8px 20px rgba(0,0,0,.06);
}

/* -------------------------------------------------
   Chart Containers
-------------------------------------------------- */

.chart-card{

    background:white;

    padding:18px;

    border-radius:18px;

    border:1px solid #E5E7EB;

    box-shadow:0 8px 20px rgba(0,0,0,.06);

    margin-bottom:20px;

}

/* -------------------------------------------------
   Buttons
-------------------------------------------------- */

.stButton>button{

    background:#2563EB;

    color:white;

    border-radius:10px;

    border:none;

    padding:.6rem 1.2rem;

    font-weight:600;

}

.stButton>button:hover{

    background:#1D4ED8;

}

/* -------------------------------------------------
   File uploader
-------------------------------------------------- */

[data-testid="stFileUploader"]{

    background:white;

    border-radius:16px;

    border:2px dashed #CBD5E1;

    padding:20px;

}

/* -------------------------------------------------
   Tabs
-------------------------------------------------- */

.stTabs [data-baseweb="tab"]{

    font-weight:600;

    font-size:15px;

}

/* -------------------------------------------------
   Dataframe
-------------------------------------------------- */

[data-testid="stDataFrame"]{

    border-radius:18px;

    border:1px solid #E5E7EB;

    overflow:hidden;

}

/* -------------------------------------------------
   Plotly Charts
-------------------------------------------------- */

.js-plotly-plot{

    border-radius:18px;

}

/* -------------------------------------------------
   Horizontal Rule
-------------------------------------------------- */

hr{

    margin-top:25px;

    margin-bottom:25px;

}

/* -------------------------------------------------
   Reduce top padding
-------------------------------------------------- */

.block-container{

    padding-top:1.2rem;

    padding-bottom:2rem;

    max-width:1450px;

}

</style>
""",
        unsafe_allow_html=True)