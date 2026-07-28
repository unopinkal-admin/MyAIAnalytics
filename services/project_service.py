import streamlit as st

from modules.loader import DataLoader
from modules.cleaner import DataCleaner
from modules.profiler import DataProfiler
from modules.context_builder import ContextBuilder
from modules.insights import InsightEngine
from modules.business_health import BusinessHealth


class ProjectService:

    @staticmethod
    def create(uploaded_file):

        # Load
        df = DataLoader.load(uploaded_file)

        if df is None:
            return None

        # Clean
        df = DataCleaner.clean(df)

        # Profile
        profile = DataProfiler.profile(df)

        # Build AI Context
        context = ContextBuilder.build(df, profile)

        # Generate Insights
        insights = InsightEngine.generate(df, context)

        # Calculate Business Health
        health = BusinessHealth.calculate({
            "profile": profile,
            "context": context
        })

        # Create Project
        project = {
            "file_name": uploaded_file.name,
            "df": df,
            "profile": profile,
            "context": context,
            "insights": insights,
            "health": health,
        }

        # Save Project
        st.session_state.project = project

        return project
