from pathlib import Path

import streamlit as st
from openai import OpenAI

from modules.prompt_builder import PromptBuilder


class AIAnalyst:

    def __init__(self):

        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=st.secrets["OPENROUTER_API_KEY"]
        )

        self.system_prompt = self.load_system_prompt()

    def load_system_prompt(self):

        prompt_path = Path("assets/system_prompt.txt")

        if prompt_path.exists():
            return prompt_path.read_text(encoding="utf-8")

        return (
            "You are MyAIAnalytics AI Business Consultant. "
            "Provide concise, professional business insights."
        )

    def _chat(self, user_message):

        response = self.client.chat.completions.create(

            model="openai/gpt-oss-20b:free",

            messages=[
                {
                    "role": "system",
                    "content": self.system_prompt
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],

            temperature=0.2
        )

        return response.choices[0].message.content

    def summarize(self, df):

        prompt = PromptBuilder.build(df)

        return self._chat(prompt)

    def ask(self, df, question):

        prompt = PromptBuilder.build(df)

        user_message = f"""
Dataset Information

{prompt}

-------------------------

Business Question

{question}

Answer as a senior business consultant.
"""

        return self._chat(user_message)
