from langgraph.graph import StateGraph
from typing import TypedDict

class AgentState(TypedDict):
    message:str

def compliment_node(state:AgentState):
    state["message"] += ",you are doing an amazing job learning Langgraph!" 
    return state

graph = StateGraph(AgentState)
graph.add_node("complimentor",compliment_node)

graph.set_entry_point("complimentor")
graph.set_finish_point("complimentor")


app = graph.compile()

result = app.invoke({"message":"Bob"})
print(result)