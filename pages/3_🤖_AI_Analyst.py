import streamlit as st

from modules.ui import UI
from modules.theme import Theme
from modules.ai import AIAnalyst

st.set_page_config(
    page_title="AI Analyst",
    page_icon="🤖",
    layout="wide"
)

Theme.load()
UI.show_sidebar()

st.title("🤖 AI Business Analyst")

# Get current project
project = st.session_state.get("project")

if project is None:
    st.warning("⚠️ No dataset loaded.")
    st.info("Please upload a dataset from the Home page.")
    st.stop()

df = project["df"]
profile = project["profile"]

ai = AIAnalyst()

st.subheader("🧠 Executive Summary")

if st.button("Generate Executive Summary", width="stretch"):

    with st.spinner("🤖 AI is analyzing your dataset..."):

        summary = ai.summarize(df)

    st.markdown(summary)

st.divider()

st.subheader("💬 Ask AI About Your Data")

question = st.text_input(
    "Ask anything about your dataset..."
)

if question:

    with st.spinner("Thinking..."):

        answer = ai.ask(df, question)

    st.markdown(answer)
