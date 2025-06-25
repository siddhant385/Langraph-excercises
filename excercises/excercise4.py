from langgraph.graph import StateGraph,START,END
from typing import TypedDict

class AgentState(TypedDict):
    num1: int
    op1 : str
    num2: int
    num3: int
    num4: int
    op2 : str
    finalNumber : int
    finalNumber2: int 

def adder(state):
    """Adds the first number addition op"""
    state["finalNumber"] = state["num1"]+state["num2"]
    return state
def subtracts(state):
    """Subtracts the first number subtraction op"""
    state["finalNumber"] = state["num1"]-state["num2"]
    return state

def decide_next(state):
    """decides where to move next"""
    if state["op1"] =="+":
        return "addition_node" 
    elif state["op1"] =="-":
        return "substraction_node"

def adder2(state):
    """Adds the first number addition op"""
    state["finalNumber2"] = state["num3"]+state["num4"]
    return state
def subtracts2(state):
    """Subtracts the first number subtraction op"""
    state["finalNumber2"] = state["num3"]-state["num4"]
    return state

def decide_next2(state):
    """decides where to move next"""
    if state["op2"] =="+":
        return "addition_node" 
    elif state["op2"] =="-":
        return "substraction_node"

graph = StateGraph(AgentState)

graph.add_node("add_node",adder)
graph.add_node("subtract_node",subtracts)
graph.add_node("router",lambda state:state)
graph.add_node("add_node2",adder2)
graph.add_node("subtract_node2",subtracts2)
graph.add_node("router2",lambda state:state)

graph.add_edge(START,"router")
graph.add_conditional_edges(
    "router",
    decide_next,
    {
        "addition_node":"add_node",
        "substraction_node":"subtract_node"
    }
)
graph.add_edge("add_node","router2")
graph.add_edge("subtract_node","router2")
graph.add_conditional_edges(
    "router2",
    decide_next2,
    {
        "addition_node":"add_node2",
        "substraction_node":"subtract_node2"
    }
)
graph.add_edge("add_node2",END)
graph.add_edge("subtract_node2",END)

app = graph.compile()
initial_state = AgentState(num1=10,op1="-",num2=5,num3=7,num4=2,op2="+",finalNumber=0,finalNumber2=0)
res = app.invoke(initial_state)
print(res)