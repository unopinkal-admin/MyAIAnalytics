from pathlib import Path
import os

import streamlit as st
from openai import OpenAI

from modules.prompt_builder import PromptBuilder


class AIAnalyst:

    def __init__(self):

        api_key = None

        # ==========================================
        # Streamlit Secrets
        # ==========================================

        try:
            api_key = st.secrets["OPENROUTER_API_KEY"]
        except Exception:
            pass

        # ==========================================
        # Environment Variable
        # ==========================================

        if not api_key:
            api_key = os.getenv("OPENROUTER_API_KEY")

        if not api_key:
            raise ValueError(
                "OPENROUTER_API_KEY was not found.\n"
                "Configure it in Streamlit secrets or "
                "as an environment variable."
            )

        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
        )

        self.system_prompt = self.load_system_prompt()

    # ==================================================
    # Load System Prompt
    # ==================================================

    def load_system_prompt(self):

        prompt_file = Path("assets/system_prompt.txt")

        if prompt_file.exists():

            return prompt_file.read_text(
                encoding="utf-8"
            )

        return """
You are Pinkal AI Analytics Pro.

You are an executive business analyst.

Your job is to analyze uploaded datasets and provide:

• Executive Summary
• KPI Analysis
• Trends
• Risks
• Opportunities
• Recommendations

Always answer using Markdown.

Use headings.

Use bullet points.

Keep responses professional.

Never invent values.

Base every answer only on the supplied dataset context.

If information is unavailable, clearly state that.
"""

    # ==================================================
    # Internal Chat
    # ==================================================

    def _chat(self, message):

        response = self.client.chat.completions.create(

            model="openai/gpt-oss-20b:free",

            messages=[
                {
                    "role": "system",
                    "content": self.system_prompt,
                },
                {
                    "role": "user",
                    "content": message,
                },
            ],

            temperature=0.2,
            max_tokens=1200,
        )

        return response.choices[0].message.content

    # ==================================================
    # Executive Summary
    # ==================================================

    def summarize(self, df):

        context = PromptBuilder.build(df)

        prompt = f"""
Create an executive business report.

Dataset Context

{context}

The report must include:

# Executive Summary

# KPI Highlights

# Business Trends

# Risks

# Opportunities

# Recommended Actions

Keep the report concise and professional.
"""

        return self._chat(prompt)

    # ==================================================
    # Ask Question
    # ==================================================

    def ask(self, df, question):

        context = PromptBuilder.build(df)

        prompt = f"""
Dataset Context

{context}

--------------------------------------------

Business Question

{question}

Answer as a senior business consultant.

If calculations are possible from the dataset,
perform them.

Use Markdown formatting.

Keep the answer concise but insightful.
"""

        return self._chat(prompt)