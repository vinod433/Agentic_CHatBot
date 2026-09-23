from src.langgraph.state.state import State


class BasicChatBotNode:
    """Basic chatbot logic implementation"""
    def __init__(self,model):
        self.llm = model


    def process(self,state:State)->dict:
        """
        process the input state and generate chatbot response"""

        return {"messages":self.llm.invoke(state["messages"])}
