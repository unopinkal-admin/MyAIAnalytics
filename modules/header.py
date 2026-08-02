import streamlit as st


class Header:

    @staticmethod
    def show(project):

        profile = project["profile"]
        health = project["health"]

        quality = profile["quality_score"]

        if quality >= 90:
            color = "#28a745"
        elif quality >= 70:
            color = "#f4b400"
        else:
            color = "#dc3545"

        st.markdown(f"""
<div style="
padding:22px;
border-radius:18px;
background:white;
border:1px solid #ECECEC;
box-shadow:0 3px 10px rgba(0,0,0,.06);
margin-bottom:20px;
">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
flex-wrap:wrap;
">

<div>

<h1 style="
margin:0;
color:#1f77b4;
font-size:34px;
">

📊 Pinkal AI Analytics

</h1>

<div style="
margin-top:8px;
font-size:18px;
color:#666;
">

Dataset:
<strong>{project["file_name"]}</strong>

</div>

</div>

<div style="
text-align:right;
">

<div style="
font-size:16px;
color:#666;
">

Business Health

</div>

<div style="
font-size:32px;
font-weight:bold;
color:{color};
">

{health["score"]}/100

</div>

<div style="
font-size:15px;
">

{health["status"]}

</div>

</div>

</div>

</div>
""",
        unsafe_allow_html=True)