#This section tells about looping graphs
from langgraph.graph import StateGraph,START,END
from typing import TypedDict,List
import random

class AgentState(TypedDict):
    name: str
    number: List[int]
    counter: int

def greeting_node(state):
    """Greeting Node which says hi to the person"""
    state['name'] = f"Hi there, {state["name"]}"
    state['counter'] = 0
    return state

def random_node(state):
    """Generates a random number from 0 to 10"""
    state["number"].append(random.randint(0,10))
    state['counter'] +=1
    return state

def should_continue(state:AgentState):
    """Function to decide what to do next"""
    if state["counter"]<5:
        print("ENTERING LOOP",state["counter"])
        return "loop"
    else:
        return "exit"

graph = StateGraph(AgentState)

graph.add_node("greeting",greeting_node)
graph.add_node("random",random_node)

graph.add_edge("greeting","random")
graph.add_conditional_edges(
    "random",
    should_continue,
    {
        "loop":"random",
        "exit":END
    }
)
graph.set_entry_point("greeting")

app = graph.compile()
res = app.invoke({
    "name":"Siddhant",
    "number":[],
    "counter":-100
})
print(res)