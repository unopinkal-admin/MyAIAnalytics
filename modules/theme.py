import streamlit as st


class Theme:

    @staticmethod
    def load():

        st.markdown("""
        <style>

        /* Main App */
        .main {
            background-color: #F8FAFC;
        }

        /* KPI Cards */
        div[data-testid="metric-container"]{
            background: white;
            border:1px solid #E5E7EB;
            padding:18px;
            border-radius:12px;
            box-shadow:0 2px 8px rgba(0,0,0,.05);
        }

        /* Buttons */
        .stButton > button{
            width:100%;
            border-radius:10px;
            height:45px;
            font-weight:600;
        }

        /* Headers */
        h1{
            color:#1E3A8A;
        }

        h2,h3{
            color:#334155;
        }

        /* Sidebar */
        section[data-testid="stSidebar"]{
            background:#111827;
        }

        section[data-testid="stSidebar"] *{
            color:white;
        }

        </style>
        """, unsafe_allow_html=True)
