import streamlit as st


class HealthCard:

    @staticmethod
    def show(health):

        score = health.get("score", 0)

        if score >= 90:
            color = "#16A34A"
            status = "🟢 Excellent"
            message = "Business performance is excellent."
        elif score >= 75:
            color = "#2563EB"
            status = "🔵 Healthy"
            message = "Business is performing well."
        elif score >= 60:
            color = "#F59E0B"
            status = "🟡 Monitor"
            message = "Some areas require attention."
        else:
            color = "#DC2626"
            status = "🔴 Critical"
            message = "Immediate action recommended."

        st.markdown(f"""
<div style="
background:white;
border-radius:22px;
padding:30px;
border:1px solid #E5E7EB;
box-shadow:0 8px 24px rgba(0,0,0,.06);
margin-bottom:25px;
">

<div style="
font-size:24px;
font-weight:700;
margin-bottom:25px;
color:#1E293B;
">
❤️ Business Health
</div>

<div style="
display:grid;
grid-template-columns:170px auto;
gap:35px;
align-items:center;
">

<div style="
width:170px;
height:170px;
border-radius:50%;
border:10px solid {color};
display:flex;
align-items:center;
justify-content:center;
margin:auto;
">

<div>

<div style="
font-size:52px;
font-weight:700;
color:{color};
text-align:center;
line-height:1;
">
{score}
</div>

<div style="
font-size:15px;
color:#64748B;
margin-top:8px;
text-align:center;
">
/100
</div>

</div>

</div>

<div>

<div style="
font-size:26px;
font-weight:700;
color:#0F172A;
margin-bottom:12px;
">
{status}
</div>

<div style="
font-size:16px;
color:#64748B;
margin-bottom:24px;
">
{message}
</div>

<div style="
display:grid;
grid-template-columns:repeat(3,1fr);
gap:18px;
">

<div style="
background:#F8FAFC;
padding:18px;
border-radius:16px;
text-align:center;
">

<div style="font-size:13px;color:#64748B;">
Financial
</div>

<div style="
font-size:24px;
font-weight:700;
margin-top:8px;
color:#16A34A;
">
Healthy
</div>

</div>

<div style="
background:#F8FAFC;
padding:18px;
border-radius:16px;
text-align:center;
">

<div style="font-size:13px;color:#64748B;">
Operations
</div>

<div style="
font-size:24px;
font-weight:700;
margin-top:8px;
color:#2563EB;
">
Stable
</div>

</div>

<div style="
background:#F8FAFC;
padding:18px;
border-radius:16px;
text-align:center;
">

<div style="font-size:13px;color:#64748B;">
Data Quality
</div>

<div style="
font-size:24px;
font-weight:700;
margin-top:8px;
color:#7C3AED;
">
Good
</div>

</div>

</div>

</div>

</div>

</div>
""", unsafe_allow_html=True)