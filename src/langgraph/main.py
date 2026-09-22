import streamlit as st
from src.langgraph.UI.streamlitUI.loadui import LoadStreamlitUI


def load_langgraph_app():
    """ Load and run agentic AI application with Streamlit UI"""

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input form the UI")
        return 

    user_message = st.chat_input("Enter your Message :")