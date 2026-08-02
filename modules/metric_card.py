import streamlit as st


class MetricCard:

    COLORS = {
        "blue": "#2563EB",
        "green": "#16A34A",
        "orange": "#EA580C",
        "purple": "#7C3AED",
        "red": "#DC2626",
        "teal": "#0F766E",
        "gray": "#475569",
    }

    @staticmethod
    def show(
        title,
        value,
        color="blue",
        subtitle=None,
        icon=None,
    ):

        accent = MetricCard.COLORS.get(color, "#2563EB")

        html = f"""
<div style="
background:white;
border-radius:18px;
padding:22px;
border-left:6px solid {accent};
box-shadow:0 6px 18px rgba(0,0,0,.08);
height:145px;
display:flex;
flex-direction:column;
justify-content:center;
transition:0.25s;
">

<div style="
font-size:15px;
font-weight:600;
color:#64748B;
margin-bottom:10px;
">

{icon or ""} {title}

</div>

<div style="
font-size:34px;
font-weight:700;
color:{accent};
line-height:1.2;
">

{value}

</div>
"""

        if subtitle:

            html += f"""
<div style="
margin-top:12px;
font-size:14px;
color:#94A3B8;
">

{subtitle}

</div>
"""

        html += "</div>"

        st.markdown(
            html,
            unsafe_allow_html=True,
        )