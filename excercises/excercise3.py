from langgraph.graph import StateGraph
from typing import TypedDict, List

class AgentState(TypedDict):
    name:str
    age:int
    skills:List[str]
    result:str

def node1(state):
    """Personalizes the greeting of the User"""
    state["result"] = f"{state["name"]}, welcome to the system! "
    return state

def node2(state):
    """Describe the user age"""
    state["result"] += f"You are {state["age"]} years old! "
    return state

def node3(state):
    """Lists user skill in formatted string"""
    state["result"] += f"You have skills in: {",".join(state["skills"])}"
    return state

graph = StateGraph(AgentState)

graph.add_node("node1",node1)
graph.add_node("node2",node2)
graph.add_node("node3",node3)

graph.set_entry_point("node1")
graph.add_edge("node1","node2")
graph.add_edge("node2","node3")
graph.set_finish_point("node3")

app = graph.compile()
res = app.invoke({
    "name":"Linda",
    "age":31,
    "skills":["Python","Javascript","Docker"]
})

print(res["result"])