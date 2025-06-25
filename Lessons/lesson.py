from langgraph.graph import StateGraph,START,END
from typing import TypedDict


class AgentState(TypedDict):
    num1:int
    operation:str
    num2:int
    finalNumber:int

def adder(state):
    """This node adds the 2 numbers"""
    state["finalNumber"] = state["num1"] + state["num2"] 
    return state

def subtractor(state):
    """This node subtracts the 2 numbers"""
    state["finalNumber"] = state["num1"] - state["num2"] 
    return state

def decide_next_node(state):
    """This node will select the next phase of the graph"""
    if state["operation"] == "+":
        return "addition_operation"
    elif state["operation"] == "-":
        return "subtraction_operation"

graph = StateGraph(AgentState)

graph.add_node("add_node",adder)
graph.add_node("subtract_node",subtractor)
graph.add_node("router",lambda state:state)

graph.add_edge(START,"router")
graph.add_conditional_edges(
    "router",
    decide_next_node,
    {
        "addition_operation":"add_node",
        "subtraction_operation":"subtract_node"
    }
)
graph.add_edge("add_node",END)
graph.add_edge("subtract_node",END)

app = graph.compile()

res = app.invoke({
    "num1":5,
    "operation":"-",
    "num2":15,
})
print(res)