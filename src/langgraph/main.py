import streamlit as st
from src.langgraph.UI.streamlitUI.loadui import LoadStreamlitUI
from src.langgraph.LLMS.groqLLM import GroqLLM
from src.langgraph.graph.graph_builder import GraphBuilder
from src.langgraph.UI.streamlitUI.display_results import DisplayResultStreamlit

def load_langgraph_app():
    """ Load and run agentic AI application with Streamlit UI"""

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input form the UI")
        return 

    user_message = st.chat_input("Enter your Message :")

    if user_message:
        try:

            obj_llm_cofig = GroqLLM(user_controls_input=user_input)
            model = obj_llm_cofig.get_llm_model()

            if not model:
                st.error("Error : LLM model could not be initialized")
                return

            usecase = user_input.get("selected_usecase")

            if not usecase:
                st.error("Error : No use case Selected")
                return 

            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_results_on_ui()
            except Exception as e:
                st.error(f"Error : Graph set up failed - {e}")    
                return



        except Exception as e:
            st.error(f"Error : Graph set up failed - {e}") 
            return
