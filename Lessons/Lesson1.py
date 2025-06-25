from typing import Dict, TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    message: str

def greeting_node(state:AgentState):
    """Simple Nodes that adds a greeting message to the state"""
    state["message"] = "Hey" + state["message"] + ",How's your day going ?"
    return state

graph = StateGraph(AgentState)
graph.add_node("greeter",greeting_node)

graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app = graph.compile()


from IPython.display import Image,display

data = app.get_graph().draw_mermaid_png()
with open("graph.png",'wb') as f:
    f.write(data)
    f.close()

result = app.invoke({"message":"Siddhant"})
print(result["message"])