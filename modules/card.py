import streamlit as st
from contextlib import contextmanager


class Card:
    """
    Pinkal AI Analytics Pro
    Reusable Card Component

    This component is the foundation for every
    dashboard section, KPI card, chart container,
    AI panel and report widget.
    """

    @staticmethod
    @contextmanager
    def container(
        title=None,
        icon=None,
        accent="#2563EB",
        padding=24,
    ):

        st.markdown(
            f"""
<style>

.pinkal-card {{
    background: rgba(255,255,255,.92);
    border:1px solid rgba(226,232,240,.9);
    border-left:6px solid {accent};
    border-radius:22px;
    padding:{padding}px;
    margin-bottom:24px;

    box-shadow:
        0 10px 25px rgba(15,23,42,.08);

    transition:all .25s ease;
}}

.pinkal-card:hover {{
    transform:translateY(-2px);
    box-shadow:
        0 18px 40px rgba(15,23,42,.12);
}}

.pinkal-card-title{{
    display:flex;
    align-items:center;
    gap:10px;

    margin-bottom:20px;

    font-size:22px;
    font-weight:700;

    color:#1E293B;
}}

.pinkal-card-icon{{
    font-size:24px;
}}

</style>

<div class="pinkal-card">
""",
            unsafe_allow_html=True,
        )

        if title:

            if icon is None:
                icon = "📊"

            st.markdown(
                f"""
<div class="pinkal-card-title">

<div class="pinkal-card-icon">
{icon}
</div>

<div>
{title}
</div>

</div>
""",
                unsafe_allow_html=True,
            )

        try:
            yield

        finally:
            st.markdown(
                "</div>",
                unsafe_allow_html=True,
            )

    @staticmethod
    def section(title, icon="📊"):

        st.markdown(
            f"""
<div style="
margin-top:10px;
margin-bottom:18px;

font-size:28px;
font-weight:700;

color:#1E293B;
">

{icon} {title}

</div>
""",
            unsafe_allow_html=True,
        )