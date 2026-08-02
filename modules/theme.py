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
   Main App Background
-------------------------------------------------- */

.stApp{

    background:
        radial-gradient(circle at top right,#dbeafe 0%,transparent 35%),
        radial-gradient(circle at bottom left,#e0f2fe 0%,transparent 30%),
        linear-gradient(180deg,#eef4ff 0%,#f8fbff 100%);

}

/* Main content */

.main .block-container{

    max-width:1450px;

    padding-top:1.2rem;

    padding-bottom:2rem;

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

    background:rgba(255,255,255,.85);

    backdrop-filter:blur(18px);

    border-radius:20px;

    padding:20px;

    border:1px solid rgba(255,255,255,.55);

    box-shadow:0 15px 40px rgba(15,23,42,.08);

}

/* -------------------------------------------------
   Chart Cards
-------------------------------------------------- */

.chart-card{

    background:rgba(255,255,255,.82);

    backdrop-filter:blur(18px);

    border-radius:22px;

    padding:22px;

    border:1px solid rgba(255,255,255,.5);

    box-shadow:0 15px 35px rgba(15,23,42,.08);

    margin-bottom:22px;

}

/* -------------------------------------------------
   Buttons
-------------------------------------------------- */

.stButton>button{

    background:#2563EB;

    color:white;

    border-radius:12px;

    border:none;

    font-weight:600;

}

.stButton>button:hover{

    background:#1D4ED8;

}

/* -------------------------------------------------
   File uploader
-------------------------------------------------- */

[data-testid="stFileUploader"]{

    background:rgba(255,255,255,.75);

    border-radius:18px;

    border:2px dashed #CBD5E1;

}

/* -------------------------------------------------
   DataFrame
-------------------------------------------------- */

[data-testid="stDataFrame"]{

    border-radius:18px;

    overflow:hidden;

}

/* -------------------------------------------------
   Plotly
-------------------------------------------------- */

.js-plotly-plot{

    border-radius:18px;

}

/* -------------------------------------------------
   Divider
-------------------------------------------------- */

hr{

    margin-top:28px;

    margin-bottom:28px;

    border-color:#dbe4f0;

}

</style>
""",
        unsafe_allow_html=True)