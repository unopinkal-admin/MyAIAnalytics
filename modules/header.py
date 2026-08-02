import streamlit as st


class Header:

    @staticmethod
    def show(project):

        st.success("✅ Header is working!")

        st.title("📊 Pinkal AI Analytics")

        st.write(project["file_name"])