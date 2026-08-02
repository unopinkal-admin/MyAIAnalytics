import streamlit as st
from contextlib import contextmanager


class Card:

    @staticmethod
    @contextmanager
    def container(title=None, icon=None):

        st.markdown(
            """
<div style="
background:white;
border:1px solid #E5E7EB;
border-radius:18px;
padding:20px;
margin-bottom:20px;
box-shadow:0 4px 12px rgba(0,0,0,.06);
">
""",
            unsafe_allow_html=True,
        )

        if title:

            heading = ""

            if icon:
                heading += f"{icon} "

            heading += title

            st.markdown(
                f"""
<h3 style="
margin-top:0;
margin-bottom:20px;
color:#1E293B;
font-size:20px;
font-weight:700;
">
{heading}
</h3>
""",
                unsafe_allow_html=True,
            )

        try:
            yield
        finally:
            st.markdown("</div>", unsafe_allow_html=True)